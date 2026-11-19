# UNIVERSALIS-OS Public Interoperability Contract Register

**Document ID:** UOS-INTEROP-001  
**Version:** 0.1.0  
**Status:** Proposed public-interface governance baseline; not owner-accepted or released  
**Target branch:** `foundation/architecture-baseline-2026-11-19`  
**Date:** 2026-11-19

## 1. Purpose

This register defines how UNIVERSALIS-OS may publish and consume optional interoperability contracts while remaining an independently governed and independently operable operating system. It describes a public-facing contract process, not a dependency on C2O-OS and not an authorization to publish this repository or any source material.

UNIVERSALIS-OS must be usable by people and implementations that have no relationship with C2O. C2O may participate as an external contributor or optional consumer under the same public rules as any other participant.

## 2. Independence requirements

1. No C2O account, service, key, policy, private infrastructure, telemetry, or repository access may be required to build, install, boot, operate, update, or recover UNIVERSALIS-OS.
2. Public contract definitions must be complete, inspectable, versioned, and testable without private C2O material.
3. UNIVERSALIS-OS defines its own maintainers, contribution process, release decisions, security response, and compatibility policy.
4. C2O has no special approval, veto, publication, roadmap, or governance authority over UNIVERSALIS-OS.
5. C2O-originated proposals are reviewed on their public merits, provenance, rights, security, interoperability, and maintenance cost.
6. Any C2O integration is an optional adapter that can be disabled or removed without reducing core OS operation.
7. A public contract does not imply that a corresponding implementation exists, is secure, or has been certified.

## 3. Contract classes

| Class | Meaning | UNIVERSALIS-OS treatment |
|---|---|---|
| PUBLIC-CANDIDATE | Non-sensitive interface with a plausible multi-implementer use case | May be specified and reviewed for public adoption |
| PUBLIC-ADOPTED | Explicitly accepted, rights-cleared and versioned public contract | May be implemented according to its normative specification |
| OPTIONAL-ADAPTER | Integration with an external system | Disabled by default; isolated, scoped, revocable |
| PRIVATE-EXCLUDED | Private data, credentials, policies, incident records, or proprietary authority | Must not enter public specification, fixtures, builds, telemetry, or release artifacts |
| UNRESOLVED | Ownership, semantics, rights, privacy, security, or use case is unclear | No implementation or publication |

## 4. Candidate public contract catalogue

These are candidate subjects, not approved APIs or protocols.

| Contract ID | Candidate subject | Potential public value | Minimum portable specification | Exclusions / caution | State |
|---|---|---|---|---|---|
| UOS-CTR-001 | Version and capability manifest | Discovery and safe feature negotiation across implementations | Stable contract ID, semantic version, feature identifiers, required/optional fields, error rules | No C2O-specific feature requirement or endpoint | PROPOSED |
| UOS-CTR-002 | Artifact identity and provenance envelope | Reproducible identification and evidence lineage | Content digest, media type, source/version locator, build/tool identity, timestamp semantics, provenance status | Never require private source locators or credentials | PROPOSED |
| UOS-CTR-003 | Signed artifact/attestation envelope | Portable verification of artifact claims | Algorithm identifiers, subject digest, predicate type, signer reference, verification and revocation semantics | Trust roots configured locally; no shared C2O root | UNRESOLVED |
| UOS-CTR-004 | Security finding taxonomy | Consistent interchange of security findings | Stable categories, severity vocabulary, component references, evidence classes | Do not publish sensitive incident details by default | UNRESOLVED |
| UOS-CTR-005 | Audit event interchange | Portable, privacy-aware event exchange | Event type, event time, clock semantics, actor/object classes, integrity metadata | No default telemetry export or raw private logs | UNRESOLVED |
| UOS-CTR-006 | SBOM and dependency metadata | Supply-chain transparency | Selected standard and version, component identifiers, hashes, licenses, relationships | Per-file and transitive license review remains necessary | PUBLIC-CANDIDATE |
| UOS-CTR-007 | Resource/health telemetry | Optional diagnostics and optimization | Units, aggregation, sampling, opt-in, retention and deletion semantics | No mandatory telemetry; no user-level tracking by default | UNRESOLVED |
| UOS-CTR-008 | Knowledge, claim and evidence record | Portable, reviewable knowledge exchange | Claim type, source, evidence class, uncertainty, status, version, correction/retraction | No unsupported universal claims or unlicensed Human Tablet material | UNRESOLVED |
| UOS-CTR-009 | Scoped capability request | Interoperation with optional external services | Purpose, target, scope, expiry, revocation, local authorization result | No ambient authority, shared identity or automatic trust | UNRESOLVED |
| UOS-CTR-010 | Package/update metadata | Interoperable package verification and rollback | Digest, version, platform constraints, signature metadata, rollback semantics | UNIVERSALIS retains independent update authority | PUBLIC-CANDIDATE |
| UOS-CTR-011 | Security advisory/incident notice | Responsible public disclosure and downstream response | Minimal advisory identifiers, severity, affected versions, remediation and disclosure status | Private incident evidence remains private absent explicit disclosure review | UNRESOLVED |
| UOS-CTR-012 | Remote cross-OS administration | No justified public value under current boundary | None | Shared control plane, remote privileged commands, policy mutation and kill-switch control are excluded | EXCLUDED |

## 5. Governance and contribution rules

- UNIVERSALIS-OS maintainers and its explicitly adopted governance process own public contract acceptance and lifecycle decisions.
- Contributors, including C2O, may submit proposals, code, tests, or review comments but receive no special authority by virtue of affiliation.
- Every contribution must identify authorship, source revision, license, NOTICE obligations, third-party dependencies, and any restrictions.
- No C2O-private document, key, policy, incident, account, evidence record, or repository locator may be used as a normative dependency or hidden test input.
- A proposal must remain reproducible from public or explicitly licensed inputs.
- Maintainers may reject, revise, defer, fork, or retire a proposal. A contributor may decline to maintain an optional adapter.
- No contract is “UNIVERSALIS standard” until an explicit decision, specification version, conformance suite, and release record exist.

## 6. Contract acceptance lifecycle

1. **Use case:** identify multiple plausible independent implementers and a concrete interoperability problem.
2. **Scope:** specify actors, data, trust boundaries, threat model, privacy class, exclusions, and non-goals.
3. **Prior-art review:** compare established standards and justify any new format.
4. **Specification:** define normative semantics, schema, canonicalization, errors, versioning, extension rules, and examples.
5. **Rights review:** establish authorship, licensing, attribution, NOTICE, and dependency obligations.
6. **Security/privacy review:** evaluate misuse, replay, spoofing, leakage, downgrade, resource exhaustion, consent and retention.
7. **Reference implementation:** provide a replaceable implementation that is not privileged by specification.
8. **Conformance suite:** publish positive, negative, malformed, boundary, adversarial, and compatibility vectors.
9. **Independent implementation:** seek an independent implementation or record why one is not yet available.
10. **Maintainer decision:** record accept/reject/defer with rationale and scope.
11. **Release and maintenance:** publish only under an explicit license/release authorization; define support, deprecation, vulnerability and migration policy.

Passing tests does not establish legal rights, security certification, or acceptance. A draft is not a standard.

## 7. Optional external adapters

An adapter to C2O or any other external system must:
- be a separate, replaceable module and disabled by default;
- use only public, documented contracts;
- require local user/administrator authorization and narrow capabilities;
- keep trust roots, credentials, and policy decisions local to UNIVERSALIS;
- disclose all data flows and provide export minimization and opt-out;
- operate with timeouts, bounded resources, rate limits and failure isolation;
- function without the external peer and recover cleanly after disconnection;
- be removable without changing the core OS contract or data model;
- never grant an external party remote administration or policy authority.

## 8. Public/private data firewall

Never include the following in public contracts, test fixtures, build artifacts, examples, logs, or release metadata without a separately documented and authorized disclosure decision:
- C2O private policies, identity records, account data, private keys, credentials, trust roots;
- private incident records, operational evidence, raw security telemetry;
- private Human Tablet content, consent records, personal data;
- unreleased research material, private source paths, repository URLs, internal deliberations;
- private service names or endpoints that could reveal sensitive topology.

Redaction is not automatically anonymization. Hashes and metadata can disclose identity, linkage, or existence. Review inference risk as well as direct content.

## 9. Independence and conformance tests

Future tests must prove:
- build and operation without any C2O credentials, services, DNS, endpoints, network routes or repository access;
- no mandatory C2O dependency in manifests, code, configuration, CI, update, recovery or documentation;
- public schemas and fixtures validate in a clean environment without private access;
- external signatures are rejected unless locally trusted by explicit UNIVERSALIS configuration;
- optional adapters can be disabled, revoked and removed without core failure;
- synthetic private canary data does not leak through exports, errors, logs, telemetry or SBOM metadata;
- unsupported major contract versions fail safely and minor-version extensions follow documented rules;
- peer failure, malformed payloads, compromised adapters and network loss cannot escalate privilege or block local recovery.

Tests are NOT_STARTED until executed and recorded with exact environment, inputs, outputs, logs, digests and review status.

## 10. Open decisions

- Which candidates solve a real interoperability problem for more than one independent implementer?
- Which existing standards should be adopted (including SBOM and provenance formats) rather than replaced?
- What public governance, maintainer succession and vulnerability-disclosure process will be adopted?
- Which licenses and contribution terms will apply to specifications, implementations, fixtures and documentation?
- Which contract versions, support windows and deprecation rules are sustainable?
- Is any external adapter justified after standalone operation is proven?

## 11. Current disposition

This register is a proposed public-interface governance baseline. It does not establish a public license, make the currently private repository public, accept any contract, authorize data exchange, or grant C2O authority. The default is independent operation with no external connection. Every contract remains proposed, unresolved, or explicitly excluded until separately specified, reviewed, accepted, implemented, and tested.
