# UNIVERSALIS-OS Architecture Baseline

**Document ID:** UOS-ARCH-001  
**Version:** 0.1.0  
**Status:** Initial architecture baseline — proposed, not accepted  
**Branch:** `foundation/architecture-baseline-2026-11-19`  
**Date:** 2026-11-19

## 1. Mission and boundary

UNIVERSALIS-OS is the independently operable, open-source-intended operating-system project of the UNIVERSALIS ecosystem: a unified architecture and intelligence environment designed to be portable across devices, vendors, languages, and hardware classes.

UNIVERSALIS-OS must function without C2O accounts, keys, services, policies, private infrastructure, or telemetry. Its governance, security, release process, and technical operation must remain independently defined. The repository is currently private; no public release or license status is implied by this architecture document.

This repository is the implementation target. Encyclopedias and research registers are source material, not substitutes for implementation.

## 2. Architecture principles

1. **Independent operation:** no mandatory C2O runtime, identity, policy, account, key, service, or telemetry dependency.
2. **Open inspectability:** intended public interfaces, formats, build instructions, tests, and design decisions should be inspectable when licensing and provenance are cleared.
3. **Portability:** device-, vendor-, architecture-, and host-specific behavior is isolated behind explicit adapters.
4. **Local-first:** core capabilities operate locally; network services are optional and replaceable.
5. **Least privilege and isolation:** user-space services, sandboxing, capability-based permissions, and small privileged boundaries.
6. **Modular interfaces:** documented APIs and versioned contracts; implementations can be replaced.
7. **Reproducible and verifiable builds:** pinned toolchains, dependency provenance, SBOM, signed artifacts, tests, and release attestations.
8. **Accessible extensibility:** clear application/runtime interfaces and accessible user interaction.
9. **Evidence traceability:** requirements map to ADRs, code, tests, and release evidence.
10. **No unearned claims:** proposed, designed, implemented, tested, verified, reviewed, accepted, licensed, and released are distinct states.

## 3. Layered target architecture

The following is a logical architecture, not a claim that these components exist yet.

- **Hardware / host adapters:** CPU architecture, firmware/boot interface, devices, storage, network, power, and input/output.
- **Boot and trust chain:** selected boot model, verified startup, recovery, and trusted update.
- **Kernel or host-platform boundary:** scheduling, memory isolation, interrupts, device access, system calls, and privilege boundary. Implementation strategy remains open.
- **Portable core services:** storage, device discovery, IPC, networking, identity, authorization, configuration, events, time, logging, update, and recovery.
- **Universal runtime:** application lifecycle, task execution, service discovery, capability negotiation, and portable APIs.
- **Knowledge and transformation services:** registries, semantic models, research workflows, transformation operations, simulations, verification, and evidence. These run as isolated services, not kernel primitives.
- **User environment:** shell/UI, sessions, accessibility, settings, and developer experience.
- **Applications and extensions:** independently permissioned, portable modules.
- **Build, test, release and operations:** reproducible builds, SBOM/provenance, signing, compatibility tests, diagnostics, rollback, and release authorization.

## 4. Placement of Elemental Alchemy and knowledge systems

Alchemy and knowledge systems are portable domain services within UNIVERSALIS-OS, not the kernel or hardware abstraction layer.

The five primary labels, 31 compositions, seven transformation operations, and interaction matrices are proposed research inputs. Runtime implementation must:
- use stable identifiers and versioned schemas;
- distinguish composition membership from operation sequence and execution history;
- require domain-specific semantics and observable evidence;
- keep symbolic classification separate from empirical causation;
- expose portable, documented interfaces;
- support local execution and user-controlled data;
- record provenance, uncertainty, failures, and review state;
- avoid asserting universal applicability from a single domain's test.

The canonical research records remain in the approved research/encyclopedia repository. UNIVERSALIS-OS contains the portable implementation, tests, adapters, and public-facing contracts only after provenance, licensing, privacy, and security review. A reference to a private C2O repository is not a public dependency.

## 5. Security and independence boundaries

- No C2O private keys, policies, accounts, incident data, or telemetry are imported.
- No C2O service is required at install, boot, runtime, update, or recovery.
- Users control local data and optional remote integrations.
- Privileged operations require transparent authorization and auditable execution.
- Applications and agents are unprivileged by default and receive scoped capabilities.
- External services and dependencies are replaceable, with offline/recovery behavior documented.
- Kernel-mode code is minimized; prefer isolated user-space services where the platform permits.
- Publication requires license, provenance, security, privacy, and owner review.

## 6. Architecture decisions still open

No kernel, bootloader, instruction-set target, programming language, package manager, filesystem, GUI stack, or distribution model is selected by this baseline. These must be decided through explicit Architecture Decision Records after comparative research and prototype criteria are agreed.

The first blocking decision is the product boundary:
- native bootable OS with its own kernel;
- OS distribution/platform built on an existing kernel;
- hosted/local-first environment integrating with existing host OSs;
- or a staged combination with a declared reference platform and portability boundary.

Do not describe UNIVERSALIS-OS as bootable, universally compatible, open-source licensed, or hardware-supported until those claims are evidenced and authorized.

## 7. Implementation evidence

Each component must have: requirement ID, design/ADR reference, owner, threat model, interface contract, source files, tests, test environment, build provenance, known limitations, review state, license/provenance state, and acceptance record.

Current repository state at baseline: only the initial README exists on `main`; this branch introduces architecture documentation only. No OS runtime, kernel, service, installer, or build pipeline is claimed implemented.
