# UNIVERSALIS-OS

**UNIVERSALIS-OS** is the independently operable, open-source-intended operating-system project of the UNIVERSALIS ecosystem.

## Project boundary

UNIVERSALIS-OS is intended to provide a portable, local-first, vendor- and device-agnostic operating environment. It must operate independently of C2O accounts, services, keys, policies, private infrastructure, and telemetry.

**Repository visibility is currently private.** This README does not grant a license or authorize public release.

## Repository structure

- `docs/architecture/ARCHITECTURE_BASELINE_v0.1.0.md` — proposed layered architecture and unresolved platform decisions.
- `docs/IMPLEMENTATION_SEQUENCE_v0.1.0.md` — gated implementation sequence and target layout.


- `docs/architecture/SOURCE_PLACEMENT_AND_MIGRATION_REGISTER_v0.1.0.md` — initial source inventory and migration controls; partial audit, no transfer authorized.

## Current status

**Status:** Proposed architecture baseline.

The default `main` branch contains only the initial repository README. The architecture baseline is being developed on `foundation/architecture-baseline-2026-11-19`. No kernel, runtime, system service, installer, or bootable image is claimed implemented. No public license or release is asserted.

## Development rules

- Implement UNIVERSALIS-OS functionality here as an independent project.
- Do not import C2O private keys, policies, accounts, incident data, services, or telemetry.
- Keep platform-specific behavior behind documented adapters.
- Require ADRs, tests, threat models, reproducible builds, dependency provenance, and independent review.
- Clear licensing, provenance, privacy, and security before public release.

See [Architecture Baseline](docs/architecture/ARCHITECTURE_BASELINE_v0.1.0.md) and [Implementation Sequence](docs/IMPLEMENTATION_SEQUENCE_v0.1.0.md).
