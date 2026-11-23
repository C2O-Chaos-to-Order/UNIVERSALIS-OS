# Cross-Domain Relationship Evidence Assessment

**Version:** 0.1.0  
**Assessment batch:** 1  
**Canonical taxonomy baseline:** v1.13.1  
**Status:** Evidence assessed; owner review pending

## 1. Scope and safeguards

The last verified canonical taxonomy contains 18 RD-P proposals, 252 hierarchy edges, and 34,446 unique subject pairs with no direct relationship stated in the source taxonomy. The previously discussed 32 extra edges were not present in the repository read-back and are excluded from this assessment and all counts.

This report does not update the canonical taxonomy. It records evidence and recommendations for controlled review. Shared identity, relatedness, dependency, enablement, hierarchy, evidence, owner acceptance, implementation, and verification remain separate concepts.

Evidence strength: **High** means direct authoritative or scholarly evidence; **Moderate** means a credible but broader/less precise interface; **Insufficient** means that co-occurrence or contextual proximity does not establish a pairwise relationship.

## 2. Assessment of existing proposals RD-001–RD-006

| ID | Assessment and scope boundary | Evidence strength | Subtype / direction assessment | Disposition |
|---|---|---|---|---|
| RD-001 Systems Theory ↔ Systems Thinking | Scholarly sources support a conceptual and methodological association. Systems thinking has multiple meanings and can include the use of systems theories, methods, approaches, and tools. | Moderate–high for association; not enough for one universal boundary | Refine to **conceptual/methodological interface**. No general direction established; this is not a dependency or universal theory-to-practice edge. | Retain as RD-P; refine subtype; owner review pending. |
| RD-002 Complexity Theory ↔ Complexity Science | Sources describe complexity theory, complexity sciences, and complex systems as overlapping labels with varying meanings. Complexity science is often presented as a collection of models and theories rather than one unified theory. | High for broad relatedness; low for a stable distinction | **Subtype unresolved.** Do not invent a sharp boundary or containment relation without owner-supplied definitions. No direction justified. | Defer subtype acceptance; preserve distinct IDs and source-stated association. |
| RD-003 Intelligence Analysis ↔ Intelligence Studies | Intelligence Studies is described as a broad academic field covering history, methods, organization, function, governance, and policy. Intelligence Analysis is analytic work carried out by intelligence organizations. | High | Refine to **field-of-study / analytic-practice relationship**. A one-way study relation is supportable: Intelligence Studies examines Intelligence Analysis. No operational dependency is implied. | Retain as RD-P; refine subtype and direction note. |
| RD-004 Logistics ↔ Supply Chain Management | CSCMP explicitly defines Logistics Management as part of Supply Chain Management, while SCM also covers sourcing, conversion, channel coordination, and other business functions. | High; direct professional-standard definition | Refine to **functional part–whole**. Direction: Logistics Management is part of Supply Chain Management. This is not a dependency edge or a new hierarchy placement. | Retain as RD-P; record part-of direction. |
| RD-005 Urban Planning ↔ Urban Studies | Urban Studies is interdisciplinary study of settlements and urban problems. Urban Planning is a disciplinary/professional field of decisions and actions affecting places. Planning practice and knowledge contribute to urban inquiry, which also draws on many other disciplines. | Moderate–high | Refine to **interdisciplinary field / planning discipline-and-practice interface**. No strict one-way dependency or containment. | Retain as RD-P; refine boundary. |
| RD-006 Infrastructure Engineering ↔ Civil Engineering | University programmes show Infrastructure Engineering focused on structural and transportation systems, resilience, materials, and built-environment assets, often within Civil and Environmental Engineering settings. Civil Engineering designs, provides, upgrades, and manages essential infrastructure. | High for technical overlap; moderate for universal boundary | Refine to **technical-scope overlap / infrastructure-specialization interface**. Institutional programme placement does not prove universal containment. No universal direction. | Retain as RD-P; refine subtype. |

All six remain proposed. None is owner-accepted by this report.

## 3. Initial subject-pair screen: Life Sciences ↔ Health Sciences

The Life Sciences inventory has 18 subjects and the Health Sciences inventory has 15, producing 270 possible cross-domain subject pairs. This pilot screened eight prioritised pairs, not the entire block.

| Screen ID | Canonical subject pair | Finding | Evidence strength | Recommended disposition |
|---|---|---|---|---|
| LSHS-001 | Medicine ↔ Physiology | Medical organ-system curricula integrate physiology with clinical teaching. | High | Candidate RD-P: clinical/foundational-science interface; no containment or dependency. |
| LSHS-002 | Medicine ↔ Anatomy | Medical curricula integrate anatomy into organ-system teaching and clinical preparation. | High | Candidate RD-P: clinical/foundational-science interface; no hierarchy edge. |
| LSHS-003 | Epidemiology ↔ Microbiology | Infectious-disease epidemiology connects population distribution and transmission with etiologic agents, infection, host factors, and microbiological evidence. | High | Candidate RD-P: population/pathogen interface; neither field contains the other. |
| LSHS-004 | Epidemiology ↔ Virology | Viral-disease epidemiology combines virus characteristics, host factors, transmission dynamics, and disease distribution in populations. | High | Candidate RD-P: viral-pathogen/population interface. |
| LSHS-005 | Mental Health ↔ Neuroscience | NIMH research explicitly studies how neural systems and biological processes contribute to psychopathology, while mental health has wider dimensions. | High | Candidate RD-P: neurobiological research interface; neuroscience does not define the whole of Mental Health. |
| LSHS-006 | Nutrition ↔ Physiology | Nutritional physiology studies nutrient use, digestion, homeostasis, metabolic regulation, and physiological requirements. | High | Candidate RD-P: nutritional/physiological interface. |
| LSHS-007 | Public Health ↔ Ecology | WHO One Health connects human, animal, plant, and ecosystem health, including ecological conditions influencing disease emergence and spread. | High for this bounded interface | Candidate RD-P: ecosystem-health/population-health interface, with scope restricted to ecological determinants and interconnected health. |
| LSHS-008 | Pharmacology ↔ Molecular Biology | Both occur in an integrated medical-science curriculum, but co-inclusion alone does not prove a specific direct relationship between their canonical subject scopes. | Insufficient for a pair-specific edge | Do not promote in this pass. Defer pending direct evidence about molecular targets or pharmacological mechanisms. |

**Pilot accounting:** 270 possible pairs = 7 candidate RD-P relationships + 1 screened but not promoted + 262 not yet individually assessed. The seven candidates are recommendations for a future controlled taxonomy update; they are not canonical RD-P rows in v1.13.1.

## 4. Evidence register

| Source ID | Source | URL |
|---|---|---|
| S20 | Tufts University School of Medicine — MD Curriculum | https://medicine.tufts.edu/academics/medicine/curriculum |
| S21 | NCBI Bookshelf — Epidemiology, General Concepts | https://www.ncbi.nlm.nih.gov/books/NBK7993/ |
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

## 5. Status and next work

- Existing RD-P proposals in the canonical baseline: 18.
- Existing proposals assessed in this batch: 6.
- Owner-accepted relationships: 0.
- Life Sciences ↔ Health Sciences pair block: 270 possible comparisons.
- Prioritised pairs screened: 8.
- Candidate relationships recommended for controlled registration: 7.
- Screened without promotion: 1.
- Still unassessed within the block: 262.

Next: assess RD-007 through RD-012; request owner review of RD-001 through RD-006; review the seven Life Sciences ↔ Health Sciences candidates for controlled insertion; then continue the remaining 262 pairs in bounded subgroups.

No canonical taxonomy amendment, owner acceptance, hierarchy reassignment, dependency, enablement, implementation, or verification is claimed by this report.
