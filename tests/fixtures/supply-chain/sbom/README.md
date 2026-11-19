# Synthetic CycloneDX 1.7 SBOM fixtures

**Fixture set:** SYN-SBOM-CDX17-001  
**Status:** Drafted; JSON syntax verified; official CycloneDX schema validation NOT RUN  
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
