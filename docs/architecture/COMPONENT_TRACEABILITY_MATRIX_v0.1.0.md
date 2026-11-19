# UNIVERSALIS-OS Component Traceability Matrix

**Document ID:** UOS-TRACE-001  
**Version:** 0.1.0  
**Status:** Initial engineering traceability baseline — proposed, incomplete, not owner-accepted  
**Target branch:** `foundation/architecture-baseline-2026-11-19`  
**Snapshot:** 2026-11-19  
**Authority:** This matrix governs traceability within the UNIVERSALIS-OS proposal only. It does not authorize source transfer, implementation, merge, publication, deployment, or release.

## 1. Purpose and boundary

UNIVERSALIS-OS is intended to be an independently operable public OS. It must not require C2O accounts, services, private keys, policy stores, telemetry, infrastructure, or access to private repositories. Any public-safe shared contract must be independently specified and implemented; it must not create a runtime dependency on C2O.

This matrix maps each proposed UNIVERSALIS requirement to a subsystem, interface, candidate source, implementation disposition, and verifiable acceptance evidence. It also maps the existing public product source candidates. All requirements in the source register remain `PROPOSED`; none is accepted merely by appearing here.

**Status vocabulary:** `PROPOSED`, `SOURCE_ONLY`, `NOT_STARTED`, and `UNRESOLVED` are planning states. No row is marked implemented, tested, verified, accepted, or released.

## 2. Pinned source baseline

| Source | Exact inspected ref | Role and limitation |
|---|---|---|
| `Research-for-the-UNIVERSALIS-Ecosystem` | main `b6fea0452aafc574f8259740c2f35cfae1c71706`; draft PR #14 head `085b27732f61533104ffe7b02ebba145ed907e25` | Reports 13–15 and 15-row requirements register. All requirements proposed. PR #14 is draft/unmerged. |
| `The-UNIVERSALIS-Ecosystem` | main `e484dd73417d3e50ff0fa5d78186cbf577f78f06`; draft PR #23 head `16d9e9eaba8416926b9f2195ceea03972cca56dd` | Public product code, schemas, tests, scaffold and prototype. Apache-2.0 LICENSE and NOTICE observed; per-file rights, dependencies, security and provenance still require review. PR #23 is draft/unmerged. |
| UNIVERSALIS-OS architecture | branch `foundation/architecture-baseline-2026-11-19` | Architecture baseline is proposed; platform/kernel/toolchain decisions remain open. |
| C2O private source | Excluded by default | No private C2O content, credentials, identifiers, locators or service dependencies may enter the public OS. |

The pinned repository commits are audit anchors, not file-level transfer packets. Each adopted file needs its own path/blob SHA, copyright/author, license, dependency and modification record. Preserve applicable Apache-2.0 LICENSE and NOTICE obligations for any derivative use of the legacy public product code.

## 3. Requirements traceability: UNI-001–UNI-015

The requirement text and acceptance evidence below follow `REGISTERS/UNIVERSALIS_REQUIREMENTS_v0.1.0.csv` at main commit `b6fea0452aafc574f8259740c2f35cfae1c71706`, blob `6f428b2c829ef258721c86d7a5b73a7995b21137`. Source requirement statuses are all PROPOSED.

| Requirement | Requirement and source scope | UNIVERSALIS-OS subsystem | Candidate contract / implementation | Acceptance evidence from source register | State |
|---|---|---|---|---|---|
| UNI-001 | Preserve system boundaries and typed relationships; mappings do not imply identity or erase differences. | Core domain model / ontology boundary | Typed entity and relationship schema; explicit mapping semantics | Boundary and mapping tests; documented exclusions | PROPOSED |
| UNI-002 | Declare initialization state, environment prerequisites and readiness separately from authorization. | Bootstrapping / readiness / identity-policy boundary | Startup state machine and readiness contract; authorization remains separate | Initialization and readiness tests | PROPOSED |
| UNI-003 | Persist records only under explicit durability, capacity, provenance and retention contracts. | Storage / temporal record | Versioned persistence schema and retention policy | Crash/restart and retention/deletion tests | PROPOSED |
| UNI-004 | Enforce identity, purpose, scope, permission, provenance and resource limits before retrieval or disclosure. | Identity, policy and retrieval gateway | Authenticated principal context; deny-by-default policy interface; pre-retrieval filtering | Positive/negative access tests; leakage tests | PROPOSED |
| UNI-005 | Preserve event, record, ingestion and applicability time plus governed correction/retraction history. | Temporal record / provenance | Temporal event and revision model | Temporal and branching-history tests | PROPOSED |
| UNI-006 | Declare measurement and inference assumptions; expose uncertainty and support abstention. | Epistemic projection / intelligence interface | Claim/evidence/uncertainty types and abstention result | Calibration, uncertainty, invalid-input and abstention tests | PROPOSED |
| UNI-007 | Expose missing, disputed, stale, invalidated, inaccessible and incomplete information with full denominators. | Evidence views / user interface | Explicit evidence-state vocabulary and coverage denominator | Coverage and accessibility tests | PROPOSED |
| UNI-008 | Separate readiness, authorization, invariant compatibility, commit, failure, recovery, acceptance and release. | Lifecycle orchestration / assurance | Distinct state machines and signed decision records | State-transition, failure-injection and rollback tests | PROPOSED |
| UNI-009 | Preserve consent, privacy, refusal, withdrawal, non-coercion and human accountability. | Human interface / privacy lifecycle | Consent and purpose records; correction, refusal and withdrawal paths | Policy tests and approved human evaluation | PROPOSED |
| UNI-010 | Monitor capability sharing, resource use, performance and ongoing integrity without self-certification. | Operations / diagnostics / capability control | Resource budgets, telemetry minimization and independent integrity evidence | Resource benchmarks, least-privilege and monitoring review | PROPOSED |
| UNI-011 | Separate event chronology, observation, coordinate description, inference and causal claims. | Domain and temporal data model | Typed claim categories and timestamp semantics | Temporal semantics and claim-type tests | PROPOSED |
| UNI-012 | Do not use quantum or entropy terminology outside a declared model and valid domain. | Modeling / domain validation | Domain-scoped model contracts and terminology metadata | Domain/type validation and terminology review | PROPOSED |
| UNI-013 | Keep chemical/biological models within evidenced domain; do not infer software life or consciousness from analogy. | Modeling / claim review | Evidence class and domain applicability contract | Claim classification and review | PROPOSED |
| UNI-014 | Preserve failure evidence and versioned acceptance history; regression or revocation changes current eligibility without erasing history. | Assurance / audit / recovery | Append-only decision history with governed correction and revocation | Incident, rollback, revocation and audit tests | PROPOSED |
| UNI-015 | Prevent coercive dependency and ensure capability sharing remains bounded, revocable and overseen. | Governance / capability broker / inter-system boundary | Scoped, expiring, revocable capability contract; no ambient authority | Abuse-case and dependency review | PROPOSED |

## 4. Product source-to-component mapping

Source: `The-UNIVERSALIS-Ecosystem` main commit `e484dd73417d3e50ff0fa5d78186cbf577f78f06`. The table is preliminary; no source code is copied by this matrix.

| Existing source component | Observed source paths / state | Target UNIVERSALIS-OS component | Disposition | Required gate before use |
|---|---|---|---|---|
| Engineering Doctor | `engineering_doctor/`; read-only Python inventory/reporting CLI; tests and run-record schema; documented as LIMITED / PUBLIC_CANDIDATE | Developer/operator observability tool | Adapt selectively | Per-module review; credential/output privacy; rate-limit and pagination behavior; dependency/test audit; portability; least-privilege read-only scope |
| Tool/evidence registry | `registry/`; JSON records, schemas and stdlib validators | Artifact/evidence registry contracts and service | Adapt schema/validation patterns | Schema dialect and semantic review; stable identifiers; provenance, lifecycle and authority separation; migration and adversarial tests |
| Knowledge records | `knowledge/`; record schema, validator and three records | Public knowledge-data contracts and validator | Adapt selectively | Source rights, semantics, provenance, claim classes, versioning, fixture review; do not infer a complete ontology/runtime |
| Research scaffold | `scaffold/`; corpus-agnostic package template, schemas, tools and tests | Research/developer tooling | Retain source; port bounded utilities | Reconcile with UNIVERSALIS-OS source boundary; verify public-only corpus controls, source locators, release gate and reproducible tests |
| Continuity prototype | `prototype/universalis/`; SQLite store, states, coverage, failures, invalidation, presentation, stewardship and trajectory; explicit bounded prototype | Read-only continuity/knowledge service | Reimplement/adapt selected models; do not transplant wholesale | Review schema/migrations, concurrency, authz stubs, caller-supplied facts, privacy, threat model and complete test corpus |
| Construction engine | PR #23 integration branch only; declarative non-executing generator and hash manifest | Build/developer tooling | Hold pending review | Resolve legacy coupling; path normalization, symlink, overwrite, manifest tampering, atomicity, permission and output-root confinement tests |
| Security/provisioning schemas | PR #23 integration branch; proposed contracts and fixtures, no proof of deployed enforcement | Portable security contracts and platform research | Research/adapt selected contract patterns | Verify trust roots, signature semantics, replay/expiry, key custody, bypass/fail-open, threat model and independent tests |
| Held workflows | PR #23 lists 32 workflow/script paths held pending owner decisions | CI and release workflows | Do not activate by default | Owner disposition; permissions, action pinning, triggers, secrets, branch protection and test review |
| Platform/OS candidate inventory | PR #23 integration branch; candidate tools and virtualization/provisioning plans | Platform adapter / platform ADR research | Research only | Verify upstream status, license, support, threat boundary, hardware/guest support and reproducible behavior |

Repository-level Apache-2.0 does not automatically clear every embedded file or third-party dependency. Any adapted files must preserve required notices, attribution and modification notices; inspect per-file provenance and dependency licensing before transfer.

## 5. Explicit engineering obligations from Report 13

Source: Report 13 at main commit `b6fea0452aafc574f8259740c2f35cfae1c71706`, blob `fe5bf638a46b859ad39caa5864cdd8e9b3415db5`. These are open gaps, not completed tests.

| Gap | Required implementation/test work | Closure evidence |
|---|---|---|
| G13-A — Forecast input-domain validation | Enforce probability [0,1], binary outcome {0,1}, numeric types, finite values, nonempty/equal-length arrays; reject bool/string/null/NaN/infinity/out-of-range/malformed input | Executed boundary and mutation tests, independent reproduction, exact environment and digest |
| G13-B — Approval-consumption validity | Build genuinely stateful reservation/consumption harness; test sequential reuse, concurrent reservations, revocation races, crash during consumption, restart recovery, exact-action binding, audit/policy failure | Durable state and concurrency evidence; fail-closed outcomes; independent security review |
| G13-C — Tablet clause-level lineage | Reconcile source lineage, renames, editions, technical/Human pairs and clause differences; preserve unresolved conflicts | Complete clause-level matrix with source pins and conflict dispositions; independent review |

Report 13's 107 research assessments and 107 finite-model records are candidate evidence, not independent studies, reproductions, empirical validation or accepted credit. Do not treat their existence as closure of any G13 gap.

## 6. Platform and OS foundation traceability

The OS substrate is not yet selected. These foundational requirements must be resolved through ADRs before a bootable product or privileged implementation is claimed.

| Foundation ID | Decision / requirement | Target | Required evidence | State |
|---|---|---|---|---|
| UOS-PLAT-001 | Product form: native kernel, mature-kernel distribution, hosted environment or staged hybrid | Product boundary | Comparative decision record with explicit user goals, cost, risk, maintainability and portability | UNRESOLVED |
| UOS-PLAT-002 | Reference VM/hardware, CPU architecture, firmware and boot path | Boot/platform adapters | Tested VM target and documented hardware support criteria | UNRESOLVED |
| UOS-PLAT-003 | Kernel/host boundary, isolation, driver model and privilege architecture | Platform/kernel boundary | Threat model, alternatives, isolation prototype and recovery plan | UNRESOLVED |
| UOS-PLAT-004 | Language/toolchain, package/dependency model and reproducible builds | Build engineering | Pinned toolchain, clean rebuild and dependency/SBOM plan | UNRESOLVED |
| UOS-PLAT-005 | Storage, IPC, networking, identity, update and recovery design | Core services | ADRs, interface contracts, failure and offline tests | UNRESOLVED |
| UOS-PLAT-006 | UI/session/accessibility and application permission model | User environment | Accessibility, app isolation, resource and user-control test plan | UNRESOLVED |
| UOS-PLAT-007 | Public release governance, license, NOTICE, SBOM, signing and vulnerability response | Release engineering | Rights review, provenance, security disclosure and release authorization | UNRESOLVED |

## 7. First vertical slice proposed by source evidence

Subject to owner acceptance and a Gate 0 architecture decision, the strongest first candidate is a **local-first, read-only continuity and evidence service using synthetic data only**:

1. Typed source, claim, evidence, identity-context and temporal records.
2. Local source registry with exact source/version locators.
3. Explicit deny-by-default policy interface outside any language model.
4. Temporal history with correction/retraction and retention controls.
5. Deterministic evidence projection exposing unknown, missing, stale, disputed and inaccessible states.
6. Read-only retrieval interface with exact citations and honest retrieval-failure states.
7. Audit, privacy lifecycle, recovery and regression tests.

This is a candidate service above the OS substrate, not a kernel capability. No real-user data, hosted provider, consequential action, or public pilot is authorized by this matrix.

## 8. Acceptance record required per component

Each component needs:
- Stable UNI/UOS requirement IDs and source rationale.
- Exact source repository/ref/commit/path/blob SHA, author, license and NOTICE obligations.
- Public/private classification and proof that no private C2O material or locator is present.
- Owner, subsystem, threat model, data flows, permissions and dependency inventory.
- Versioned interface/schema and compatibility policy.
- Copy/adapt/reimplement/retain/reject decision.
- Executed positive, negative, boundary, adversarial, privacy, recovery and portability tests as appropriate.
- Exact environment, inputs, outputs, logs, artifact digest and limitations.
- Independent review, owner acceptance and separate publication/release authorization.

## 9. Open blockers

- All UNI-001–UNI-015 remain PROPOSED in the source register.
- The source product repo still describes itself as the implementation home; transition to UNIVERSALIS-OS needs a separately reviewed plan.
- Legacy product PR #23 and research PR #14 remain draft/unmerged; held workflows are not approved.
- Full per-file licensing, NOTICE, provenance, dependency and security review is outstanding.
- G13-A, G13-B and G13-C remain open.
- Platform/kernel/boot/toolchain/storage/network/UI ADRs are not selected.
- No code migration, kernel, OS service, installer, bootable image, public release or deployment is claimed.

**Current matrix disposition:** proposed engineering traceability baseline only. It preserves source lineage, keeps all 15 source requirements proposed, and explicitly separates public product implementation from private C2O authority.
