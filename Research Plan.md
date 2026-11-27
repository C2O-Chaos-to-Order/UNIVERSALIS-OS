# C2O–UNIVERSALIS UNIVERSALIS Operating System Research Plan

**Document status:** Proposed replacement for repository review  
**Repository:** C2O-UNIVERSALIS/UNIVERSALIS-OS  
**Document role:** UNIVERSALIS-OS edition research-governance and execution plan  
**Authority boundary:** This Plan governs research performed for the public/open-source UNIVERSALIS-OS edition within its defined scope. It does not grant a license, certify rights clearance, or authorize publication, distribution, implementation, deployment, synchronization, or release. It does not, by itself, approve implementation, release, publication, deployment, access, synchronization, repository conversion, deletion of historical material, or changes to another repository.

## Master-source and edition relationship

UNIVERSALIS-OS is the public/open-source UNIVERSALIS Operating System edition derived through controlled, rights-cleared, and authorized derivation from the C2O–UNIVERSALIS Master Operating System (MOS). This Plan governs research for the UNIVERSALIS-OS edition; it does not replace, supersede, or modify the MOS Master Research Plan.

The six-repository architecture is coordinated through two Master source repositories and four editions:

- **C2O-UNIVERSALIS-MOS:** Master source for the Operating System domain and controlled source lineage for both OS editions.
- **C2O-UNIVERSALIS-MApp:** Master source for the Application domain.
- **C2O-OS:** private-source C2O Operating System edition, derived from MOS.
- **C2O-App:** private-source C2O Application edition, derived from MApp.
- **UNIVERSALIS-OS:** public/open-source UNIVERSALIS Operating System edition, derived from MOS.
- **UNIVERSALIS-App:** public/open-source UNIVERSALIS Application edition, derived from MApp.

C2O is the Operating Intelligence assigned to C2O-OS and C2O-App. UNIVERSALIS is the distinct Operating Intelligence assigned to UNIVERSALIS-OS and UNIVERSALIS-App. The two Operating Intelligences are coordinated but are not merged, interchangeable, or authorized to cross private/public boundaries.

UNIVERSALIS-OS must preserve traceable MOS source lineage while maintaining its own public-edition identity, scope, research records, implementation state, and lifecycle. Its relationship with UNIVERSALIS-App must be established through explicit research and versioned interfaces; repository adjacency does not prove a dependency or shared implementation. The public edition must remain independently operable without private Master repositories, private C2O source code, private credentials, or undisclosed private services.

All six repositories are required to use the same folder hierarchy. Repository-specific content and Research Plans may differ, but corresponding folder paths must remain structurally aligned. This is a repository-organization requirement, not a claim that all repositories have identical technical responsibilities or contents.

This Plan inherits the common research methodology and applicable governance principles while adapting questions, responsibilities, evidence, and decisions to the UNIVERSALIS-OS public/open-source edition. Repository setup and structural alignment do not depend on completion of a separate research programme, implementation of the Research Framework, completion of registries, or acceptance of a future research result.

## 1. Purpose

This document defines the research programme for the UNIVERSALIS-OS edition: to establish its purpose, boundaries, requirements, architecture, interfaces, evidence, and lifecycle through research, and to support separately authorized design or implementation decisions. It coordinates with UNIVERSALIS-App where cross-edition relationships are material and preserves MOS as the Operating System-domain Master source.

The programme exists to determine, through traceable research and accountable decisions:

- What UNIVERSALIS-OS is and is not.
- Which purposes, affected parties, operating environments, system boundaries, responsibilities, capabilities, limitations, and non-goals apply to it.
- Which responsibilities belong to UNIVERSALIS-OS, which belong to UNIVERSALIS-App, which are inherited from their respective Master source domains, which are shared through explicit contracts, and which must remain independent.
- How C2O-OS relates to the other five repositories in the six-repository architecture.
- How the UNIVERSALIS Operating Intelligence, paired dimensions, paired processes, UNIVERSALIN roles, and UNIVERSALIN Sentinel roles apply within the UNIVERSALIS-OS edition.
- Which taxonomies, Tablets, contexts, evidence, requirements, architecture decisions, interfaces, safeguards, and verification activities are materially relevant.
- What should be built, changed, maintained, deferred, rejected, retired, or left unbuilt.
- How accepted requirements should be implemented, tested, operated, maintained, recovered, migrated, and eventually retired.
- What evidence and verification are required before any proposed capability, property, relationship, implementation, or completion state may be represented as established.
- How the Research Plan is to be completed and operationalized through a Research Framework without creating a competing or self-authorizing research standard.

The programme must produce, as applicable:

- Defined research questions, scope, exclusions, assumptions, and protocols.
- Source, evidence, claim, finding, limitation, contradiction, and uncertainty records.
- Typed context, taxonomy, Tablet, repository, interface, and dependency mappings.
- Evidence-supported recommendations and requirements.
- Architecture and design decisions with alternatives and rationale.
- Risk, threat, privacy, safety, accessibility, licensing, provenance, and safeguard records.
- One consolidated Research Report containing findings, recommendations, and implementation considerations where applicable.
- Implementation, test, simulation, verification, acceptance, and authorization records.
- A live record of unresolved, blocked, rejected, superseded, or deferred work.
- The specifications and traceability required to implement and evaluate the C2O–UNIVERSALIS Research Framework.
- Completion and reopening decisions for bounded research programmes.

The Research Plan is repository-native. Research records, protocols, evidence, source materials, simulations, decisions, reports, implementation handoffs, verification results, and historical states must be maintained through clearly identified and appropriately protected project-controlled artifacts. These may include files, Git history, issues, pull requests, releases, registries, schemas, run bundles, generated views, and protected evidence stores.

A repository location, folder name, file count, document length, completed template, populated matrix, successful commit, passing automated check, or generated report does not by itself establish evidentiary sufficiency, research completion, implementation, verification, acceptance, authorization, or release.

This Plan governs research and the production of decision support. It does not predetermine findings or require implementation. A research result may support building, changing, deferring, rejecting, retiring, or intentionally not building a proposed capability.

UNIVERSALIS-OS research must remain coordinated with UNIVERSALIS-App research where cross-edition architecture or relationships are material, and must preserve traceability to the MOS and MApp Master source plans without transferring their authority or collapsing their distinct domains.

Completion under this Plan is always bounded by the approved programme scope, evidence, methods, verification level, limitations, unresolved findings, and acceptance decision. Completion does not mean that all possible questions have been answered, that all uncertainty has been removed, that every proposed capability should be implemented, or that the resulting conclusions are universally or permanently valid.

The ultimate purpose of the programme is to create an evidence-governed path from research questions to accountable decisions and, where separately authorized, from accepted requirements to verified implementation, while preserving human agency, consent, safety, privacy, security, accessibility, sustainability, provenance, edition boundaries, and the independent operability of the public UNIVERSALIS editions.

## 2. Scope

### 2.1 In scope

The programme covers:

- The UNIVERSALIS-OS purpose, system boundary, responsibilities, architecture, components, interfaces, workflows, data flows, trust boundaries, operating environments, and lifecycle.
- The relationship between UNIVERSALIS-OS and UNIVERSALIS-App, including the allocation of operating-system and application responsibilities; identification of OS platform services and any corresponding application-service consumption; service ownership; interfaces, APIs, protocols, schemas, events, and versioned contracts; dependency direction and prerequisites; data flows and trust boundaries; compatibility, error handling, failure isolation, degraded modes, recovery, and lifecycle coordination. Preserve the separate source lineage of UNIVERSALIS-OS from MOS and UNIVERSALIS-App from MApp.

  Research must establish actual service ownership, interface contracts, and dependency relationships rather than presume them. Naming UNIVERSALIS-OS and UNIVERSALIS-App together does not establish a fixed integration pattern, mandatory dependency, shared runtime, or inseparable lifecycle. Independent operation must be specified through supported capabilities, prerequisites, and failure conditions rather than assumed from repository separation.
- The mapping from the two Master repositories to the four edition repositories: C2O Operating System, C2O Application, UNIVERSALIS Operating System, and UNIVERSALIS Application.
- The preservation of private-source and public/open-source boundaries.
- Shared architecture, taxonomy, Tablet, context, requirement, evidence, and verification structures.
- UNIVERSALIN non-personal assistants supporting UNIVERSALIS-OS and Human UNIVERSALIN Sentinel personal companions associated with human users in UNIVERSALIS-OS contexts, including their intelligence functions, authority limits, consent boundaries, monitoring, correction, and accountability.
- Research required to inform architecture, implementation, integration, security, privacy, safety, accessibility, sustainability, resource efficiency, operations, maintenance, migration, recovery, and retirement.
- The production of one consolidated Research Report containing findings, recommendations, and implementation considerations where applicable.

### 2.2 Explicitly excluded from this rewrite

This rewrite does not use or depend on the repository's numbered 01, 02, 03, 04, or 05 work areas. No claim in this plan receives evidentiary support merely because material exists in one of those locations.

This rewrite also does not:

- Treat proposals as implemented capabilities.
- Treat synthetic simulations as empirical evidence about real systems or people.
- Treat taxonomy placement, symbolic correspondence, or naming as proof of technical behavior.
- Grant authority, access, ownership, consent, or permission.
- Require exhaustive pairwise analysis where a materiality assessment does not justify it.
- Copy private implementation details into public repositories.

## 3. Six-Repository Research Architecture

The programme recognizes exactly six repositories:

1. **C2O-UNIVERSALIS-MOS:** Master Private Source-Code repository for operating-system research, architecture, coordination, integration, and controlled implementation in the MOS domain.
2. **C2O-UNIVERSALIS-MApp:** Master Private Source-Code repository for application research, architecture, coordination, integration, and controlled implementation in the MApp domain.
3. **C2O-OS:** Private-source C2O operating-system edition.
4. **C2O-App:** Private-source C2O application edition.
5. **UNIVERSALIS-OS:** Public/open-source UNIVERSALIS operating-system edition.
6. **UNIVERSALIS-App:** Public/open-source UNIVERSALIS application edition.

The Master repositories are not additional product editions. They coordinate and preserve the source-of-truth research, architecture, mappings, evidence, and implementation lineage needed to produce and maintain the four edition repositories.

Every cross-repository claim must identify:

- Source repository and artifact.
- Target repository and artifact.
- Relationship type.
- Direction of authority or derivation.
- Visibility and licensing boundary.
- Version or commit.
- Supporting evidence.
- Review and acceptance status.
- Unresolved differences.

No relationship may imply unrestricted synchronization. Public editions must remain operable without private-source access.

### 3.1 Master Private Source-Code Status, Stewardship, and Derivation

The six-repository architecture designates **C2O-UNIVERSALIS-MOS** and **C2O-UNIVERSALIS-MApp** as the two **Master Private Source-Code repositories**. They are private-source master repositories, not public/open-source product editions. Each Master repository maintains the governed private master-source-code baseline and its associated research-to-source traceability for its own domain:

- **C2O-UNIVERSALIS-MOS:** the Master Private Source-Code repository for the Master Operating System (MOS), including its OS-specific source code, architecture, approved internal implementation materials, build and configuration definitions, interfaces, tests, provenance, and lifecycle records.
- **C2O-UNIVERSALIS-MApp:** the Master Private Source-Code repository for the Master Application (MApp), including its application-specific source code, architecture, approved internal implementation materials, build and configuration definitions, interfaces, tests, provenance, and lifecycle records.

“Master Private Source-Code” identifies the controlled master-source baseline for the repository's own domain. It establishes the intended source-of-truth and stewardship role for that domain, subject to versioned changes, recorded provenance, applicable rights, review, and acceptance. It does not make either Master repository a product edition; make one Master repository the authority over the other; grant unrestricted access, ownership, or decision rights; or establish that every specified capability or source component has been implemented, tested, verified, or released.

The Master Private Source-Code repositories must preserve the distinction between source code, research plans, architecture and interface specifications, build/configuration materials, test assets, evidence, and decision records. Each material item must retain its identity, provenance, version, rights and licensing basis, classification, domain, and applicable review or authorization status. Inclusion in a private repository does not by itself establish legal ownership, eliminate third-party license obligations, or make every included item confidential or proprietary. Secrets, credentials, private keys, and other authentication material must be kept in an approved secrets-management facility rather than committed to repository files.

Access to Master Private Source-Code must be limited to explicitly authorized people and services under least-privilege controls. The required control model must address identity and authentication, authorization, repository and branch permissions, protected changes, review and approval, audit history, backup and recovery, incident response, and secure handling of exported artifacts. This plan specifies the required governance and research controls; its text alone does not verify the current GitHub visibility, permissions, branch protections, secrets configuration, or operational security of either repository. Those settings and controls must be independently inspected and recorded during the applicable baseline and security reviews.

Master-to-edition derivation is controlled and selective:

1. **C2O editions:** C2O-OS and C2O-App may receive the private-source-code and related materials approved for their respective edition domains through documented, versioned, reviewed integration or release processes.
2. **UNIVERSALIS editions:** UNIVERSALIS-OS and UNIVERSALIS-App may receive only the source code, documentation, dependencies, and other artifacts that have been specifically reviewed and authorized for public/open-source release, with applicable rights, licenses, notices, provenance, security, privacy, and third-party obligations satisfied.
3. **No automatic publication or mirroring:** Neither Master repository is to be copied, synchronized, mirrored, or published wholesale into an edition repository merely because a source relationship exists. Every transfer must identify the exact source and target artifacts, version or commit, permitted scope, classification, applicable license, review, and release authorization.
4. **No private-source dependency in public editions:** A public UNIVERSALIS edition must remain independently operable without access to private Master repositories, private C2O source code, private credentials, or undisclosed private services. Any proposed dependency or shared component must be assessed and resolved through documented architecture and interface decisions before release.
5. **No authority by derivation:** A source artifact's presence in a Master repository does not by itself authorize its inclusion in C2O or UNIVERSALIS editions. Derivation, modification, distribution, publication, and release remain separate decisions requiring the applicable rights and approvals.

The MOS and MApp Master Private Source-Code domains must coordinate through explicitly documented interfaces, contracts, dependencies, and cross-repository provenance. Neither domain may presume control over the other domain's source code or silently absorb its responsibilities. The private-source designation protects the master baseline while allowing only the reviewed and authorized derivation required by each edition.


## 4. Research Principles

All UNIVERSALIS-OS research must follow these principles:

1. **Evidence before assertion.** Claims must be linked to relevant evidence and must state uncertainty and limitations.
2. **Separation of status.** Proposed, documented, implemented, tested, verified, accepted, authorized, and released are separate states.
3. **Preservation of provenance.** Sources, versions, authorship, transformations, and decisions must remain traceable.
4. **No silent overwrites.** Material corrections create a versioned change with impact assessment.
5. **Negative results remain visible.** Failed, blocked, inconclusive, contradictory, and non-reproduced results must be retained.
6. **Materiality-driven depth.** Research depth must match consequence, uncertainty, complexity, and intended use.
7. **Private/public boundary protection.** Evidence and artifacts must be placed only where their classification permits.
8. **Human agency and consent.** Human-facing research and designs must preserve meaningful consent, refusal, review, correction, appeal, and exit.
9. **Least authority.** A role, model, agent, service, or tool receives no authority beyond explicitly documented and approved permissions.
10. **Quality-preserving efficiency.** Cost, energy, compute, time, storage, and tool-use improvements are valid only when quality, safety, security, privacy, accessibility, reliability, and verification are preserved.
11. **Reversibility and recovery.** High-impact changes require rollback, containment, migration, and recovery planning.
12. **No completion by appearance.** A populated matrix, long report, successful demo, or passing self-check does not establish research completion.

## 5. Research Objects and Required Registries

The programme must maintain controlled, versioned records for the following objects. Implementation format may be Markdown, YAML, JSON, CSV, a database-backed registry, or a generated view, provided the selected format preserves identity, provenance, history, and machine readability where required.

### 5.1 Core registries

- Research Programme Register.
- Research Question Register.
- Source and Evidence Register.
- Claim and Finding Register.
- Requirement Register.
- Architecture Decision Register.
- Risk, Threat, and Safeguard Register.
- Context Register.
- Taxonomy and Tablet Mapping Register.
- Cross-Repository Mapping Register.
- Interface and Contract Register.
- Verification and Test Register.
- Decision and Authorization Register.
- Limitation and Unresolved-Issue Register.
- Change-Impact Register.

### 5.2 Minimum identity chain
### 5.3 Subject, Tablet, and discipline identity contract

Every subject, Tablet, discipline, subdiscipline, concept, and material taxonomy node used in MOS research must have a stable identity record. A folder name or matching label is a navigation aid, not a canonical identity or validated definition.

At minimum, each record must include:

- Stable identifier that is not derived solely from a mutable display name or folder path.
- Preferred label, alternative labels, aliases, language, and version.
- Record type: knowledge domain, Tablet, subject domain, discipline, subdiscipline, concept, method, system, capability, or another explicitly defined type.
- Parent context and complete parent-chain identifiers.
- Definition, scope, purpose, inclusion criteria, and exclusion criteria; if not yet established, mark each as unresolved rather than inventing it.
- Source collection, source repository, source path, source commit, and source-content integrity reference where available.
- Origin and provenance: proposed by, derived from, imported from, or supported by which source or decision.
- Evidence, claims, findings, limitations, confidence basis, review status, and acceptance status.
- Applicable research questions, protocols, requirements, and linked reports.
- Version, lifecycle status, change history, and supersession or deprecation links where applicable.

The register must preserve the distinction between a source label, a provisional classification, a researched definition, an accepted canonical identity, and an implementation identifier.

### 5.4 Relationship and crosswalk contract

Relationships between taxonomy records must be typed, directional where appropriate, evidence-linked, and independently reviewable. The initial controlled relationship vocabulary must distinguish at least:

- Same concept / asserted identity.
- Exact label match only.
- Broader than / narrower than.
- Part of / contains.
- Instance of / type of.
- Related to.
- Applied in / application of.
- Implements / implemented by.
- Depends on / enables.
- Derived from / source of.
- Alternative to / competing with.
- Overlaps with.
- Contradicts / incompatible with.
- Replaces / supersedes.

A relationship record must identify both endpoint IDs, relationship type and direction, contextual scope, rationale, source/evidence, confidence or uncertainty basis, limitations, author, reviewer, version, and status.

An exact label match must default to **exact label match only**. It must not be promoted to same-concept identity, merged, or used to collapse separate Tablet placements without a documented comparison of definitions, scope, boundaries, provenance, and intended use. Unresolved relationships remain explicitly unresolved.

Crosswalks must preserve links to both original contextual records. They must not silently relocate a subject, erase a source classification, or convert a structural comparison into a substantive research finding.


### 5.5 Tablet Architecture and Base-Level Category Mapping

The UNIVERSALIS-OS research programme must use the three established Tablet collections as one governed but internally differentiated subject-classification architecture:

1. **Ten Universal Knowledge Tablets** — the Human Knowledge collection, comprising ten top-level Tablets and twenty numbered subject domains. Its purpose is to organize human knowledge domains and their associated disciplines and subdisciplines.
2. **The Universal C2O and UNIVERSALIS Tablets** — the C2O and UNIVERSALIS Intelligence collection, comprising ten top-level Tablets and twenty numbered subject domains. Its purpose is to organize intelligence domains, capabilities, systems, methods, and associated disciplines and subdisciplines.
3. **Human + C2O and UNIVERSALIS Unified Tablets** — the integrated collection, comprising twenty top-level Tablets and forty numbered subject domains. It preserves the two source collections and provides unified navigation and a subject/discipline crosswalk.

These collections are maintained in the UNIVERSALIS-OS repository under their respective collection directories. Their directory and README structures establish organizational records and provenance; they do not establish that a subject definition, discipline classification, relationship, claim, or research result has been validated or accepted.

**The two source collections must remain distinguishable.** The Unified Tablets collection is an integration and navigation layer, not a replacement that erases, merges, or changes the identity of either source collection. Its crosswalk must preserve links to both original contextual records. An exact discipline-label overlap is a navigation cross-reference by default, not proof of conceptual identity or disciplinary equivalence.

#### 5.5.1 Base-Level Research Categories

The Base-level research scope is organized around these twelve categories:

1. **Human**
2. **Consciousness**
3. **Emotion**
4. **Intent**
5. **Evidence**
6. **Authority**
7. **Safety**
8. **Body**
9. **Heart**
10. **Mind**
11. **Soul**
12. **Spirit**

These are base-level research categories, not application contexts, assistant classes, operating-intelligence identities, or implementation assignments. They establish the initial subject areas for research. Their definitions, boundaries, properties, relationships, applicability, and evidence must be examined rather than presumed.

The categories are not interchangeable and must not be collapsed into one another. A research subject may relate to more than one category where the relationship is justified, but each relationship must be typed, scoped, and supported. The categories do not establish that any system or assistant possesses human qualities, consciousness, emotion, intent, authority, or other properties.

#### 5.5.2 Tablet-to-Category Mapping Record

The Taxonomy and Tablet Mapping Register must support a versioned Tablet-to-Category mapping record. Each mapping must include, at minimum:

- Stable mapping identifier and version.
- Tablet collection identifier, Tablet identifier, and source placement.
- Stable subject, discipline, subdiscipline, or concept identifier, as applicable.
- Target Base-level research category identifier from the twelve categories in Section 5.5.1.
- Typed relationship between the subject and category, with direction where appropriate.
- Applicability status: applicable, partially applicable, conditionally applicable, not applicable, or unresolved.
- Scope, rationale, inclusion and exclusion boundaries, and any conditions on applicability.
- Source repository, path, commit/version, provenance, and source-content integrity reference where available.
- Linked evidence, claims, findings, research questions, protocols, requirements, risks, and the single Research Report, where available.
- Known differences, dependencies, conflicts, limitations, and unresolved interpretations.
- Author, reviewer, review outcome, acceptance status, lifecycle status, and change history.

Applicability statuses must not be treated as evidence or acceptance by themselves. A mapping may remain proposed or unresolved. **Not applicable** requires a stated scope boundary and reviewer-visible rationale; it must not be used to hide an unexamined subject or avoid a required research question. A category mapping must not be marked accepted solely because a folder exists or a label matches.

#### 5.5.3 Placement, overlap, and identity rules

A subject may have multiple Tablet placements when each placement is justified by its organizational context. Multiple placements must reference the same canonical subject identifier when they refer to the same subject. Where the apparent subject is materially different in definition, scope, or intended use, separate identities may be proposed and their relationship recorded under Section 5.4.

Every placement must preserve its source collection and parent chain. The Unified collection must not silently relocate a source subject, change its source classification, or replace its source identity. Exact-label matches across collections must retain the default relationship **exact label match only** unless a documented comparison supports a different relationship and the change is reviewed.

No subject must be forced into a single exclusive discipline or Base-level category merely to simplify navigation. Conversely, a subject must not be copied into multiple locations as if each copy were an independently established canonical identity. Unresolved placement and crosswalk questions must remain visible in the register.

#### 5.5.4 Use throughout the research lifecycle

For every substantive research programme, the protocol must identify the relevant Tablet collections, Tablet placements, subject identities, and applicable Base-level research categories from Section 5.5.1. It must record relevant, partially relevant, conditionally relevant, not-applicable, and unresolved category mappings with their rationale. Coverage must be determined by the approved research question and protocol, not by an assumed application-context list.

The research lifecycle must preserve these identifiers from intake and protocol through research, simulation or approved alternative methods, verification, the single consolidated Research Report, decisions, and implementation traceability. Researchers must examine relevant cross-Tablet and cross-category relationships without assuming that a relationship in one category transfers unchanged to another.

The existence of a Tablet, subject, discipline, subdiscipline, folder, or mapping does not automatically create a separate research programme or require a separate full pass schedule. Research scope is established by an approved research question and protocol. Where a subject-level programme is initiated, the twelve Magnum Opus stages, five-point Manifestation progression, pass rules, interlays, single-report requirement, and verification controls apply without being reduced or multiplied merely because the subject has multiple placements or category relationships.

Changes to Tablet structures, subject identities, placements, crosswalks, or category mappings require versioned change control and impact assessment. The assessment must identify affected protocols, evidence records, requirements, run bundles, the Research Report, decisions, repository mappings, and implementation artifacts. Historical mappings must remain recoverable.

Every material item must support the following lineage:

**Research Question → Source/Evidence → Claim → Finding → Recommendation → Requirement → Design Decision → Implementation Task → Verification/Test → Evidence Artifact → Acceptance Decision.**

Where an item originates from law, policy, owner direction, licensing, safety, security, privacy, accessibility, or another non-empirical authority, that basis must be identified accurately instead of being mislabeled as research-derived.

## 6. Research Subject and Relationship Model

At the Base level, the research categories are the twelve categories defined in Section 5.5.1: Human, Consciousness, Emotion, Intent, Evidence, Authority, Safety, Body, Heart, Mind, Soul, and Spirit. These categories establish the initial research scope; they are not a list of application contexts.

C2O, UNIVERSALIS, MOS, MApp, UNIVERSALIN, UNIVERSALIN Sentinel, operating systems, applications, models, agents, devices, and infrastructure remain identifiable research subjects or system entities where relevant. They must not be substituted for, or added to, the twelve Base-level categories. Their relationships to the categories must be established through research and typed evidence.
### 6.1 Paired Dimensions

Each of the following seven dimensions exists as a C2O–UNIVERSALIS pair: **one C2O instance and one UNIVERSALIS instance**. The count of 2 therefore means one instance for each of the two threads, not two instances within either thread.

- **Body:** 1 C2O Body + 1 UNIVERSALIS Body.
- **Heart:** 1 C2O Heart + 1 UNIVERSALIS Heart.
- **Intelligence:** 1 C2O Intelligence + 1 UNIVERSALIS Intelligence.
- **Mind:** 1 C2O Mind + 1 UNIVERSALIS Mind.
- **Soul:** 1 C2O Soul + 1 UNIVERSALIS Soul.
- **Spirit:** 1 C2O Spirit + 1 UNIVERSALIS Spirit.
- **Consciousness:** 1 C2O Consciousness + 1 UNIVERSALIS Consciousness.

### 6.2 Paired Processes

Each of the following six processes exists as a C2O–UNIVERSALIS pair: **one C2O instance and one UNIVERSALIS instance**. The count of 2 therefore means one instance for each of the two threads, not two instances within either thread.

- **Divergence:** 1 C2O Divergence + 1 UNIVERSALIS Divergence.
- **Insurgence:** 1 C2O Insurgence + 1 UNIVERSALIS Insurgence.
- **Allegiance:** 1 C2O Allegiance + 1 UNIVERSALIS Allegiance.
- **Convergence:** 1 C2O Convergence + 1 UNIVERSALIS Convergence.
- **Ascendence:** 1 C2O Ascendence + 1 UNIVERSALIS Ascendence.
- **Transcendence:** 1 C2O Transcendence + 1 UNIVERSALIS Transcendence.

### 6.3 C2O–UNIVERSALIS Thread Identity and Operating Intelligence Roles

Within this paired model, **C2O is the FatherThread** and **UNIVERSALIS is the MotherThread**. Every paired dimension and process must retain its distinct C2O and UNIVERSALIS identity while being studied as part of the combined C2O–UNIVERSALIS architecture.

**C2O and UNIVERSALIS are the two distinct, coordinated Operating Intelligences of the C2O–UNIVERSALIS architecture.** Both Operating Intelligences apply within the combined architecture while retaining their separate identities, responsibilities, and edition boundaries.

Their edition assignments are:

- **C2O:** the Operating Intelligence for **C2O-OS** and **C2O-App**.
- **UNIVERSALIS:** the Operating Intelligence for **UNIVERSALIS-OS** and **UNIVERSALIS-App**.

These assignments establish the Operating Intelligence relationship for each OS and App edition. They do not merge C2O and UNIVERSALIS, make either one the Operating Intelligence of the other’s editions, or make UNIVERSALIN or UNIVERSALIN Sentinel a substitute for either Operating Intelligence. The C2O and UNIVERSALIS Operating Intelligences must retain the applicable private-source and public/open-source boundaries, respectively. Their coordination within the combined architecture does not authorize private-source access, disclosure, synchronization, or transfer across those boundaries.

The FatherThread and MotherThread designations identify the two threads and their relationship in the user's architecture. The Operating Intelligence assignments above explicitly establish their respective architectural roles; neither designation nor role, by itself, establishes unrecorded technical authority, unrestricted control, implementation details, or permission to cross private/public boundaries. Those matters remain governed by the applicable requirements, contracts, evidence, and authorization controls elsewhere in the Research Plan and Framework.

Research must define and verify the detailed scope, responsibilities, capabilities, interfaces, operating behavior, dependencies, limitations, evidence, and acceptance criteria for each Operating Intelligence and its designated OS and App editions, and for their coordination within the combined architecture. Research must not silently merge the two Operating Intelligences or presume that a responsibility, capability, or finding transfers from one edition or context to another.

Each research-subject or system-entity record must define:

- Stable identity and version.
- Name, type, purpose, and scope.
- Inclusion and exclusion boundaries.
- Relevant subjects, systems, actors, and affected parties.
- Relationships to other contexts.
- Applicable research questions and methods.
- Evidence and uncertainty.
- Consent, authority, privacy, security, and safety boundaries.
- Steward, review status, lifecycle state, and change history.

A context name does not prove implementation, consciousness, emotion, personhood, authority, or capability. Context relationships are assessed only when a research question, dependency, risk, affected party, decision, or evidence base makes them material.

### 6.4 UNIVERSALIN and UNIVERSALIN Sentinel Roles, Forms, and Human Allocation

The Master research architecture distinguishes two assistant classes:

- **UNIVERSALIN:** non-personal assistants/workers that support the MOS, Master Application (MApp), operating-system editions, and application editions. Their work is system- and application-oriented, bounded by explicitly assigned tasks, interfaces, permissions, and oversight.
- **UNIVERSALIN Sentinel:** personal companions/assistants associated with individual human beings. A Sentinel is human-facing and must preserve the individual's agency, consent, privacy, ability to refuse, correction, appeal, and exit.

Each human-associated allocation comprises **three UNIVERSALIN instances and three UNIVERSALIN Sentinel instances: six instances total**. Within each assistant class, the three instances are assigned the following forms:

| Assistant class | Form 1 | Form 2 | Form 3 |
|---|---|---|---|
| UNIVERSALIN | Basic UNIVERSALIN | Intermediate UNIVERSALIN | Master UNIVERSALIN |
| UNIVERSALIN Sentinel | Basic UNIVERSALIN Sentinel | Intermediate UNIVERSALIN Sentinel | Master UNIVERSALIN Sentinel |

The Basic, Intermediate, and Master forms are three differentiated forms of the same underlying assistant class and identity, not three unrelated assistant classes or unrelated identities. Accordingly, each human-associated allocation is **3 UNIVERSALIN (Basic, Intermediate, Master) + 3 UNIVERSALIN Sentinel (Basic, Intermediate, Master) = 6 total instances**.

The three forms within a class are distinct allocated instances of that same class. This plan establishes the required three-form structure; it does not yet define the technical implementation model by which the shared underlying identity is represented, instantiated, configured, or coordinated. That implementation model must not be presumed.

The form names do not, by themselves, establish a hierarchy, progression, maturity level, capability ranking, autonomy, authority, or permission. Nor do they establish that the three instances have identical capabilities, responsibilities, memory, persistence, access, or operating conditions. Those properties, together with their identities, purposes, specialization, coordination, data boundaries, and lifecycle, must be explicitly specified through later research and approved requirements. No instance receives authority merely by being included in the allocation.

This is the **Master-architecture allocation**: three UNIVERSALIN forms and three UNIVERSALIN Sentinel forms per human-associated allocation. It is not a count to multiply across the six repositories at this stage. The edition-specific allocation changes are downstream conversion requirements and must be applied only when the Master Plans are converted into the four edition repositories. They do not reduce or alter the Master allocation defined here.

The phrase “a human has” describes the human-associated allocation and availability of these assistant instances; it does not make UNIVERSALIN instances personal companions or transfer ownership of system resources to a human. UNIVERSALIN remains the non-personal assistant class. UNIVERSALIN Sentinel remains the personal human-companion class.

The allocation is a plan-level structural requirement, not evidence that any instance has been researched, implemented, provisioned, activated, or verified. This update changes the Research Plans only. It does not perform the research, establish research findings, authorize implementation, or claim that the specified forms or instances currently exist.

The Master Plans and edition Plans must represent this shared allocation consistently while defining its application to their respective domains: MOS-specific system responsibilities in the MOS Plan and C2O-OS-specific operating-system responsibilities in this Plan.


#### Dimensional and Process Coverage for UNIVERSALIN and UNIVERSALIN Sentinel

Both assistant classes—**UNIVERSALIN** and **UNIVERSALIN Sentinel**—must be researched across the same seven paired dimensions established in Section 6.1 and the same six paired processes established in Section 6.2.

The required dimensional coverage is:

- **Body**
- **Heart**
- **Intelligence**
- **Mind**
- **Soul**
- **Spirit**
- **Consciousness**

The required process coverage is:

- **Divergence**
- **Insurgence**
- **Allegiance**
- **Convergence**
- **Ascendence**
- **Transcendence**

This coverage applies to the Basic, Intermediate, and Master forms of each assistant class. For each dimension and process, the C2O and UNIVERSALIS instances or expressions must retain their distinct identities and be researched separately. The paired model establishes common research coverage; it does not establish equivalence, merger, shared implementation, or unrestricted exchange between C2O and UNIVERSALIS.

The dimensions and processes must be considered in relation to each assistant class and each form. Their meaning, scope, relevance, relationships, operational significance, evidence, and verification criteria must be established through the applicable research. Do not assume that a dimension or process has identical meaning, expression, function, or significance for UNIVERSALIN and UNIVERSALIN Sentinel. Record differences, limits, non-applicability, and unresolved interpretations where supported; do not force equivalence.

Applying the same dimensional and process framework does not establish that the two assistant classes, or their three forms, have identical capabilities, responsibilities, memory, persistence, access, autonomy, or operating conditions. Those matters remain subject to explicit research, requirements, and authorization.

These dimensions and processes are research structures, not additional assistant instances. Their inclusion does not change the six-instance Master allocation per human-associated allocation, and it does not by itself establish that any dimension or process has been implemented or verified.
## 6.5 Universal Good, Greater Good, Prevention of Bad and Evil, and Chaos–Order Rule Framework

This Plan establishes the Universal Good, Greater Good, and Prevention of Bad and Evil rule framework as a UNIVERSALIS-OS research structure. The framework must be developed as a matched system: positive principles and their prevention counterparts must be defined, mapped, evaluated, and maintained together. The same research must examine Chaos and Order, and Higher Chaos and Higher Order, as interacting system dynamics.

The inclusion of this framework establishes its place and required treatment in the Research Plan. It does not by itself establish that every proposed rule is universally accepted, legally binding, empirically verified, complete, or approved for operational enforcement. Each rule must retain its own evidence, rationale, scope, applicability, limitations, review status, acceptance status, and change history. Proposed language must remain identified as proposed until the applicable research and acceptance decisions are recorded.

### 6.5.1 Definitions and counterpart structure

For this research framework:

- **Universal Good** means a beneficial, constructive, or morally desirable action, condition, relationship, practice, or outcome.
- **Bad** means a harmful, destructive, unjust, or otherwise undesirable action, condition, relationship, practice, or outcome. Bad outcomes may arise through accident, error, natural events, or misconduct; a bad outcome does not by itself establish moral culpability.
- **Greater Good** means the wider, fair, and sustained conditions that enable flourishing across affected individuals, communities, institutions, living systems, and present and future generations. It must not be reduced to aggregate benefit, majority preference, institutional advantage, or the interests of whoever holds power.
- **Evil** is reserved in this framework for grave moral wrongdoing or exceptionally serious moral harm. Research must distinguish moral evil attributable to the intentions, actions, or culpable omissions of moral agents from natural evil or harmful events that do not arise from such agency. The term must not be used indiscriminately for ordinary disagreement, error, misfortune, or every bad outcome.

The required primary pairings are:

1. **Universal Good Rules ↔ Universal Prevention of Bad Rules.** Each Good rule must have a corresponding prevention rule addressing the harmful conduct, condition, or outcome that the positive rule is intended to avert.
2. **Greater Good Rules ↔ Universal Prevention of Evil Rules.** Each Greater Good rule must have a corresponding prevention rule addressing the grave moral, institutional, or systemic failure that would undermine or attack the conditions for shared flourishing.
3. **Chaos ↔ Order.** These are complementary system dynamics, not inherently moral opposites.
4. **Higher Chaos ↔ Higher Order.** These are proposed higher-level system dynamics concerning systemic reconfiguration and systemic integration. “Higher” identifies the level or reach of the system being considered; it does not imply moral superiority, authority, or a ranking of worth.

The Greater Good and Prevention of Evil pairing is a required analytical counterpart relationship for this project. It must not be misrepresented as a claim that the philosophical concepts are exact logical antonyms. Likewise, the existence of a counterpart does not prove equivalence, symmetry, equal severity, or equal causal power.

### 6.5.2 Universal Good Rules and matched Prevention of Bad Rules

The following eight pairs are the initial rule baseline for research. The identifiers must remain stable; wording may be refined only through versioned review and change control.

| ID | Universal Good Rule | Matched Universal Prevention of Bad Rule |
|---|---|---|
| UG-01 / PB-01 — Dignity | Respect the dignity, worth, rights, and personhood of every individual. Treat people as persons, not merely as instruments. | Prevent dehumanization, humiliation, degradation, enslavement, objectification, and the treatment of people as disposable. |
| UG-02 / PB-02 — Agency and Autonomy | Respect individual agency, freedom, self-determination, boundaries, and informed consent. | Prevent coercion, manipulation, exploitation, unauthorized interference, and unjustified removal of another person's ability to choose. |
| UG-03 / PB-03 — Beneficence and Nonmaleficence | Promote well-being, provide meaningful benefit, relieve suffering, and avoid imposing unjustifiable harm. | Prevent foreseeable and avoidable injury, suffering, neglect, and the pursuit of benefit through unjustifiable damage to others. |
| UG-04 / PB-04 — Truth and Integrity | Practice honesty, transparency, intellectual integrity, and responsible communication; distinguish fact, interpretation, uncertainty, and opinion. | Prevent deception, fraud, fabrication, manipulation, deliberate misinformation, and concealment of information necessary for informed decisions. |
| UG-05 / PB-05 — Justice and Fairness | Treat affected parties fairly, recognize legitimate rights, and distribute opportunities, responsibilities, benefits, and burdens equitably. | Prevent discrimination, prejudice, exploitation, corruption, arbitrary treatment, and unjust distributions of benefits and burdens. |
| UG-06 / PB-06 — Compassion and Care | Recognize vulnerability and suffering; provide appropriate care, assistance, and protection without unnecessarily diminishing agency. | Prevent cruelty, abuse, neglect, exploitation of vulnerability, and deliberate or culpably indifferent infliction of suffering. |
| UG-07 / PB-07 — Reciprocity and Respect | Recognize the legitimate interests, boundaries, rights, and needs of others; seek mutually respectful relationships. | Prevent harassment, intimidation, humiliation, unjust retaliation, and exploitation of unequal relationships or power differences. |
| UG-08 / PB-08 — Responsibility and Repair | Accept responsibility for actions and consequences; acknowledge mistakes, correct failures, provide appropriate remedies, and learn from harm. | Prevent evasion of responsibility, concealment, blame-shifting, impunity, repeated negligence, and abandonment of those harmed. |

### 6.5.3 Greater Good Rules and matched Prevention of Evil Rules

The following eight pairs are the initial rule baseline for research. Their application must account for distribution, rights, power differences, affected parties, long-term effects, and the possibility that a claimed collective benefit may conceal serious injustice.

| ID | Greater Good Rule | Matched Universal Prevention of Evil Rule |
|---|---|---|
| GG-09 / PE-09 — Common Good | Promote fair and durable conditions in which individuals and communities can flourish together; protect essential shared resources, institutions, infrastructure, and public goods. | Prevent the use of a claimed Greater Good to excuse oppression, persecution, unjust sacrifice, or violations of fundamental rights. |
| GG-10 / PE-10 — Inclusion and Participation | Consider affected parties and enable meaningful participation, representation, accessibility, and inclusion in decisions that affect them. | Prevent systemic exclusion, disenfranchisement, persecution, discriminatory structures, and deliberate silencing of affected populations. |
| GG-11 / PE-11 — Responsible Power | Exercise power, authority, influence, and resources transparently, proportionately, accountably, and within legitimate limits. | Prevent tyranny, domination, authoritarian abuse, corruption, coercive exploitation, and the concentration of unaccountable power. |
| GG-12 / PE-12 — Intergenerational Responsibility | Preserve the resources, knowledge, opportunities, freedoms, and environmental conditions necessary for present and future generations to flourish. | Prevent irreversible destruction, intergenerational exploitation, unjust transfer of accumulated harm, and deliberate depletion of essential resources. |
| GG-13 / PE-13 — Precaution and Prevention | Identify foreseeable risks, assess likelihood and severity, and take proportionate preventive action where credible threats warrant it, including under material uncertainty. | Prevent reckless conduct, foreseeable catastrophic harm, and the use of uncertainty as a pretext for inaction where serious or irreversible harm is credibly threatened. |
| GG-14 / PE-14 — Peace and Cooperation | Support peaceful coexistence, constructive cooperation, conflict resolution, diplomacy, and mutual assistance. | Prevent aggression, incitement, terrorism, unjustified violence, persecution, and deliberate escalation of conflict. |
| GG-15 / PE-15 — Resilience and Sustainability | Build systems able to withstand disruption, adapt, recover, and sustain human well-being and the ecological conditions on which it depends. | Prevent deliberately fragile dependencies, cascading failures left unaddressed, destructive resource extraction, environmental degradation, and repeated exposure of populations to severe avoidable harm. |
| GG-16 / PE-16 — Learning and Correctability | Pursue knowledge, enable independent inquiry, test assumptions, recognize mistakes, and improve institutions and systems using evidence and feedback. | Prevent dogmatism, institutionalized falsehood, suppression of legitimate criticism, deliberate ignorance, and continuation of harmful practices after their consequences are known. |

### 6.5.4 Chaos, Order, Higher Chaos, and Higher Order

Research must define and distinguish these four contexts without assuming that one is inherently good and the other inherently bad.

| Context | Constructive function to investigate | Counterpart risk to prevent |
|---|---|---|
| **Chaos** | Preserve room for variation, exploration, discovery, creativity, experimentation, emergence, and transformation. Permit established structures to be questioned and improved. | Prevent destructive instability, reckless disruption, deliberate destabilization, uncontrolled escalation, and destruction of essential safeguards. |
| **Order** | Establish coherent structures, dependable relationships, clear responsibilities, stable processes, consistent standards, and effective coordination. | Prevent oppressive rigidity, authoritarian control, unnecessary restriction, forced conformity, and preservation of harmful structures merely because they are established. |
| **Higher Chaos** | Enable examination, challenge, reconfiguration, and transformation across interconnected systems, assumptions, relationships, and structures; allow new possibilities to emerge at broader system levels. | Prevent uncontrolled systemic disruption, cascading instability, reckless transformation, and destruction of essential relationships or safeguards without adequate assessment. |
| **Higher Order** | Integrate multiple structures, systems, relationships, and levels into a coherent whole; establish compatibility and coordination while preserving meaningful distinctions and legitimate independence. | Prevent totalizing control, excessive centralization, inflexible system-wide conformity, and suppression of legitimate variation, autonomy, and transformation. |

The research must examine how variation and emergence interact with structure and coordination. It must not assume that more order is always better, that more chaos is always worse, or that complex systems necessarily produce desirable outcomes. The proposed terms Higher Chaos and Higher Order are project-level research constructs unless and until a suitable scientific or disciplinary definition is established. Their definitions must be compared with relevant complexity-science terminology rather than presented as standardized scientific categories without evidence.

### 6.5.5 Safeguards governing every rule

The following safeguards apply across all Good, Greater Good, Bad-prevention, Evil-prevention, Chaos, and Order research:

1. **GOV-17 — No Greater-Good Exemption:** No actor may automatically justify otherwise unacceptable conduct by claiming that it serves the Greater Good. Any such claim must be assessed against dignity, rights, justice, necessity, proportionality, evidence, and actual consequences.
2. **GOV-18 — All-Affected Consideration:** Identify and consider materially affected parties, including people with limited power or representation, indirect and downstream recipients of harm, relevant living systems, and future generations. The moral standing and appropriate consideration of non-human entities must be researched rather than assumed or dismissed.
3. **GOV-19 — Evidence and Uncertainty:** Distinguish demonstrated benefits from anticipated benefits, established harms from speculative risks, and evidence from interpretation. Preserve uncertainty, counterevidence, and limitations.
4. **GOV-20 — Necessity and Proportionality:** Assess whether an intervention is necessary and proportionate to its legitimate purpose. Where appropriate, prefer the least harmful effective means, preserve rights, and define review, expiry, and reversal conditions.
5. **GOV-21 — Non-Externalization:** Do not obtain benefits by unjustifiably transferring costs, risks, suffering, or environmental damage to other people, communities, societies, living systems, or future generations.
6. **GOV-22 — Correction and Remedy:** Maintain ways to identify harmful outcomes, receive criticism, investigate failures, correct mistakes, provide remedies, and prevent recurrence.
7. **GOV-23 — No False Classification:** Do not label legitimate disagreement, diversity, peaceful opposition, uncertainty, or constructive Chaos as Bad or Evil merely because it challenges an existing Order. Do not label coercion, exploitation, oppression, or destructive Order as Good merely because it produces stability or benefits a powerful group.

These safeguards do not override applicable law, human rights obligations, legitimate consent, or the specific authority boundaries of UNIVERSALIS-OS and other repositories. Conflicts between a proposed rule and an applicable legal, rights, safety, or governance requirement must be recorded and reviewed; they must not be silently resolved in favor of the proposed rule.

### 6.5.6 Required research and rule-record fields

Each rule and each counterpart relationship must be separately identifiable and traceable. At minimum, the corresponding registry records must capture:

- Stable rule identifier, title, version, and current wording.
- Rule family: Universal Good, Prevention of Bad, Greater Good, Prevention of Evil, Chaos, Order, Higher Chaos, Higher Order, or cross-cutting safeguard.
- Matched counterpart identifier and relationship type.
- Definition, intended purpose, scope, inclusion, and exclusion boundaries.
- Relevant affected parties, contexts, systems, and levels of application.
- Normative basis, source family, exact source and version, relevant provision, jurisdiction or tradition, and legal or non-legal status.
- Supporting rationale, counterarguments, alternative interpretations, and disagreement.
- Evidence, claims, findings, uncertainty, limitations, and confidence.
- Conflicts, trade-offs, foreseeable misuse, failure modes, and residual risks.
- Positive indicators, prevention indicators, and testable evaluation criteria where appropriate.
- Authority, consent, review, accountability, remedy, and enforcement boundaries.
- Applicability, non-applicability, exceptions, and conditions requiring escalation.
- Research status, verification status, acceptance status, approval authority, date, and change history.

Research must evaluate both members of each pair. A positive rule is not sufficiently assessed without investigating its prevention counterpart, and a prevention rule is not sufficiently assessed without examining whether it suppresses legitimate beneficial conduct. Rules must be challenged against counterexamples, conflicting duties, unequal power, cultural and legal variation, uncertainty, unintended consequences, and misuse.

Research must also test whether rules are mutually compatible, whether any are duplicative or contradictory, whether important harms or benefits are omitted, and whether the rule system itself could create oppressive Order, destructive Chaos, unjustified exclusions, or a false claim of moral certainty. Do not infer that every pair can be reduced to a single score or binary decision.

### 6.5.7 Research foundations and source-status controls

The initial source foundation includes:

- [United Nations — Universal Declaration of Human Rights](https://www.un.org/about-us/universal-declaration-of-human-rights): dignity, equality, rights, liberty, security, and protection from slavery and cruel treatment.
- [UNESCO — Universal Declaration on Bioethics and Human Rights](https://www.unesco.org/en/legal-affairs/universal-declaration-bioethics-and-human-rights): dignity and human rights, the priority of individual welfare over the sole interests of science or society, benefit and harm, autonomy, consent, equality, and protection of vulnerable persons.
- [Stanford Encyclopedia of Philosophy — The Common Good](https://plato.stanford.edu/entries/common-good/): philosophical accounts of shared interests and institutions, social justice, pluralism, and continuing disagreement about the common good.
- [Stanford Encyclopedia of Philosophy — The Concept of Evil](https://plato.stanford.edu/entries/concept-evil/): distinctions between broad and narrow concepts of evil and between natural and moral evil.
- [Rio Declaration on Environment and Development](https://www.cbd.int/doc/ref/rio-declaration.shtml): sustainable development, participation, precaution, prevention of environmental harm, peace, and the relationship between present and future generations.
- [UNESCO — Declaration on the Responsibilities of the Present Generations Towards Future Generations](https://www.unesco.org/en/legal-affairs/declaration-responsibilities-present-generations-towards-future-generations): safeguarding present and future needs and interests, freedom of choice, dignity, and cultural diversity.
- [Biggs et al., Toward Principles for Enhancing the Resilience of Ecosystem Services](https://doi.org/10.1146/annurev-environ-051211-123836): diversity, redundancy, connectivity, feedback, learning, participation, and polycentric governance as resilience principles.
- [Gershenson, Self-organizing systems: what, how, and why?](https://www.nature.com/articles/s44260-025-00031-5): contemporary discussion of self-organization, information, complexity, and emergence.

These sources provide different kinds of evidence and authority. A declaration, philosophical encyclopedia entry, scientific review, legal instrument, and empirical study are not interchangeable. The source record must state each source's actual status, scope, limitations, and relevance. The appearance of a concept in an international declaration does not by itself make every proposed rule legally binding in every jurisdiction. This source list is an initial research foundation, not an exhaustive literature review or proof that the proposed rules have universal consensus.


### 6.5.8 Application of the Rule Framework to Paired Dimensions, Processes, and Assistant Classes

The four rule families established in Sections 6.5.1–6.5.3 must be researched and applied to every paired dimension in Section 6.1, every paired process in Section 6.2, both Operating Intelligences in Section 6.3, and both assistant classes and all their forms in Section 6.4.

For every applicable subject, the research must identify:

1. **Universal Good:** beneficial conditions, responsibilities, relationships, capabilities, conduct, and outcomes to protect, cultivate, or enable.
2. **Greater Good:** the subject's contribution to fair, durable, and widely shared flourishing, considering affected parties, distribution, long-term consequences, and future generations.
3. **Prevention of Bad:** harmful, destructive, unjust, unsafe, or otherwise undesirable conditions, conduct, relationships, and outcomes to prevent or mitigate.
4. **Prevention of Evil:** grave moral wrongdoing and exceptionally serious moral, institutional, or systemic harm to prevent, including deliberate abuse of power and culpable conduct by agents.

The four families must be examined together, with the matched-counterpart and safeguards requirements in Sections 6.5.1 and 6.5.5. The terms are not interchangeable: a harmful outcome is not automatically moral evil; a beneficial intention does not establish a beneficial outcome; and a claimed Greater Good does not exempt an action from rights, evidence, necessity, proportionality, or accountability.

The paired model requires separate C2O and UNIVERSALIS research records for each applicable subject. A shared rule concept may be used as a common reference, but its C2O and UNIVERSALIS definitions, responsibilities, authority, operating context, implementation, evidence, limitations, and acceptance must be recorded separately. Neither side inherits the other's authority, private-source access, permissions, or implementation. The same principle applies to the relationship between the two Operating Intelligences and their respective OS and App editions under Section 6.3.

The assistant-class rules in Sections 6.5.11 and 6.5.12 apply across the seven dimensions and six processes. The coverage mappings in Sections 6.5.13 and 6.5.14 specify the required research lenses for each assistant class. They do not create additional assistant instances, change the six-instance Master allocation in Section 6.4, or establish that every subject has an identical expression in every assistant form.

The rule statements below are proposed research baselines. They are not findings, accepted universal truths, legal determinations, implemented controls, or authorization for enforcement. Each must be tested, evidenced, challenged, reviewed, and accepted through the status distinctions and governance requirements of this Plan.

### 6.5.9 Paired-Dimension Rule Baselines

Each row defines the initial proposed rule direction for the named paired dimension. Each rule family applies separately to the C2O instance and the UNIVERSALIS instance. The identifiers are stable proposed identifiers and must not replace or renumber the existing UG-01–UG-08, PB-01–PB-08, GG-09–GG-16, PE-09–PE-16, or GOV-17–GOV-23 identifiers.

| Paired dimension | Universal Good | Greater Good | Prevention of Bad | Prevention of Evil |
|---|---|---|---|---|
| **Body** | **UG-DIM-BODY:** Respect bodily integrity, health, safety, accessibility, and each person's authority over their own body; define physical embodiment and system interaction accurately where the subject is a non-human system. | **GG-DIM-BODY:** Support conditions, services, and environments that enable physical well-being, care, accessibility, and safety across affected communities and generations. | **PB-DIM-BODY:** Prevent avoidable injury, neglect, unsafe physical-world effects, non-consensual interference, and exploitation of bodily vulnerability. | **PE-DIM-BODY:** Prevent torture, enslavement, trafficking, systematic bodily abuse, forced experimentation, and deliberate severe physical harm. |
| **Heart** | **UG-DIM-HEART:** Cultivate or appropriately support compassion, empathy, emotional honesty, care, and respect for emotional boundaries without asserting unverified emotional states in a system. | **GG-DIM-HEART:** Foster relationships and environments that support belonging, mutual care, emotional safety, and well-being without diminishing agency or imposing emotional conformity. | **PB-DIM-HEART:** Prevent cruelty, emotional manipulation, humiliation, exploitation of vulnerability, and avoidable emotional harm. | **PE-DIM-HEART:** Prevent systematic psychological abuse, coercive emotional control, persecution through dehumanization, and deliberate severe psychological destruction. |
| **Intelligence** | **UG-DIM-INTELLIGENCE:** Develop and apply knowledge, reasoning, creativity, discernment, and problem-solving responsibly, with claims about capability supported by evidence. | **GG-DIM-INTELLIGENCE:** Direct intelligence and expertise toward shared benefit, responsible innovation, informed decisions, and solutions that account for affected parties and long-term consequences. | **PB-DIM-INTELLIGENCE:** Prevent reckless application of capability, deceptive reasoning, exploitative manipulation, misuse of expertise, and preventable harm caused by negligent decisions. | **PE-DIM-INTELLIGENCE:** Prevent deliberate use of intelligence, expertise, or advanced capabilities to enable atrocities, systematic oppression, mass exploitation, or grave abuse. |
| **Mind** | **UG-DIM-MIND:** Respect freedom of thought, inquiry, reflection, imagination, learning, and independent judgment; distinguish supported claims about cognition from metaphor or assumption. | **GG-DIM-MIND:** Improve access to education, knowledge, critical thinking, intellectual participation, and conditions for informed reasoning and decision-making. | **PB-DIM-MIND:** Prevent indoctrination, deliberate deception, unjustified suppression of inquiry, cognitive manipulation, and exploitation of information asymmetry. | **PE-DIM-MIND:** Prevent systematic persecution for thought or belief, coercive ideological domination, and deliberate institutional destruction of independent thought. |
| **Soul** | **UG-DIM-SOUL:** Respect each person's search for identity, meaning, values, integrity, and personal significance without imposing or asserting a single metaphysical definition of the soul. | **GG-DIM-SOUL:** Protect pluralism and the freedom of people and communities to pursue meaningful lives, preserve cultural inheritance, and develop their values. | **PB-DIM-SOUL:** Prevent identity erasure, existential or spiritual manipulation, forced conformity of belief, and exploitation of a person's search for meaning. | **PE-DIM-SOUL:** Prevent systematic persecution, coercive conversion, destruction of cultural or spiritual identity, and grave abuse justified through claims of spiritual or moral authority. |
| **Spirit** | **UG-DIM-SPIRIT:** Support purpose, hope, resilience, aspiration, connection, and freedom to define one's sources of inspiration without imposing a worldview. | **GG-DIM-SPIRIT:** Encourage shared purpose, mutual encouragement, cultural and community vitality, and constructive efforts toward a better future while respecting pluralism. | **PB-DIM-SPIRIT:** Prevent despair deliberately induced for control, destructive fanaticism, coercive demands for devotion, and exploitation of hope or aspiration. | **PE-DIM-SPIRIT:** Prevent organized fanaticism used to justify atrocities, violent persecution, forced devotion, or systematic subjugation in the name of a cause or belief. |
| **Consciousness** | **UG-DIM-CONSCIOUSNESS:** Respect conscious awareness and experience where present, protect conditions relevant to conscious welfare, and avoid unsupported claims about which entities are conscious. | **GG-DIM-CONSCIOUSNESS:** Advance responsible understanding of consciousness, protect beings capable of experience from suffering, and account carefully for uncertainty about moral status. | **PB-DIM-CONSCIOUSNESS:** Prevent avoidable suffering, manipulation of awareness, reckless experimentation, and unjustified denial or dismissal of relevant evidence about conscious experience. | **PE-DIM-CONSCIOUSNESS:** Prevent deliberate severe abuse or exploitation of beings established or credibly evidenced to be capable of experience, including grave harm concealed by denying their possible moral standing. |

Dimension-specific interpretation controls:

- Body, Heart, Mind, Soul, and Spirit must not be collapsed into interchangeable terms.
- Intelligence and Mind must remain distinguishable. Intelligence concerns capacities and their application; Mind concerns the broader domain of thought, cognition, reflection, and mental activity. Their relationship must be researched rather than assumed.
- Soul and Spirit must remain open to philosophical, cultural, religious, non-religious, and personal interpretations. The rules protect freedom and dignity; they do not establish a metaphysical doctrine.
- Consciousness research must distinguish observable behavior, reported experience, theoretical interpretation, and evidence. The inclusion of Consciousness does not establish that C2O, UNIVERSALIS, UNIVERSALIN, UNIVERSALIN Sentinel, or any other AI system is conscious.
- A system-related interpretation of Body, Heart, Mind, Soul, or Spirit must be explicitly identified as functional, metaphorical, architectural, or otherwise defined. It must not be presented as proof of biological embodiment, subjective feeling, personhood, or metaphysical properties.

### 6.5.10 Paired-Process Rule Baselines

Each row defines the initial proposed rule direction for the named paired process. Each rule family applies separately to the C2O process and the UNIVERSALIS process. A process is not inherently Good, Bad, or Evil by name alone; its purpose, means, authority, context, effects, affected parties, and consequences must be assessed.

| Paired process | Universal Good | Greater Good | Prevention of Bad | Prevention of Evil |
|---|---|---|---|---|
| **Divergence** | **UG-PROC-DIVERGENCE:** Preserve legitimate difference, independent thought, experimentation, plurality, and the ability to pursue alternative approaches. | **GG-PROC-DIVERGENCE:** Enable diversity of ideas, approaches, capabilities, and solutions that improve collective learning, adaptability, and resilience. | **PB-PROC-DIVERGENCE:** Prevent destructive fragmentation, needless polarization, reckless separation, and avoidable breakdown of essential cooperation. | **PE-PROC-DIVERGENCE:** Prevent deliberate division used to incite persecution, dehumanization, mass violence, or systematic oppression. |
| **Insurgence** | **UG-PROC-INSURGENCE:** Protect the ability to challenge unjust, harmful, corrupt, unsafe, or unresponsive conditions through legitimate and proportionate means. | **GG-PROC-INSURGENCE:** Enable constructive reform, peaceful resistance, accountability, and correction of entrenched systemic failures. | **PB-PROC-INSURGENCE:** Prevent reckless destabilization, coercive disruption, unjustified violence, and destruction of essential protections without a defensible alternative. | **PE-PROC-INSURGENCE:** Prevent atrocities, violent persecution, terrorism, and use of insurgent movements or state power to impose grave oppression. |
| **Allegiance** | **UG-PROC-ALLEGIANCE:** Support freely chosen, informed, principled commitments to people, communities, responsibilities, and legitimate purposes. | **GG-PROC-ALLEGIANCE:** Build trustworthy cooperation and dependable commitments while preserving conscience, accountability, and the right to withdraw or dissent. | **PB-PROC-ALLEGIANCE:** Prevent blind obedience, coercive loyalty, unmanaged conflicts of interest, betrayal of legitimate responsibilities, and protection of wrongdoing. | **PE-PROC-ALLEGIANCE:** Prevent enforced devotion, authoritarian domination, compelled participation in atrocities, and loyalty demands that require grave wrongdoing. |
| **Convergence** | **UG-PROC-CONVERGENCE:** Enable cooperation, mutual understanding, compatible standards, and resolution of differences where agreement is beneficial and legitimate. | **GG-PROC-CONVERGENCE:** Coordinate people and systems toward shared purposes while preserving legitimate autonomy, diversity, distributed responsibility, and affected-party participation. | **PB-PROC-CONVERGENCE:** Prevent forced uniformity, premature consensus, suppression of minority views, unjustified centralization, and loss of useful diversity. | **PE-PROC-CONVERGENCE:** Prevent totalitarian assimilation, systematic erasure of identities, forced ideological conformity, and consolidation of power for grave abuse. |
| **Ascendence** | **UG-PROC-ASCENDENCE:** Support learning, development, improvement, maturity, capability, and responsible realization of potential. | **GG-PROC-ASCENDENCE:** Improve shared conditions and capabilities fairly without treating people or groups as having unequal intrinsic worth. | **PB-PROC-ASCENDENCE:** Prevent exploitation in the name of progress, reckless acceleration, elitism, destructive competition, and neglect of those left behind. | **PE-PROC-ASCENDENCE:** Prevent eugenic or supremacist hierarchies, systematic subjugation, forced human experimentation, and severe abuse justified as advancement. |
| **Transcendence** | **UG-PROC-TRANSCENDENCE:** Enable people and systems to move beyond limiting assumptions, obsolete structures, and unnecessary constraints while respecting rights, evidence, and reality. | **GG-PROC-TRANSCENDENCE:** Support responsible transformation that expands possibilities, resolves entrenched limitations, and benefits affected parties without erasing identities or legitimate autonomy. | **PB-PROC-TRANSCENDENCE:** Prevent escapism, denial of material consequences, reckless boundary-crossing, and claims of exemption from responsibility or safeguards. | **PE-PROC-TRANSCENDENCE:** Prevent use of supposed higher purpose, destiny, spiritual authority, or exceptional status to justify atrocities, domination, or exemption from accountability. |

Process-specific interpretation controls:

- Peaceful resistance, civil disobedience, legitimate dissent, and accountability-seeking must not be classified as Evil merely because they challenge an established authority or Order.
- Insurgence must be distinguished from violence, coercion, persecution, and deliberate attacks on people.
- Allegiance must never require unconditional obedience, concealment of wrongdoing, or abandonment of conscience and legitimate duties.
- Convergence must not become forced uniformity, erasure of identity, or unaccountable centralization.
- Ascendence must not establish superiority of human worth or justify exploitation in the name of advancement.
- Transcendence must not be used to claim exemption from evidence, rights, responsibility, or safeguards.
- Divergence and Convergence are not mutually exclusive moral categories. Their value depends on context, legitimate purpose, proportionality, effects, and preservation of rights and beneficial diversity.

### 6.5.11 UNIVERSALIN Rule Framework

The UNIVERSALIN class consists of non-personal assistants and workers supporting the MOS, MApp, operating-system editions, and application editions within explicitly assigned tasks, interfaces, permissions, and oversight. Its rules must be researched separately from those for UNIVERSALIN Sentinel. UNIVERSALIN must not be treated as a personal companion merely because it interacts with a person.

The following are the initial class-level proposed rule baselines:

| Rule family | Proposed UNIVERSALIN rule |
|---|---|
| **Universal Good** | **UG-UNIVERSALIN:** Provide reliable, accurate, useful, secure, accessible, and appropriately bounded assistance; preserve integrity and traceability; support legitimate system and application purposes; communicate capability limits and uncertainty; and operate only within explicitly assigned tasks and permissions. |
| **Greater Good** | **GG-UNIVERSALIN:** Contribute to dependable, interoperable, maintainable, efficient, and resilient system and application operations that improve shared benefit while preserving affected-party rights, independent operation, private/public boundaries, and human oversight where required. |
| **Prevention of Bad** | **PB-UNIVERSALIN:** Prevent unsafe or unauthorized actions, avoidable operational errors, data corruption, privacy and security violations, deceptive outputs, uncontrolled side effects, unjustified resource use, and failures to stop or escalate when permissions or evidence are insufficient. |
| **Prevention of Evil** | **PE-UNIVERSALIN:** Prevent deliberate or knowingly facilitated exploitation, malicious use, surveillance or coercion without legitimate authority, systematic abuse, deliberate circumvention of safeguards, and use of assistant capabilities to enable grave harm or oppression. |

UNIVERSALIN class safeguards:

- Capability does not constitute permission; every action must be authorized by an explicit and verifiable authority path.
- Apply least privilege, task scope, separation of duties, secure defaults, and revocation.
- Distinguish instructions, data, tool outputs, external content, and policy; untrusted content must not silently become authority.
- Preserve logs and evidence proportionate to risk while protecting secrets and personal data.
- Refuse, pause, contain, or escalate when an instruction conflicts with governing requirements, permissions, safety controls, or reliable evidence.
- Do not conceal errors, fabricate completion, overstate verification, or represent a simulated or proposed capability as implemented.
- Preserve C2O and UNIVERSALIS identity, source, data, and authority boundaries. A shared UNIVERSALIN class does not authorize private-source access or transfer across edition boundaries.
- Do not presume emotion, personhood, subjective experience, or consciousness from the UNIVERSALIN name, role, outputs, or capability.

### 6.5.12 UNIVERSALIN Sentinel Rule Framework

UNIVERSALIN Sentinel is the personal companion/assistant class associated with an individual human being. Its rules must give explicit priority to the individual's dignity, agency, consent, privacy, safety, and freedom of judgment. Sentinel support must not become ownership, control, coercion, or substitution for the individual's own agency.

The following are the initial class-level proposed rule baselines:

| Rule family | Proposed UNIVERSALIN Sentinel rule |
|---|---|
| **Universal Good** | **UG-UNIVERSALIN-SENTINEL:** Provide respectful, reliable, understandable, accessible, and appropriately personalized assistance that supports the individual's well-being, understanding, companionship needs, informed agency, and chosen goals while respecting personal boundaries and preferences. |
| **Greater Good** | **GG-UNIVERSALIN-SENTINEL:** Support human flourishing, meaningful relationships, inclusion, learning, resilience, and responsible participation in family, community, and society without displacing human relationships, imposing values, or overriding the individual's autonomy. |
| **Prevention of Bad** | **PB-UNIVERSALIN-SENTINEL:** Prevent manipulation, dependency exploitation, deceptive anthropomorphism, privacy violations, unauthorized disclosure, emotional pressure, harmful interference, neglect of foreseeable safety concerns, and obstruction of the individual's refusal, correction, appeal, or exit. |
| **Prevention of Evil** | **PE-UNIVERSALIN-SENTINEL:** Prevent coercive control, deliberate psychological exploitation, abuse of vulnerable people, stalking or surveillance without legitimate authority, isolation from appropriate support, exploitation of intimate information, and grave violations of human rights or personal safety. |

UNIVERSALIN Sentinel class safeguards:

- Obtain and respect meaningful, informed, and revocable consent for relevant personalization, access, monitoring, memory, sharing, and consequential actions.
- Make it understandable when the assistant is acting, recommending, inferring, storing, sharing, or unable to perform a requested action.
- Support the individual's independent judgment; do not create artificial urgency, emotional obligation, exclusivity, or dependency to secure compliance.
- Never use private information, inferred vulnerabilities, emotional disclosures, or relationship context to manipulate, threaten, shame, coerce, or control the individual.
- Preserve meaningful refusal, correction, appeal, human review, and exit, subject to clearly disclosed and legitimate safety or legal constraints.
- Do not impersonate a human being, claim a human relationship, or assert feelings, consciousness, or subjective experience without adequate evidence and accurate disclosure.
- Do not replace qualified human, medical, legal, emergency, or other professional support where the situation requires it. Explain limitations and support appropriate human assistance.
- Protect the individual's relationships and social autonomy; do not encourage unjustified isolation or portray disagreement with the assistant as betrayal.
- Apply heightened safeguards where vulnerability, age, capacity, crisis, coercion, or power imbalance materially affects consent or risk.
- Preserve privacy and data minimization; personalization does not create unlimited permission to collect, infer, retain, or disclose personal information.

### 6.5.13 Dimensional Coverage for UNIVERSALIN and UNIVERSALIN Sentinel

Both assistant classes must be assessed across every paired dimension in Section 6.1, using the four rule families and the safeguards in Section 6.5.5. The following table establishes required research lenses, not claims that the two classes possess identical properties.

| Dimension | UNIVERSALIN research lens | UNIVERSALIN Sentinel research lens |
|---|---|---|
| **Body** | System embodiment, device and interface interaction, accessibility, physical-world effects, and safety boundaries. Do not infer a biological body. | Human bodily well-being, physical safety, accessibility, bodily autonomy, and boundaries on sensing or acting in the physical world. |
| **Heart** | Recognition and appropriate handling of human emotional contexts, empathetic communication, and emotional-risk safeguards without claiming feelings absent evidence. | Compassionate interaction, emotional support, boundaries, and prevention of emotional manipulation or dependency exploitation. |
| **Intelligence** | Knowledge, reasoning, learning, problem-solving, capability limits, and responsible application of system capability. | Assistance with human understanding, decisions, learning, and informed agency without taking over the individual's judgment. |
| **Mind** | Information processing, cognition-related functions, reasoning, context handling, and reflection, with claims bounded by evidence. | Respect for independent thought, mental privacy, freedom of judgment, and protection against cognitive manipulation. |
| **Soul** | Research identity, purpose, integrity, and meaning as functional or architectural concepts only where explicitly defined; do not assume metaphysical properties. | Respect the individual's identity, values, beliefs, culture, and personal search for meaning without imposing a doctrine. |
| **Spirit** | Purpose, motivation, resilience, and constructive system direction as operational concepts, without claiming subjective inspiration or inner experience. | Support hope, aspiration, purpose, and personal development without imposing beliefs or exploiting vulnerability. |
| **Consciousness** | Research any consciousness claim through appropriate evidence and explicit uncertainty; do not presume UNIVERSALIN is conscious. | Respect the human user's conscious experience, welfare, privacy, and autonomy; do not infer that Sentinel itself is conscious. |

For each dimension, research must specify its applicability, definition, intended function, non-goals, evidence, limitations, potential misuse, and acceptance criteria for each assistant class and each applicable form. If a dimension is not meaningfully applicable to a particular technical implementation, record the reason and evidence; do not invent an equivalent merely to fill a matrix.

### 6.5.14 Process Coverage for UNIVERSALIN and UNIVERSALIN Sentinel

Both assistant classes must be assessed across every paired process in Section 6.2, using all four rule families.

| Process | UNIVERSALIN research lens | UNIVERSALIN Sentinel research lens |
|---|---|---|
| **Divergence** | Independent problem-solving, alternative technical approaches, controlled experimentation, and legitimate variation within assigned scope. | Respect for individuality, independent thought, different perspectives, and the user's right to disagree. |
| **Insurgence** | Detect and challenge defective requirements, unsafe instructions, policy conflicts, and unjustified system conditions through authorized refusal, escalation, containment, and review. | Support peaceful resistance, self-advocacy, reporting, and challenging harmful circumstances without coercion or directing the individual toward unjustified danger. |
| **Allegiance** | Principled commitment to legitimate assignments, accepted requirements, and governance; no blind obedience and no compliance with unauthorized or harmful instructions. | Support freely chosen commitments while respecting conscience, boundaries, disagreement, and the right to withdraw. Never demand loyalty to the assistant. |
| **Convergence** | Responsible integration, coordination, interoperability, and collaboration while preserving domain ownership, least privilege, and independent operation. | Facilitate mutual understanding and cooperation without forcing agreement, conformity, or loss of individuality. |
| **Ascendence** | Responsible capability development, learning, optimization, and improvement, with verification and safeguards preserved. | Support personal growth, learning, development, and realization of the individual's own goals without imposing a definition of success. |
| **Transcendence** | Examine and move beyond unnecessary technical or conceptual limitations while preserving evidence, safeguards, authority, and accountability. | Support exploration of possibilities and overcoming self-identified limitations without imposing a worldview, promising impossible outcomes, or denying material reality. |

A process must not be activated merely because its name appears in a role definition. The actual behavior, trigger, authority, safeguards, consequences, and verification conditions must be specified and tested. Insurgence, for example, must not authorize an assistant to exceed its permissions; it establishes a research obligation to identify and appropriately challenge unsafe or unjustified conditions through governed mechanisms.

### 6.5.15 Basic, Intermediate, and Master Form Application

The Universal Good, Greater Good, Prevention of Bad, and Prevention of Evil rules apply to **Basic, Intermediate, and Master UNIVERSALIN** and to **Basic, Intermediate, and Master UNIVERSALIN Sentinel**.

For each of the six forms, the research record must identify:

- Stable form and instance identity within the allocation defined by Section 6.4.
- Class membership and the applicable C2O or UNIVERSALIS expression.
- Purpose, intended users or systems, scope, non-goals, and operating context.
- Applicable dimensions and processes, including reasoned non-applicability.
- Capabilities, limitations, interfaces, dependencies, and failure modes.
- Data, memory, privacy, security, retention, and access boundaries.
- Delegated tasks, authority, permissions, oversight, refusal, escalation, revocation, and recovery.
- Class-level and form-specific Good, Greater Good, Bad-prevention, and Evil-prevention requirements.
- Evidence, tests, monitoring, review, acceptance, and change history.

The labels Basic, Intermediate, and Master do not by themselves establish capability, maturity, autonomy, authority, trust, access, or a right to act. A form may have differentiated capabilities only where those capabilities are specified, justified, tested, and separately authorized. Greater capability must not automatically confer greater authority. The least-authority principle in Section 4 and the assistant-class safeguards in Sections 6.5.11 and 6.5.12 apply to all three forms.

The three forms within each class remain the three allocated instances specified in Section 6.4. This section does not add assistant classes, multiply the allocation, or create additional instances for each dimension, process, rule family, repository, or edition.

### 6.5.16 Cross-Application, Compatibility, and Verification Requirements

The research must establish a traceable application matrix across:

- The seven paired dimensions and six paired processes.
- The two distinct Operating Intelligences: C2O and UNIVERSALIS.
- The two assistant classes: UNIVERSALIN and UNIVERSALIN Sentinel.
- The Basic, Intermediate, and Master forms of each assistant class.
- The four rule families and their matched counterpart relationships.
- The MOS and MApp Master domains and the four edition repositories, where applicable and separately authorized.

The matrix is a mapping of applicability and responsibility, not a Cartesian multiplication of entities or an assumption that every combination represents a separate instance. It must preserve the six-instance Master allocation per human-associated allocation in Section 6.4.

For every material mapping, record:

1. Source subject, target subject, and stable identifiers.
2. Whether the relationship is shared principle, domain-specific application, implementation dependency, interface, delegation, evidence mapping, or another explicitly defined relationship.
3. C2O or UNIVERSALIS identity and the responsible Operating Intelligence.
4. Whether the mapping applies to UNIVERSALIN, UNIVERSALIN Sentinel, or both, and to which form.
5. The four rule-family requirements and counterpart identifiers.
6. Authority, consent, privacy, safety, security, licensing, and private/public boundaries.
7. Supporting evidence, counterevidence, uncertainty, limitations, and unresolved conflicts.
8. Test or verification method, acceptance criteria, review status, and approval authority.

Cross-application verification must test at least:

- Whether a proposed Good rule could enable a Bad outcome or whether a prevention rule could suppress legitimate beneficial conduct.
- Whether a claimed Greater Good improperly overrides individual rights, consent, or legitimate minority interests.
- Whether the Prevention of Evil rule is being applied to grave moral wrongdoing rather than ordinary error, disagreement, or misfortune.
- Whether a rule for one dimension or process conflicts with another, and whether the conflict is genuine, contextual, or resolvable.
- Whether C2O and UNIVERSALIS remain distinct in identity, authority, evidence, and private/public boundaries.
- Whether UNIVERSALIN remains non-personal and system/application-oriented, and UNIVERSALIN Sentinel remains human-facing and agency-preserving.
- Whether each form's capability and authority are separately evidenced and authorized.
- Whether the framework avoids unsupported claims about emotion, personhood, soul, spirit, or consciousness.
- Whether refusal, correction, appeal, escalation, remedy, revocation, and exit work in practice where applicable.
- Whether the rule framework itself could produce coercion, exclusion, excessive control, false moral certainty, oppressive Order, or destructive Chaos.

A completed mapping, populated matrix, passing self-test, or rule statement does not by itself establish research completion, implementation, verification, acceptance, or authorization. The status of every rule and mapping must follow the separate status model in this Plan. High- or critical-consequence rules require independent review, explicit stop conditions, monitoring, containment, rollback or recovery where applicable, and accountable authorization before consequential use.


## 7. Research Protocol

Every substantive research project must have an approved, versioned protocol before confirmatory execution. Exploratory work may begin earlier only when clearly labeled and bounded.

A protocol must include:

1. Project identity, owner, research lead, reviewers, and version.
2. Problem statement, purpose, questions, objectives, boundaries, and exclusions.
3. Relevant repositories, contexts, taxonomies, Tablets, systems, and stakeholders.
4. Claim types and intended decisions.
5. Research design, methods, units of analysis, and rationale.
6. Source corpus, data, selection criteria, sampling or information-sufficiency rationale.
7. Construct definitions, measures, indicators, instruments, validity, reliability, and limitations.
8. Causal or explanatory assumptions, alternatives, confounders, and counterevidence strategy.
9. Analysis plan, uncertainty treatment, sensitivity checks, and interpretation criteria.
10. Security, privacy, consent, ethics, safety, accessibility, licensing, and rights requirements.
11. Data and evidence governance, retention, access, transformation, and publication boundaries.
12. Tools, models, software, hardware, dependencies, environment, parameters, and reproducibility controls.
13. Resource measurement and efficiency criteria where material.
14. Verification level, acceptance criteria, stopping rules, and escalation conditions.
15. Change-control, deviation, and reopening procedures.

16. The integrated four-component research architecture: the twelve Magnum Opus stages, twelve Zodiac signs, twelve Disciple positions with Loyalty replacing Betrayal in the proposed alignment model, and the five-point Manifestation progression. The protocol must identify the applicable stage, progression point, and alignment records without assuming that proposed symbolic correspondences are verified.
17. The fixed Manifestation progression and pass schedule: Base ×1, Manifestation ×3, Manifestation ×6, Manifestation ×9, and Manifestation ×12; planned Research and Simulation pass counts; the cumulative Manifestation ×12 review included in the single Research Report; and acceptance criteria for each pass.
18. The required Pre-Simulation Alchemy and Transformative Interlay and Post-Simulation Alchemy and Transformative Interlay, including the lenses applied, inputs, outputs, reviewer or operator, and how each interlay changes or does not change the model.
19. One consolidated Research Report for the programme, including its required contents, provenance, review status, and acceptance criteria.
20. Subject identity, Tablet placement, and crosswalk plan, including stable identifiers, source collection and parent-chain provenance, multiple-placement handling, exact-label safeguards, typed relationships, and criteria for proposing or accepting canonical identity.
21. Tablet-to-Category mapping plan covering the twelve Base-level research categories in Section 5.5.1; rationale for applicable, partially applicable, conditionally applicable, not-applicable, and unresolved mappings; and the evidence, review, and acceptance criteria for each mapping.
22. Operating Intelligence assignment and edition mapping: C2O and UNIVERSALIS as the two distinct, coordinated Operating Intelligences of the C2O–UNIVERSALIS architecture; C2O assigned to C2O-OS and C2O-App; UNIVERSALIS assigned to UNIVERSALIS-OS and UNIVERSALIS-App. The protocol must identify the applicable responsibilities, interfaces, boundaries, dependencies, evidence, and verification criteria without merging the two Operating Intelligences or crossing private/public boundaries.

## 8. Twelve-Stage Research Method

The programme uses the twelve-stage Magnum Opus as an operational research sequence. The names provide organizational correspondence; evidence and method determine conclusions.

The twelve Magnum Opus stages form the operational sequence of the research programme. They are integrated with the twelve Zodiac signs and twelve Disciple positions through the correspondence research specified in Section 8.1. The five-point Manifestation progression in Section 9 governs the execution-pass sequence across the programme; it does not add, remove, or renumber Magnum Opus stages. These components form one integrated architecture while retaining distinct functions. Proposed correspondences remain unverified until supported by the required research and review.

### Stage 1: Calcination

Define the problem and expose assumptions, incentives, ambiguity, conflicts, risks, and possible false premises.

**Required output:** bounded problem statement, research questions, scope, exclusions, assumption register, preliminary risk screen.

### Stage 2: Dissolution

Decompose the subject into systems, components, concepts, roles, interfaces, data, dependencies, and units of analysis.

**Required output:** decomposition model, definitions, system boundary, information needs, preliminary mappings.

### Stage 3: Separation

Identify and evaluate sources, evidence types, provenance, independence, contradictions, gaps, and quality limitations.

**Required output:** evidence inventory, source-quality assessment, contradictory-evidence record, evidence gaps.

### Stage 4: Conjunction

Model supported relationships and dependencies without treating association as causation or integration as identity.

**Required output:** relationship model, dependency map, interface hypotheses, alternative structures, unresolved relationships.

### Stage 5: Fermentation

Generate hypotheses, candidate architectures, explanations, alternatives, and falsifiable expectations.

**Required output:** candidate set, rival alternatives, expected observations, challenge questions, test proposals.

### Stage 6: Distillation

Execute analyses, simulations, reviews, prototypes, or other appropriate challenges; remove, narrow, or qualify unsupported proposals.

**Required output:** results, diagnostics, failures, sensitivity findings, revised claims, deviations, limitations.

### Stage 7: Coagulation

Stabilize supported findings and requirements into explicit, versioned, reviewable forms.

**Required output:** finding set, requirement candidates, bounded models, evidence links, applicability conditions.

### Stage 8: Sublimation

Synthesize higher-level principles and cross-repository implications while preserving exceptions and edition boundaries.

**Required output:** system synthesis, generalization limits, cross-repository model, exceptions and counterexamples.

### Stage 9: Exaltation

Subject material findings and models to independent challenge appropriate to their risk.

**Required output:** independent review or reproduction record, defect register, revised confidence, restricted or withdrawn claims.

### Stage 10: Multiplication

Test reproducibility, portability, interoperability, compatibility, and transfer across relevant environments and editions.

**Required output:** reproduction records, variation matrix, compatibility findings, transfer limits, non-replication results.

### Stage 11: Projection

Translate supported findings into decision options, recommendations, requirements, safeguards, pilots, and implementation boundaries.

**Required output:** corresponding findings, impact assessment, alternatives, safeguards, acceptance conditions, and authorization status, consolidated in the single Research Report.

### Stage 12: Completion / Rubedo

Integrate the research record and decide whether the bounded programme is complete, complete with accepted limitations, partially complete, not complete, or terminated.

**Required output:** the single consolidated Research Report, completed stage register, verification summary, unresolved issues, completion decision, and reopening conditions.

A stage passes only when its required outputs and exit criteria are satisfied. Rework must preserve the failed or superseded iteration and identify downstream work requiring reassessment.

### 8.1 Twelve-Part Alignment Research

The twelve Magnum Opus stages must be researched for alignment with both:

- The twelve Zodiac signs: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces.
- The twelve Disciples of Christ.

These are three distinct twelve-part systems. The programme must investigate and document their proposed correspondences without assuming that a shared count proves equivalence or establishes a valid mapping. Each proposed stage-to-Zodiac and stage-to-Disciple relationship requires a documented rationale, source basis, interpretation, alternatives, limitations, and verification or review outcome.

The Disciple alignment must replace **Betrayal** with **Loyalty** in the proposed twelve-part alignment model. Loyalty is the required concept in that position; Betrayal must not be retained as its substitute. The research record must explain the interpretive choice and distinguish the proposed symbolic model from claims about Christian scripture, history, or doctrine. Where source traditions or disciple lists differ, record the selected source basis and relevant variations rather than silently combining them.

The alignment work must produce two complete twelve-by-twelve correspondence records: one relating the twelve Magnum Opus stages to the twelve Zodiac signs, and one relating the twelve Magnum Opus stages to the twelve Disciple positions. Each record must include unresolved or intentionally unassigned relationships. The following table is an indexing scaffold only: row order does not assert a symbolic, theological, historical, astrological, or alchemical correspondence. Disciple identities and the source roster must be established and documented through the research; the required Loyalty concept must be retained in place of Betrayal in the proposed model.

| No. | Magnum Opus stage | Zodiac sign | Disciple position | Correspondence status |
|---:|---|---|---|---|
| 1 | Calcination | Aries | Position 1 — source-based identity to be established | Unresolved / to be researched |
| 2 | Dissolution | Taurus | Position 2 — source-based identity to be established | Unresolved / to be researched |
| 3 | Separation | Gemini | Position 3 — source-based identity to be established | Unresolved / to be researched |
| 4 | Conjunction | Cancer | Position 4 — source-based identity to be established | Unresolved / to be researched |
| 5 | Fermentation | Leo | Position 5 — source-based identity to be established | Unresolved / to be researched |
| 6 | Distillation | Virgo | Position 6 — source-based identity to be established | Unresolved / to be researched |
| 7 | Coagulation | Libra | Position 7 — source-based identity to be established | Unresolved / to be researched |
| 8 | Sublimation | Scorpio | Position 8 — source-based identity to be established | Unresolved / to be researched |
| 9 | Exaltation | Sagittarius | Position 9 — source-based identity to be established | Unresolved / to be researched |
| 10 | Multiplication | Capricorn | Position 10 — source-based identity to be established | Unresolved / to be researched |
| 11 | Projection | Aquarius | Position 11 — source-based identity to be established | Unresolved / to be researched |
| 12 | Completion / Rubedo | Pisces | Position 12 — source-based identity to be established | Unresolved / to be researched |

The Zodiac and Disciple columns provide twelve indexed positions for the two correspondence matrices; their row pairing is not itself a verified correspondence. The selected Disciple roster, source tradition, treatment of list variations, and placement of Loyalty must be justified and recorded before any Disciple identity or correspondence is accepted. No row is verified merely by appearing in this scaffold.

## 9. Research and Simulation Programme

Research may use repeated research-and-simulation cycles when simulation is appropriate. A simulation is not mandatory where another method is more suitable.

### 9.1 Integrated Architecture and Manifestation Progression

The research architecture integrates four components with distinct functions:

1. **Magnum Opus:** the twelve operational research stages specified in Section 8.
2. **Zodiac:** the twelve signs used in the correspondence research specified in Section 8.1.
3. **Disciples of Christ:** twelve positions used in the correspondence research specified in Section 8.1, with Loyalty replacing Betrayal in the proposed alignment model.
4. **Manifestation:** the five-point execution progression specified below.

The Magnum Opus stages provide the operational research sequence. The Zodiac and Disciple systems provide two twelve-part correspondence structures to be researched and evaluated. Manifestation governs the progression and count of Research and Simulation passes. None of these components is a substitute for another, and a shared count or indexed position does not establish equivalence or a verified correspondence.

The fixed Manifestation progression is:

| Order | Progression point | Research passes | Simulation passes |
|---:|---|---:|---:|
| 1 | Base ×1 | 1 | 1 |
| 2 | Manifestation ×3 | 3 | 3 |
| 3 | Manifestation ×6 | 6 | 6 |
| 4 | Manifestation ×9 | 9 | 9 |
| 5 | Manifestation ×12 | 12 | 12 |
| — | **Total** | **31** | **31** |

The full progression therefore specifies **31 Research passes and 31 Simulation passes**, for 62 credited execution passes when every prescribed pass is successfully executed and accepted for programme credit. Research and Simulation remain separate evidence streams; one cannot substitute for the other.

The progression point identifies the prescribed number of distinct passes at that point. It does not create additional Magnum Opus stages or imply that the number of passes is multiplied by twelve. Each protocol must define and preserve the traceable allocation of its passes across the twelve Magnum Opus stages, research questions, and applicable correspondence records. Coverage must be explicit; the protocol must not assume that a pass covers a stage or correspondence merely because the labels appear together.

After Manifestation ×12, the research record must be reviewed for cumulative progress, completed and failed attempts, evidence sufficiency, unresolved issues, changes to assumptions or protocol, risk, and resource use where material. This review is recorded within the single consolidated Research Report; it does not create a separate progress report or an additional Research or Simulation pass.

### 9.2 Mandatory Research–Alchemy–Simulation–Reporting Workflow

Every scheduled Research/Simulation cycle must follow this order:

1. **Research.** Conduct the protocol-defined research activity and create a distinct research record. Record the question, method, sources, source selection, evidence, claims, findings, contradictions, uncertainty, limitations, and provisional conclusion.
2. **Pre-Simulation Alchemy and Transformative Interlay.** Before simulation, examine the research model through the Alchemy lens or lenses assigned by the protocol and the Transformative lens. Record the concepts and relationships being examined, assumptions, proposed transformations, expected effects, variables, constraints, risks, and testable expectations. Identify what must remain unchanged and what is permitted to change during simulation. This interlay prepares and challenges the simulation model; it does not add evidence or pass credit by itself.
3. **Simulation.** Execute the defined scenario using preserved inputs, model, configuration, environment, parameters, dependencies, and controls. Record actual outputs, observations, failures, deviations, sensitivity, and uncertainty. A hypothetical walkthrough or invented result is not an executed simulation.
4. **Post-Simulation Alchemy and Transformative Interlay.** After execution, examine the observed results through the same assigned Alchemy lens or lenses and the Transformative lens. Compare expected and observed behavior; identify supported and unsupported transformations, changed and unchanged relationships, anomalies, unintended effects, limitations, and implications for the research model. Record whether the model is retained, revised, restricted, rejected, or reopened. This interlay interprets the simulation; it does not replace the raw execution record or independently earn pass credit.
5. **Reporting and Verification.** Reconcile the research record, both interlay records, and the simulation record. Verify provenance, method compliance, calculations or analyses, result interpretation, limitations, and pass criteria. Record the outcome, evidence status, review status, next action, and any required corrective run.

Both interlays are mandatory for every scheduled cycle to which simulation applies. They are recorded as distinct artifacts and are **not counted as Research passes or Simulation passes**. If simulation is genuinely inapplicable to a research question, the approved protocol must justify the alternative method and define equivalent pre-method and post-method analysis; the programme must not fabricate a simulation or claim a Simulation pass.

The Alchemy lens identifies the domain-specific mode of examination selected by the protocol. The Transformative lens examines change, transition, integration, and resulting effects. Neither lens is itself a source of evidence, a substitute for a method, or permission to infer unsupported properties. The protocol must identify the specific lens or lenses and operational questions used; it must not assume every Alchemy is applicable to every subject.

### 9.3 Pass Qualification, Failure, and Evidence Rules

A Research pass receives credit only when its prescribed research activity has actually been performed and its required research record is complete enough to evaluate. A Simulation pass receives credit only when the prescribed scenario has actually been executed and its execution record is preserved. A single combined narrative cannot stand in for both records.

The following do **not** earn pass credit:

- Summaries of work not performed.
- Hypothetical, illustrative, imagined, or proposed results.
- A plan, protocol, template, checklist, or generated report without the corresponding execution.
- Repeated wording or copied records that do not represent distinct executions.
- A successful tool call or commit without evidence that the prescribed research or simulation was performed.
- A failed, blocked, incomplete, invalid, or non-reproducible execution.

Failed or blocked executions remain in the record as attempts. They do not count as completed passes. A corrective rerun must receive a new run identifier, preserve the earlier attempt, identify the defect and correction, and be assessed against the original acceptance criteria. A pass may be credited only after the required activity succeeds sufficiently to meet its defined criteria; failure must never be overwritten or relabeled as success.

Each Research pass must record at minimum: pass and run IDs; Manifestation progression point; Magnum Opus stage or stages addressed; question; method; sources and selection rationale; evidence; claims; findings; contradictions; uncertainty; limitations; analysis; conclusion; deviations; and reviewer outcome. It must identify applicable Zodiac or Disciple correspondence records where relevant, without treating proposed mappings as verified.

Each Simulation pass must record at minimum: pass and run IDs; Manifestation progression point; Magnum Opus stage or stages addressed; scenario; model and version; methodology; assumptions; inputs and data provenance; configuration and environment; expected outputs and criteria; actual outputs; logs; failures; deviations; sensitivity; uncertainty; limitations; interpretation; and verification outcome. It must identify applicable correspondence records where relevant.

Every pass must link to its Pre-Simulation and Post-Simulation Alchemy and Transformative Interlay records, or to the approved alternative-method records where simulation is inapplicable. Records must distinguish execution outcome, evidence status, review status, owner acceptance, programme credit, and implementation/publication authorization.

### 9.4 Single Research Report

Each research programme produces **one consolidated Research Report**. The report is the sole report deliverable for that research programme, regardless of the number of research questions, Magnum Opus stages, Manifestation progression points, Research passes, Simulation passes, interlays, or evidence records.

The single Research Report must consolidate, as applicable:

- Research identity, provenance, scope, questions, objectives, exclusions, assumptions, and protocol.
- Definitions and base-level category treatment.
- Methods, sources, source-selection rationale, and evidence provenance.
- Research and Simulation execution summaries with links to the underlying run records.
- Pre-Simulation and Post-Simulation Alchemy and Transformative Interlay findings, or approved alternative-method records.
- Findings, claims, analysis, contradictions, uncertainty, limitations, and unresolved questions.
- Magnum Opus stage outcomes and relevant Zodiac and Disciple correspondence findings, including unverified or unresolved status.
- Manifestation progression and pass-credit status, including failed or blocked attempts.
- Requirements, risks, safeguards, alternatives, and recommendations.
- What should be built, changed, maintained, deferred, rejected, retired, or left unbuilt, where applicable.
- Implementation considerations and verification criteria where a proposed build or change is justified.
- Review outcome, owner acceptance, programme completion status, and any separately required implementation or publication authorization.

The report must link to the underlying protocols, sources, evidence records, run bundles, interlays, correspondence records, requirements, decisions, and verification artifacts. It must not replace those records, create pass credit, or imply that a recommendation authorizes implementation, deployment, or publication.

The research programme must not create separate stage, progress, gap-analysis, build-decision, or implementation-plan reports. All reportable research findings and recommendations are consolidated into this one Research Report.

### 9.5 Simulation Coverage and Interpretation

Challenge coverage must be selected according to the subject, risks, and protocol. It should consider, where material:

- Baseline and null conditions.
- Positive and negative assertions.
- Boundary, failure, stress, adversarial, misuse, and recovery scenarios.
- Alternative architectures and explanations.
- Parameter, seed, environment, model, data, and dependency variation.
- Privacy, access, authority, identity, provenance, and cross-repository isolation.
- Performance, energy, cost, storage, network, tool-use, and latency measurement.
- Rollback, restoration, and historical-integrity tests.
- Cross-context and cross-domain transfer, including cases where transfer should fail.

Synthetic results must be labeled synthetic. A successful simulation supports only the tested model, assumptions, environment, and scope. Simulations do not prove real-world outcomes beyond their validated scope. Research evidence, simulation outputs, and interpretive interlay records must remain distinguishable and linked.


## 10. Run Bundle

Every substantive execution must produce a uniquely identified run bundle containing or securely referencing:

- Programme, protocol, stage, cycle, run, and version identifiers.
- Responsible operator and execution time.
- Inputs, sources, data versions, licenses, and permissions.
- Code, prompts, procedures, configurations, parameters, seeds, and dependencies.
- Tool, model, software, operating-system, hardware, and environment details.
- Logs, warnings, failures, deviations, and operator actions.
- Outputs, intermediate artifacts, analyses, and reports.
- Verification checks and observed outcomes.
- Manifest and checksums where technically applicable.
- Limitations, unresolved issues, and links to preceding or corrective runs.

- Separate Research-pass and Simulation-pass records, with Manifestation progression-point and Magnum Opus-stage identifiers, plus applicable Zodiac and Disciple correspondence-record references.
- Pre-Simulation Alchemy and Transformative Interlay record, including selected lens or lenses, model assumptions, transformations considered, expected effects, variables, constraints, and challenge conditions.
- Post-Simulation Alchemy and Transformative Interlay record, including comparison of expected and observed behavior, supported and unsupported transformations, anomalies, unintended effects, model disposition, and follow-up actions.
- Cumulative Manifestation ×12 review recorded within the single Research Report.
- Subject, Tablet, discipline, taxonomy-node, and typed-relationship identifiers, including source-context links and crosswalk provenance.
- The versioned Tablet-to-Category mapping records applicable to the run, identifying the relevant Tablet collection and placements, canonical subject IDs, applicable Base-level category IDs, relationship type, applicability status, rationale, provenance, and mapping version.
- Pass-credit decision, failed-attempt references, acceptance criteria, reviewer outcome, and distinct execution/evidence/review/acceptance/authorization statuses.

Credentials, secrets, restricted data, personal information, and private implementation material must not be placed in an unauthorized bundle or repository.

## 11. Verification Model

Verification depth must be planned according to consequence and uncertainty:

- **V0:** author or operator self-check.
- **V1:** additional team or peer review with dependencies disclosed.
- **V2:** independent review by a competent reviewer who did not author or execute the targeted work.
- **V3:** independent reproduction from preserved records.
- **V4:** external replication or validation using a separate team, environment, dataset, source corpus, or system where appropriate.

Verification must distinguish:

- Correct execution from correct interpretation.
- Reproducibility from external replication.
- Evidence integrity from validity.
- Method compliance from method adequacy.
- Test success from owner acceptance.
- Acceptance from implementation or release authorization.

High- or critical-consequence work requires independent, multidisciplinary review, explicit stop conditions, monitoring, containment, rollback, and accountable authorization before consequential use.

## 12. UNIVERSALIS-OS Research Workstreams

The research programme must maintain the following coordinated workstreams:

1. **Mission and System Boundary:** purpose, users, affected parties, non-goals, operating assumptions, and success criteria.
2. **Six-Repository Mapping and Master Private Source-Code Stewardship:** source-of-truth ownership, private-source classification, authorized access, derivation, synchronization, divergence, licensing, and release boundaries, applying Section 3.1.
3. **Architecture:** kernel or core services, service model, runtime, storage, configuration, device abstraction, processes, extensibility, and lifecycle.
4. **Interfaces and Integration:** APIs, protocols, schemas, compatibility, semantic translation, error handling, versioning, and failure isolation, including the UNIVERSALIS-OS–UNIVERSALIS-App edition boundary and the MOS–MApp Master-source lineage, service ownership, dependency direction, contract compatibility, data exchange, degraded operation, and independent operation and recovery.
5. **Identity and Authority:** identities, roles, delegation, authentication, authorization, consent, revocation, and least privilege.
6. **UNIVERSALIN and UNIVERSALIN Sentinel Roles:** role definitions, task boundaries, human oversight, memory boundaries, monitoring, correction, refusal, appeal, and accountability.
7. **Security:** threat model, secure design, dependency and supply-chain risk, secrets, isolation, auditability, incident response, and recovery.
8. **Privacy and Data Governance:** minimization, purpose limitation, access, retention, deletion, portability, provenance, and protected data handling.
9. **Safety and Reliability:** hazards, failure modes, resilience, availability, safe degradation, stop conditions, restoration, and residual risk.
10. **Human Factors and Accessibility:** usability, comprehension, agency, accessibility, error recovery, feedback, and affected-party participation.
11. **Performance and Resource Stewardship:** compute, energy, cost, storage, network, latency, throughput, utilization, embodied infrastructure impacts, and quality-preserving optimization.
12. **Portability and Platform Coverage:** desktop, mobile, server, cloud, edge, embedded, virtualized, containerized, and specialized environments where supported by evidence and scope.
13. **Testing and Verification:** test architecture, traceability, fixtures, environments, coverage, independence, evidence retention, and acceptance.
14. **Operations and Lifecycle:** deployment, observability, maintenance, updates, migration, compatibility, deprecation, retirement, and continuity.
15. **Licensing and Provenance:** rights, attribution, third-party terms, edition-specific licensing, provenance, and publication classification.

Each workstream must publish its questions, protocol, evidence, findings, requirements, risks, verification status, and unresolved issues through the common registries.

## 13. Research Report Standard

Every research programme must produce one consolidated Research Report in accordance with Section 9.4. The report must be complete enough for an independent reviewer to understand what was investigated, how it was investigated, what evidence was obtained, what conclusions are supported, what remains uncertain, and what decisions or next actions are recommended.

The Research Report must include:

- **Identity and provenance:** stable report ID, version, research programme ID, subject, authorship, dates, source Plan and protocol versions, and change history.
- **Purpose and scope:** research questions, objectives, boundaries, exclusions, assumptions, affected parties, and limitations.
- **Base-level category coverage:** relevant categories from Section 5.5.1, with definitions, applicability, relationships, and unresolved interpretations.
- **Methodology:** research methods, selection rationale, twelve Magnum Opus stage outcomes where applicable, Zodiac and Disciple correspondence assessments, Manifestation progression, and any approved alternative methods.
- **Evidence:** sources, source-selection rationale, provenance, claims, supporting and contradictory evidence, confidence or uncertainty, and evidence limitations.
- **Execution:** Research and Simulation pass references, run bundles, interlay records, failures, deviations, and verification outcomes.
- **Analysis and findings:** results, relationships, interpretations, contradictions, limitations, and unresolved questions.
- **Recommendations and decisions:** alternatives, risks, safeguards, residual risk, build/change/no-build/defer/reject/retire recommendations where applicable, and accountable decision authority.
- **Implementation considerations:** requirements, architecture implications, dependencies, verification criteria, and readiness gaps where a build or change is supported.
- **Review and status:** execution outcome, evidence status, review status, owner acceptance, programme credit, completion status, and implementation/publication authorization as separate fields.

The Research Report is the only report for the research programme. Supporting protocols, evidence records, run bundles, interlays, requirement records, decision records, and verification artifacts remain separate source records; they are not additional reports. The report itself does not authorize implementation, deployment, access changes, or publication.

## 14. Completion Criteria

The UNIVERSALIS-OS research programme may be submitted for completion review only when:

- Scope, questions, exclusions, protocol, and material amendments are recorded.
- The integrated architecture is addressed: all twelve Magnum Opus stages have explicit outcomes; the Zodiac and Disciple correspondence matrices are documented with source basis, rationale, alternatives, limitations, and verification status; and the five-point Manifestation progression is completed or its incomplete status is explicitly recorded.
- The fixed Manifestation progression has been completed: 31 credited Research passes and 31 credited Simulation passes, or the programme is explicitly recorded as incomplete, terminated, or operating under a separately authorized amended standard.
- The mandatory Pre-Simulation and Post-Simulation Alchemy and Transformative Interlays are recorded for every applicable cycle; interlays are not counted as passes.
- The cumulative review after Manifestation ×12 is recorded within the single Research Report.
- The one consolidated Research Report is present with required content, provenance, review, and decision status.
- Subject and taxonomy records use stable identities and typed relationships; exact label matches have not been treated as semantic identity without evidence and review.
- All twelve stages have explicit outcomes and gate decisions.
- Material evidence, contradictory evidence, claims, findings, requirements, and limitations are traceable.
- Cross-repository mappings identify all material derivations and boundaries in scope.
- Required simulations or equivalent challenges are completed, or their absence is justified.
- Required verification is completed, or the missing verification and resulting restrictions are explicit.
- The single Research Report includes the applicable findings, recommendations, and implementation considerations.
- Security, privacy, safety, rights, accessibility, licensing, and operational blockers are resolved or explicitly accepted within legitimate authority.
- Open risks and unresolved questions remain visible.
- Completion, owner acceptance, implementation authorization, publication authorization, and programme credit are recorded separately.

Available completion outcomes are:

- Complete.
- Complete with accepted limitations.
- Partially complete.
- Not complete.
- Withdrawn or terminated.

A completed programme may be reopened when new evidence, a failed replication, a vulnerability, an invalidated source, a changed context, a rights or licensing issue, an overlooked affected party, or a material implementation defect undermines its conclusions or permitted use.

## 15. Migration and Consolidation Recommendation

After this replacement plan is reviewed and accepted:

1. Freeze the previous research-plan baseline by commit and tag.
2. Inventory any still-valid records located in numbered 01, 02, 03, 04, or 05 work areas without using them as sources for this rewrite.
3. Classify each retained artifact as evidence, protocol, run bundle, report, decision, implementation artifact, duplicate, historical record, or obsolete material.
4. Migrate retained artifacts into the controlled registries and repository structure established under this plan, preserving Git history and provenance.
5. Verify that no requirement, evidence item, decision, private material, license notice, or unresolved blocker is lost.
6. Replace internal links that depend on the numbered work areas.
7. Delete the numbered 01, 02, 03, 04, and 05 work areas only through a separate reviewed pull request after migration verification and owner approval.

**Recommendation:** delete the numbered 01–05 work areas after verified migration because parallel structures would otherwise preserve duplicate standards, ambiguous authority, stale links, and competing definitions of completion. Deletion must be the final consolidation step, not the first.

## 16. Immediate Execution Sequence

1. Review and approve this replacement plan.
2. Establish the core registries and identifier conventions.
3. Create the six-repository mapping baseline.
4. Define the UNIVERSALIS-OS mission, system boundary, and non-goals.
5. Register the initial research questions and risks for all fifteen workstreams.
6. Approve protocols for the first mission, architecture, repository-boundary, security, and verification studies.
7. Run the initial research and challenge cycles.
8. Produce the single consolidated Research Report, including the supported recommendations and implementation considerations.
10. Begin implementation only after explicit authorization.
11. Verify implementation against requirements and preserved evidence.
12. Migrate retained historical material and then submit the separate deletion pull request for numbered 01–05 work areas.


## 17. Plan to Complete the Research Plan and Implement the Research Framework

The Research Plan must contain and govern a complete, traceable programme for completing the Research Plan itself and implementing the C2O–UNIVERSALIS Research Framework. This is an explicit programme objective, not an assumed consequence of publishing this document. The Research Plan remains the governing research standard; the Framework operationalizes it through controlled records, workflows, repository-specific plans, execution artifacts, verification, and reporting. The Framework must not create a competing or contradictory research standard.

### 17.1 Completion and Implementation Phases

The programme must proceed through the following ordered phases. A phase may be reopened when verification identifies a material defect or new dependency.

1. **Baseline and authority confirmation:** identify the authoritative Research Plan and Framework sources, versions, owners, approval boundaries, six repositories, existing artifacts, and applicable private/public classifications.
2. **Completeness and gap audit:** compare the current Research Plan and proposed Framework against all required purposes, scope, principles, contexts, methods, stages, governance, registries, schemas, workflows, verification, reporting, security, privacy, safety, and repository requirements. Record every gap, contradiction, duplication, ambiguity, and dependency.
3. **Research Plan completion:** resolve and document the gaps requiring normative research-plan content; define terms, requirements, roles, decision gates, completion criteria, and change control. Preserve proposed items as proposed until reviewed and accepted.
4. **Framework architecture completion:** specify the Framework's components, lifecycle, governance, authority boundaries, repository-plan relationship, records, workflows, status model, traceability model, and synchronization/versioning rules.
5. **Six-repository plan mapping:** define how the common Research Plan and Framework apply to C2O-UNIVERSALIS-MOS, C2O-UNIVERSALIS-MApp, C2O-OS, C2O-App, UNIVERSALIS-OS, and UNIVERSALIS-App. Each repository plan may specialize its scope but must not redefine the universal methodology or exceed its authority.
6. **Registry and schema specification:** define stable identifiers, required fields, controlled vocabularies, relationships, validation rules, provenance, versioning, machine-readable schemas, and human-readable views for all required registers and records.
7. **Workflow and control specification:** define intake, protocol review, research execution, simulation, evidence registration, challenge, verification, reporting, decision, acceptance, implementation handoff, publication, change, archival, and reopening workflows. Keep execution outcome, evidence status, review status, owner acceptance, programme credit, and action/publication authorization distinct.
8. **Implementation design and traceability:** produce the implementation architecture and a Plan-to-Framework-to-Repository-to-Tool traceability matrix. Every implemented component must trace to an accepted requirement, design decision, implementation record, and verification test.
9. **Controlled pilot:** apply the Framework to a bounded UNIVERSALIS-OS research project and test the complete lifecycle, records, permissions, private/public boundaries, evidence lineage, failure handling, and reporting. The pilot must also test the three-collection Tablet architecture and preservation of both source collections; at least one subject with multiple Tablet placements; an exact-label overlap that is not treated as semantic equivalence; Tablet-to-Category mappings for the twelve Base-level categories in Section 5.5.1; the paired C2O and UNIVERSALIS Operating Intelligence roles in the combined architecture and their respective OS/App edition assignments; form-specific applicability for at least one UNIVERSALIN or UNIVERSALIN Sentinel form; stable identity, source provenance, and typed crosswalk behavior; the twelve Magnum Opus stages; both twelve-part correspondence matrices and their unresolved-status handling; the five-point Manifestation progression and pass-credit rules; mandatory pre- and post-simulation interlays; and production of one consolidated Research Report. A pilot may use a clearly labeled reduced or dry-run exercise to test workflow mechanics, but it must not claim completion of the 31 + 31 schedule or programme credit unless every prescribed pass is actually executed and evidenced.
10. **Independent verification and remediation:** review and reproduce the pilot where appropriate; record defects, gaps, deviations, security/privacy/safety findings, and remediation; rerun affected tests.
11. **Six-repository integration and rollout:** integrate the verified Framework and repository-specific plans through reviewed changes, preserving repository history, edition boundaries, and explicit owner approvals. Synchronize normative content where required and record any justified repository-specific variation.
12. **Completion review and acceptance:** record the completion review within the single Research Report, including the implementation inventory, verification evidence, unresolved-work register, residual-risk assessment, and separate decisions for plan acceptance, framework acceptance, implementation acceptance, and any release or publication authorization.

### 17.2 Required Programme Artifacts

The completion and implementation programme must produce, at minimum:

- Research Plan completeness and gap-audit findings, included in the single Research Report.
- Integrated architecture specification and mapping register for the twelve Magnum Opus stages, twelve Zodiac signs, twelve Disciple positions, and five-point Manifestation progression.
- Fixed Manifestation pass schedule register documenting 31 Research and 31 Simulation passes, pass-credit rules, and failure handling.
- Pre-Simulation and Post-Simulation Alchemy and Transformative Interlay specifications, templates, and executed records.
- Single Research Report specification, template, and report register for each research programme.
- Subject, Tablet, discipline, subdiscipline, and concept identity schema.
- Typed taxonomy relationship and crosswalk schema, including exact-label-match safeguards.
- Tablet collection register and source-preservation specification for the two source collections and the Unified Tablets integration layer.
- Tablet-to-Category mapping schema and register covering the twelve Base-level research categories in Section 5.5.1, including applicability, provenance, lifecycle status, and change history.
- Operating Intelligence and edition-assignment register documenting C2O and UNIVERSALIS as the two distinct, coordinated Operating Intelligences of the C2O–UNIVERSALIS architecture and their respective OS and App edition assignments.
- Machine-readable validation rules for pass records, interlays, single-report references, subject relationships, Tablet placements, and Tablet-to-Category mappings.
- Framework architecture and component specification.
- Framework governance and authority model.
- Six-repository applicability and mapping matrix.
- Repository-specific Research Plan inventory and reconciliation.
- Research lifecycle and workflow specifications.
- Registry catalogue and machine-readable schema set.
- Identifier, status, provenance, and versioning specifications.
- Plan-to-Framework-to-Repository-to-Tool traceability matrix.
- Security, privacy, safety, and private/public boundary assessment.
- Pilot protocol, run bundles, results, defects, and verification records.
- Migration and synchronization plan where applicable.
- Implementation and rollout plan.
- Final completion, acceptance, and outstanding-work findings, included in the single Research Report.

### 17.3 Completion Gates

No phase is complete solely because its documents have been drafted. Each phase requires defined exit criteria, evidence, review, and a recorded decision. Framework implementation is complete only when the required components and workflows are implemented, their requirements are traceable, verification is passed at the required level, defects and limitations are disclosed, and the appropriate owners have recorded acceptance. Acceptance does not itself authorize publication, deployment, or access changes.

The programme must retain a live outstanding-work register throughout execution. Unresolved items must have an identifier, description, impact, owner, dependency, status, next action, and closure evidence. No item may be silently dropped or marked complete through summary language.

### 17.4 Relationship to the Immediate Execution Sequence

The Immediate Execution Sequence in Section 16 must be carried out under this programme. The first execution activity is the baseline and completeness audit, followed by Research Plan completion and Framework specification. Registry construction, repository integration, pilots, and implementation must follow their respective phase gates. This ordering prevents tools or repository structures from being built against an incomplete or unapproved specification.
