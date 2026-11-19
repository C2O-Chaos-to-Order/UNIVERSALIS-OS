# UNIVERSALIS Research Source Audit — 2026-11-19

**Target:** `C2O-Chaos-to-Order/UNIVERSALIS-OS`  
**Source:** `C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem`  
**Audit class:** Partial requirements, reports, and integration-branch audit  
**Decision:** No research files transferred; no implementation, owner acceptance, or public release is implied.

## 1. Source state

The public research repository's `main` tree was inspected at `b6fea0452aafc574f8259740c2f35cfae1c71706`: 31 entries, not truncated. It contains:
- Reports 13, 14, and 15.
- A 15-row UNIVERSALIS requirements register; every requirement is `PROPOSED`.
- A research charter and repository/source-boundary governance documents.
- Golden Compass source/governance records and a manual repository-verification workflow.

The only open PR is [#14](https://github.com/C2O-Chaos-to-Order/Research-for-the-UNIVERSALIS-Ecosystem/pull/14), draft and unmerged, from `integrate/master-2026-11-16` at `085b27732f61533104ffe7b02ebba145ed907e25`. It changes 91 paths and reports 159 commits. Its tree contains 134 entries, including 76 research-package entries. Its description says prior PR work was consolidated, with specific workflow files held pending owner decisions; public text was also reworked to avoid direct references to private repository names/links.

## 2. Reports 13–15: useful substance, changed implementation destination

The three reports form a coherent, bounded research recommendation:

- **Report 13 — Requirements and Gap Analysis:** further research is required before claiming a secure real-world continuity/knowledge service. It identifies three material gaps: forecast input-domain validation; durable, stateful approval consumption; and clause-level Technical/Human Tablet lineage audit.
- **Report 14 — What to Build:** recommends a read-only, local-first, modular service that can establish what is recorded, its source/version, changes over time, uncertainty, and whether the current user may access it.
- **Report 15 — How to Build:** proposes typed records, a local source registry, explicit policy interface, temporal records, deterministic projections, citations, audit, privacy lifecycle, recovery, and regression tests. It prefers a modular monolith or well-separated library/service boundary initially, rather than premature microservices or custom cryptography.

All three reports remain proposed; independent review, owner acceptance, and implementation/release authorization are pending.

The reports were written when `The-UNIVERSALIS-Ecosystem` was described as the product implementation home. The new approved repository approach makes **UNIVERSALIS-OS** the implementation target. Therefore:
- Keep Reports 13–15 and the research evidence in this research repository.
- Translate accepted requirements into UNIVERSALIS-OS architecture decisions and traceability records.
- Implement the continuity/knowledge capability as a user-space service above the OS substrate, not as a kernel feature.
- Do not copy the reports wholesale into runtime code or treat their proposed architecture as already selected.

## 3. Requirements register

The current register contains 15 proposed requirements spanning:
- typed system boundaries and relationships;
- initialization/readiness versus authorization;
- persistence, durability, provenance, retention;
- identity, purpose, scope, permissions, and retrieval;
- temporal history, correction, and retraction;
- uncertainty, invalid inputs, and abstention;
- incomplete/disputed/stale/invalidated/inaccessible states;
- readiness, authorization, commit, failure, recovery, acceptance, and release;
- consent, privacy, refusal, and withdrawal;
- resource use and ongoing integrity;
- event chronology versus observation/inference/causality;
- model-domain boundaries for quantum, entropy, chemical, biological, and consciousness analogies;
- failure evidence, rollback, revocation, and bounded capability sharing.

Every row is currently `PROPOSED`. The tablet-pair references are research traceability inputs, not proof that the paired Tablets are authoritative or accepted. Each requirement needs a stable implementation ID, owning subsystem, acceptance tests, source pin, dependencies, threat model, and disposition in UNIVERSALIS-OS.

## 4. Research evidence and limitations

Report 13 describes 107 research assessments and 107 finite-model execution records across 11 model families. It explicitly says these mappings are internally consistent records, not independent studies, independent reproductions, empirical validation, or accepted programme credit. Preserve that distinction.

The reports identify:
- **G13-A:** forecast inputs must validate probability/outcome domains, numeric types, finite values, and malformed arrays.
- **G13-B:** approval consumption requires a genuinely stateful harness that tests sequential reuse, concurrency, revocation races, crashes, restart recovery, exact-action binding, and audit/policy failure.
- **G13-C:** a collection-level filename match is not a clause-level Tablet lineage audit; reconcile source lineage, renames, edition records, and pair differences without silently normalizing history.

These gaps are not closed merely because the reports or research package exist. Any future implementation must execute the specified tests and record exact source commit, environment, inputs, outputs, and limitations.

## 5. Public/private boundary observation

The current main README directly links to the private C2O Research Plan. PR #14's integration-branch rework replaces that direct link and private repository names with neutral public wording, stating that a private counterpart governs methodology and that public work must remain usable without access to private repositories.

The integration branch's version is a proposed draft and is not merged. Do not silently modify the public source repository during this audit. Before public release or any further public research changes, reconcile the README/report wording with the source boundary and ensure no private paths, credentials, source content, or internal identifiers are disclosed.

The research repository's own source-boundary document also states that the Technical/Human Tablet collections remain in the C2O research repository and are proposed contemporary research artifacts—not independent scientific authority, implementation proof, or permission to act.

## 6. Placement matrix

| Artifact | UNIVERSALIS-OS treatment |
|---|---|
| Reports 13–15 | Retain in research source; use as requirements/design inputs with exact source pins |
| 15-row requirements register | Convert to OS traceability records after requirement review; keep each current status proposed until accepted |
| Research charter | Retain as research governance; do not make it an OS runtime dependency |
| 107 assessment/execution records | Preserve as historical/synthetic evidence records with limitations; independently reproduce before credit |
| G13-A/B/C gaps | Create explicit engineering/test obligations; do not mark closed until tests execute and are reviewed |
| Public source-boundary text | Retain as governance source; reconcile proposed public wording before any release |
| Tablet-pair references | Preserve as provenance links; no automatic import of C2O-private content into UNIVERSALIS-OS |

## 7. Immediate next actions

1. Create a UNIVERSALIS-OS requirement traceability matrix from UNI-001–UNI-015, with exact source commit/blob pins and a proposed subsystem owner for each.
2. Map requirements to OS services: identity/policy, source/evidence registry, retrieval, temporal record, epistemic projection, human interface, audit/privacy/recovery.
3. Reconcile G13-A/B/C into executable acceptance tests and ensure they are not misrepresented as already closed.
4. Compare PR #14's public-safe wording changes against current main and decide their disposition through normal review; do not merge automatically.
5. Keep the first service read-only, local-first, and synthetic-data-only until its threat model, test evidence, privacy lifecycle, and authorization boundaries are accepted.

## 8. Audit limits

This is a partial audit of main, PR #14's integration tree/description, Reports 13–15, the requirements register, charter, and source-boundary text. It is not a complete review of every research-package file, a reproduction of the 107 executions, or an authorization. No research source files were copied into UNIVERSALIS-OS by this audit.
