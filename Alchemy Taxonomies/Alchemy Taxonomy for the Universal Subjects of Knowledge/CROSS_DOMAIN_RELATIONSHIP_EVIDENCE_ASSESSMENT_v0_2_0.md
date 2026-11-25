# Cross-Domain Relationship Evidence Assessment

**Version:** 0.2.0  
**Assessment batch:** 1 and 2  
**Canonical taxonomy baseline:** v1.13.8  
**Status:** Evidence assessed; owner review pending

## 1. Scope and safeguards

The last verified canonical taxonomy contains 18 RD-P proposals, 252 hierarchy edges, and 34,446 unique subject pairs with no direct relationship stated in the source taxonomy. The previously discussed 32 extra edges were not present in the repository read-back and are excluded from this assessment and all counts.

This report does not update the canonical taxonomy. It records evidence and recommendations for controlled review. Shared identity, relatedness, dependency, enablement, hierarchy, evidence, owner acceptance, implementation, and verification remain separate concepts.

Evidence strength: **High** means direct authoritative or scholarly evidence; **Moderate** means a credible but broader/less precise interface; **Insufficient** means that co-occurrence or contextual proximity does not establish a pairwise relationship.

## 2. Assessment of existing proposals RD-001–RD-006

| ID | Assessment and scope boundary | Evidence strength | Subtype / direction assessment | Disposition |
|---|---|---|---|---|
| RD-001 (USA-FS-014 Systems Theory ↔ USA-MKS-009 Systems Thinking) | Scholarly sources support a conceptual and methodological association. Systems thinking has multiple meanings; one established usage includes systems theories, methods, approaches, and tools. This supports an interface, not identity or a universal definition. [S26, S39] | Moderate–high for association; not enough for one universal boundary | Refine to **conceptual/methodological interface**. No general direction established; this is not a dependency or universal theory-to-practice edge. | Retain as RD-P; refine subtype; owner review pending. |
| RD-002 (USA-FS-019 Complexity Theory ↔ USA-MKS-010 Complexity Science) | Scholarly sources describe overlapping terminology and characterize complexity science as a collection of models and theories rather than one unified theory. They support a broad conceptual neighborhood, not a settled scope boundary. [S27, S28] | High for broad relatedness; low for a stable distinction | **Subtype unresolved.** Do not invent a sharp boundary or containment relation without owner-supplied definitions. No direction justified. | Defer subtype acceptance; preserve distinct IDs and source-stated association. |
| RD-003 (USA-SP-005 Intelligence Analysis ↔ USA-MKS-012 Intelligence Studies) | Sources distinguish Intelligence Studies as a field of inquiry from Intelligence Analysis as analysis performed by intelligence organizations. [S29, S30, S31] | High for the field/practice distinction | Refine to **field-of-study / analytic-practice relationship**. A one-way study relation is supportable: Intelligence Studies examines Intelligence Analysis. No operational dependency is implied. | Retain as RD-P; refine subtype and direction note. |
| RD-004 (USA-TI-003 Logistics ↔ USA-BES-010 Supply Chain Management) | CSCMP defines **Logistics Management** as part of Supply Chain Management (SCM), which also covers sourcing, procurement, conversion, and channel coordination. The canonical taxonomy subject is **Logistics**, not Logistics Management. The source directly supports the part-of relation for logistics-management activities, but does not by itself establish that the entire canonical Logistics subject is wholly contained within SCM. [S32] | High for the Logistics Management function; qualified for the broader canonical Logistics subject | Refine to **functional interface; bounded part-of relation**. Record that Logistics Management activities form part of SCM; do not generalize this into an unqualified part–whole claim about the broader canonical Logistics subject without a source definition establishing equivalence. No dependency edge or new hierarchy placement. | Retain as RD-P; correct subtype and scope; owner review pending. |
| RD-005 (USA-TI-005 Urban Planning ↔ USA-HDC-006 Urban Studies) | Sources characterize Urban Studies as interdisciplinary and describe Urban Planning as a distinct field concerned with planning and the built environment. Together they support an interface, not identity or containment. [S33, S34, S35] | Moderate–high | Refine to **interdisciplinary field / planning discipline-and-practice interface**. No strict one-way dependency or containment. | Retain as RD-P; refine boundary. |
| RD-006 (USA-TI-006 Infrastructure Engineering ↔ USA-ET-004 Civil Engineering) | University programme sources show Infrastructure Engineering addressing structural and transportation systems, resilient infrastructure, and built-environment assets; Civil Engineering sources describe the design, provision, upgrading, and management of infrastructure. Institutional programme placement does not establish universal containment. [S36, S37, S38] | High for technical overlap; moderate for universal boundary | Refine to **technical-scope overlap / infrastructure-specialization interface**. Institutional programme placement does not prove universal containment. No universal direction. | Retain as RD-P; refine subtype. |

All six remain proposed. None is owner-accepted by this report.

## 3. Initial subject-pair screen: Life Sciences ↔ Health Sciences

The Life Sciences inventory has 18 subjects and the Health Sciences inventory has 15, producing 270 possible cross-domain subject pairs. This pilot screened eight prioritised pairs, not the entire block.

| Screen ID | Canonical subject pair | Finding | Evidence strength | Recommended disposition |
|---|---|---|---|---|
| LSHS-001 | USA-HS-002 Medicine ↔ USA-LS-014 Physiology | Medical organ-system curricula integrate physiology with clinical teaching. [S20] | High | Candidate RD-P: clinical/foundational-science interface; no containment or dependency. |
| LSHS-002 | USA-HS-002 Medicine ↔ USA-LS-015 Anatomy | Medical curricula integrate anatomy into organ-system teaching and clinical preparation. [S20] | High | Candidate RD-P: clinical/foundational-science interface; no hierarchy edge. |
| LSHS-003 | USA-HS-007 Epidemiology ↔ USA-LS-006 Microbiology | Infectious-disease epidemiology connects population distribution and transmission with etiologic agents, infection, host factors, and microbiological evidence. [S21, S22] | High | Candidate RD-P: population/pathogen interface; neither field contains the other. |
| LSHS-004 | USA-HS-007 Epidemiology ↔ USA-LS-017 Virology | Viral-disease epidemiology combines virus characteristics, host factors, transmission dynamics, and disease distribution in populations. [S22] | High | Candidate RD-P: viral-pathogen/population interface. |
| LSHS-005 | USA-HS-012 Mental Health ↔ USA-LS-013 Neuroscience | NIMH research studies how neural systems and biological processes contribute to psychopathology; this is a bounded neurobiological interface and does not define the whole of Mental Health. [S23] | High for the bounded research interface | Candidate RD-P: neurobiological research interface; neuroscience does not define the whole of Mental Health. |
| LSHS-006 | USA-HS-008 Nutrition ↔ USA-LS-014 Physiology | Nutritional physiology studies nutrient use, digestion, homeostasis, metabolic regulation, and physiological requirements. [S24] | High | Candidate RD-P: nutritional/physiological interface. |
| LSHS-007 | USA-HS-006 Public Health ↔ USA-LS-005 Ecology | WHO One Health describes interdependence among human, animal, plant, and ecosystem health, including environmental conditions influencing disease emergence and spread. This supports a bounded interface, not identity or containment. [S25] | High for the stated One Health/ecosystem-health interface | Candidate RD-P: ecosystem-health/population-health interface, with scope restricted to ecological determinants and interconnected health. |
| LSHS-008 | USA-HS-005 Pharmacology ↔ USA-LS-010 Molecular Biology | Both are included in an integrated medical-science curriculum, but co-inclusion alone does not prove a specific direct relationship between their canonical subject scopes. [S20] | Insufficient for a pair-specific edge | Do not promote in this pass. Defer pending direct evidence about molecular targets or pharmacological mechanisms. |

**Pilot accounting:** 270 possible pairs = 7 candidate RD-P relationships + 1 screened but not promoted + 262 not yet individually assessed. The seven candidates are recommendations for a future controlled taxonomy update; they are not canonical RD-P rows in v1.13.8.

## 4. Evidence register

| Source ID | Source | URL |
|---|---|---|
| S20 | Tufts University School of Medicine — MD Curriculum | https://medicine.tufts.edu/academics/medicine/curriculum |
| S21 | NCBI Bookshelf — Medical Microbiology, 4th ed., Chapter 9: Epidemiology (General Concepts) | https://www.ncbi.nlm.nih.gov/books/NBK7993/ |
| S22 | Epidemiology of Viral Infections | https://pmc.ncbi.nlm.nih.gov/articles/PMC7150207/ |
| S23 | National Institute of Mental Health — Central-Peripheral Interactions Pathophysiology Program | https://www.nimh.nih.gov/about/organization/dtr/adult-pathophysiology-and-biological-interventions-development-branch/central-peripheral-interactions-pathophysiology-program |
| S24 | University of Bologna — Nutritional Physiology, 2026/2027 | https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2026/494585 |
| S25 | World Health Organization — One Health, 8 May 2026 | https://www.who.int/news-room/fact-sheets/detail/one-health |
| S26 | Gates et al. — Introducing systems- and complexity-informed evaluation | https://doi.org/10.1002/ev.20466 |
| S27 | Oxford Bibliographies — Complexity | https://academic.oup.com/reference/62356/reference-article-abstract/554489967?login=false |
| S28 | Ladyman & Wiesner — What Is a Complex System? | https://academic.oup.com/yale-scholarship-online/book/37751/chapter-abstract/332121776 |
| S29 | What Is Intelligence Studies? | https://www.tandfonline.com/doi/full/10.1080/23800992.2016.1150679 |
| S30 | Oxford Bibliographies — Intelligence | https://academic.oup.com/reference/62360/reference-article-abstract/554546709?login=false |
| S31 | Oxford Research Encyclopedia — Intelligence Analysis: Once Again | https://academic.oup.com/edited-volume/61835/chapter-abstract/546987914 |
| S32 | Council of Supply Chain Management Professionals — FAQ / definitions | https://cscmp.org/CSCMP/CSCMP/Develop/Starting_Your_Career/Frequently_Asked_Questions.aspx |
| S33 | Stanford University — What Is Urban Studies? | https://urbanstudies.stanford.edu/academics/what-urban-studies |
| S34 | MIT Course Catalog — Department of Urban Studies and Planning | https://catalog.mit.edu/schools/architecture-planning/urban-studies-planning/ |
| S35 | Oxford Bibliographies — Urban Planning | https://academic.oup.com/reference/62419/reference-article-abstract/573026018 |
| S36 | University of Iowa — Infrastructure Engineering | https://engineering.uiowa.edu/cee/prospective-students/graduate-program/infrastructure-engineering |
| S37 | University of Melbourne — Department of Infrastructure Engineering | https://infrastructure.eng.unimelb.edu.au/study/undergraduate |
| S38 | Penn State — Civil Systems Engineering | https://www.engr.psu.edu/ce/area_civil_systems.html |
| S39 | Understanding Systems Science: A Visual and Integrative Approach | https://onlinelibrary.wiley.com/doi/full/10.1002/sres.2215 |

## 5. Batch 1 status retained from version 0.1.0

Batch 1 assessed RD-001 through RD-006 and screened eight prioritised Life Sciences ↔ Health Sciences pairs. Its original findings, evidence register, and accounting are retained above without retroactive changes. The planned next assessment of RD-007 through RD-012 is completed in Batch 2 below.

### 5.1 Substantive audit record carried forward — assessment v0.1.0

**Audit date:** 2026-11-24  
**Audit scope:** taxonomy identity, relationship interpretation, evidence traceability, and pilot accounting  
**Audit status:** first-pass substantive review completed; source-quality review and owner review remain pending

#### 5.1.1 Taxonomy identity and relationship traceability

The six existing proposal pairs were reconciled to their canonical subject-Alchemy identifiers in taxonomy v1.13.8: RD-001 USA-FS-014 ↔ USA-MKS-009; RD-002 USA-FS-019 ↔ USA-MKS-010; RD-003 USA-SP-005 ↔ USA-MKS-012; RD-004 USA-TI-003 ↔ USA-BES-010; RD-005 USA-TI-005 ↔ USA-HDC-006; and RD-006 USA-TI-006 ↔ USA-ET-004. The seven promoted Life Sciences ↔ Health Sciences candidates and the one screened-but-not-promoted pair were likewise reconciled to their canonical identifiers in the assessment table. No subject identity or hierarchy placement is changed by this assessment.

#### 5.1.2 Material correction — RD-004 scope overstatement

The prior assessment described RD-004 as an unqualified part–whole relationship from Logistics to Supply Chain Management. The cited CSCMP definition specifically states that **Logistics Management** is part of Supply Chain Management. The canonical taxonomy subject, however, is **Logistics**, not Logistics Management, and the taxonomy does not supply a definition establishing that the two scopes are identical. The prior wording therefore generalized evidence about a functional management area to the broader canonical subject. The corrected assessment confines the supported part-of statement to Logistics Management activities and retains only a qualified functional interface for the broader Logistics subject. Owner review remains required before accepting a more precise subtype.

#### 5.1.3 Evidence traceability correction

The initial assessment listed sources in a register but did not identify the supporting source IDs alongside each relationship finding. Source IDs have now been added to the corresponding RD and LSHS rows, and S21's bibliographic description has been made more precise. This improves claim-to-source traceability; it does not, by itself, establish that every cited source is sufficient for every claim. Source quality, exact support, publication currency, and any access limitations remain subject to the continuing source-level review.

#### 5.1.4 Pilot accounting and interpretation

The 18 × 15 calculation is a screening universe of 270 possible cross-domain comparisons, not 270 proven relationships. The eight listed pairs are a prioritised sample: seven are candidate recommendations and one is not promoted. The remaining 262 pairs are unassessed, not negative. The seven candidates are not canonical RD-P rows and must not be counted as additions to the 18 proposals in taxonomy v1.13.8. No owner acceptance, taxonomy amendment, implementation, or verification is claimed.

#### 5.1.5 Outstanding review items

- Independently validate the full text and provenance of each source cited in S20–S39; inaccessible abstracts or partial records must be recorded as limitations rather than treated as full-text verification.
- Confirm the source-candidate records RD-CAND-001–RD-CAND-006 and the historical provenance of the excluded 32-edge discussion.
- Obtain owner review of RD-001–RD-006 and the seven LSHS candidate recommendations.
- Continue with the next assessment only after this assessment's corrections are re-read against the canonical taxonomy and the PR diff.

**Disposition:** RD-004's prior unqualified part–whole wording is corrected. The other six proposal interpretations and the seven candidate recommendations remain provisional, evidence-bounded findings. This assessment is not marked fully verified.


## 6. Assessment of existing proposals RD-007–RD-012

The six records below are already present in the canonical v1.13.8 proposal register. This assessment refines the evidentiary rationale, scope boundary, subtype, and direction note; it does not create six new relationship edges.

| ID | Canonical subject pair | Assessment and scope boundary | Evidence strength | Subtype / direction assessment | Disposition |
|---|---|---|---|---|---|
| RD-007 | USA-TI-001 Transportation and Infrastructure ↔ USA-ET-006 Aerospace Engineering | The strongest direct interface is aeronautical transportation and its supporting infrastructure. Aerospace-engineering teaching material treats airports as fundamental infrastructure for intermodal transportation and covers airport planning, configuration, and operations. This supports an interface involving aerospace transport systems and transport infrastructure, not a claim that all Aerospace Engineering is a branch of Transportation and Infrastructure or that all transport infrastructure is aerospace-related. [S40, S41] | High for the bounded air-transport/infrastructure interface | Refine to **transport-system infrastructure / aerospace-engineering application interface**. No single universal direction: aerospace transport design and operations interact with infrastructure planning, design, and operation. A specific project may have directional requirements, but this proposal does not establish a general dependency or containment edge. | Retain as RD-P; refine scope and subtype; owner review pending. |
| RD-008 | USA-HDC-001 Human Development and Civilization ↔ USA-SS-012 Cultural Studies | Cultural Studies examines culture and society, including how identity categories, language, institutions, and social relations are organized. Scholarly work on social change, culture, and human development provides a direct research bridge: cultural context and change are relevant to the study of human development. The relationship is analytical and interpretive, not a claim that Cultural Studies defines all human development or civilization. [S42, S43] | High for the bounded analytical interface | Refine to **cultural-analysis contribution**. Direction is supportable only as a knowledge contribution when Cultural Studies concepts and methods are used in HDC inquiry: Cultural Studies → selected HDC analyses. This is not a dependency or hierarchy assignment. | Retain as RD-P; refine contribution and boundary; owner review pending. |
| RD-009 | USA-HDC-001 Human Development and Civilization ↔ USA-SS-009 Demography | Demography contributes analysis of population size, growth, mortality, fertility, age structure, and spatial distribution. UN DESA directly connects demographic processes and population trends with social, economic, and environmental dimensions of development. The relationship supports demographic evidence as one analytical input to human-development and civilization studies; it does not reduce either field to population statistics. [S44] | High | Refine to **demographic-evidence / population-dynamics contribution**. Direction is limited to Demography → HDC analyses that use population data and demographic explanation. No dependency, containment, or hierarchy change is established. | Retain as RD-P; refine contribution and boundary; owner review pending. |
| RD-010 | USA-HDC-001 Human Development and Civilization ↔ USA-SS-003 Sociology | Sociology systematically studies groups, social interaction, societies, culture, and patterns at micro and macro levels. These are directly relevant analytical dimensions for examining human development and civilization, especially social institutions, organization, inequality, collective behaviour, and social change. The connection is not an assertion that Sociology is equivalent to, or wholly contained in, the HDC domain. [S45] | High | Refine to **social-structure and social-process analytical contribution**. Direction is limited to Sociology → HDC inquiry when sociological concepts, methods, or findings are applied. This is a contribution relation, not an operational dependency. | Retain as RD-P; refine contribution and boundary; owner review pending. |
| RD-011 | USA-HDC-001 Human Development and Civilization ↔ USA-SS-008 Human Geography | Human Geography studies relationships among people, places, and environments, including the spatial organization of human activity and the distribution of social and cultural systems. These spatial and place-based analyses contribute to understanding settlement, migration, urbanization, cultural landscapes, and civilizational change. The relation is bounded to human-spatial analysis; it does not imply that all HDC inquiry is geographical. [S46] | High | Refine to **human-spatial / place-and-population analytical contribution**. Direction is limited to Human Geography → HDC inquiry when spatial and place-based analysis is used. No dependency, containment, or new hierarchy edge is justified. | Retain as RD-P; refine contribution and boundary; owner review pending. |
| RD-012 | USA-ESP-001 Earth, Space, and Planetary Sciences ↔ USA-PS-016 Astronomy | Astronomy studies matter and phenomena in outer space, including the positions, distribution, motion, composition, energy, and evolution of celestial bodies. NASA identifies astronomy and astrophysics as foundational to understanding the universe beyond the solar system and documents astronomy as one of the disciplines intersecting planetary science. This is a strong subject-matter intersection within the wider Earth, Space, and Planetary Sciences scope. It does not make Astronomy equivalent to that broader domain or imply that Earth science is a subset of Astronomy. [S47, S48] | High for the space-science intersection | Refine to **astronomical-science / broader space-science scope intersection**. A limited knowledge contribution can be expressed as Astronomy → relevant ESP investigations of celestial bodies and space. No whole-domain containment, dependency, or identity merger is established. | Retain as RD-P; refine intersection and boundary; owner review pending. |

### 6.1 Batch 2 interpretation and controls

1. All six proposals have subject-pair-level support for the bounded relation stated above.
2. RD-007 is an engineering/application interface centred on aerospace transportation infrastructure; it must not be generalized to all aerospace engineering.
3. RD-008 through RD-011 are analytical contributions into selected Human Development and Civilization inquiries. Their arrows describe the direction of a possible knowledge contribution, not a prerequisite, dependency, or authority relationship.
4. RD-012 is a disciplinary scope intersection. Astronomy contributes to parts of the broader space-science inquiry, but it does not exhaust the Earth, Space, and Planetary Sciences domain.
5. No proposal creates a shared identity, parent-child hierarchy, implementation requirement, or service dependency.
6. The canonical IDs, subject names, domain assignments, and taxonomy hierarchy remain unchanged.
7. Each record remains RD-P and pending owner review. Evidence-based refinement is not owner acceptance.


### 6.2 Batch 2 source-to-claim audit note

The source identifiers are attached to the individual Batch 2 findings rather than left only in the evidence register. The accessible source material was checked against the bounded claims as follows:

- RD-007 [S40, S41]: supports the airport/air-transport infrastructure interface and the presence of infrastructure within aerospace activity; it does not support whole-domain containment.
- RD-008 [S42, S43]: supports Cultural Studies as an interdisciplinary study of culture and society and a research bridge between cultural/social change and human development.
- RD-009 [S44]: supports demographic processes and population trends as evidence relevant to social, economic, and environmental development.
- RD-010 [S45]: supports sociology's study of groups, social interaction, societies, culture, and social structure as analytical inputs to selected HDC inquiries.
- RD-011 [S46]: supports the people-place-environment and spatial-analysis contribution of Human Geography to selected HDC inquiries.
- RD-012 [S47, S48]: supports the astronomy/space-science intersection and the bounded subject-matter scope of Astronomy.

This is a first-pass source-to-claim check of the accessible source content, not a full independent bibliographic/provenance audit. Source currency, source-version capture, complete-text access where applicable, and owner review remain open. Evidence strength applies only to the bounded interface stated in each row; it does not establish identity, universal direction, hierarchy, dependency, or owner acceptance.

## 7. Additional evidence sources for Batch 2

| Source ID | Source | URL |
|---|---|---|
| S40 | Engineering LibreTexts — Fundamentals of Aerospace Engineering, Chapter 9: Airports (Manuel Soler Arnedo, Universidad Carlos III de Madrid) | https://eng.libretexts.org/Bookshelves/Aerospace_Engineering/Fundamentals_of_Aerospace_Engineering_(Arnedo)/09:_Airports |
| S41 | Engineering LibreTexts — Fundamentals of Aerospace Engineering, Section 1.2: Aerospace Activity | https://eng.libretexts.org/Bookshelves/Aerospace_Engineering/Fundamentals_of_Aerospace_Engineering_(Arnedo)/01:_The_Scope/1.02:_Aerospace_activity |
| S42 | University of California, Davis — 2026–2027 General Catalog, Cultural Studies M.A. | https://catalog.ucdavis.edu/departments-programs-degrees/cultural-studies/cultural-studies-ma/ |
| S43 | Greenfield — Studying social change, culture, and human development: A theoretical framework and methodological guidelines, Developmental Review 50 (2018), 16–30 | https://doi.org/10.1016/j.dr.2018.05.003 |
| S44 | United Nations Department of Economic and Social Affairs, Population Division — Global Population Growth and Sustainable Development (2022) | https://desapublications.un.org/publications/global-population-growth-and-sustainable-development |
| S45 | OpenStax — Introduction to Sociology 3e, Section 1.1: What Is Sociology? | https://openstax.org/books/introduction-sociology-3e/pages/1-1-what-is-sociology |
| S46 | Dartmouth College Library — Research Guide: Human Geography, Defining Human Geography | https://researchguides.dartmouth.edu/human_geography/main |
| S47 | NASA Ames — Core Area of Expertise: Space and Earth Science | https://www.nasa.gov/ames/core-area-of-expertise-space-and-earth-science/ |
| S48 | NASA Science — Universe Glossary, Astronomy entry | https://science.nasa.gov/universe/glossary/ |

## 8. Cumulative status and next work

| Measure | Status at version 0.2.0 |
|---|---:|
| Canonical taxonomy baseline | v1.13.8 |
| Existing canonical RD-P proposals | 18 |
| Existing proposals assessed in Batch 1 (RD-001–RD-006) | 6 |
| Existing proposals assessed in Batch 2 (RD-007–RD-012) | 6 |
| Existing proposals assessed cumulatively | 12 of 18 |
| Existing proposals still unassessed (RD-013–RD-018) | 6 |
| Owner-accepted relationships | 0 |
| Canonical taxonomy RD-P count | 18 — unchanged |
| Established hierarchy edges (HI) | 252 — unchanged |
| Pairs with no direct relationship stated in source taxonomy (NS) | 34,446 — unchanged |
| Life Sciences ↔ Health Sciences possible pairs | 270 |
| Prioritised pairs screened in that block | 8 |
| Candidate RD-P recommendations from that pilot | 7 |
| Screened without promotion | 1 |
| Still unassessed in that block | 262 |

The 34,446 NS pairs remain source-unlinked, not confirmed unrelated. The seven Life Sciences ↔ Health Sciences recommendations remain candidates for controlled registration and are not included in the canonical 18 RD-P rows. Likewise, the six assessments in Batch 2 refine existing proposals; they do not add six edges to the canonical register.

**Next work:** continue the Life Sciences ↔ Health Sciences block in smaller, topic-focused groups as planned. RD-013 through RD-018 (including Cosmology and Planetary Science proposals) remain a separate unassessed portion of the existing proposal queue and must be assessed before all 18 proposals can be described as evidence-assessed.

No canonical taxonomy amendment, owner acceptance, hierarchy reassignment, dependency, enablement, implementation, or verification is claimed by this report.


## Taxonomy alignment correction — 2026-11-24

**Canonical taxonomy baseline:** v1.13.8  
**Canonical taxonomy Git blob SHA:** `3e7c570943b4e65307f01618ac81b031051ad1a9`

This correction supersedes the former v1.13.1 baseline reference. The v1.13.8 change record confirms that Universal Subject hierarchies, canonical subject-Alchemy identities, 22-context mappings, relationship-matrix values, shared-identity relationships, cross-domain proposals, and cumulative totals were preserved. Life Sciences remains 18 subject Alchemies and Health Sciences remains 15, with their canonical identifiers unchanged; the 270-pair screening universe is unchanged. This report assesses relationships between subject Alchemies; it does not assess or complete the taxonomy's 22-context contextual expressions. Historical findings, evidence assessments, source records, and dispositions are retained. No owner acceptance or canonical taxonomy amendment is implied.
