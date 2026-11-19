# UNIVERSALIS-OS Public Standards Comparison and Synthetic Conformance Fixture Plan

**Document ID:** UOS-STANDARDS-001  
**Version:** 0.1.0  
**Status:** Public-interface research baseline and proposed test plan; not owner-accepted, implemented, or released  
**Date:** 2026-11-19  
**Target branch:** `foundation/architecture-baseline-2026-11-19`

## 1. Purpose and independence boundary

This document records a standards comparison and proposes a synthetic, offline conformance fixture plan for UNIVERSALIS-OS. It is not a public standard, publication authorization, license grant, certification, or permission to exchange data with C2O.

Every public schema and fixture must be reproducible by an independent implementer without C2O accounts, repositories, services, keys, policies, private data, infrastructure or personnel. UNIVERSALIS owns its own trust configuration, public governance, release decisions and acceptance.

## 2. Standards comparison

Research snapshot: 2026-11-19. Recheck upstream versions and schemas before implementation.

| Domain | Standard/reference | Strength and fit | Limits / implementation caution | Proposed UNIVERSALIS disposition |
|---|---|---|---|---|
| SBOM | SPDX 3.0.1 | Broad software bill-of-materials model; SBOM class describes elements for a package and supports composition, provenance, licensing, quality and security information | SPDX 3 is a major model evolution; validate selected serialization/profile and tool support across intended language ecosystems | Required interoperability candidate; validate SPDX 3.0.1 support before choosing primary output |
| SBOM | CycloneDX 1.7 / ECMA-424, 2nd edition | Broad BOM model for software/hardware, services, dependencies, vulnerabilities, cryptographic assets, formulation and declarations; JSON/XML/Protobuf | BOM completeness is not guaranteed by schema validity; evaluate producer/consumer coverage and conversion fidelity | Preferred first operational candidate for evaluation; not finally selected |
| SBOM tooling | CycloneDX CLI | Supports validation, analysis, diff, merge, conversion, signing and verification; CLI documents CycloneDX 1.7 support | Its documented SPDX conversion target is SPDX JSON 2.3, not SPDX 3; do not assume lossless SPDX 3 interchange | Candidate for isolated validation experiments |
| Provenance | in-toto Attestation Framework v1.2 | Predicate, Statement, Envelope and Bundle layers; Statement binds claims to immutable subject digests and predicate types | Predicate semantics and builder identity still require verification; framework/tooling are evolving | Adopt established structure where suitable; no proprietary replacement |
| Build provenance | SLSA Build Provenance v1.2 | Approved in-toto predicate describing where, when and how artifacts were produced | Provenance is a verifiable claim, not self-authenticating proof; trust builder identity and verify claims under explicit policy | Preferred build-provenance candidate |
| Signing envelope | DSSE | Pre-authentication encoding binds payload type and exact payload bytes before signing | Envelope alone does not define signer identity, trust roots, key custody, transparency, revocation or authorization | Evaluate with in-toto; trust roots remain consumer-local |
| Update security | TUF 1.0.37 | Root, Targets, Snapshot and Timestamp roles; threshold signatures, delegation, expiry, rollback/freeze/mix-and-match defenses | Does not define package formats or perform installation; safe install, recovery and platform integration remain separate | Strong candidate for public update metadata interoperability |
| JSON contract validation | JSON Schema 2020-12 | Established structural validation vocabulary and meta-schema | Structural validity does not establish semantic correctness, trust, authorization or safe resource consumption | Use for a new JSON contract only after proving a standards gap |
| Platform artifact descriptors | OCI Image Specification | Content-addressed descriptors and image indexes for OS/architecture-specific artifacts | OCI image index is for container image distribution, not general-purpose OS feature negotiation | Reuse relevant concepts only; do not make OCI the universal OS manifest |
| Secure development | NIST SP 800-218 SSDF 1.1 final | Established secure development practice baseline | Rev. 1 / SSDF 1.2 public draft is not final | Use final 1.1 as baseline; track draft separately |

### Primary sources

- SPDX 3.0.1 specification: https://spdx.github.io/spdx-spec/v3.0.1/
- SPDX SBOM model: https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Sbom/
- CycloneDX 1.7 overview: https://cyclonedx.org/specification/overview/
- ECMA-424: https://ecma-international.org/publications-and-standards/standards/ecma-424/
- CycloneDX CLI: https://github.com/CycloneDX/cyclonedx-cli
- in-toto Attestation Framework: https://github.com/in-toto/attestation/tree/main/spec
- in-toto Statement v1: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
- SLSA Build Provenance 1.2: https://slsa.dev/spec/v1.2/build-provenance
- DSSE: https://github.com/secure-systems-lab/dsse
- TUF 1.0.37: https://theupdateframework.github.io/specification/v1.0.37/
- JSON Schema 2020-12: https://json-schema.org/specification
- OCI Image Specification: https://github.com/opencontainers/image-spec
- NIST SSDF 1.1: https://csrc.nist.gov/pubs/sp/800/218/final

## 3. Preliminary engineering decisions

These are research recommendations for independent maintainer review, not final selections.

1. **SBOM:** evaluate CycloneDX 1.7 as the first operational generation candidate because it models broad system inventories and has an available CLI validator. Require SPDX 3.0.1 interoperability evaluation. CycloneDX CLI conversion to SPDX JSON 2.3 does not establish SPDX 3 support.
2. **Provenance:** prefer in-toto Statement v1 with SLSA Build Provenance v1.2 for build claims. Avoid inventing a competing subject/predicate model without a documented gap.
3. **Envelope:** evaluate DSSE for payload signing. Treat key ID only as a key-selection hint, not identity or trust.
4. **Update metadata:** evaluate TUF 1.0.37. The public specification must define interoperable metadata behavior while each independent implementation retains its own trust roots and release authority. Installation, atomicity, boot selection and recovery remain platform-specific.
5. **Capability manifest:** do not define a new public manifest yet. OCI describes platform artifact selection and JSON Schema validates structure; neither alone defines general OS feature negotiation. First document the use cases and prior-art gap.
6. **Independence:** all tests, schemas, examples and verification procedures must be runnable without C2O. C2O is an ordinary external contributor/consumer only, with no privileged trust or governance status.

## 4. Synthetic fixture package

Use a clearly fictional product such as `example-universalis-demo`, fictional component names and non-routable example identifiers. Do not include real user data, credentials, private repository paths, private C2O material, or real incident data.

Proposed directory layout:

```text
tests/fixtures/supply-chain/
  README.md
  sbom/
    cyclonedx-1.7-valid.json
    cyclonedx-1.7-missing-component-id.json
    cyclonedx-1.7-incomplete-composition.json
    spdx-3.0.1-valid.json
    spdx-3.0.1-invalid-reference.json
    cross-format-reconciliation.json
  provenance/
    intoto-statement-valid.json
    slsa-provenance-valid.json
    subject-digest-mismatch.json
    unknown-builder.json
    missing-material.json
  signatures/
    dsse-valid-envelope.json
    dsse-payload-type-substitution.json
    dsse-invalid-signature.json
    dsse-unknown-key-hint.json
    revoked-test-key.json
  tuf/
    root-threshold-valid.json
    root-threshold-insufficient.json
    timestamp-expired.json
    snapshot-rollback.json
    targets-hash-mismatch.json
    delegated-target-valid.json
    root-rotation-sequence/
  capability/
    manifest-valid.json
    unsupported-required-feature.json
    unknown-optional-feature.json
    duplicate-feature-id.json
    unsupported-major-version.json
  expected/
    expected-results.json
    fixture-digests.txt
```

This is a target layout proposal only; no fixtures have yet been created.

## 5. Public conformance test catalogue

| Suite | Positive cases | Negative/adversarial cases | Required assertion |
|---|---|---|---|
| SBOM-01 | Valid CycloneDX 1.7 and SPDX 3.0.1 documents | Invalid schema, missing identifiers, malformed license expression, unresolved dependency, incomplete composition marked complete | Structural validity is distinguished from completeness; uncertainty is retained |
| SBOM-02 | Synthetic dependency graph represented in BOM | Omitted known component, duplicate identity, contradictory hashes, fabricated supplier | Reconciliation detects missing or contradictory inventory |
| SBOM-03 | Supported cross-format conversion | Unsupported profile/version, dropped relationships or licensing semantics | Conversion losses are reported; never presumed lossless |
| PROV-01 | in-toto Statement subject digest matches artifact | Wrong digest, missing subject digest, subject substitution | Attestation is bound to exact artifact bytes |
| PROV-02 | SLSA provenance with known source, builder, invocation and dependencies | Unknown builder, inconsistent revision, missing required field, fabricated builder | Syntax, builder trust and policy acceptance remain distinct |
| DSSE-01 | Correct payload type and exact payload verify | Payload type substitution, payload mutation, malformed PAE, invalid signature | Signature authenticates exact payload bytes and payload type |
| DSSE-02 | Locally trusted test key verifies | Unknown/revoked key, duplicate signature counting, key ID collision | Key ID is a hint; trust comes from explicit local verification policy |
| TUF-01 | Valid root/targets/snapshot/timestamp chain and target digest | Insufficient threshold, expired metadata, rollback, freeze, mix-and-match, target substitution | Client follows TUF verification workflow and rejects invalid metadata |
| TUF-02 | Sequential root rotation | Skipped root version, untrusted root, interrupted rotation | Root rotation follows TUF rules and preserves recoverable trust state |
| CAP-01 | Supported major version and known required/optional features | Unknown required feature, malformed version, duplicate ID, incompatible major | Unknown required features fail safely; optional unknown features follow declared rules |
| CAP-02 | Compatible minor extension | Downgrade, ambiguous alias, contradictory platform constraints | Negotiation does not silently downgrade security or misstate capability |
| RESOURCE-01 | Inputs within declared bounds | Oversized/deep JSON, duplicate keys, invalid Unicode, decompression bomb, hostile external reference | Parser is bounded, deterministic, offline by default, and performs no implicit fetch |

## 6. Capability manifest research gate

Before drafting a schema, publish a use-case record answering:

- Which independent implementations exchange capability information?
- Is this install-time platform compatibility, runtime feature negotiation, API discovery, or multiple distinct problems?
- What stable feature identifier namespace and governance model will be used?
- How are required, optional, experimental and deprecated features represented?
- What happens when a consumer encounters an unknown required feature?
- How are OS/architecture constraints distinguished from runtime capabilities?
- How is downgrade resistance addressed?
- Can a client validate a manifest offline?

The manifest must not carry credentials, trust roots, private policy or authorization claims. JSON Schema 2020-12 may validate structure, but normative semantics and compatibility behavior require their own specification.

## 7. Reproducibility and public evidence

Each fixture and run records:
- fixture ID/version and synthetic-data declaration;
- upstream specification and exact revision/version;
- fixture SHA-256 digest;
- tool/version and invocation;
- operating system, architecture and runtime;
- expected and observed results;
- stdout/stderr or equivalent logs;
- exit status, limitations and reviewer disposition.

The initial suite must run offline. TUF tests use a local test repository and disposable test trust configuration. No production key may appear in fixtures. Test keys must be disposable and isolated from any real trust store.

Statuses remain separate: PROPOSED, FIXTURE_DRAFTED, IMPLEMENTED, EXECUTED, PASSED, FAILED, VERIFIED, ACCEPTED, RELEASED. A passing schema check does not prove complete inventory, authentic provenance, trusted signer, safe update, or maintainer acceptance.

## 8. Sequenced next work

1. Create a synthetic dependency graph and evaluate CycloneDX 1.7 generation and validation.
2. Validate SPDX 3.0.1 tooling and identify practical profile/serialization interoperability.
3. Build an in-toto/SLSA provenance example with synthetic artifact and explicit builder identity.
4. Evaluate DSSE verification using disposable test keys and a local trust policy.
5. Build a local TUF repository and test metadata verification, root rotation and rollback rejection.
6. Complete capability-manifest prior-art/use-case analysis before authoring a schema.
7. Package public-safe vectors and expected results for independent implementations.
8. Update the Component Traceability Matrix only after evidence exists; do not count research as implementation.

## 9. Open decisions and limitations

- Which SPDX 3.0.1 serialization/profile and validators are supported across target languages?
- Does CycloneDX CLI cover all needed 1.7 semantics and provide adequate generation for the target build ecosystem?
- Which build platforms can produce independently verifiable SLSA provenance?
- Which DSSE trust and identity model will be supported without centralizing authority?
- How will TUF metadata integrate with different package formats, bootloaders and recovery systems?
- Is a distinct capability manifest justified after reviewing existing platform/API descriptors?
- Which independent implementations can execute the same vectors?

## 10. Current disposition

This document is a public-interface research baseline and proposed test plan. No SBOM format is finally selected; no fixtures, keys, schemas, verifiers, updater, or conformance suite are implemented or executed. No public release or cross-OS exchange is authorized. The next work is synthetic fixture construction and tool evaluation, beginning with SBOMs.
