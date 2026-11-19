# UNIVERSALIS-OS

**UNIVERSALIS-OS** is the independently operable, open-source-intended operating-system project of the UNIVERSALIS ecosystem.

## Project boundary

UNIVERSALIS-OS is intended to provide a portable, local-first, vendor- and device-agnostic operating environment. It must operate independently of C2O accounts, services, keys, policies, private infrastructure, and telemetry.

**Repository visibility is currently private.** This README does not grant a license or authorize public release.

## Repository structure

- `docs/architecture/ARCHITECTURE_BASELINE_v0.1.0.md` — proposed layered architecture and unresolved platform decisions.
- `docs/IMPLEMENTATION_SEQUENCE_v0.1.0.md` — gated implementation sequence and target layout.
- `docs/architecture/SOURCE_PLACEMENT_AND_MIGRATION_REGISTER_v0.1.0.md` — initial source inventory and migration controls; partial audit, no transfer authorized.
- `docs/architecture/PLATFORM_STRATEGY_RESEARCH_v0.1.0.md` — preliminary platform strategy comparison; not an ADR or platform selection.
- `docs/architecture/COMPONENT_TRACEABILITY_MATRIX_v0.1.0.md` — initial requirement-to-component, source, interface, implementation, verification and acceptance traceability; proposed and incomplete.
- `docs/audits/UNIVERSALIS_SOURCE_REPOSITORY_AUDIT_2026-11-19.md` — partial file/tree and integration-branch audit of the legacy UNIVERSALIS source repository; no files transferred.
- `docs/audits/UNIVERSALIS_RESEARCH_SOURCE_AUDIT_2026-11-19.md` — partial audit of Reports 13–15, the 15 proposed requirements, research gaps, and the changed OS implementation target.

## Current status

**Status:** Proposed architecture baseline.

The default `main` branch contains only the initial repository README. The architecture baseline is being developed on `foundation/architecture-baseline-2026-11-19`. No kernel, runtime, system service, installer, or bootable image is claimed implemented. No public license or release is asserted.

## Development rules

- Implement UNIVERSALIS-OS functionality here as an independent project.
- Do not import C2O private keys, policies, accounts, incident data, services, or telemetry.
- Keep platform-specific behavior behind documented adapters.
- Require ADRs, tests, threat models, reproducible builds, dependency provenance, and independent review.
- Clear licensing, provenance, privacy, and security before public release.

See [Architecture Baseline](docs/architecture/ARCHITECTURE_BASELINE_v0.1.0.md), [Implementation Sequence](docs/IMPLEMENTATION_SEQUENCE_v0.1.0.md), the [Source Repository Audit](docs/audits/UNIVERSALIS_SOURCE_REPOSITORY_AUDIT_2026-11-19.md), and the [Research Source Audit](docs/audits/UNIVERSALIS_RESEARCH_SOURCE_AUDIT_2026-11-19.md).
