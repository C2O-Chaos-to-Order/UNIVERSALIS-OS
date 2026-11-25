# Contextual Expression Register

**Register release:** 1.0.3 (baseline status-code boundaries clarified)  
**Canonical source:** `Alchemy Taxonomies/Alchemy Taxonomy for the Universal Subjects of Knowledge/ALCHEMY_TAXONOMY_FOR_THE_UNIVERSAL_SUBJECTS_OF_KNOWLEDGE.md`  
**Canonical source version:** 1.13.8  
**Canonical source blob SHA:** `3e7c570943b4e65307f01618ac81b031051ad1a9`

## Purpose and scope

This register tracks the individually required contextual expressions for every unique subject Alchemy in the Universal Subjects of Knowledge taxonomy.

The canonical source contains **20 supplied top-level subject hierarchies**, **272 hierarchy positions**, and **264 unique subject-Alchemy identities**. Eight identities have more than one top-level hierarchy membership; each remains one canonical subject Alchemy and is registered once. Every unique subject Alchemy is mapped to all **22 canonical contexts**, yielding **5,808 unique subject–context records**.

The existing 20 domain matrices were checked against the canonical context key: 272 matrix rows occur across the 20 hierarchies, each with 22 mapped positions. The eight shared identities recur as hierarchy references; the unique node index contains 264 identifiers. The register therefore contains 264 × 22 = 5,808 unique records, without double-counting shared identities.

**This register is a tracking structure, not a set of completed contextual expressions.** Every row begins with mapping recorded and expression authoring, review, evidence assessment, owner acceptance, implementation, and publication authorization left pending or unasserted.

## Stable record identity

Each record uses `{subject_alchemy_id}-{context_id}`, for example `USA-FS-001-C01`.

This is a tracking identifier only. It does not create a new Universal Subject, Alchemy, operating system, application, intelligence, assistant, or guardian. The canonical subject name, Alchemy name, definition, and hierarchy membership remain in the canonical source node index. Context names resolve through the crosswalk below.

## Canonical context crosswalk

| Context ID | Canonical context name |
|---|---|
| C01 | C2O Operating System |
| C02 | UNIVERSALIS Operating System |
| C03 | C2O Intelligence |
| C04 | UNIVERSALIS Intelligence |
| C05 | C2O Application |
| C06 | UNIVERSALIS Application |
| C07 | C2O Operating System — UNIVERSALIN |
| C08 | UNIVERSALIS Operating System — UNIVERSALIN |
| C09 | C2O Application — UNIVERSALIN |
| C10 | UNIVERSALIS Application — UNIVERSALIN |
| C11 | C2O Operating System — UNIVERSALIN Intelligence |
| C12 | UNIVERSALIS Operating System — UNIVERSALIN Intelligence |
| C13 | C2O Application — UNIVERSALIN Intelligence |
| C14 | UNIVERSALIS Application — UNIVERSALIN Intelligence |
| C15 | C2O Operating System — UNIVERSALIN Guardian |
| C16 | UNIVERSALIS Operating System — UNIVERSALIN Guardian |
| C17 | C2O Application — UNIVERSALIN Guardian |
| C18 | UNIVERSALIS Application — UNIVERSALIN Guardian |
| C19 | C2O Operating System — UNIVERSALIN Guardian Intelligence |
| C20 | UNIVERSALIS Operating System — UNIVERSALIN Guardian Intelligence |
| C21 | C2O Application — UNIVERSALIN Guardian Intelligence |
| C22 | UNIVERSALIS Application — UNIVERSALIN Guardian Intelligence |

## CSV schema

| Field | Meaning |
|---|---|
| `expression_record_id` | Stable subject–context tracking identifier |
| `subject_alchemy_id` | Canonical ID from the source node index |
| `context_id` | C01–C22 context key |
| `mapping_status` | `M`: mapping is recorded in the source matrix |
| `expression_status` | `NA`: contextual expression not yet authored |
| `review_status` | `NR`: contextual expression not yet reviewed |
| `evidence_status` | `NE`: expression evidence not yet assessed |
| `owner_acceptance` | `P`: owner acceptance pending |
| `implementation_status` | `NI`: implementation is not asserted by this register |
| `publication_authorization` | `P`: publication authorization pending |
| `testing_status` | `Not yet tested`: no testing outcome has been recorded |
| `verification_status` | `Not yet verified`: no verification outcome has been recorded |
| `canonical_source_version` | Exact version of the canonical taxonomy used for this record |
| `canonical_source_blob_sha` | Git blob SHA identifying the exact canonical taxonomy file used for this record |
| `contextual_definition` | Context-specific definition; blank until authored |
| `purpose_and_responsibilities` | Context-specific purpose and responsibilities; blank until authored |
| `scope_and_exclusions` | Contextual scope and explicit exclusions; blank until authored |
| `operations_and_processes` | Context-appropriate operations and processes; blank until authored |
| `relationships_and_dependencies` | Relationships and dependencies; blank until authored |
| `authority_permissions_constraints` | Context authority, permissions, and constraints; blank until authored |
| `inputs_outputs_effects` | Relevant inputs, outputs, and effects; blank until authored |
| `evidence_and_validation` | Supporting evidence and validation criteria; blank until authored |
| `supporting_sources` | Traceable supporting sources; blank until sourced |
| `limitations` | Limitations, uncertainty, and unresolved points; blank until assessed |

## Required content for each contextual expression

Each record must be individually authored from the actual Universal Subject and the exact selected context. It must include:

1. The exact canonical subject-Alchemy identity and context identity.
2. The context-specific definition.
3. Purpose and responsibilities.
4. Scope and exclusions.
5. Operations and processes.
6. Relationships and dependencies.
7. Authority, permissions, and constraints.
8. Inputs, outputs, and effects.
9. Supporting evidence and validation criteria.
10. Supporting sources, limitations, uncertainty, and unresolved points.

Do not mechanically copy a generic paragraph across the 22 contexts. Shared subject identity does not imply identical responsibilities, operations, authority, implementation, or source visibility.

## Status codebook and separation

The register keeps these states separate:

- Mapping (`M`) records the existing source-matrix assignment.
- Expression (`NA`) records that detailed expression authoring has not yet been completed.
- Review (`NR`) records that no review outcome has been recorded.
- Evidence (`NE`) records that supporting evidence for the expression has not yet been assessed.
- Owner acceptance (`P`) remains pending.
- Implementation (`NI`) is not asserted.
- Publication authorization (`P`) remains pending.

A change to one state must not silently change another.

**Codebook release boundary.** This release defines `M` as the only permitted `mapping_status` value. For `expression_status`, `review_status`, `evidence_status`, `owner_acceptance`, `implementation_status`, and `publication_authorization`, the values listed above are the baseline values currently assigned in this register; this release does not define a complete lifecycle or authorize additional values or transitions. Until a subsequent controlled codebook revision defines permitted values, transition conditions, required supporting records, decision authority where applicable, and change-history requirements—and that revision has been reviewed and explicitly accepted—retain these baseline values. Do not invent codes, infer a state change from the presence of another record, or advance a field to imply progress. Substantive work or decisions may be recorded in linked records without changing these register fields until the codebook is extended and accepted. The testing and verification fields are separate: their permitted values are explicitly enumerated below, and every change still requires its own traceable test or verification record.

Testing and verification are recorded in their own fields and use separate controlled values. The permitted testing values are:
- `Not yet tested`: no test has been performed or recorded.
- `Testing in progress`: testing has begun but has no completed outcome.
- `Tested — passed`: the defined test criteria were met; the supporting test record must be traceable.
- `Tested — failed`: the defined test criteria were not met; the failure and evidence must be retained.
- `Testing blocked`: testing could not proceed; the blocking condition must be recorded.

The permitted verification values are:
- `Not yet verified`: no verification outcome has been recorded.
- `Verification in progress`: verification has begun but has no completed outcome.
- `Verified`: the defined verification criteria were met; the supporting verification record must be traceable.
- `Verification failed`: the defined verification criteria were not met; the failure and evidence must be retained.
- `Verification blocked`: verification could not proceed; the blocking condition must be recorded.

Testing values describe test execution and its outcome. Verification values describe the independent confirmation against specified requirements or evidence. A passed test does not automatically mean verified, and verification does not imply implementation, owner acceptance, or publication authorization. The initial values in all 5,808 rows are `Not yet tested` and `Not yet verified`; these record the absence of recorded outcomes and do not claim that testing or verification has occurred. A value may change only when its own traceable record supports the change. A record must not be marked authored, reviewed, evidenced, accepted, implemented, verified, or authorized without its own supporting record and appropriate approval. Testing and verification remain distinct from implementation and from one another; neither is represented by reusing an existing CSV status code. Until separately recorded in traceable supporting records, neither should be inferred as completed.

## Edition and visibility boundaries

Expressions must preserve the C2O private-source and UNIVERSALIS public/open-source edition boundaries. Public expressions must not expose private C2O implementation details, credentials, confidential operational evidence, or private policies. UNIVERSALIS expressions must remain understandable and usable without access to C2O private implementation repositories.

The register does not authorize publication or distribution. Rights and licensing must follow the applicable rights-holder authority, the dual-licensing-by-edition policy, and third-party terms.

## Controlled authoring sequence

1. Select a bounded group of canonical subject Alchemies.
2. Confirm each subject's supplied definition and hierarchy placement.
3. Author context-specific expressions in bounded batches, retaining each record ID.
4. Identify sources, evidence, limitations, and context boundaries.
5. Review each expression independently.
6. Record owner acceptance separately from technical review.
7. Record implementation, testing, verification, and publication authorization only when independently evidenced and approved.
8. Preserve a traceable change history.

## Source and completion boundary

Each CSV row carries the canonical source version and exact source-file Git blob SHA so that the record remains provenance-identifiable when separated from this Markdown companion. All rows currently identify version `1.13.8` and blob `3e7c570943b4e65307f01618ac81b031051ad1a9`. The source taxonomy version 1.13.8 records the canonical subject and context structure used for this register. The register's 5,808 rows were checked against that source: all 264 subject-Alchemy identifiers are present, all 22 context identifiers are represented, and all 5,808 subject–context record identifiers are unique. This confirms the register's identity and context coverage; it does not claim that any detailed contextual expression has been authored, reviewed, evidenced, accepted, implemented, tested, verified, or authorized.
