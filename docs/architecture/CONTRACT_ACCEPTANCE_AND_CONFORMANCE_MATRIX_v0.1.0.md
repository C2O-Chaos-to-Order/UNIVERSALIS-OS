# UNIVERSALIS-OS Contract Acceptance and Conformance Matrix

**Document ID:** UOS-CONFORMANCE-001  
**Version:** 0.1.0  
**Status:** Proposed public-interface engineering requirements; not owner-accepted, implemented, or released  
**Date:** 2026-11-19  
**Target branch:** `foundation/architecture-baseline-2026-11-19`

## 1. Purpose and independence guarantee

This matrix converts proposed public interoperability subjects into bounded, testable requirements. It is not a public standard, publication authorization, license grant, or approval to exchange data with C2O.

UNIVERSALIS-OS must be independently buildable, operable, updateable, and recoverable without C2O accounts, repositories, services, keys, policies, telemetry, private infrastructure, or personnel. Its public contracts must be complete and testable by unrelated implementers.

## 2. Research baseline and proposed reuse

| Area | Reference baseline | Proposed UNIVERSALIS posture | Limitation |
|---|---|---|---|
| Interface versioning | Semantic Versioning 2.0.0 | Use SemVer for stable public APIs where applicable; separately version schemas and protocol revisions | A version label is not proof of compatibility |
| Provenance | SLSA 1.2 Build Provenance; in-toto Statement | Prefer established subject/predicate provenance and verifiable build claims | Provenance claims require authenticated builder identity and verification policy |
| Attestation envelope | in-toto / DSSE ecosystem | Adopt established envelope formats where fit; no proprietary signature envelope without demonstrated gap | Trust roots are configured independently by each consumer |
| SBOM | SPDX 3.0.1; CycloneDX 1.7 (ECMA-424) | Publish at least one standards-compliant SBOM format for releasable artifacts; evaluate second-format support | SBOM validity does not prove completeness or license compliance |
| Update metadata | The Update Framework (TUF), current specification | Evaluate TUF for signed metadata, delegation, expiry and rollback-resistant update discovery | Installation, atomicity, recovery and platform integration require additional design |
| Secure development | NIST SP 800-218 SSDF 1.1 final; SP 800-218 Rev. 1 / SSDF 1.2 initial public draft | Use final 1.1 as baseline guidance; track Rev. 1 draft as draft-only watch item | Do not describe the draft as finalized |

Primary references:
- https://semver.org/spec/v2.0.0.html
- https://slsa.dev/spec/v1.2/
- https://slsa.dev/spec/v1.2/build-provenance
- https://spdx.dev/use/specifications/
- https://ecma-international.org/publications-and-standards/standards/ecma-424/
- https://theupdateframework.github.io/specification/latest/
- https://csrc.nist.gov/pubs/sp/800/218/final
- https://csrc.nist.gov/pubs/sp/800/218/r1/ipd

## 3. Public contract acceptance matrix

| ID | Contract family | Reuse before inventing | Minimum portable requirement | Required negative tests | Initial disposition |
|---|---|---|---|---|---|
| UNI-CTR-001 | Version and capability manifest | SemVer for interface/package version; declared schema language for structural validation | Stable contract ID; schema version; implementation version; feature identifiers; required/optional feature distinction; platform constraints; explicit unknown-feature behavior | Unknown major version; missing required field; duplicate feature; malformed version; unsupported required capability; downgrade attempt | PROPOSED |
| UNI-CTR-002 | Artifact identity and provenance | SLSA 1.2 and in-toto Statement | Artifact digest; media type; public source/material references; builder identity; invocation; timestamp semantics; predicate type; verification status | Digest mismatch; missing material; fabricated builder; timestamp inconsistency; source revision mismatch; tampering | PROPOSED |
| UNI-CTR-003 | Signed artifact/attestation envelope | DSSE/in-toto ecosystem; TUF for update repository metadata | Signed payload binding; subject digest; algorithm identifiers; signer reference; locally configured trust and revocation semantics | Invalid signature; wrong subject; untrusted signer; revoked key; replay/expiry; downgrade; duplicate signer counting | RESEARCH REQUIRED |
| UNI-CTR-004 | SBOM and dependency metadata | SPDX 3.0.1 and CycloneDX 1.7 | Component identity/version/supplier, license expression, hashes, dependency relationships, generation metadata, known incompleteness | Invalid schema; missing identifiers; contradictory hashes; omitted known dependency; invalid license; hostile external reference | PUBLIC-CANDIDATE |
| UNI-CTR-005 | Package/update metadata | TUF; platform-specific package formats behind replaceable adapters | Package digest/version/platform constraints; signature metadata; trusted metadata version/expiry; rollback semantics; recovery behavior | Expired metadata; rollback/freeze; mix-and-match; substitution; threshold failure; compromised mirror; interrupted update | PUBLIC-CANDIDATE |
| UNI-CTR-006 | Conformance/test-vector package | Published schemas and upstream format-specific vectors | Versioned positive/negative fixtures, expected outcomes, fixture provenance and deterministic offline runner | Parser differential; oversized/deep payload; duplicate keys; invalid Unicode; resource exhaustion; canonicalization ambiguity | PROPOSED |

No new capability manifest schema should be created until a multi-vendor/multi-implementation use case and a genuine standards gap are documented.

## 4. Normative design constraints

1. **Independent governance:** UNIVERSALIS maintainers and its adopted governance process decide acceptance, release, compatibility, and deprecation.
2. **No C2O dependency:** every public schema, example, test vector, build, and conformance runner must work without private C2O access.
3. **No implicit trust:** version, name, URL, digest, publisher label, or key identifier alone does not authenticate or authorize an artifact.
4. **Digest verification:** recompute declared artifact digests over the exact specified byte representation before acceptance.
5. **Identity separation:** artifact identity, publisher identity, builder identity, signer identity, and local trust decision are separate.
6. **Local trust roots:** trust configuration belongs to the UNIVERSALIS installation/operator; C2O keys are not trusted by default.
7. **Fail safely:** unsupported required features, invalid signatures/digests, expired metadata, and rollback attempts reject the operation.
8. **Resource bounds:** specify maximum payload sizes, nesting, collection counts, timeouts, decompression limits, and external-reference behavior.
9. **No implicit fetching:** parsers must not dereference arbitrary URLs in manifests, SBOMs or attestations. Fetching is a separate policy-controlled action.
10. **Privacy and rights:** do not publish personal data, private repository paths, credentials, unreleased research, or uncleared third-party material.
11. **Immutable releases:** published versions are immutable; corrections require a new version and a traceable release record.
12. **Status separation:** schema-valid, signature-valid, locally trusted, maintainer-accepted, implemented, tested and released are distinct states.

## 5. Public acceptance criteria

| ID | Acceptance criteria | Evidence required | Status |
|---|---|---|---|
| UNI-CTR-001 | Independent clients can discover supported contract versions/features and safely reject unsupported required capabilities | Public schema, examples, compatibility rules, test vectors, independent client run | NOT_STARTED |
| UNI-CTR-002 | Provenance subject digest matches bytes and source/material/build claims are internally consistent | SLSA/in-toto fixtures, digest verification output, verification report | NOT_STARTED |
| UNI-CTR-003 | Signature verification binds exact payload to signer and consumer-local trust policy | Threat model, trust configuration, key rotation/revocation tests, invalid-signature fixtures | NOT_STARTED |
| UNI-CTR-004 | A release artifact has a valid SBOM in the selected published format and known synthetic dependency graph is represented accurately | SPDX/CycloneDX validator output, dependency reconciliation, license review | NOT_STARTED |
| UNI-CTR-005 | Update client rejects invalid, expired, substituted and rolled-back metadata while preserving recovery | TUF verification evidence, adversarial fixtures, interrupted-update and recovery tests | NOT_STARTED |
| UNI-CTR-006 | Public test suite is deterministic, offline-capable, bounded and independently reproducible | Runner, fixture digests, environment record, independent repeat-run report | NOT_STARTED |

## 6. Threat and failure coverage

Model at minimum: compromised publisher, compromised build worker, stolen signing key, malicious mirror, replay/rollback/freeze, dependency confusion, parser differential, malicious SBOM/attestation, SSRF through external references, decompression bomb, oversized/nested input, clock skew, interrupted installation, corrupted local trust state, unauthorized trust-root replacement, and malicious adapter.

A passing schema validator is not a security assessment. Public conformance claims must state what was tested, what was not tested, and under which assumptions.

## 7. Implementation sequence

1. Identify a real public interoperability use case and independent implementers for each contract family.
2. Publish a standards comparison with selection rationale and known gaps.
3. Select an initial SBOM output format; document import/export interoperability goals for the other.
4. Define a minimal capability manifest only if existing standards do not meet the demonstrated use case.
5. Publish synthetic fixtures and adversarial negative vectors before implementation.
6. Implement offline parsers and verifiers as unprivileged, replaceable components.
7. Design update trust-root lifecycle and recovery before integrating platform installers.
8. Obtain independent implementation and conformance evidence.
9. Complete governance, licensing, provenance, security and privacy reviews before any public release.

## 8. Evidence and status rules

Every conformance run records: contract ID/version; source revision; upstream specification revision; toolchain; environment; fixture digests; command; inputs; outputs; exit status; logs; limitations; reviewer; and disposition. Failed tests remain in the record. Re-runs do not erase failures.

Statuses: PROPOSED, RESEARCHED, SPECIFIED, IMPLEMENTED, TESTED, VERIFIED, ACCEPTED, RELEASED, DEPRECATED, REJECTED, UNRESOLVED. No state is inferred from another.

## 9. Open decisions

- Which SBOM format is the initial release requirement, and which formats must be accepted on import?
- Which builder identities and provenance claims can be independently verified?
- What key custody, threshold, rotation, backup, revocation and recovery design is appropriate?
- Which platform package/update systems can be safely adapted to TUF metadata verification?
- Does the capability manifest solve a demonstrated gap?
- What public governance, contribution, license, maintainer succession and vulnerability disclosure policies will apply?
- What independent implementations are available to validate portability?

## 10. Current disposition

All six contract families remain proposed or research-required. No public standard is declared adopted; no schema, code, key, updater, SBOM generator, attestation verifier, or conformance suite is claimed implemented. No publication or cross-OS exchange is authorized. The next deliverable is a standards comparison and synthetic conformance fixture plan—not privileged runtime code.
