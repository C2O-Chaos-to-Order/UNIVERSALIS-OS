# Cross-Domain Relationship Evidence Assessment

**Version:** 0.36.0  
**Assessment date:** 2026-11-23  
**Canonical taxonomy baseline:** v1.13.8  
**Status:** Three additional unique Life Sciences ↔ Health Sciences subject pairs screened; all three are recommended as bounded candidate related-but-distinct (RD-P) relationships for owner review. No owner acceptance or canonical taxonomy amendment is claimed.

## 1. Scope and safeguards

This report continues the Life Sciences ↔ Health Sciences cross-domain screening programme. It assesses three previously unassessed pairs selected from the reconciled inventory of 109 remaining pairs:

- Marine Biology ↔ Emergency Medicine: emergency assessment and management of selected marine-organism injuries and envenomations, including toxic effects, respiratory or cardiovascular compromise, neurotoxicity, and wound complications.
- Cell Biology ↔ Rehabilitation Science: cellular mechanotransduction, tissue remodeling, muscle and connective-tissue adaptation, and repair mechanisms investigated in rehabilitation research.
- Molecular Biology ↔ Emergency Medicine: rapid molecular and host-response diagnostics in selected acute-care presentations, particularly respiratory infection and suspected sepsis, and the translation of molecular test outputs into time-sensitive clinical decisions.

The three interfaces are distinct. Marine Biology contributes knowledge of marine organisms, their biological characteristics, and relevant toxins or venomous structures; Emergency Medicine assesses and manages acute injury or envenomation. Cell Biology contributes knowledge of cellular processes and responses to mechanical and biochemical stimuli; Rehabilitation Science investigates how these processes relate to rehabilitation interventions, functional adaptation, and outcomes. Molecular Biology contributes nucleic-acid, gene-expression, and molecular diagnostic methods; Emergency Medicine evaluates selected patients and determines whether test results are sufficiently timely and actionable to inform acute decisions.

The scope is deliberately bounded. It does not imply that every marine injury requires specialist marine-biological identification, that every rehabilitation outcome is explained by cellular mechanisms, or that a molecular diagnostic result independently determines emergency treatment. Marine envenomation guidance varies by organism and geography; local poison-centre or toxicology advice and current clinical protocols remain important. Mechanistic cellular findings do not establish clinical efficacy or an individualized rehabilitation prescription. Molecular pathogen detection, host-response classification, and sepsis-risk assessment are different diagnostic tasks and must not be conflated. A positive molecular test does not by itself establish disease severity, causality, or the need for a particular treatment.

The canonical taxonomy remains the authority for subject names, identifiers, and hierarchy. The inventory contains 18 Life Sciences subjects and 15 Health Sciences subjects, producing 270 possible cross-domain pairs. The preceding assessment snapshots v0.1.0 through v0.35.0 record 161 unique screened pairs, 146 candidate recommendations, and 15 screened but not promoted or deferred, leaving 109 individually unassessed pairs before this batch.

Each selected pair was checked as an unordered subject pair against all 35 prior assessment snapshots, including early name-only rows and later stable-ID rows. The historical assessment IDs LSHS-001 through LSHS-161 were reconciled. None of the three selected pairs appears in the prior ledger.

A candidate RD-P recommendation is a proposal for owner review, not an accepted or registered canonical edge. A candidate does not establish hierarchy, dependency, enablement, implementation, testing, or verification. No canonical change is made by this report.

## 2. New unique subject-pair screening

| Assessment ID | Canonical subject pair | Evidence and scope boundary | Evidence assessment | Recommended disposition and direction |
|---|---|---|---|---|
| LSHS-162 | USA-LS-009 Marine Biology ↔ USA-HS-014 Emergency Medicine | Current emergency-care guidance explicitly addresses injuries and envenomations from marine organisms including blue-ringed octopus, cone snails, stonefish, box jellyfish, sea snakes, sea urchins, and stingrays. The NSW Emergency Care Institute clinical tool describes delayed and severe envenomation, neurotoxicity, respiratory paralysis, cardiovascular collapse, anaphylaxis, wound complications, observation, resuscitation, and organism-specific management. Its adult emergency-care assessment and treatment protocol, published October 2026, includes rapid clinical assessment, airway/breathing/circulation/disability/exposure assessment, recognition of neurotoxic paralysis and shock, escalation, analgesia, and organism-specific care. These sources demonstrate a direct acute-care interface with knowledge of marine organisms and their biological hazards. The evidence is strongest for specific organisms and coastal contexts; it does not establish that all marine biological knowledge is routinely used in every emergency department or that species identification is always possible. [S367–S368] | High for the bounded marine-organism injury and envenomation interface. Current clinical tools and an October 2026 adult emergency-care protocol directly specify marine taxa, toxic effects, recognition, assessment, and acute management. The relationship is organism- and region-specific, and management recommendations must be interpreted within local protocols and toxicology advice. | Candidate RD-P: marine-organism biology, taxonomy, venomous structures, toxins, and organism-specific exposure characteristics / emergency recognition, triage, assessment, stabilization, symptom management, monitoring, and escalation for selected marine injuries and envenomations interface. Marine Biology contributes organism and hazard knowledge that can improve exposure characterization and differential assessment; Emergency Medicine manages the patient's acute physiological threat, injury, and complications. Clinical cases and surveillance can identify marine hazards relevant to biological study. Reciprocal, bounded interface; no claim that Marine Biology replaces clinical toxicology or that every marine exposure is an emergency. |
| LSHS-163 | USA-LS-011 Cell Biology ↔ USA-HS-015 Rehabilitation Science | A 2026 review of mechanotransduction in orthopedic rehabilitation describes how cells convert mechanical stimuli into biochemical signals and examines cellular pathways involved in tissue adaptation and repair in rehabilitation contexts. A second 2026 review examines genomic and epigenetic regulatory mechanisms in exercise-based rehabilitation, including integrin–FAK and Hippo YAP/TAZ signaling, AMPK–PGC-1α, SIRT1, mTOR, extracellular-matrix turnover, muscle satellite cells, fibro-adipogenic progenitors, endothelial cells, and microvascular adaptation. It explicitly cautions that acute exercise-induced molecular responses should not be interpreted as proof of sustained tissue adaptation and that biomarker translation remains limited by tissue specificity, kinetics, analytical variability, and the need for standardized validation against structural and functional outcomes. These sources support a research interface between cellular mechanisms and rehabilitation science. They do not establish that a cellular pathway predicts an individual's response or that a molecular marker is ready to guide routine rehabilitation decisions. [S369–S370] | Moderate–high for the bounded mechanobiology, tissue-adaptation, and rehabilitation-research interface. Current reviews directly connect cell-level mechanotransduction and molecular remodeling with rehabilitation processes. The evidence is mechanistic and translational; clinical validation, standardized biomarkers, and individual-level treatment utility remain limited. | Candidate RD-P: cellular structure and function, mechanotransduction, cell signaling, tissue remodeling, extracellular-matrix biology, and cell-specific adaptation / rehabilitation research on intervention mechanisms, tissue response, functional adaptation, outcome measurement, and translational validation interface. Cell Biology contributes explanatory models of cellular responses to mechanical and biochemical stimuli; Rehabilitation Science investigates how rehabilitation interventions relate to tissue-level mechanisms and functional outcomes. Rehabilitation findings can generate new cellular hypotheses and identify translational questions. Reciprocal, bounded research interface; no claim that cellular mechanisms alone determine patient outcomes or prescribe rehabilitation dosage. |
| LSHS-164 | USA-LS-010 Molecular Biology ↔ USA-HS-014 Emergency Medicine | Recent evidence documents molecular testing in emergency-care workflows. A 2026 review of rapid diagnostics examines molecular assays, host-response platforms, turnaround times, and clinical actionability, while emphasizing that analytical performance and rapid results do not automatically produce clinical utility. A prospective 2025–2026 emergency-department evaluation of rapid multiplex point-of-care PCR reported real-time results for acute respiratory infections and associations with lower antibiotic prescribing for viral infections and shorter ED length of stay, but it was a single-centre evaluation. A separate 2025–2026 ED implementation study found multiplex PCR feasible for rapid respiratory pathogen detection and potentially useful for antimicrobial decisions and isolation strategies. However, a 2026 systematic review and meta-analysis of 25 randomized trials involving 12,638 patients found that molecular point-of-care testing probably had little to no important effect on overall antibiotic use or treatment duration, despite improving appropriate antibiotic prescribing; the authors did not support routine use for adults with acute respiratory infections. The 2026 Surviving Sepsis Campaign also states that sepsis is a clinical diagnosis and that evidence is insufficient to recommend novel rapid host-response diagnostics. These sources support a bounded interface in selected acute infectious presentations, while showing that test performance, workflow integration, and clinical benefit are separate evidentiary questions. [S371–S373] | Moderate–high for the bounded molecular-diagnostics / emergency-decision interface. Molecular assays and host-response measurements are directly used or evaluated in acute-care settings, but clinical impact is heterogeneous and often modest. The evidence does not support universal molecular testing, automatic antibiotic decisions, or treating molecular test output as a substitute for clinical assessment. | Candidate RD-P: nucleic-acid amplification, pathogen-targeted molecular detection, gene-expression and host-response measurement, assay design, and molecular diagnostic interpretation / emergency assessment and management of selected acute infectious presentations, time-sensitive testing decisions, interpretation of diagnostic results, isolation decisions, and antimicrobial-stewardship workflows interface. Molecular Biology contributes the molecular methods and biological interpretation of assay targets; Emergency Medicine determines whether testing is indicated, interprets results in clinical context, and makes time-sensitive management decisions. Acute-care needs inform molecular assay development and implementation research. Reciprocal, bounded interface; pathogen detection, host-response classification, and severity assessment remain distinct tasks, and testing does not replace resuscitation or clinical judgment. |

## 3. Duplicate, distinction, and scope cross-check

The three selected pairs were checked as unordered subject pairs against all 35 prior assessment snapshots, v0.1.0 through v0.35.0. The reconciled prior ledger contains 161 unique screened pairs with assessment IDs LSHS-001 through LSHS-161. Exact normalized-pair checks found no occurrence of Marine Biology ↔ Emergency Medicine, Cell Biology ↔ Rehabilitation Science, or Molecular Biology ↔ Emergency Medicine in the prior ledger. Canonical subject names and identifiers were checked against taxonomy v1.13.8.

Previously assessed and related pairs remain distinct:

- Marine Biology ↔ Medicine (LSHS-060), Marine Biology ↔ Public Health (LSHS-061), Marine Biology ↔ Preventive Medicine (LSHS-062), and Marine Biology ↔ Nutrition (LSHS-066) concern other Health Sciences applications. LSHS-162 is specifically about acute injury and envenomation assessment and management in Emergency Medicine.
- Zoology ↔ Emergency Medicine (LSHS-068) concerns animal-associated injury and exposure more broadly. Marine Biology ↔ Emergency Medicine narrows the biological scope to marine organisms and their specific envenomation and injury mechanisms; it is not a duplicate merely because some animal taxa overlap.
- Cell Biology ↔ Physical Therapy (LSHS-134) concerns cellular mechanotransduction and tissue adaptation in physical-therapy applications. LSHS-163 concerns the broader research discipline of Rehabilitation Science, including rehabilitation intervention mechanisms, outcome measurement, and translational validation. Physical Therapy is a clinical profession; Rehabilitation Science is not interchangeable with that practice scope.
- Molecular Biology ↔ Medicine (LSHS-018), Molecular Biology ↔ Surgery (LSHS-031), Molecular Biology ↔ Preventive Medicine (LSHS-023), Molecular Biology ↔ Nursing (LSHS-097), Molecular Biology ↔ Epidemiology (LSHS-093), Molecular Biology ↔ Public Health (LSHS-094), Molecular Biology ↔ Nutrition (LSHS-124), Molecular Biology ↔ Mental Health (LSHS-127), and Molecular Biology ↔ Physical Therapy (LSHS-133) concern other disciplinary interfaces. LSHS-164 is specifically bounded to molecular and host-response diagnostics used in selected acute-care workflows.
- Microbiology ↔ Emergency Medicine (LSHS-041), Virology ↔ Emergency Medicine (LSHS-044), and Mycology ↔ Emergency Medicine (LSHS-049) address organism-specific clinical microbiology, viral disease, and fungal disease. Molecular Biology ↔ Emergency Medicine is a methods-and-mechanisms interface focused on nucleic-acid and gene-expression assays; it is not a claim that molecular biology is interchangeable with Microbiology or Virology.
- The 2026 sepsis guideline's caution about novel host-response diagnostics is retained. It does not negate the use of pathogen-specific molecular assays in selected ED workflows, but it prevents conflating a molecular test with a validated sepsis diagnosis or a universally actionable host-response test.

Direction and scope:

- LSHS-162 is reciprocal within the bounded marine-injury interface: Marine Biology contributes organism and hazard knowledge; Emergency Medicine assesses and manages acute injury, envenomation, and physiological compromise. Clinical cases and surveillance can identify hazards for biological investigation.
- LSHS-163 is reciprocal within the bounded research interface: Cell Biology contributes cellular mechanisms; Rehabilitation Science evaluates rehabilitation-related tissue responses, functional adaptation, and outcomes. Rehabilitation research can generate new mechanistic questions for cell biology.
- LSHS-164 is reciprocal within the bounded acute-diagnostics interface: Molecular Biology contributes assay and molecular interpretation methods; Emergency Medicine determines clinical indication, interprets results, and manages the patient. Acute-care workflow needs can inform molecular assay development and implementation research.

None of these proposals is a hierarchy edge, universal dependency, or enablement claim. The evidence does not imply that marine biological identification is always available, cellular biomarkers are clinically validated, or molecular test results independently determine emergency treatment.

## 4. Evidence register

Sources were accessed or rechecked on 2026-11-23. The register prioritizes current clinical guidance, peer-reviewed translational reviews, prospective ED implementation evidence, a randomized-trial meta-analysis, and a current international sepsis guideline.

| Ref | Source | Relevance |
|---|---|---|
| S367 | NSW Health, Emergency Care Institute, [Venomous marine stings](https://aci.health.nsw.gov.au/networks/eci/clinical/tools/venomous-marine-stings), published December 2024, minor revision December 2025 | Current clinical tool covering blue-ringed octopus, box jellyfish, cone snail, sea snake, and stonefish; describes neurotoxicity, respiratory paralysis, cardiovascular collapse, anaphylaxis, observation, resuscitation, and organism-specific management. |
| S368 | NSW Health, [Insect bites or marine stings — Adult ECAT protocol](https://aci.health.nsw.gov.au/ecat/adult/insect-bites-marine-stings), published October 2026 | Current adult emergency-care assessment and treatment protocol with rapid assessment, A-to-G evaluation, recognition of envenomation and deterioration, and management guidance for marine stings including sea urchin, jellyfish, stingray, and stonefish. |
| S369 | Wang et al., [Mechanotransduction and its impact on regenerative medicine in orthopedic rehabilitation](https://pubmed.ncbi.nlm.nih.gov/41823544/), *International Journal of Molecular Medicine* 57(5) (May 2026), DOI: 10.3892/ijmm.2026.5798 | Review of cellular mechanotransduction as a biological mechanism underlying tissue adaptation and repair in orthopedic rehabilitation. |
| S370 | [Genomic and epigenetic regulatory mechanisms in exercise-based rehabilitation processes: Cellular and tissue remodeling, microvascular adaptation, and circulating biomarkers](https://pubmed.ncbi.nlm.nih.gov/42722290/) (2026) | Review of cellular, genomic, epigenetic, extracellular-matrix, muscle, vascular, and immune-cell mechanisms in exercise-based rehabilitation; explicitly identifies biomarker and clinical-translation limitations. |
| S371 | [Rapid Diagnostics for Distinguishing Bacterial and Viral Infections: A Review of Technologies, Clinical Utility, and Stewardship Implications](https://pmc.ncbi.nlm.nih.gov/articles/PMC13604791/) (2026) | Review of molecular assays and host-response diagnostics in acute care; distinguishes analytical performance, turnaround time, clinical actionability, and demonstrated stewardship impact. |
| S372 | Bigaud et al., [Impact of multiplex PCR point-of-care platform implementation for respiratory pathogen detection in an emergency department with high daily patient volume](https://pmc.ncbi.nlm.nih.gov/articles/PMC12802140/), *Journal of Clinical Microbiology* 64(1), e01313-25 (published 1 December 2025; issue January 2026), DOI: 10.1128/jcm.01313-25 | Real-world ED implementation study of multiplex molecular pathogen detection with results within approximately 20 minutes; reports feasibility and effects on patient flow, antimicrobial decisions, and infection-control strategies. |
| S373 | Society of Critical Care Medicine, [Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026](https://sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026) (2026) | Current international guideline emphasizing that sepsis is a clinical diagnosis, treatment and resuscitation must begin immediately, and evidence is insufficient to recommend novel rapid host-response diagnostics. |

## 5. Updated Life Sciences ↔ Health Sciences accounting

| Measure | Count |
|---|---:|
| Total possible cross-domain subject pairs | 270 |
| Unique pairs screened through v0.35.0 | 161 |
| New unique pairs screened in v0.36.0 | 3 |
| **Cumulative unique pairs screened** | **164 of 270** |
| Candidate recommendations before this batch | 146 |
| New candidate recommendations in this batch | 3 |
| **Cumulative candidate RD-P recommendations** | **149** |
| Cumulative screened but not promoted / deferred | 15 |
| **Pairs still individually unassessed** | **106** |
| **Screening coverage** | **60.74%** |

Accounting check:

270 = 149 candidates + 15 not promoted/deferred + 106 unassessed

The 15 previous non-promotions and deferrals remain unchanged. This batch adds three candidate recommendations and no new non-promotions. Candidate status does not imply owner acceptance or canonical registration.

## 6. Canonical status and governance

- Canonical taxonomy remains **v1.13.8**.
- The canonical taxonomy blob SHA remains **3e7c570943b4e65307f01618ac81b031051ad1a9**.
- The 18 canonical RD-P proposals remain unchanged.
- Canonical hierarchy-edge, RD-P, and source-unlinked sparse-matrix counts remain **252 / 18 / 34,446**.
- The three recommendations in this report have **not** been inserted into the canonical taxonomy.
- Owner-accepted relationships remain **zero**.
- No dependency, enablement, hierarchy reassignment, implementation, testing, or verification is inferred from these relationship assessments.
- The six existing proposals **RD-013 through RD-018** remain a separate workstream and are not assessed or altered by this report.
- Candidate recommendations remain supplemental evidence-review records pending explicit owner review.

## 7. Next work

Continue with another topic-focused group from the **106 remaining** Life Sciences ↔ Health Sciences pairs. Select the next subgroup only after checking every proposed unordered pair against all **36 preceding assessment snapshots**, v0.1.0 through v0.36.0, and confirming canonical subject identifiers.

The separate RD-013–RD-018 proposal-assessment workstream remains open and is not folded into the 270-pair Life Sciences ↔ Health Sciences screening count.

**Review condition before any canonical insertion:** verify unordered-pair uniqueness, stable identifiers, relationship subtype, direction, evidence provenance, scope boundary, sparse-matrix effect, and explicit owner acceptance.


## Taxonomy alignment correction — 2026-11-24

**Canonical taxonomy baseline:** v1.13.8  
**Canonical taxonomy Git blob SHA:** `3e7c570943b4e65307f01618ac81b031051ad1a9`

This correction supersedes the former v1.13.1 baseline reference. The v1.13.8 change record confirms that Universal Subject hierarchies, canonical subject-Alchemy identities, 22-context mappings, relationship-matrix values, shared-identity relationships, cross-domain proposals, and cumulative totals were preserved. Life Sciences remains 18 subject Alchemies and Health Sciences remains 15, with their canonical identifiers unchanged; the 270-pair screening universe is unchanged. This report assesses relationships between subject Alchemies; it does not assess or complete the taxonomy's 22-context contextual expressions. Historical findings, evidence assessments, source records, and dispositions are retained. No owner acceptance or canonical taxonomy amendment is implied.
