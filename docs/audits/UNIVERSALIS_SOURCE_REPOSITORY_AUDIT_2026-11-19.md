# UNIVERSALIS Source Repository Audit — 2026-11-19

**Target:** `C2O-Chaos-to-Order/UNIVERSALIS-OS`  
**Source examined:** `C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem`  
**Audit class:** Partial source-to-component audit; read-only inspection  
**Decision:** No source files transferred. No adoption, acceptance, release, or migration authorized by this record.

## 1. Scope and reproducibility anchors

The source repository's `main` tree was read recursively from commit `e484dd73417d3e50ff0fa5d78186cbf577f78f06`: 220 entries, not truncated.

The open draft master-integration PR is [#23](https://github.com/C2O-Chaos-to-Order/The-UNIVERSALIS-Ecosystem/pull/23), head branch `integrate/master-2026-11-16`, head `16d9e9eaba8416926b9f2195ceea03972cca56dd`. Its recursive tree contained 343 entries, not truncated. The PR changes 84 paths and its commit listing returned 100 entries on the first page. Its description explicitly says it is draft, must not be merged without owner review, and must use a merge commit (not squash or rebase) if separately authorized.

The repository exposes 25 branches in the inspected branch listing. This audit does not establish that every branch, tag, release, historical commit, or closed PR has been reviewed. PR #23 describes two earlier PRs (#20 and #21) folded into its integration branch and lists 32 workflow/script paths held pending owner decisions C-12a/b. Two workflow paths in that list are reported by the PR as byte-identical to the active main baseline. Treat the hold list as a review queue, not approval to activate those workflows.

## 2. Main-branch inventory

The 220-entry main tree includes:

- `engineering_doctor/` — 41 entries.
- `scaffold/` — 79 entries.
- `prototype/` — 40 entries.
- `registry/` — 17 entries.
- `knowledge/` — 19 entries.
- `foundation/` — 8 entries.
- `ARCHITECTURE/` — public repository/tooling contracts and schemas.
- `.github/workflows/` — two workflows.
- `tools/cross_repo_checker.py`.

No root `pyproject.toml`, `requirements.txt`, `package.json`, `Cargo.toml`, or `go.mod` appeared in the recursive main tree. Engineering Doctor has an optional, hash-pinned pytest/Hypothesis extra; its core and the other inspected Python components describe standard-library operation. The active repository-verification workflow installs PyYAML 6.0.2 for changed-file checks. A complete dependency/SBOM inventory has not yet been produced.

The repository has an Apache-2.0 LICENSE and a NOTICE file. The NOTICE identifies Engineering Doctor and the UNIVERSALIS Ecosystem contributors. This is a useful repository-level starting point, not a substitute for per-file copyright/author/provenance checks, dependency-license review, attribution retention, and review of any content with separate rights. Any derivative redistribution must preserve applicable Apache-2.0 notices and NOTICE attributions and mark modified files as required by the license.

## 3. Component disposition matrix

| Source component | Observed role/status | Preliminary disposition for UNIVERSALIS-OS | Gate before use |
|---|---|---|---|
| Engineering Doctor | Read-only Python repository inventory/reporting CLI; explicitly LIMITED / PUBLIC_CANDIDATE | **Adapt** as a developer/repository observability utility; not an OS kernel or privileged control plane | Review every module, API/rate-limit behavior, credential handling, output privacy, branch coverage, test provenance, and operating-system portability |
| Tool/evidence registry | JSON records, schemas, fail-closed stdlib validators; LIMITED | **Adapt** its schema/validation patterns into a versioned artifact and evidence registry | Reconcile schema dialect/coverage, identifiers, trust/authority semantics, migrations, signature/provenance model, and registry lifecycle |
| Knowledge records | Small public knowledge-record schema/validator and three records | **Adapt selectively** as knowledge-data contracts, not as a universal ontology or full knowledge runtime | Validate semantics, provenance, source rights, interpretation classes, versioning, and separation of data from executable behavior |
| Research/evidence scaffold | Corpus-agnostic package template, research/simulation records, validators, provenance rules | **Retain as source; adapt selected tooling** to a research/developer subsystem | Keep private corpora outside public builds; verify Plan conformance, public-release gate, source locators, and status separation |
| Continuity prototype | SQLite-backed records/claims/dependencies, failure/invalidation/presentation and stewardship/trajectory modules; explicitly bounded prototype | **Reimplement/adapt selected models**; do not transplant as the OS core | Review storage model, migrations, concurrency, access controls, caller-supplied facts, authorization stub, threat model, and complete test corpus |
| Construction Engine (PR #23 branch only) | Dependency-free declarative file generator with hash manifest; non-executing | **Hold / adapt only after hardening** | Resolve C2O naming and target-ecosystem coupling; test symlink and overwrite behavior, path normalization, manifest tampering, atomicity, permissions, and output-root confinement |
| Platform/OS provisioning architecture (PR #23 branch) | Proposed virtualization and guest-provisioning architecture; candidates not yet verified | **Research/specification input only** | Independently verify each upstream project, license, release, guest support, threat boundary, and reproducible behavior; decide OS substrate through a separate ADR |
| Security/cybersecurity architecture and contracts (PR #23 branch) | Public schemas/fixtures and proposed controls; document states third-party tools are not installed/integrated | **Adapt contract patterns; do not claim enforcement** | Independently review schemas, crypto/proof semantics, key custody, replay/expiry, trust roots, enforcement location, bypass/fail-open behavior, and adversarial tests |
| Construction/architecture schemas and fixtures (PR #23 branch) | Numerous domain-specific schemas, fixtures, architecture and validation documents | **Selective reference / possible contract candidates** | Reconcile with new OS architecture and ontology; verify semantic coverage, consistency, provenance, fixture quality, and owner decisions |
| Held-back `.github` contracts/workflows | Explicitly withheld in PR #23 pending C-12a/b | **Do not activate or port by default** | Owner decision plus isolated workflow security review, permissions audit, action pinning, trigger review, and test evidence |
| Domain/Guardian/website/immersive tool inventories | Candidate lists and conceptual architecture; many upstreams remain unverified | **Research backlog only** | Exact canonical upstream, active maintenance, license, security, compatibility, privacy, and independent test required |

## 4. Findings that materially affect migration

### 4.1 This source repository is not yet the OS implementation

The inspected main tree and PR #23 integration tree contain meaningful Python utilities, schemas, evidence tooling, fixtures, and architecture documents. They do not establish a bootable operating system. The inspected inventory did not identify a kernel, bootloader, OS image build, hardware driver stack, init/service manager, package manager for an OS distribution, installer, or hardware compatibility suite. This is a scoped tree finding, not proof that no such work exists in any uninspected branch or external source.

### 4.2 Repository role is now inconsistent with the new two-OS plan

At this audit snapshot, the main README described this repository as the UNIVERSALIS product source home, including implementation code, specifications, tests, workflows, packages, and release artifacts. That conflicts with the decision to make UNIVERSALIS-OS the system implementation target. A later owner-approved migration plan establishes the four OS/App destinations and artifact-level batch gates. The detailed per-file destination map, licensing/provenance review, release continuity, and legacy README transition remain open. Do not change the legacy README or move/delete content until the relevant batch is reviewed and verified.

### 4.3 Construction Engine has a boundary and filesystem review issue

The PR #23 branch's engine uses the module name/CLI `c2o-build`, a `c2o-build-spec/v0.1` format, and accepts `target_ecosystem` values `universalis` and `c2o`. This is not evidence of private data leakage, but it creates avoidable identity and boundary ambiguity in a public UNIVERSALIS tool. The output writer also needs explicit review for symlink traversal, existing-file overwrite, output-root confinement, atomic writes, and manifest self-consistency before use with untrusted specifications. Its current tests include a basic `../` traversal rejection and tamper detection; those do not settle the broader filesystem threat model.

### 4.4 Security architecture documents are not deployed security controls

The PR #23 security architecture describes useful separation of policy evaluation, interception, telemetry, approval, and hard enforcement. Its validation record expressly states that no scanner, gateway, eBPF program, sandbox, DPU watchdog, SBOM generator, signature service, or vulnerability database was installed or invoked by that change. Portable contract validation and CI are not equivalent to runtime enforcement, penetration testing, security certification, or OS hardening.

### 4.5 Existing evidence has a narrow scope

The repository documents tests and CI receipts for particular commits and components. Those receipts do not automatically apply to a new commit, the OS integration, a different Python/toolchain version, or a future port. The Engineering Doctor README itself says it scans configured repositories and default-branch content, not every feature branch, and does not verify authorization, scientific validity, independent review, or security certification.

## 5. Transfer packet required for every selected artifact

Before any source is copied, adapted, or reimplemented in UNIVERSALIS-OS, record:

1. Source repository, exact ref/branch/tag, commit SHA, repository-relative path, and source blob SHA.
2. Author/contributor and copyright notices; repository license, file-specific license, NOTICE obligations, and third-party dependency licenses.
3. Source lineage and any derived/private origins; public-release clearance and privacy/security review.
4. Decision: retain as external source, copy, adapt, reimplement, reject, or unresolved—with technical rationale.
5. Target OS path and owning subsystem; public interface and compatibility/version policy.
6. Dependency inventory/SBOM, supply-chain provenance, build instructions, and reproducibility requirements.
7. Tests to rerun, new OS-specific tests, threat-model review, and known limitations.
8. Separate statuses for implementation, evidence, independent review, owner acceptance, programme credit, and release authorization.

## 6. Immediate next audit actions

1. Reconcile PR #23's full 84-file change set against its exact head and the current main baseline; inspect the remainder of its 343-entry tree and all held-back workflow/script paths.
2. Inspect source branches and relevant closed PRs for Engineering Doctor, registry, knowledge, scaffold, prototype, and construction-engine history; establish the exact commit/blob used for each candidate.
3. Perform per-module code review and run the source suites from a clean checkout at pinned commits; distinguish recorded CI receipts from newly reproduced tests.
4. Build a dependency, license, NOTICE, provenance, secret, and SBOM inventory for both main and the integration branch.
5. Reconcile public research requirements (including the UNIVERSALIS research reports) with actual source components before choosing any transfer.
6. Only after that audit, create the UNIVERSALIS-OS component mapping and implementation ADRs. No bulk migration.

## 7. Audit limits

This is a partial audit of the observed main tree, PR #23, selected files, and the returned branch inventory. It is not a complete history/branch/tag/release audit, legal opinion, security assessment, independent reproduction, or authorization. No source content was copied into UNIVERSALIS-OS by this audit.
