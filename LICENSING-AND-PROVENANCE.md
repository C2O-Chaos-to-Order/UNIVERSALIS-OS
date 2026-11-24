# Licensing and Provenance — UNIVERSALIS-OS

**Policy decision:** Dual licensing by edition approved on 2026-11-24.  
**Repository role:** UNIVERSALIS public open-source edition repository.  
**Document status:** Adopted project policy and working provenance register. Rights clearance is incomplete; this document does not certify that every file is cleared for licensing.

## 1. Six-repository edition model

C2O and UNIVERSALIS are the private-source and open-source editions of the same underlying operating-system and application architecture.

| Repository | Role | Edition license model |
|---|---|---|
| `C2O-OS` | Public C2O OS project and documentation | C2O proprietary |
| `C2O-App` | Public C2O application project and documentation | C2O proprietary |
| `C2O-OS-Private-Implementation` | Private C2O OS implementation | C2O proprietary for C2O-exclusive implementation |
| `C2O-App-Private-Implementation` | Private C2O application implementation | C2O proprietary for C2O-exclusive implementation |
| `UNIVERSALIS-OS` | Public UNIVERSALIS OS edition | Apache-2.0 |
| `UNIVERSALIS-App` | Public UNIVERSALIS application edition | Apache-2.0 |

UNIVERSALIS must remain independently operable and must not require access to either C2O private implementation repository.

## 2. Dual licensing by edition

The project's intended policy for shared, rights-cleared C2O/UNIVERSALIS architecture and taxonomy materials is:

- **C2O edition:** proprietary licensing for the C2O distribution, issued only by the applicable rights holder or an authorized agent.
- **UNIVERSALIS edition:** Apache-2.0 licensing for the UNIVERSALIS distribution, issued only by the applicable rights holder or an authorized agent.
- **C2O-exclusive implementation:** private-source and proprietary, subject to the applicable rights holder's authority.
- **Third-party materials:** excluded from any blanket project grant and governed by their own licenses, permissions, and notices.
- **Contributor-created materials:** licensed only to the extent the contributor or other rights holder authorized the applicable grant.

This is an edition-based licensing policy, not a representation that every repository file has already passed rights clearance.

## 3. Existing Apache-2.0 grants are preserved

The UNIVERSALIS repositories contain Apache License 2.0. That license grants qualifying rights on a perpetual and irrevocable basis, subject to its terms. Nothing in a C2O proprietary notice, private-repository copy, policy document, or later repository change is intended to revoke, narrow, or add conditions to an Apache-2.0 grant already made for the same work or version.

Recipients who received a work under Apache-2.0 retain the rights granted by that license for that work, subject to its terms. A separate C2O proprietary licensing path may be offered for a C2O edition only where the applicable rights holder has authority to do so. A proprietary notice must not be used to imply that pre-existing Apache-2.0 permissions have disappeared.

The Apache-2.0 license text itself defines the scope and conditions of its grant. This document does not amend that license.

## 4. Shared taxonomy inventory and integrity evidence

The eight taxonomy collections are:

1. Alchemy Taxonomies
2. Meta Alchemy Taxonomies
3. Super Alchemy Taxonomies
4. Hyper Alchemy Taxonomies
5. Ultra Alchemy Taxonomies
6. Quantum Alchemy Taxonomies
7. Magic Alchemy Taxonomies
8. Transformative Alchemy Taxonomies

The canonical order places **Quantum before Magic**.

The live Git tree audit verified 416 taxonomy files and 344 taxonomy directories in each of the six repositories. The 416 taxonomy file blobs match across all six repositories at the time of this audit. The companion `RIGHTS-AND-PROVENANCE-REGISTER.csv` records each taxonomy path and its Git blob SHA.

**Integrity limitation:** matching paths and blob hashes prove that copies are identical. They do not prove who authored a file, who owns its copyright, whether its contents include third-party material, or whether a person has authority to license it.

## 5. Rights and provenance status

The file-level register currently marks taxonomy entries as pending. The following evidence is required before a row can be changed to verified:

- Original author(s), contributor(s), and creation or contribution history.
- Rights holder for the protectable expression in the file.
- Any assignment, employment, contractor, collaboration, or other agreement affecting ownership or licensing authority.
- Third-party quotations, images, tables, diagrams, examples, excerpts, or other incorporated material.
- Applicable source license or permission and whether its terms allow the intended distribution.
- The edition-specific license grant and the person or entity authorized to make it.

Project-level attribution to Kyle Alexander Steen as **Original Project Originator and Architect** is preserved. That attribution is not, by itself, proof of sole authorship or sole ownership of every file.

## 6. Required treatment by material class

| Material class | Intended treatment | Clearance status |
|---|---|---|
| Shared C2O/UNIVERSALIS taxonomy and architecture | Dual-license by edition | File-level rights review pending |
| C2O-exclusive implementation code and internal implementation materials | C2O proprietary | No implementation source code was present in the audited repositories at the time of this policy draft |
| UNIVERSALIS implementation and project materials | Apache-2.0 | Grant authority must be established for each rights holder's contribution |
| Third-party materials | Their own applicable terms; no blanket relicensing | Source-by-source review pending |
| Contributor-created material | Terms granted by the contributor/rightsholder | Agreement and contribution records pending where not already present |

## 7. Attribution, acknowledgement, and recognition

Preserve accurate project attribution, contributor credit, copyright notices, and third-party notices as required by the applicable license or written agreement. The project attribution is:

**Kyle Alexander Steen — Original Project Originator and Architect**

Where attribution is requested beyond what Apache-2.0 requires, that request is a recognition request and not an additional restriction on Apache-2.0 use. Any stronger obligation must be supported by a separate agreement accepted by the relevant parties or a separately licensed work.

Attribution must not erase the authorship or rights of contributors and third-party rights holders, and it must not imply endorsement.

## 8. Clearance workflow and evidence states

Use these states distinctly:

- **Proposed:** intended license classification recorded, evidence incomplete.
- **Documented:** source and provenance information recorded.
- **Verified:** rights holder and authority to grant the designated license supported by evidence.
- **Third-party review required:** incorporated material needs separate license/permission analysis.
- **Unresolved:** ownership, permission, or license compatibility remains unknown.
- **Excluded:** material is not included in the project's license grant.

Do not mark a file verified solely because it appears in a repository, was committed by a project account, has a matching SHA, or carries project-level attribution.

## 9. Reference materials

- [Apache License, Version 2.0 — official text](https://www.apache.org/licenses/LICENSE-2.0.html)
- [17 U.S.C. § 204 — execution of transfers of copyright ownership](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section204&num=0&edition=prelim)
- [GitHub Docs — Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

This project document is a governance and evidence-control record, not legal advice, a copyright assignment, a contributor agreement, or a customer EULA. Final license grants and agreements should be reviewed by qualified counsel.
