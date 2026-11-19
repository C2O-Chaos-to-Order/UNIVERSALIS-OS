# Synthetic CycloneDX 1.7 SBOM fixtures

**Fixture set:** SYN-SBOM-CDX17-001  
**Status:** Drafted; JSON syntax and dependency-reference closure checked; official CycloneDX schema validation NOT RUN  
**Data classification:** Entirely synthetic; no private or production data

## Dependency graph

```text
Example Universal Demo Application 1.0.0
├── Example Demo Core 2.1.0
│   └── Example Demo Crypto Wrapper 1.4.2
└── Example Demo UI Framework 3.0.1
```

## Files

- `cyclonedx-1.7-valid.json`: intended positive fixture with a root application and three fictional dependencies.
- `cyclonedx-1.7-invalid-format.json`: intentionally schema-invalid fixture; `bomFormat` violates the CycloneDX enum.

## Validation boundary

The official CycloneDX 1.7 JSON Schema declares JSON Schema Draft 7. Use a validator that supports Draft 7 and the official schema at:

https://cyclonedx.org/schema/bom-1.7.schema.json

A JSON parser success is only syntax validation. It is not CycloneDX schema validation, semantic dependency reconciliation, completeness validation, provenance verification, or security review.

## Required next run

1. Pin the official schema revision or content digest.
2. Run a Draft 7-capable validator against both fixtures.
3. Expect the positive fixture to validate and the negative fixture to fail on `bomFormat`.
4. Record validator name/version, schema digest, command, output, exit code, and environment.
5. Reconcile the positive fixture's dependency graph against the graph above.
6. Preserve all failures and rerun records; do not overwrite the original evidence.

## Recorded preliminary checks

**Run ID:** SBOM-EXP-001  
**Date:** 2026-11-19

| Check | Result | Scope |
|---|---|---|
| Positive fixture JSON parsing | PASS | Valid JSON syntax only |
| Negative fixture JSON parsing | PASS | Valid JSON syntax only |
| Positive dependency-reference closure | PASS | Every `ref` and `dependsOn` entry resolves to the declared root/component set |
| Official CycloneDX 1.7 Draft 7 schema validation | NOT RUN | Official schema was not locally pinned and CycloneDX CLI was not available in the execution environment |
| Completeness / provenance / license verification | NOT RUN | Outside this preliminary syntax/graph check |

The negative fixture is intentionally syntactically valid JSON with an invalid `bomFormat` enum value. Its expected schema rejection is a test expectation, not an observed validator result. Do not mark either fixture as CycloneDX-schema-validated until the official Draft 7 schema validator run is recorded.


## Pinned official schema source

The official CycloneDX 1.7 JSON Schema is vendored at `schemas/cyclonedx-bom-1.7.schema.json` for offline, reproducible validation. It is copied unchanged from the CycloneDX specification repository at commit `5fee6af48d43c751dc6a5b31138f06af2b10bac5` (schema Git blob SHA-1: `1ca17a2e3f1f684dfcbe66b4f182d6ea21464278`). The schema declares JSON Schema Draft 7. Upstream source: https://github.com/CycloneDX/specification/blob/5fee6af48d43c751dc6a5b31138f06af2b10bac5/schema/bom-1.7.schema.json . The schema source identifies Apache-2.0 licensing; retain this attribution when redistributing the schema.

**Important:** vendoring and pinning the schema is a source-control/provenance step, not a validation result. Positive and negative fixture validation remains **NOT RUN** until a Draft 7 validator is executed and its version, command, output, exit codes, and environment are recorded.


## Offline schema-validation harness and observed execution

The official CycloneDX 1.7 schema and its three external Draft 7 schema dependencies are vendored under `schemas/` from the same upstream CycloneDX specification commit `5fee6af48d43c751dc6a5b31138f06af2b10bac5`:

| Schema | Upstream Git blob SHA-1 |
|---|---|
| `cyclonedx-bom-1.7.schema.json` | `1ca17a2e3f1f684dfcbe66b4f182d6ea21464278` |
| `spdx.schema.json` | `566c4a32518c60778e55a56ccf71bf781320b279` |
| `jsf-0.82.schema.json` | `f46bfb1e52731ad1280123ff3e2bd29bd18d4bc2` |
| `cryptography-defs.schema.json` | `1f8e0d3c4f6226f1ce8093a503e0a73de7e10ed7` |

An offline validator script is provided at `tools/validate_sbom_fixtures.py`; it is designed to use `jsonschema==4.23.0`, Draft 7, local references only, and checks both expected schema outcomes plus dependency graph closure. A GitHub Actions workflow is provided at `.github/workflows/sbom-fixture-validation.yml` to execute it on the baseline branch and relevant pull-request changes.

**Execution record — 2026-11-19:** GitHub Actions created run `44564611940` for the pull-request event. The run conclusion was `failure`. The GitHub connector returned no job-step records; downloading the job log returned HTTP 404 (BlobNotFound). Therefore no validator version banner, command output, schema-validation result, or process exit code could be observed. The failure cause is unresolved. Do not interpret this as a positive or negative fixture-validation result; both remain **NOT VERIFIED**.

A separate structural check of the positive synthetic fixture was performed against the repository contents: JSON parsed; four distinct component references were found (metadata application plus three components); all four had dependency entries; all three dependency edges resolved; no unknown references or missing nodes were found. This graph-closure check is recorded separately from JSON Schema validation and does not establish schema conformance.
