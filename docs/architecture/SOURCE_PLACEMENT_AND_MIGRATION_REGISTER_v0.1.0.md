# UNIVERSALIS-OS Source Placement and Migration Register

**Record ID:** UOS-SRC-001  
**Version:** 0.1.0  
**Status:** Initial inventory and placement proposal — partial audit; no transfer authorized  
**Snapshot:** 2026-11-19  
**Target:** UNIVERSALIS-OS

## 1. Purpose

This register identifies existing public UNIVERSALIS material that may contribute to UNIVERSALIS-OS. It prevents duplication, loss of provenance, unreviewed licensing assumptions, and accidental import of private C2O material.

UNIVERSALIS-OS is the independent implementation target for the public UNIVERSALIS operating system. Historical and specialist repositories remain source repositories unless a specific artifact is reviewed and deliberately integrated. This register does not authorize bulk copying, deletion, merging, publication, or source transfer.

## 2. Audit coverage and limits

An organization inventory returned 31 repositories on 2026-11-19. One GAIA-named legacy repository is excluded from this work by explicit scope. The remaining 30 repositories were inventoried by name, visibility, default branch, and repository size. Selected repository trees and files were inspected, including The UNIVERSALIS Ecosystem, UNIVERSALIS Research, the domain-content repositories, the encyclopedia repositories, and the two OS targets.

**This is not yet a complete file-by-file, branch-by-branch, PR-by-PR, license, security, dependency, or provenance audit of all public UNIVERSALIS repositories.** No claim of complete source recovery, public-release readiness, or placement correctness is made.

## 3. Public UNIVERSALIS source repositories and disposition

| Source repository | Observed role/state | UNIVERSALIS-OS disposition | Transfer status |
|---|---|---|---|
| `The-UNIVERSALIS-Ecosystem` | Public product repository with LICENSE (Apache-2.0), NOTICE, architecture contracts, Engineering Doctor, registry, knowledge validator, prototype, scaffold, tests, and workflows. Main tree observed at 220 entries, including 94 code/config/test paths. | Primary existing software source to assess for selective porting or adaptation. Candidate components include Engineering Doctor, registry/validators, knowledge records, research scaffold, and prototype modules. They are not automatically OS components. | Strongest implementation source candidate; per-file license/provenance/dependency/security/test and architecture review required before migration. |
| `Research-for-the-UNIVERSALIS-Ecosystem` | Public research repository with charter, requirements, evidence, and Reports 13–15 (“What to Build” and “How to Build”). Main tree observed at 31 entries. | Research and requirements source. Accepted requirements and public-safe specifications may be re-authored or referenced in UNIVERSALIS-OS with exact provenance. | No bulk transfer. Reconcile report status, PR history, and requirements first. |
| `The-UNIVERSALIS-Ontology` | Public document repository containing a master Human/Intelligence ontology DOCX and Markdown plus README; no root license was observed in the inspected tree. | Candidate ontology/data source, not executable code. Validate rights, definitions, scope, source provenance, legacy terminology, and schema before import. | Not cleared for import. |
| `The-UNIVERSALIS-Human-Knowledge`, `The-UNIVERSALIS-Human-Capabilities`, `The-UNIVERSALIS-Human-Skills`, `The-UNIVERSALIS-Human-Powers` | Public document repositories with Markdown/DOCX content and README; no root license was observed in inspected trees. | Candidate Human-domain knowledge/content packages. Not kernel or system-service code. | Not cleared for import. |
| `The-UNIVERSALIS-Intelligence-Knowledge`, `The-UNIVERSALIS-Intelligence-Capabilities`, `The-UNIVERSALIS-Intelligence-Skills`, `The-UNIVERSALIS-Intelligence-Powers` | Public document repositories with Markdown/DOCX content and README; one has an additional capability architecture document; no root license was observed in inspected trees. | Candidate Intelligence-domain content and capability specifications. Runtime services must be implemented independently inside UNIVERSALIS-OS. | Not cleared for import. |
| `The-UNIVERSALIS-Encyclopedias` | Public repository; inspected main contains README only. | Future public encyclopedia content source if developed and licensed. | No content ready for import. |

## 4. Private C2O sources are excluded by default

The following are not public UNIVERSALIS source dependencies:
- `Research-for-the-C2O-Ecosystem`, including the private governing Research Plan and private Technical/Human Tablet collections;
- `The-C2O-Ecosystem` and private C2O governance, infrastructure, credentials, policies, and internal tools;
- `The-C2O-Encyclopedias` and any private research branch;
- C2O knowledge, ontology, human, and intelligence repositories.

Private C2O material may not be copied, mirrored, linked as a required dependency, or exposed through build workflows. A public-safe derivative requires source-specific provenance, rights/license, privacy, security, IP, and owner release review. A private source locator must not appear in public build metadata or public test fixtures.

## 5. Placement rules inside UNIVERSALIS-OS

- `docs/architecture/`: accepted public OS architecture, ADRs, interfaces, and integration decisions.
- `docs/security/`: threat models, security architecture, hardening, and assurance requirements.
- `knowledge/`: public-safe, licensed knowledge packages with provenance manifests.
- `schemas/` or service-local schema directories: versioned portable contracts.
- `services/`: actual executable user-space services, including registry, research, Alchemy, knowledge, identity integration, and evidence services where approved.
- `platform/`: hardware and host-platform adapters.
- `tests/`: unit, integration, property, conformance, adversarial, recovery, portability, and reproducibility tests.
- `tools/`: developer, build, verification, and operator tools that belong to UNIVERSALIS-OS.

Do not place research pass narratives, raw private source material, unlicensed third-party documents, or exploratory interpretations into the public product. Do not treat an existing prototype as accepted, secure, production-ready, or suitable for kernel execution merely because its tests pass.

## 6. Required transfer packet for every adopted artifact

Every source transfer or adaptation must record:
1. Exact source repository, path, branch/tag/commit, and original blob SHA.
2. Source owner, authorship, license/rights, NOTICE obligations, and provenance status.
3. Confirmation that the artifact contains no private C2O material, secrets, internal locators, personal data, or restricted content.
4. Why the artifact belongs in UNIVERSALIS-OS and which public requirement or ADR it satisfies.
5. Whether it is copied verbatim, adapted, reimplemented, or merely referenced.
6. Destination path, destination commit, and content digest.
7. Dependency inventory, tests, security review, independent review, limitations, and unresolved questions.
8. Explicit owner acceptance and public-release authorization where applicable.

A repository-level license does not prove every embedded file or dependency is clear. A successful copy is not acceptance. A passing test is not security approval.

## 7. Immediate source-to-build order

1. Audit the public UNIVERSALIS product repository at file, branch, PR, license, dependency, and workflow level.
2. Reconcile the public requirements and research reports against the current product implementation.
3. Identify a small, non-privileged, local-first vertical slice with clear user value and testable requirements.
4. Decide the OS product boundary, reference platform, toolchain, and service architecture.
5. Reimplement or port the selected components inside UNIVERSALIS-OS with provenance, tests, SBOM, and build attestations.
6. Keep the resulting system independently operable without C2O access or services.

## 8. Current disposition

- UNIVERSALIS-OS `main` remains unchanged and contains only its original README.
- The architecture proposal is on `foundation/architecture-baseline-2026-11-19` and is under draft PR #1.
- This register is a proposal on that same branch and is not owner-accepted.
- No software or private source has been copied into UNIVERSALIS-OS by this register.
- The current repository visibility is private. This register does not grant a license or authorize public release.
