# UNIVERSALIS-OS Implementation Sequence

**Document ID:** UOS-PLAN-001  
**Version:** 0.1.0  
**Status:** Proposed sequence — gated, not a completion report  
**Date:** 2026-11-19

## Governing rule

Build UNIVERSALIS-OS in this repository as the independently governed public system implementation target. Under MPR-053/054, migrate all eligible public UNIVERSALIS artifacts into one canonical UNIVERSALIS-OS or UNIVERSALIS-App home by system versus user-facing responsibility, using artifact-level move/adapt/split/link decisions and preserving source provenance/history. Exclude C2O-private material. Until a destination batch is accepted and verified, the legacy repository remains the source of origin and an untouched history snapshot. Do not create a parallel permanent software product in a legacy research repository.

## Work sequence and exit gates

### Gate 0 — Architecture, openness, and scope
- Confirm product boundary: native kernel, existing-kernel distribution, hosted environment, or staged hybrid.
- Define initial reference platform, virtual machine, hardware scope, and portability claims.
- Research Windows, macOS, Linux/BSD, and OS-development approaches comparatively; do not copy proprietary internals.
- Resolve license, contribution, provenance, trademark, security disclosure, and release-governance requirements before public release.
- Complete ADRs for boot, kernel/host strategy, language/toolchain, security model, storage, IPC, updates, and UI.
- Exit only when each decision has rationale, alternatives, risks, evidence, and review.

### Gate 1 — Reproducible development foundation
- Establish repository layout, contribution rules, threat model, coding standards, build scripts, static analysis, test harness, and CI.
- Pin toolchain versions; define reproducible builds and dependency provenance.
- Plan SBOM, signing, release attestations, vulnerability reporting, and support lifecycle.
- No privileged component before its design and threat review.

### Gate 2 — Smallest executable vertical slice
- Implement one safe, non-privileged local service or hosted prototype selected by Gate 0 ADR.
- Demonstrate configuration, structured logging, documented API/IPC, test isolation, failure handling, and reproducible build.
- Run automated tests in CI and publish evidence without claiming broader OS functionality.

### Gate 3 — Portable core services
- Implement services justified by the chosen strategy: identity, permissions, storage, IPC, device abstraction, networking, process lifecycle, update, recovery, and diagnostics.
- Keep platform-specific code behind adapters and verify compatibility claims on declared targets.

### Gate 4 — User environment and application model
- Build session, shell/UI, accessibility, settings, application lifecycle, package/install model, and developer interfaces.
- Enforce application isolation, permissions, capability negotiation, and resource limits.

### Gate 5 — UNIVERSALIS capabilities
- Integrate knowledge registries, research execution, Alchemy runtime, transformation pipelines, simulation, evidence/provenance, and reporting as isolated portable services.
- Implement from reviewed specifications; do not treat proposed models as established fact.
- Add domain-specific, adversarial, offline, portability, and recovery tests.

### Gate 6 — Hardening and release readiness
- Complete threat modeling, secure boot/update review, dependency and supply-chain review, independent security testing, backup/recovery drills, performance/resource tests, accessibility, and compatibility testing.
- Complete license/provenance/privacy review and explicit owner authorization before public release.

## Initial repository layout (target, not yet created)

```text
/
├── README.md
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── security/
│   ├── governance/
│   └── research-integration/
├── boot/                 # only if selected by architecture decision
├── kernel/               # only if selected by architecture decision
├── platform/
├── services/
├── runtime/
├── shell/
├── applications/
├── tests/
├── tools/
└── .github/workflows/
```

Do not create empty directories as a substitute for working components. Add each directory with its first real, scoped artifact.

## Status discipline

A document or directory is not implementation. A source file is not a passing test. A passing test is not independent verification. A branch is not a merge. A draft is not an accepted architecture. An open repository is not automatically an open-source release.
