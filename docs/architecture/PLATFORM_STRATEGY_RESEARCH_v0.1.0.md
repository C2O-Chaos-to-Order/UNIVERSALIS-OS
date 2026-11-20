# OS Platform Strategy Research Brief

**Document ID:** UOS-PLATFORM-RESEARCH-001  
**Version:** 0.1.0  
**Status:** Preliminary comparative research — not an Architecture Decision Record  
**Research date:** 2026-11-19

## 1. Decision to be made

Choose the implementation boundary for UNIVERSALIS-OS:
1. A new native kernel and operating-system stack.
2. An OS distribution built around an established kernel.
3. A hosted operating environment running on an existing host OS.
4. A staged hybrid, with a hosted development prototype followed by a bootable distribution and a separately gated native-kernel research track.

No option is selected by this brief. The architecture baseline deliberately leaves kernel, boot, hardware target, language, toolchain, filesystem, and UI open.

## 2. Comparative assessment

| Criterion | Native kernel | Existing-kernel distribution | Hosted environment | Staged hybrid |
|---|---|---|---|---|
| Own boot and kernel control | Highest | Inherits selected kernel and boot stack | None | Grows by stage |
| Initial engineering scope | Very high | High, but bounded by upstream platform | Lowest | Controlled |
| Hardware/driver access | Must build or port drivers | Benefits from upstream drivers | Limited by host APIs | Starts host-limited, then inherits platform |
| User-space service freedom | Full, but must build base services | High | High within host constraints | High |
| Security boundary | Entire trusted computing base must be designed and maintained | Can leverage mature kernel isolation, but must configure and maintain it | Host controls core isolation | Incremental |
| Portability | Must port to each architecture/device family | Depends on kernel and upstream support | Depends on host OS/runtime | Can grow across adapters |
| Bootable product | Yes, after substantial work | Yes | No | Yes at distribution stage |
| Dependency risk | Toolchain, firmware, boot protocols, drivers, libraries | Upstream kernel, base distribution, packages | Host OS and runtime APIs | Explicitly managed by stage |
| Best fit | Unique kernel-level requirements and long-term kernel team | Practical first bootable product | Early UX/service prototyping | Current leading candidate for evaluation |

## 3. What the established platforms teach us

### 3.1 Privilege boundaries

Microsoft documents that user-mode processes have separate virtual address spaces, while kernel-mode components share a privileged address space; a kernel-mode driver fault can crash the entire OS. Microsoft also supports user-mode driver frameworks for suitable device classes. Apple's current guidance recommends DriverKit and system extensions in user space where possible, reserving kernel extensions for tasks that cannot be handled otherwise. These are strong reasons to keep our own privileged computing base small and place domain services, including Alchemy, in isolated user space wherever feasible.

### 3.2 Kernel development is a separate engineering programme

Linux maintains distinct documentation for architecture-specific interfaces, core and driver APIs, user-space APIs, build processes, testing, tracing, and development workflow. OSDev's bare-bones guidance emphasizes cross-compilation and using an existing bootloader/toolchain rather than trying to invent a compiler, bootloader, and kernel simultaneously. A native kernel is therefore not just another application module; it creates a substantial platform engineering and maintenance obligation.

### 3.3 Security and build provenance begin at project inception

NIST SSDF recommends integrating secure development practices throughout the software lifecycle. SLSA Build Provenance records where, when, and how artifacts were produced, with stronger levels adding authenticated provenance and hardened build environments. UNIVERSALIS-OS should design for threat modeling, dependency inventory, build provenance, test isolation, signing, and recovery from the beginning—not retrofit these after the first release.

## 4. Preliminary recommendation

Evaluate **an existing-kernel OS distribution as the first bootable product**, using a hosted prototype only as a short-lived development and validation harness. Do not begin by writing a new kernel.

For UNIVERSALIS-OS, this is a recommendation for the first implementation stage, not a permanent commitment to a particular kernel, distribution, vendor, or license. A native kernel remains a possible future research track only if measurable requirements cannot be met by the selected established kernel.

The first bootable target should be a declared virtual-machine reference platform. Physical hardware support should be added only after a specific device/architecture matrix is selected and tested.

## 5. Required decisions before implementation

The following must be answered in project-specific Architecture Decision Records:

1. Product boundary: distribution, hosted environment, native kernel, or staged hybrid.
2. Initial reference platform: virtual machine, CPU architecture, firmware/boot mode, and storage/network devices.
3. Kernel/base candidates and their support lifecycle.
4. License, notices, source obligations, patent terms, and dependency policy.
5. Language/toolchain and reproducible build strategy.
6. Boot, partitioning, filesystem, package/install, update, rollback, and recovery design.
7. Process isolation, IPC, identity, capabilities, privilege separation, and audit model.
8. User environment, accessibility, application model, and developer interface.
9. CI test matrix, emulation, hardware-in-loop strategy, SBOM, artifact signing, and provenance.
10. Exit criteria for expanding from VM to physical hardware.

No component should be selected because it is familiar or fashionable. Compare candidates against written requirements and evidence.

## 6. Initial development tool categories

The exact products are deferred until platform selection. The required categories are:

- Source control and reviewed change workflow.
- Cross-compilation-capable compiler/linker/assembler toolchain appropriate to the chosen kernel and target.
- Boot/firmware specifications and bootloader tooling.
- Virtual machine/emulator and debugging interface.
- Image/partition/filesystem construction and inspection.
- Static analysis, formatting, dependency and license scanning.
- Unit, integration, conformance, fuzz, fault-injection, and recovery testing.
- CI build isolation, SBOM generation, signing, and provenance attestation.
- Reproducible artifact storage, checksums, release manifests, and rollback verification.

## 7. Evidence and limitations

This is preliminary desk research, not a complete Windows/macOS/Linux/BSD platform comparison, not a threat model, and not an implementation decision. Product-specific comparisons, lifecycle/support research, licensing analysis, benchmark evidence, and prototype tests remain required.

## 8. Sources consulted

- Microsoft Learn, [User Mode and Kernel Mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode).
- Microsoft Learn, [Architecture of UMDF](https://learn.microsoft.com/windows-hardware/drivers/wdf/detailed-view-of-the-umdf-architecture).
- Apple Developer, [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/systemextensions/implementing-drivers-system-extensions-and-kexts).
- Linux Kernel Documentation, [The Linux Kernel documentation](https://docs.kernel.org/).
- OSDev Wiki, [Bare Bones](https://wiki.osdev.org/Barebones) and [Creating an Operating System](https://wiki.osdev.org/Creating_an_Operating_System). Community-maintained technical guidance, not a normative standard.
- NIST, [SP 800-218 Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final); [SP 800-218 Rev. 1 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd).
- SLSA, [Build Track Basics v1.2](https://slsa.dev/spec/v1.2/build-track-basics) and [Build Provenance v1.2](https://slsa.dev/spec/v1.2/build-provenance).

All sources accessed 2026-11-19.