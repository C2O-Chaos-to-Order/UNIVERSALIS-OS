#!/usr/bin/env python3
"""Offline validation of the pinned synthetic CycloneDX 1.7 fixtures."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator, RefResolver, __version__ as jsonschema_version

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "supply-chain" / "sbom"
SCHEMA_DIR = FIXTURES / "schemas"
SCHEMA_PATH = SCHEMA_DIR / "cyclonedx-bom-1.7.schema.json"
DEPENDENCY_SCHEMAS = (
    "spdx.schema.json",
    "jsf-0.82.schema.json",
    "cryptography-defs.schema.json",
)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def main() -> int:
    print(f"jsonschema_version={jsonschema_version}")
    schema = load_json(SCHEMA_PATH)
    if schema.get("$schema") != "http://json-schema.org/draft-07/schema#":
        raise SystemExit("FAIL: pinned schema does not declare JSON Schema Draft 7")

    store = {schema["$id"]: schema}
    for name in DEPENDENCY_SCHEMAS:
        dependency = load_json(SCHEMA_DIR / name)
        store[dependency["$id"]] = dependency

    Draft7Validator.check_schema(schema)
    resolver = RefResolver.from_schema(schema, store=store)
    validator = Draft7Validator(schema, resolver=resolver)

    positive_path = FIXTURES / "cyclonedx-1.7-valid.json"
    positive = load_json(positive_path)
    positive_errors = sorted(
        validator.iter_errors(positive),
        key=lambda error: (list(map(str, error.absolute_path)), error.message),
    )
    if positive_errors:
        for error in positive_errors:
            print(f"POSITIVE_SCHEMA_ERROR path={list(error.absolute_path)!r} keyword={error.validator!r}: {error.message}")
        print("FAIL: positive fixture rejected by the pinned CycloneDX 1.7 schema")
        return 1
    print("PASS: positive fixture conforms to pinned CycloneDX 1.7 Draft 7 schema")

    negative_path = FIXTURES / "cyclonedx-1.7-invalid-format.json"
    negative = load_json(negative_path)
    negative_errors = list(validator.iter_errors(negative))
    expected = [
        error for error in negative_errors
        if list(error.absolute_path) == ["bomFormat"] and error.validator == "enum"
    ]
    if not expected:
        for error in negative_errors:
            print(f"NEGATIVE_SCHEMA_ERROR path={list(error.absolute_path)!r} keyword={error.validator!r}: {error.message}")
        print("FAIL: negative fixture was not rejected specifically for bomFormat enum")
        return 1
    print("PASS: negative fixture rejected for bomFormat enum as expected")

    # Reconcile the positive fixture's component/dependency graph.
    bom = positive
    known_refs = []
    metadata_component = bom.get("metadata", {}).get("component")
    if metadata_component and metadata_component.get("bom-ref"):
        known_refs.append(metadata_component["bom-ref"])
    known_refs.extend(
        component["bom-ref"]
        for component in bom.get("components", [])
        if component.get("bom-ref")
    )
    if len(known_refs) != len(set(known_refs)):
        print("FAIL: duplicate bom-ref values in positive fixture")
        return 1
    known = set(known_refs)
    dependency_entries = bom.get("dependencies", [])
    dependency_refs = [entry.get("ref") for entry in dependency_entries]
    if len(dependency_refs) != len(set(dependency_refs)):
        print("FAIL: duplicate dependency ref entries")
        return 1
    missing_nodes = sorted(known - set(dependency_refs))
    unknown_refs = sorted(
        {ref for entry in dependency_entries for ref in ([entry.get("ref")] + entry.get("dependsOn", [])) if ref}
        - known
    )
    if missing_nodes or unknown_refs:
        print(f"FAIL: dependency graph closure missing_nodes={missing_nodes!r} unknown_refs={unknown_refs!r}")
        return 1
    edge_count = sum(len(entry.get("dependsOn", [])) for entry in dependency_entries)
    print(f"PASS: dependency graph closed; nodes={len(known)} edges={edge_count}")
    print("RESULT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
