# Cross-Domain Relationship Evidence Assessment

**Version:** 0.20.0  
**Assessment date:** 2026-11-23  
**Status:** Three additional unique Life Sciences ↔ Health Sciences subject pairs screened. All three are recommended as bounded candidate related-but-distinct (RD-P) relationships, with different evidence strengths. The batch examines Neuroscience, Physiology, and Anatomy interfaces with Pharmacology. The Neuroscience relationship is bounded to neuropharmacology; the Physiology relationship to pharmacodynamics and quantitative systems pharmacology; and the Anatomy relationship to anatomical targeting and local-anesthetic delivery in selected regional-anesthesia procedures. No owner acceptance or canonical taxonomy amendment is claimed.

## 1. Canonical baseline and scope

The canonical source is ALCHEMY_TAXONOMY_FOR_THE_UNIVERSAL_SUBJECTS_OF_KNOWLEDGE.md, version 1.13.1. It was checked in all four in-scope repositories and returned the same Git blob SHA:

`f054a687bb649f8e67982a607b59a5156e8e9a46`

The canonical Life Sciences inventory contains 18 subject Alchemies and the Health Sciences inventory contains 15, yielding 270 possible cross-domain subject pairs.

Assessment snapshots v0.1.0 through v0.19.0 record 113 unique Life Sciences ↔ Health Sciences subject pairs screened: 101 candidate recommendations and 12 not promoted/deferred. This report screens three additional unique pairs, LSHS-114 through LSHS-116.

### Selected subgroup

The selected 3 × 1 subgroup consists of:
- USA-LS-013 Neuroscience;
- USA-LS-014 Physiology;
- USA-LS-015 Anatomy;
- USA-HS-005 Pharmacology.

The three possible pairings are:
- Neuroscience ↔ Pharmacology;
- Physiology ↔ Pharmacology;
- Anatomy ↔ Pharmacology.

Each subject identifier and canonical name was checked against the v1.13.1 taxonomy. Each unordered pair was checked against every assessment table in v0.1.0 through v0.19.0, including the earliest name-only entries and all later stable-ID entries. The previous ledger contains 113 unique screened pairs with sequential identifiers LSHS-001 through LSHS-113. None of the three selected pairs is an exact duplicate.

No subject is renamed, merged, reparented, or expanded.

## 2. Method and important terminology boundaries

Each pair is assessed for a specific interface between the canonical Life Sciences subject and Pharmacology. The evidence distinguishes neural mechanisms, whole-system physiological responses, and anatomical placement from pharmacological targets, drug exposure, dose-response, mechanism of action, and therapeutic effects.

Important boundaries:
- **Neuroscience is not synonymous with Pharmacology.** Neuroscience studies the nervous system, including its structure, function, development, networks, cellular and molecular mechanisms, and behaviour. Pharmacology studies drug action, targets, dose-response, exposure, disposition, safety, and therapeutic use. Neuropharmacology is an established interface focused on drugs and targets that influence the brain, spinal cord, and peripheral nerves in health and disease.
- **Neuropharmacology is a bounded specialty interface, not the whole of either subject.** It does not imply that every neuroscience question is pharmacological or that every pharmacological intervention acts on the nervous system. A molecular target, promising compound, or preclinical response is not equivalent to an approved and clinically effective treatment.
- **Physiology is not synonymous with Pharmacology.** Physiology explains normal and disordered function of living systems. Pharmacology investigates how drugs alter those systems through target engagement, dose-response, pharmacokinetics, pharmacodynamics, and safety. Quantitative systems pharmacology (QSP) directly integrates mechanistic representations of biology and physiology with quantitative pharmacology to support drug-development and clinical decisions.
- **QSP is a specialised modelling approach, not a synonym for all Pharmacology or all Physiology.** It uses defined questions, model structure, data, assumptions, context of use, and evaluation of uncertainty. A model's ability to integrate physiological mechanisms does not make its predictions automatically valid or clinically sufficient.
- **Anatomy is not synonymous with Pharmacology.** Anatomy describes body structures, their spatial relationships, variation, and regional organisation. Pharmacology studies the actions and effects of drugs. Their direct interface in this batch is limited to targeted regional drug delivery, especially regional anesthesia, where nerve location, fascial planes, vessels, bony landmarks, and anatomical variants influence needle trajectory, drug placement, and local-anesthetic spread.
- **Regional anesthesia is not a general proxy for all drug delivery.** It is a specialised clinical procedure involving anatomy, local-anesthetic pharmacology, physiology, procedural skill, imaging, monitoring, and patient-specific risk assessment. The selected pair does not imply that Anatomy determines the pharmacological dose, receptor action, or systemic safety of a drug by itself.
- **Physiological and anatomical contributions must not be collapsed.** Physiology helps explain perfusion, tissue response, nerve function, and systemic drug effects; Anatomy identifies structures, boundaries, and spatial variation. Both can inform pharmacological applications, but they answer distinct questions.
- A candidate RD-P is a proposal for owner review, not an accepted or registered canonical edge. Evidence of an interface does not establish universal dependency, containment, hierarchy, or guaranteed therapeutic benefit.
- Evidence grades describe the strength and directness of the bounded subject-pair interface, not the certainty that every compound, model, nerve block, or drug-delivery approach is effective in every patient or context.

## 3. New unique subject-pair screening

| Assessment ID | Canonical subject pair | Evidence and scope boundary | Evidence assessment | Recommended disposition and direction |
|---|---|---|---|---|
| LSHS-114 | USA-LS-013 Neuroscience ↔ USA-HS-005 Pharmacology | Neuropharmacology is an explicitly defined research specialty studying drugs and their targets that influence the nervous system—including brain, spinal cord, and peripheral nerves—in health and disease. Its scope includes cellular and molecular biology of drug targets, clinical neuropharmacology, drug effects on isolated tissues and whole organisms, and neuropharmacological mechanisms. A 2026 review examines emerging CNS therapeutic strategies targeting synaptic plasticity, neuroinflammation, and ion-channel regulation, while identifying the blood-brain barrier, complex pathophysiology, and drug-development limitations as continuing challenges. These sources support a direct interface between neural mechanisms and pharmacological targets, mechanisms, exposure, and therapeutic evaluation. The relationship is limited to neuropharmacology and CNS/PNS-active agents; it does not make all neuroscience pharmacological or imply that all neurobiological mechanisms have clinically validated drug targets. [S251, S252] | High; a defined neuropharmacology specialty scope and a current peer-reviewed review directly connect nervous-system mechanisms with drug targets and therapeutic strategies. Translation and clinical efficacy remain target- and disease-specific. | Candidate RD-P: neural systems, circuits, and neurochemical mechanisms / neuropharmacological targets, drug action, and therapeutic evaluation interface. Neuroscience contributes knowledge of neural structure, function, signalling, circuits, and disease mechanisms; Pharmacology contributes compound-target interaction, mechanism of action, dose-response, exposure, safety, and therapeutic evaluation. Reciprocal research and clinical interface; no containment or universal dependency. |
| LSHS-115 | USA-LS-014 Physiology ↔ USA-HS-005 Pharmacology | Pharmacodynamics concerns the biochemical, physiological, and molecular effects of drugs on the body, including receptor binding, sensitivity, post-receptor effects, and dose-response. Quantitative systems pharmacology integrates mechanistic representations of biology and quantitative pharmacology and explicitly incorporates disease pathophysiology and human physiology into predictive frameworks. A 2026 review describes QSP as an established component of model-informed drug development, with applications in mechanism-based dose and regimen selection, combination strategies, biomarker-informed patient stratification, and lifecycle decisions. A 2024 review likewise describes QSP as an integrative approach combining physiology and pharmacology, with examples in glucose regulation, oncology, autoimmune disease, and HIV treatment. These sources establish a direct systems-level interface: physiology describes the biological systems and responses represented in models; pharmacology characterizes drug exposure, target engagement, response, and therapeutic decisions. QSP models remain dependent on model assumptions, data, defined context of use, and evaluation of uncertainty. [S253–S255] | High; current QSP synthesis and clinical-pharmacology reference material explicitly connect physiology and pharmacological effects, while distinguishing model-supported decisions from unvalidated prediction. | Candidate RD-P: physiological systems, regulation, and response / pharmacodynamic and quantitative systems-pharmacology interface. Physiology contributes mechanistic descriptions of organ-system function and disease-state responses; Pharmacology contributes drug mechanism, exposure-response, target effects, dosing, and safety evaluation. Reciprocal modelling and translational interface; physiology is not a branch of Pharmacology, and QSP is not assumed to represent every pharmacological question. |
| LSHS-116 | USA-LS-015 Anatomy ↔ USA-HS-005 Pharmacology | Regional-anesthesia practice provides a bounded anatomical-pharmacological interface. A 2025 narrative review published in 2026 reports that anatomical variation in nerves and adjacent structures can influence ultrasound-guided block needle trajectory, local-anesthetic spread, and block efficacy, and may contribute to technical failure or complications; the authors also state that the literature on specific anatomical variations remains limited. Clinical regional-anesthesia guidance explains how local anesthetic is deposited near peripheral nerves, within fascial planes, or in neuraxial spaces, with anatomical landmarks and target structures defining placement. OpenAnesthesia's 2026 regional-anesthesia resource states that accurate identification of bony and surface landmarks remains important for safe and effective blocks and that ultrasound supplements rather than replaces anatomical knowledge. Pharmacological decisions additionally require selection and dosing of the local anesthetic and recognition of systemic toxicity; anatomy alone does not provide those pharmacological decisions. This evidence supports a specialised regional-delivery and local-anesthetic interface, not a general relationship covering all anatomy and all pharmacology. [S256–S258] | Moderate; direct procedural sources and a recent anatomical-variation review demonstrate that anatomy affects drug placement and local-anesthetic distribution, but the interface is specialised and the anatomical-variation literature is acknowledged to be limited. | Candidate RD-P, narrowly scoped: regional structure and anatomical variation / targeted local-anesthetic placement and regional pharmacological effect interface. Anatomy contributes spatial relationships, landmarks, nerve courses, fascial planes, and variant structures; Pharmacology contributes local-anesthetic mechanism, selection, concentration, dose, duration, and systemic safety. Bounded procedural and applied interface; no claim that Anatomy determines drug action or that all pharmacological administration requires detailed regional anatomy. |

## 4. Duplicate, direction, and scope cross-check

The three pairs were compared as unordered subject pairs against every assessment row in v0.1.0 through v0.19.0. The previous ledger contains 113 unique screened pairs with identifiers LSHS-001 through LSHS-113. Historical rows before stable IDs were introduced were checked by canonical subject names; later entries were checked using both IDs and names. None of the selected pairs is present in the prior ledger.

Previously assessed and related pairings remain distinct:
- Neuroscience ↔ Medicine (LSHS-033 is Neuroscience ↔ Emergency Medicine; no Neuroscience ↔ Pharmacology entry);
- Neuroscience ↔ Mental Health (LSHS-005);
- Neuroscience ↔ Rehabilitation Science (LSHS-032);
- Neuroscience ↔ Physical Therapy (LSHS-034);
- Physiology ↔ Medicine (LSHS-001);
- Physiology ↔ Nutrition (LSHS-006);
- Physiology ↔ Emergency Medicine (LSHS-037);
- Physiology ↔ Rehabilitation Science (LSHS-038);
- Physiology ↔ Physical Therapy (LSHS-039);
- Anatomy ↔ Medicine (LSHS-002);
- Anatomy ↔ Occupational Therapy (LSHS-086);
- Anatomy ↔ Physical Therapy (LSHS-087);
- Anatomy ↔ Rehabilitation Science (LSHS-088).

These do not duplicate the new pharmacology pairings. The distinction is substantive:
- LSHS-114 concerns drug action on neural targets and neuropharmacological mechanisms, rather than neurological assessment, rehabilitation, or mental-health research alone.
- LSHS-115 concerns physiological systems and drug effects, including mechanistic quantitative models, rather than physiological knowledge applied to medicine, nutrition, emergency resuscitation, or rehabilitation.
- LSHS-116 concerns regional anatomy and the placement/spread of local anesthetic in selected regional techniques, rather than anatomy used in general medical, occupational-therapy, physical-therapy, or surgical practice.

Direction is recorded as reciprocal at the bounded interface where both subject scopes contribute:
- LSHS-114: neuroscience identifies relevant neural targets and functional mechanisms; pharmacology tests and characterizes compounds that modulate those targets and responses.
- LSHS-115: physiology defines system function and disease-state mechanisms; pharmacology quantifies how drug actions alter these systems and how dose/regimen choices affect outcomes. QSP integrates both.
- LSHS-116: anatomy defines regional structures and variants relevant to placement; pharmacology defines the properties and safe use of the local-anesthetic agent. The procedural interface uses both, but neither discipline alone determines the clinical decision.

None of these proposals is a hierarchy edge, universal dependency, or enablement claim.

## 5. Evidence register

Sources were accessed or rechecked on 2026-11-23. A specialist journal scope, a current peer-reviewed neuropharmacology review, current quantitative-systems-pharmacology synthesis, clinical pharmacodynamics reference material, and regional-anesthesia anatomy sources were used. The register distinguishes an established subfield from systems modelling and a specialised procedural application.

| Ref | Source | Relevance |
|---|---|---|
| S251 | Frontiers in Neuroscience, [Neuropharmacology section: Scope](https://www.frontiersin.org/journals/neuroscience/sections/neuropharmacology/about) | Defines the peer-reviewed specialty section's scope as research on drugs and targets influencing the brain, spinal cord, and peripheral nerves in health and disease; includes cellular/molecular drug targets, clinical work, drug effects, and mechanisms. |
| S252 | Shrivastava et al., [Advances in neuropharmacology: Innovative drug strategies targeting synaptic plasticity, neuroinflammation, and ion channel regulation for future CNS treatments](https://pubmed.ncbi.nlm.nih.gov/42103070/), *Life Sciences* 397, 124436 (15 July 2026), DOI: 10.1016/j.lfs.2026.124436 | Current review of CNS-targeted pharmacological strategies focused on synaptic plasticity, neuroinflammation, and ion channels; identifies blood-brain barrier impermeability and complex pathophysiology as translational challenges. |
| S253 | Wang et al., [Quantitative Systems Pharmacology (QSP): Bridging Biology and Mechanism with Clinical Drug Development Decisions](https://pubmed.ncbi.nlm.nih.gov/42742475/), *Journal of Clinical Pharmacology* 66(9), e70289 (15 September 2026), DOI: 10.1002/jcph.70289 | Current review explaining how QSP integrates mechanistic biology, human physiology, disease pathophysiology, and quantitative pharmacology to inform dose/regimen selection, patient stratification, combination strategies, and development decisions; emphasizes context of use, assumptions, and model credibility. |
| S254 | Ramasubbu et al., [Applying quantitative and systems pharmacology to drug development and beyond: An introduction to clinical pharmacologists](https://pubmed.ncbi.nlm.nih.gov/39250624/), *Indian Journal of Pharmacology* 56(4), 268–276 (2024), DOI: 10.4103/ijp.ijp_644_23 | Review explicitly describes QSP as an integrative approach combining physiology and pharmacology; discusses applications including glucose regulation, oncology, autoimmune disease, and HIV treatment. |
| S255 | MSD Manual Professional Edition, [Overview of Pharmacodynamics](https://www.msdmanuals.com/professional/clinical-pharmacology/pharmacodynamics/overview-of-pharmacodynamics) (last reviewed June 2025) | Defines pharmacodynamics as the biochemical, physiological, and molecular effects of drugs; explains dose-response, receptor/post-receptor effects, and physiological factors that modify drug response. |
| S256 | Zhang et al., [Clinical Implications of Anatomical Variations in Nerves and Adjacent Structures for Regional Anesthesia: A Narrative Review](https://pubmed.ncbi.nlm.nih.gov/41273595/), *Pain and Therapy* 15(1), 41–69 (published online 22 November 2025; issue February 2026), DOI: 10.1007/s40122-025-00797-5 | Review of nerve, vessel, spine, and nerve-root variants relevant to ultrasound-guided regional anesthesia; describes effects on needle trajectory, local-anesthetic spread, block efficacy, and complications, while acknowledging the limited literature for some variants. |
| S257 | Folino & Mahboobi, [Regional Anesthetic Blocks](https://www.ncbi.nlm.nih.gov/books/NBK563238/), *StatPearls* (last updated 29 January 2023) | Clinical procedural reference describing anatomical landmarks and placement of local anesthetics near nerves, fascial planes, and neuraxial spaces; identifies the need for detailed anatomical knowledge, trained operators, monitoring, and complication preparedness. |
| S258 | Labban & Wu, [Regional Anesthesia: Bony Landmarks](https://www.openanesthesia.org/keywords/regional-anesthesia-bony-landmarks/) (updated 28 January 2026) | Current professional educational resource explaining that accurate bony and surface anatomy landmarks remain important for safe regional blocks; notes that ultrasound supplements rather than replaces anatomical knowledge and that landmark errors can cause block failure or neurovascular injury. |

## 6. Updated Life Sciences ↔ Health Sciences accounting

| Measure | Count |
|---|---:|
| Total possible cross-domain subject pairs | 270 |
| Unique pairs screened through v0.19.0 | 113 |
| New unique pairs screened in v0.20.0 | 3 |
| **Cumulative unique pairs screened** | **116 of 270** |
| Candidate recommendations before this batch | 101 |
| New candidate recommendations in this batch | 3 |
| **Cumulative candidate RD-P recommendations** | **104** |
| Cumulative screened but not promoted / deferred | 12 |
| **Pairs still individually unassessed** | **154** |
| **Screening coverage** | **42.96%** |

Accounting check:

`270 = 104 candidates + 12 not promoted/deferred + 154 unassessed`

The 12 prior non-promotions/deferred remain unchanged. This batch adds three candidate recommendations and no new non-promotions. Candidate status does not imply owner acceptance or canonical registration.

## 7. Canonical status and governance

- Canonical taxonomy remains **v1.13.1**.
- The canonical taxonomy blob SHA remains `f054a687bb649f8e67982a607b59a5156e8e9a46`.
- The 18 canonical RD-P proposals remain unchanged.
- Canonical hierarchy-edge, RD-P, and source-unlinked sparse-matrix counts remain **252 / 18 / 34,446**.
- The three recommendations in this report have **not** been inserted into the canonical taxonomy.
- Owner-accepted relationships remain **zero**.
- No dependency, enablement, hierarchy reassignment, implementation, testing, or verification is inferred from these relationship assessments.
- The six existing proposals **RD-013 through RD-018** remain a separate workstream and are not assessed or altered by this report.
- Candidate recommendations remain supplemental evidence-review records pending explicit owner review.

## 8. Next work

Continue with another non-duplicative topic-focused group from the 154 remaining Life Sciences ↔ Health Sciences pairs. Select the next subgroup only after checking every proposed unordered pair against the complete assessment ledger and confirming canonical subject IDs.

The separate RD-013–RD-018 proposal-assessment workstream remains open and is not folded into the 270-pair Life Sciences ↔ Health Sciences screening count.

**Review condition before any canonical insertion:** verify unordered-pair uniqueness, stable identifiers, relationship subtype, direction, evidence provenance, scope boundary, sparse-matrix effect, and explicit owner acceptance.
