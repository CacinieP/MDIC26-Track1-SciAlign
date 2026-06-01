# Resistance to neoadjuvant talazoparib in triple-negative breast cancer by BRN2-induced ATR/STAT3 pathways or SHLD2 subclone expansion

Noor M. Abdulkareema,1 , Yan Jianga,1 , Yuan Qia,b , Xuan Liuc , Xiaomei Zhanga , Shirong Caia , Jiansu Shaoa , Sabrina Jeter-Jonesa , Amanda L. Rinkenbaugha , Chun-Chun Chenga , Faiza Hancocka , Jill Schwartzd , Jennifer K. Littond , Jeffrey T. Changb,c,2 , and Helen Piwnica-Wormsa,2

Affiliations are included on p. 11.

This contribution is part of the special series of Inaugural Articles by members of the National Academy of Sciences elected in 2023. Contributed by Helen Piwnica-Worms; received June 3, 2025; accepted March 13, 2026; reviewed by Laura M. Heiser and Lee Zou

Intrinsic and acquired resistance to poly(ADP-ribose) polymerase (PARP) inhibitors (PARPi) remains a major barrier in treating homologous recombination (HR) repair-deficient tumors, including those with germline or somatic BRCA1/2 mutations. Although PARPi are FDA approved for adjuvant treatment of locally advanced or metastatic breast cancer in patients with germline BRCA1/2 mutations, emerging data support their use as monotherapy in the neoadjuvant setting. Promising safety profiles of newer-generation PARPi further support this potential. However, resistance mechanisms specific to the neoadjuvant setting are poorly understood. To address this gap, we leveraged resources from a phase II neoadjuvant clinical trial (NCT03499353), analyzing tumors from patients with germline BRCA1/2 mutant breast tumors before and after six months of talazoparib monotherapy. Whole-transcriptome analyses were performed on these samples. Additionally, we established orthotopic patient-derived xenograft models from a subset of the patient tumors and conducted whole-exome and whole-transcriptome analysis. This integrative approach revealed both known and previously unknown PARPi resistance mechanisms. In one case, overexpression of BRN2, encoding a transcription factor that plays a critical role in neurogenesis, led to activation of ATR/RAD51 and STAT3 pathways, restoring HR repair. BRN2-driven resistance could be reversed with ATR and STAT3 inhibitors, resensitizing cells to talazoparib. In another, an HR repair proficient tumor subclone lacking Shieldin 2 expression expanded during treatment and accounted for intrinsic resistance. Our findings highlight the need to determine intrinsic and anticipate acquired resistance pathways in treatment-naïve tumors and support combining PARPi with targeted agents to improve outcomes in the neoadjuvant setting.

triple-negative breast cancer | PARP inhibitor | BRN2 | SHLD2 | PDX models

BRCA1/2 deficient tumors cannot perform homologous recombination (HR) repair efficiently and instead rely on lower fidelity mechanisms of DNA double-strand break (DSB) repair, such as classical Non-Homologous End Joining (c-NHEJ) (1). The seminal discoveries demonstrating that BRCA1/2 deficiency sensitizes cancer cells to poly(ADP-ribose) polymerase (PARP) inhibition led to the development of PARP inhibitors (PARPi) as targeted therapies for BRCA1/2 deficient cancers (2, 3). The therapeutic application of PARPi was subsequently expanded for treating non- BRCA1/2 mutant tumors exhibiting defects in HR repair, including ovarian, breast, prostate, and pancreatic cancers (4).

PARPi target PARP proteins (predominantly PARP1 and PARP2), which are enzymes that catalyze the formation of poly(ADPribose) chains in response to genotoxic stress. This posttranslational modification serves to recruit DNA repair proteins to the site of damage and ultimately to release PARP1/2 from the damage site (5, 6). PARPi not only inhibit the enzymatic activity of PARP1/2 but also trap PARP on the DNA, creating lesions that are repairable by HR in normal but not in BRCA1/2-deficient cells (7). The inability of PARP1/2 to dissociate from sites of DNA damage, due to PARPi trapping, results in replication fork collapse and DNA DSBs. This is particularly true in talazoparib-treated HR-repair-deficient cells, where trapping activity is high (8). Given that cells with defective BRCA1/2 cannot perform HR repair efficiently, they rely on lower fidelity mechanisms of DSB repair, such as c-NHEJ, which results in additional genotoxic stress and ultimately cell death (1). Along with their role in HR repair, BRCA1/2 also function to protect stalled replication forks, thereby preserving genome stability. Recent

## Significance

Improved safety profiles of newer generation selective poly(ADPribose) polymerase inhibitors support their expanded use in the neoadjuvant setting. To optimize clinical benefit, it is critical to identify resistance mechanisms to predict nonresponders and adjust therapies when resistance emerges. To address this, we analyzed tumors from patients with triple-negative breast cancer (TNBC) with germline BRCA1 /2 mutations, collected before and after six months of neoadjuvant talazoparib monotherapy, and corresponding patient-derived xenografts. Two resistance mechanisms restoring homologous recombination repair were identified: BRN2 overexpression, which activated downstream ATR/RAD51 and STAT3 signaling, and expansion of a Shieldin 2-deficient subclone under treatment pressure. Targeting ATR or STAT3 sensitized BRN2-driven resistance to talazoparib, offering potential strategies for overcoming resistance in BRN2-high TNBC.

studies indicate that PARPi sensitivity of BRCA1/2-deficient cells correlates with the extent of replication gap formation (9).

Unfortunately, both intrinsic and acquired mechanisms of PARPi resistance are commonly encountered in BRCA1/2-deficient tumors, generally leading to restoration of HR repair through BRCA1/2-dependent or -independent mechanisms and/or by stabilization of replication forks (5, 10, 11). Our current understanding of how a patient’s tumor becomes resistant to PARP1/2 inhibition derives from clinical trials where the number of tumors interrogated is small, and it is important to note that the patients on these trials had recurrence or metastasis at the time of PARPi therapy and had undergone extensive treatment prior to receiving the PARPi (12). Thus, the ability to assign a resistance mechanism specifically to the PARPi was confounded because the tumors were subjected to selective pressure from several therapies, some of which have resistance mechanisms that overlap with those of PARPi (13–15). Across several clinical cases, restoration of BRCA function was found to be the most common mechanism of PARPi resistance (16–23).

The mechanisms by which tumors from patients with triple-negative breast cancer (TNBC) resist cell killing by PARPi monotherapy in the neoadjuvant setting have yet to be elucidated and functionally validated. To address this knowledge gap, we analyzed tumor tissue from patients with germline BRCA1/2 mutant breast cancer before and after a six-month course of PARPi (talazoparib) monotherapy, as part of a phase II neoadjuvant clinical trial (NCT03499353) conducted at MD Anderson Cancer Center (24). Here, patient tumors, corresponding patient-derived xenograft (PDX) models, and TNBC cell lines were evaluated to identify mechanisms of resistance to PARPi monotherapy without the confounding effects of additional therapies. Restoration of BRCA function was not identified as a PARPi resistance mechanism in these tumors.

## Results

High BRN2 Expression is Linked to Talazoparib Resistance and Poor Overall Survival in Patients With Breast Cancer. We interrogated the transcriptomes of tumors obtained from patients with breast cancer who had a germline BRCA1/2 pathogenic mutation enrolled in a phase II clinical trial (NCT03499353) of neoadjuvant single-agent talazoparib (24). The objective of the trial was to evaluate the pathologic response and toxicity of singleagent talazoparib in 20 patients with stage I to III breast cancer who were germline BRCA1/2-positive before definitive surgery. Upon enrollment, patients provided pretreatment biopsies for genomic and transcriptomic characterization, then began a sixmonth course of daily talazoparib, followed by a posttreatment biopsy and surgery where residual cancer burden (RCB) (25) was determined (Fig. 1A). We successfully obtained high-quality DNA and RNA from pretreated tumors in 13 patients, including six who were resistant to talazoparib and seven who were sensitive (26).

To predict genes that may confer PARPi resistance in individual patient tumors, we compared the expression of genes in seven sensitive patient tumors against each of the six resistant ones, individually. Because we did not expect the resistance mechanisms to be highly recurrent, this outlier analysis was designed to identify a mechanism that may be active in only one tumor. To do that, we looked for genes that had high expression in a resistant tumor (|Z| ≥ 3) and low expression in all sensitive tumors (Fig. 1B). This analysis identified BRN2 , a gene encoding a POU-domain containing transcription factor that plays a critical role in neurogenesis. BRN2 expression was low in the majority (11/13) of germline BRCA mutant breast tumors. However, two patient tumors, 18 and 31, had expression significantly higher than the average expression of the sensitive tumors, demonstrating a correlation between high BRN2 expression and PARPi resistance (Fig. 1B). Next, we mined The Cancer Genome Atlas (TCGA) data and found that the survival of patients with high BRN2 expressing breast cancer was significantly worse than those with low BRN2 tumor expressing breast cancer (Fig. 1C) (27). These findings underscore the need to understand the process associated with or driven by BRN2 in breast cancer.

A  
<!-- image-->  
B

C  
<!-- image-->

<!-- image-->

D  
<!-- image-->  
E

<!-- image-->  
Fig. 1.   Elevated BRN2 expression is associated with talazoparib resistance and decreased overall survival in breast cancer patients. (A) Twenty patients with germline BRCA1/2 mutations were enrolled in a neoadjuvant clinical trial and treated with single-agent talazoparib. Tumor biopsies were collected at baseline (pretreatment) and at surgery following 6 mo of therapy. PDX models were successfully established from six baseline and two posttreatment tumor samples. (B) Histogram showing the distribution of BRN2 expression (log2-transformed TPM values; each unit corresponds to a twofold change in expression) in tumors classified as either sensitive (black) or resistant (red) to talazoparib. The two resistant tumors with high BRN2 expression are indicated. (C) Kaplan–Meier survival analysis of breast cancer patients from TCGA, stratified into high- and low-BRN2 expression cohorts. The percentage of patients surviving (y-axis) is plotted over time in months (x-axis). (D) Drug sensitivity data from the Genomics of Drug Sensitivity in Cancer database were analyzed in cell lines stratified by BRN2 expression level. (E) Sensitivity to talazoparib (y-axis) is shown for individual cell lines grouped by BRN2 expression. Each point represents a single cell line. Statistical significance was determined using an unpaired two-tailed Student’s t test with Welch’s correction (P < 0.05).

BRN2 has been shown to contribute to the aggressiveness of tumors with neural or neuroendocrine origins, including glioblastoma, neuroblastoma, small cell lung cancer, and neuroendocrine prostate cancer (28, 29). BRN2 remains understudied in breast cancer. Given our results and the fact that BRN2 levels influence how melanoma responds to both chemotherapy and targeted therapy, with higher BRN2 expression correlating with drug resistance (30), we examined drug screening data from the Genomics of

Drug Sensitivity in Cancer database (31) to look for associations between BRN2 expression and PARPi resistance. We focused on the BRCA1/2 mutant cell lines, and since BRN2 is normally expressed in the neural lineage, we excluded cell lines derived from neuroblastomas, glioblastomas, or low-grade gliomas. Among the remaining 114 cell lines, we found that cells with the highest expression of BRN2 were significantly associated with resistance to talazoparib (Fig. 1 D and E). In contrast, the expression of GAPDH, a negative control, was not associated with talazoparib sensitivity (SI Appendix, Fig. S1 A and B).

Generation of PDX Models. To investigate the contribution of BRN2 to PARPi resistance and to get around the limitations associated with working with small amounts of patient tumor tissue, we established a collection of orthotopic PDX models from a subset of the tumors obtained from patients enrolled in the clinical trial. Biopsies were obtained from patients prior to treatment with talazoparib and following a 6-mo course of talazoparib, if there was residual disease at the time of surgery (Fig.  1A). In total, the collection includes eight PDX models from the tumors of six patients, including two pairs of matched treatment-naïve (baseline) and residual disease (surgical) tumors, plus an additional four from treatment-naïve tumors. All PDX models were derived from triple-negative breast tumors, and all retained the deleterious mutations in both BRCA1 (germline) and TP53 (somatic) identified in the corresponding patient samples (SI Appendix, Table S1). PDX tumors were subjected to wholeexome sequencing (WES) and bulk RNA sequencing (RNAseq) to determine how closely their genomes and transcriptomes resembled those of their corresponding patient tumors. WES and RNA-seq profiling data from cognate patient tumors were only available for four of the PDX models (26). This included baseline tumors from patients used to establish PDX16_B, PDX17_B, PDX34_B, and PDX18_B (SI Appendix, Table S1). Molecular profiles could not be obtained from the other four patient tumors due to poor-quality samples, low quantity of material, or low tumor cellularity. WES and RNA-seq profiling data were used to compare patient and PDX transcriptomes, classify tumors according to the Vanderbilt subtyping system (32), and assess copy number alterations using Pearson correlation. Results showed concordance between patient and PDX tumors in these characteristics (SI Appendix, Fig. S2 A and B and Table S2).

Genomic Profiling of PDX Tumors. Next, WES data were analyzed to identify recurrent, nonsynonymous somatic mutations in PDX tumors and corresponding patient tumors where WES data was available. We verified that the BRCA1 mutations seen in the WES and RNA-Seq data matched those previously identified by Myriad BRACAnalysis (SI Appendix, Table S3). All tumors derived from the same patient exhibited the same BRCA1 mutation, indicating that the mutation was preserved during the engraftment process. However, in each PDX model, except for those established from patient 27, the mutant allele was enriched relative to the patient tumor and very few sequencing reads from the wild-type allele were observed. Fifty-one genes were found to be recurrently mutated in the PDX collection, with TP53 mutations being present in all eight PDX tumors (SI  Appendix, Fig.  S3A). All patient TP53 mutations were conserved in their respective PDX models (SI  Appendix, Table  S1), and all were reported to be deleterious in the literature (SI Appendix, Table S4). In addition to the TP53 mutations, there were four additional genes, reported in the COSMIC database (33), with recurrent mutations: (FGFR1, NCOA2, PIK3CA, and PLCG1) (SI Appendix, Fig. S3A). While

PIK3CA mutations have been implicated in PARPi resistance (34, 35), here the PIK3CA mutations were present only in talazoparibsensitive models (PDX18_B1, PDX20_B1, and PDX20_B2) (SI  Appendix, Fig.  S3A). Few mutations with known roles in PARPi resistance arose in our resistant models, suggesting that the acquisition of new genomic mutations likely did not account for talazoparib resistance in our models. Additionally, we looked specifically for genomic alterations in a subset of genes implicated in PARPi resistance in clinical samples and preclinical models (26). All PDX tumors, except for PDX17_B, had mutations and/or copy number alterations in a subset of these genes (SI Appendix, Fig. S3B).

Sensitivity of PDX Tumors to Talazoparib In  Vivo. We next conducted preclinical studies to evaluate the sensitivity of each PDX model to talazoparib (Fig.  2A). In the original Phase II clinical trial, residual cancer burden (RCB) (25) was assessed at the time of surgery following 6 m of neoadjuvant talazoparib treatment. Patients achieving either a pathologic complete response (pCR) or classified as RCB-I were considered sensitive to talazoparib, whereas those classified as RCB-II or RCB-III were deemed resistant (24). Based on this criterion, three of the six patient tumors used to generate the PDX models were classified as sensitive (patients 16,17, and 20) while the remaining three were resistant (patients 18, 27, and 34) (SI Appendix, Table S1). In preclinical studies, tumors derived from treatment-naïve patient samples either regressed (16_B, 17_B, 20_B, 27-B, 34_B) or remained fairly stable (18_B) on therapy (Fig. 2A). In contrast, PDX tumors established from posttreatment surgical samples (18_S and 27_S) continued to grow on treatment, indicating resistance to talazoparib (Fig.  2A). These findings demonstrate that resistance observed in patient tumors following treatment was preserved in the corresponding PDX models. Furthermore, the PDX responses generally mirrored the clinical responses of the original patient tumors- except for PDX34_B which responded to therapy despite being derived from a tumor clinically classified as resistant (RCB-II).

High BRN2 levels Correlate With PARPi Resistance. Given that the acquisition of new genomic mutations was not an obvious cause of talazoparib resistance in our models, but that high BRN2 expression correlated with talazoparib resistance and poor overall survival in patients with breast cancer (Fig. 1 B and C), we assessed BRN2 protein levels in control cell lines (Fig. 2 B and C) and in our panel of PDX tumors using immunohistochemistry (IHC). BRN2 was undetectable in PARPi-sensitive PDX models, including PDX16_B, PDX17_B, PDX20_B, and PDX34_B (Fig.  2 D–G). By contrast, BRN2 was detected in PDX tumors derived from PARPi-resistant patients, including PDX27 and PDX18 (SI  Appendix, Table  S1). In PDX27_B, BRN2 was observed but exhibited a focal rather than uniform distribution within the tumor (Fig.  2H). Notably, BRN2 was absent in PDX27_S, the posttreatment surgical specimen (Fig. 2I). BRN2 was readily detected in the PDX tumor derived from patient 18 (Fig.  2 J and K), whose primary tumors exhibited high expression of BRN2 (Fig. 1B) and was clinically resistant to talazoparib (RCB-III; SI Appendix, Table S1). BRN2 was evident in the corresponding baseline PDX tumor (Fig. 2 J and L) and further enriched in the surgical tumor (Fig. 2 K and L). Preclinical studies in mice demonstrated that PDX18_B tumors remained static during treatment, whereas PDX18_S tumors continued to grow, confirming resistance to talazoparib (Fig. 2A). Collectively, these findings suggest that BRN2 may potentially mediate PARPi resistance in PDX18_S. Like the tumor from patient 18, the tumor from patient 31 also exhibited resistance to talazoparib (RCB-II) and high BRN2 expression (Fig. 1B). Unfortunately, we were unable to establish a PDX model from this patient’s tumor. Consequently, BRN2 functional studies were carried out using the PDX18 model and established TNBC cell lines.

A  
<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

B  
<!-- image-->

C  
<!-- image-->

D  
<!-- image-->

E  
<!-- image-->

F  
<!-- image-->

G  
<!-- image-->

<!-- image-->

<!-- image-->

J  
<!-- image-->

K  
<!-- image-->  
L

<!-- image-->  
Fig. 2.   Talazoparib response and BRN2 expression in PDX models. (A) Preclinical evaluation of talazoparib sensitivity in PDX models. Tumor cells were orthotopically engrafted into immunodeficient mice. Upon reaching \~150 mm3 , mice were randomized to receive either vehicle control or talazoparib (0.165 mg/kg), administered daily via oral gavage. Tumor volumes were measured biweekly using calipers, and calculated values are presented as mean ± SEM (n > 3 per group). (B–K) BRN2 protein expression was assessed by IHC. Representative IHC images are shown for: (B) U2OS (osteosarcoma, negative control), (C) A375 (melanoma, positive control), and PDX tumor samples (D) PDX16_B, (E) PDX17_B, (F) PDX20_B, (G) PDX34_B, (H) PDX27_B, (I) PDX27_S, (J) PDX18_B, and (K) PDX18_S. (Scale bar, 100 μm.) (L) Quantification of BRN2 staining by IHC in paired PDX18_B vs. PDX18_S tumors. \*P < 0.05 by unpaired two-tailed Student’s t test (n = 6), indicating a statistically significant difference.

Effects of BRN2 Knockdown and Overproduction On Talazoparib Response in PDX Tumor Cells and Established TNBC Cell Lines. Next, we asked if high BRN2 expression causally mediates PARPi resistance. To do this, we generated PDX-derived organoid cultures from PDX18_B and $\mathrm { P D X 1 8 \_ S } \left( \mathrm { F i g . 3 } A \right)$ . We first tested the talazoparib response in the organoid models, and as expected, PDX18_S showed increased talazoparib resistance (IC50 = 142.1 nM) compared to PDX18_B (IC50 = 50.23 nM) (Fig. 3B). We then used shRNA knockdown to reduce BRN2 levels in PDX18_S organoid cells. BRN2 knockdown increased the sensitivity of PDX18_S tumor cells to talazoparib (Fig. 3 C and D). We also overproduced BRN2 in two breast cancer cell lines, one that is BRCA1 wild-type (MDA-MB-231) and one that is BRCA1 mutant (SUM-149). In both cell lines, BRN2 overproduction decreased talazoparib sensitivity relative to control cells (Fig.  3 E and F). These results indicate that BRN2 has a causal role in conferring PARPi resistance and that its activity is not restricted to BRCA1 mutant breast cancer.

<!-- image-->  
B

<!-- image-->

<!-- image-->  
C

D  
<!-- image-->

<!-- image-->  
E

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 3.   BRN2 modulation alters talazoparib sensitivity in PDX-derived organoids and TNBC cell lines. (A) Schematic illustration of the generation of 3D organoid cultures from PDX tumors. Image created in BioRender (https://BioRender.com/rrx2xvs). (B) Representative bright-field images of organoid cultures derived from PDX18_B and PDX18_S. (Scale bar, 200 μm.) Organoids were treated with vehicle or varying concentrations of talazoparib for 14 d. Cell viability was assessed using the CellTiter-Glo 3D assay, and percent viability is shown relative to vehicle-treated controls. Error bars represent SEM from triplicate measurements, $n = { \bar { 3 } } . ( C )$ Western blot confirmation of BRN2 knockdown in PDX18_S organoid cells transduced with nontargeting or 2 different BRN2-targeting $\mathsf { s h R N A s } , n = 2 .$ (D) Organoids from panel C were treated with talazoparib for 14 d, and cell viability was measured using the CellTiter-Glo 3D assay. The graph shows percent viability relative to vehicle-treated control cells. Error bars represent SEM from triplicate measurements, $n = 3 .$ BRN2 overproduction in (E) SUM149 (BRCA1 mutant) and (F) MDA-MB-231 (BRCA1 wild-type) cells was confirmed by western blotting, n = 3. Cells were treated with vehicle or talazoparib for 14 d, and drug sensitivity was evaluated by clonogenic assay. Fixed colonies were stained with crystal violet; representative images are shown. Bars represent mean ± SEM $( n = 6 ) . { \star \check { P } } < 0 . 0 5$ by unpaired two-tailed Student’s t test.

Regulation of Stemness and STAT3 Activation by BRN2. To identify potential BRN2 targets relevant to PARPi resistance, we queried the publicly available TFLink database (36), which contains experimentally validated transcription factor-target gene interactions. Notably, ALDH1A1 and EpCAM, well-established breast cancer stem cells (CSCs) markers, and STAT3 were identified as direct BRN2 targets (SI  Appendix, Table  S5). Additionally, CD44, another key CSC marker, is transcriptionally regulated by STAT3, and STAT3 itself has been reported to regulate BRN2 expression, suggesting a possible feedback loop (36). Given the known association between stemness and drug resistance, including resistance to PARPi (37–39), we examined stemnessrelated gene expression in our RNAseq dataset. PDX18_S (PARPresistant) tumors exhibited elevated expression of stemness markers compared to PARPi-sensitive PDX18_B tumors (SI  Appendix, Fig.  S4). Consistent with transcriptomic data, protein levels of ALDH1A1, CD44, total STAT3, and pSTAT3 (Y705) were all increased in PDX18_S tumor cells relative to PDX18_B (Fig. 4A). Importantly, BRN2 knockdown in PDX18_S organoids reduced levels of ALDH1A1, CD44, and pSTAT3 (Y705), supporting a functional link (SI  Appendix, Fig.  S5). CD44 exhibits a broad molecular weight range, from 80 kDa to over 250 kDa, due to alternative splicing and extensive glycosylation. The standard isoform migrates at approximately 89 to 90 KDa, whereas the higher molecular weight variant isoforms can range from 150 kDa to 250 kDa. The standard isoform is the predominant isoform in PDX tumors propagated in mice (Fig. 4 A and C). Interestingly, the variant isoforms become enriched when PDX tumors are propagated as organoid cultures in vitro (SI Appendix, Fig. S5).

Flow cytometry analysis further confirmed an enrichment of ALDH+ and CD44high/CD24low CSC populations in PDX18_S relative to PDX18_B (Fig. 4B). Ectopic overproduction of BRN2 in SUM-149 and MDA-MB-231 TNBC cell lines led to increased levels of pSTAT3 (Y705) and CD44 (SI Appendix, Fig. S6A), as well as enhanced secondary mammosphere formation, a functional readout of stemness (SI Appendix, Fig. S6B). To investigate whether BRN2-mediated STAT3 activation is enriched in CSCs, we sorted CD44-/lo w and CD44high cell populations from PDX18_S cells using fluorescence-activated cell sorting. Due to the low percentage of ALDH+ cells, we were unable to isolate enough of these cells for further analysis. Western blotting of sorted populations revealed that BRN2, total STAT3, and pSTAT3 (Y705) levels were markedly higher in CD44high cells relative to CD44low cells (Fig. 4C), suggesting a preferential activation of the BRN2– STAT3 axis in CSCs. Pharmacologic inhibition of STAT3 using TT1-101 (40) sensitized PDX18_S cells to talazoparib. Combining TTI-101 with talazoparib resulted in a synergistic reduction in cell viability, as indicated by combination index (CI) (41) values below one across a broad range of concentrations (Fig. 4D) and a significant reduction in levels of CD44 were observed in cells treated with the combination of PARP and STAT3 inhibitors (Fig. 4E). Finally, TT1-101 treatment decreased BRN2 protein levels, validating the role of STAT3 in regulating BRN2 expression (Fig. 4F and SI Appendix, Table S5). Collectively, these findings suggest that high BRN2 expression promotes stem-like features via STAT3. Targeting STAT3 in combination with PARP inhibition may offer a therapeutic strategy in BRN2-high TNBC.

The ATR/RAD51 Pathway Contributes to PAPPi Resistance in BRN2-High TNBC Cells. Data mining from the TFLink database (36) also revealed several key components of the ATR pathway as direct BRN2 targets, including ATR itself, as well as PALB2, XRCC2, XRCC3, and RAD51 (SI Appendix, Table S5). Previous studies have shown that the ATR/RAD51 pathway plays a critical role in regulating HR repair and replication fork protection in PARPi-resistant BRCA1 mutant cells (Fig. 5A) (42). Consistent with these findings, we observed elevated expression of ATR/ RAD51 pathway components in PDX18_S relative to PDX18_B tumors (Fig.  5B), as well as in SUM-149 and MDA-MB-231 cells engineered to overproduce BRN2 (SI Appendix, Fig. S6A). Conversely, BRN2 knockdown in PDX18_S organoid cells led to reduced expression of pATR (ser428) and total ATR, further supporting a regulatory relationship (SI Appendix, Fig. S5). BRN2 knockdown or overproduction in MDA-MB-436 cells did not significantly alter cell cycle distribution (SI  Appendix, Fig.  S7) indicating that the observed alterations in ATR and RAD51 expression are unlikely to be secondary to cell cycle effects.

Protein analysis of CD44high cells isolated from PDX18_S tumors showed enrichment of ATR/RAD51 pathway proteins, including pATR (ser428), total ATR, XRCC2, XRCC3, and RAD51 relative to CD44low cells (Fig. 5C). In line with restored HR repair capacity, a greater proportion of S/G2 phase cells displayed RAD51 foci in irradiated PDX18_S cells compared to irradiated PDX18_B cells (Fig. 5D).

Pharmacological inhibition of ATR using VE-822 (43) sensitized PDX18_S tumor cells to talazoparib with most CI values near 1, across a wide concentration range, indicating an additive effect of the two drugs (Fig. 5E). Similarly, in colonogenic assays, VE-822 enhanced the sensitivity of BRN2-overproducing SUM-149 and MDA-MB-231 cells to talazoparib (SI Appendix, Fig. S6C). Target engagement of the ATR pathway was confirmed by a reduction in pChk1 (ser345) levels following VE-822 treatment (Fig. 5F). VE-822 treatment significantly reduced the percentage of RAD51/geminin-positive cells, indicating ATR inhibition induced HR repair deficiency to restore PARPi sensitivity (Fig. 5G). Collectively, these results suggest that CD44high cells with elevated BRN2 may depend on the ATR/RAD51 pathway for restoring HR repair and conferring PARPi resistance. Thus, cotargeting PARP and the ATR/RAD51 pathway may present a viable strategy to overcome resistance in BRN2-high TNBC.

Intrinsic Resistance in PDX27 Due to Expansion of a Tumor Subclone Lacking Shieldin 2 (SHLD2) Expression. In addition to patient 18, we established longitudinal PDX models from the breast tumor of patient 27, both before (PDX27_B) and after (PDX27_S) talazoparib treatment. PDX27_B tumors remained fairly static on talazoparib treatment, while PDX27_S tumors exhibited resistance (Fig. 2A). Since BRN2 was not detected in the posttreatment surgical sample (Fig. 2I), we looked for other mechanisms of PARPi resistance. As restoration of HR repair is one of the most common mechanisms of PARPi resistance (44), we assessed the longitudinal models for mutational signature 3, a robust biomarker of HR deficiency (45, 46). PDX27_S showed a reduced signature 3 score compared to PDX27_B, suggesting an increase in HR repair capacity in PDX27_S (Fig. 6 A and B).

In addition to a reduction in HR deficiency, large-scale structural chromosomal aberrations, as measured by large-scale state transitions (47, 48) and the weighted genome instability index (49), were also reduced in PDX27_S (Fig. 6 C and D). These results indicate less genome instability in PDX27_S relative to PDX27_B. As we did not identify any genomic alteration that would have restored HR repair in PDX27_S, we used Pyclone (50) to investigate the subclonal architecture of PDX27_B and PDX27_S. Indeed, we observed enrichment of a subclone in PDX27_S, suggesting resistance arose from clonal expansion (Fig. 6E). To characterize the subclone features contributing to the PARPi resistance, we looked specifically for alterations in a subset of 52 genes implicated in PARPi resistance. Comparison of PDX27_S to PDX27_B revealed a greater than 30-fold decrease in SHLD2 expression in PDX27_S (Fig. 6F), which was accompanied by copy number loss of SHLD2 in PDX27_S (SI Appendix, Fig. S3). The decrease of SHLD2 mRNA was validated by quantitative PCR (qPCR) (Fig. 6G). Loss of SHLD2 is known to restore end resection to facilitate HR repair, leading to PARPi resistance (4, 51, 52). Taken together, these results suggest that a minor SHLD2-deficient subclone in PDX27_B expanded under treatment pressure, thereby driving talazoparib resistance.

A  
<!-- image-->

B  
<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

C  
<!-- image-->

D  
<!-- image-->

E  
<!-- image-->

<!-- image-->

F  
<!-- image-->  
Fig. 4.   BRN2 regulates stemness features and STAT3 in PDX tumor cells. (A) Representative western blot of BRN2, pSTAT(Y705), total STAT3, and stemnessassociated markers ALDH1A1 and CD44 in PDX18_B and PDX18_S tumor cells. Proteins were quantified using ImageJ, and values were normalized to GAPDH. Fold change was calculated relative to PDX18_B. For pSTAT3, the ratio of phospho to total protein was calculated after normalization to GAPDH. Bars represent mean ± SEM $( n = 3 ) .$ . \*Indicates statistically significant difference compared to PDX18_B; $\dot { P } < 0 . 0 5$ by unpaired two-tailed Student’s t test. (B) Flow cytometric analysis of cancer stem cell markers in PDX18_B and PDX18_S tumor cells stained with antibodies against CD44, CD24, and ALDH. The percentage of markerdefined cell populations is shown. Bars represent mean ± ${ \mathsf { S E M } } ( n \geq 3 ) . { \star P } < 0 . 0 5$ by unpaired two-tailed Student’s t test. (C) Fluorescence-activated cell sorting (FACS) of PDX18_S tumor cells stained with CD44 (APC) and CD24 (PE) antibodies. $C D 4 4 ^ { 1 0 \mathsf { w } / - }$ and $C D 4 4 ^ { \mathrm { { h i g h } } }$ subpopulations were isolated. Western blotting was performed on lysates from bulk tumor cells (presort), $\mathsf { C D 4 4 ^ { \vert \circ w / - } }$ , and $C D 4 4 ^ { \mathsf { h i g h } }$ populations to assess expression of the indicated proteins. (D) Cell viability assay ${ \tt O P D } \times 1 8 \_ S$ organoid cultures treated with talazoparib alone, the STAT3 inhibitor TTI-101 (300 nM) alone, or the two together for 14 d. Error bars represent SEM for triplicate measurements, $n = 3$ . Combination index (CI) values were calculated using CompuSyn software: $\mathsf { C l } < \mathsf { \Omega }$ indicates synergy; $\mathsf { C l } = \mathsf { 1 }$ indicates an additive effect. (E) Quantification of western blot of cell lysates from PDX18_S organoids treated with vehicle or talazoparib and TTI-101 for 7 d. Bars represent mean ± SEM $( n = 3$ to 4). \*Indicates statistically significant difference compared to vehicle; $P < 0 . 0 5$ by unpaired two-tailed Student’s t test. Proteins were quantified using ImageJ, and the values were normalized first to GAPDH and then to the vehicle control. (F) Lysates from $\mathsf { P D X 1 8 } \_ S$ organoids treated with vehicle, talazoparib, TTI-101, or both talazoparib and TTI-101 for 7 d were also probed for the indicated proteins.

<!-- image-->  
B

<!-- image-->

<!-- image-->

D  
<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
G

<!-- image-->

<!-- image-->  
Fig. 5.   The ATR/RAD51 pathway mediates PARP inhibitor resistance in BRN2-high TNBC cells. (A) Schematic model illustrating how activation of the ATR/RAD51 pathway promotes replication fork protection and homologous recombination (HR) repair, contributing to resistance to PARP inhibition (PARPi). Figure created with BioRender (https://BioRender.com/ t4om5vl). (B) Western blot analysis of ATR pathway proteins in PDX18_B and PDX18_S tumor cells. Proteins were quantified using ImageJ, and values were normalized to Vinculin. Fold change was calculated relative to PDX18_B. For pATR, the ratio of phospho to total protein was calculated after normalization to Vinculin. Bars represent mean ± SEM $( n = 3 ) . \star P < 0 . 0 5$ by unpaired two-tailed Student’s t test compared to PDX18_B. (C) FACS-based separation of CD44low/− and CD44high subpopulations from PDX18_S tumor cells stained with CD44 (APC) and CD24 (PE) antibodies. Western blotting was performed on lysates from presorted, $C D 4 4 ^ { \vert \mathrm { o w } / - }$ , and $C D 4 4 ^ { \mathrm { { h i g h } } }$ cells to assess the indicated protein levels. (D) Immunofluorescence staining and quantification of RAD51 nuclear foci in geminin-positive (G2/S phase) cells from PDX18_B and PDX18_S tumors. (Scale bar, 10 μm.) The percentage of RAD51+ /geminin+ cells was quantified. Bars represent mean ± SEM $( n = 3 ) .$ $^ { \star } P < 0 . 0 { \stackrel { \sim } { 5 } }$ by unpaired two-tailed Student’s t test. (E) Cell viability of PDX18_S organoid cells treated with talazoparib alone, ATR inhibitor (VE-822, 50 nM) alone, or the two together for 14 d. Error bars represent SEM for triplicate measurements, $n = 3 .$ Combination index (CI) values were calculated using CompuSyn software: $\mathsf { C l } < 1$ indicates synergy; CI = 1 indicates an additive effect. (F) Western blot analysis of total lysates from PDX18_S organoid cells treated as indicated for 7 d, probing for the indicated proteins. (G) PDX18_S organoid cells were treated with vehicle, talazoparib (50 nM, 16 h), VE-822 (50 nM, 30 min), or a combination of both. Cells were then irradiated (10 Gy) and fixed 4 h postirradiation. Representative immunofluorescence images show RAD51 (red), geminin (green), DAPI (blue), and merged channels. (Scale bar, 10 μm.) Quantification of RAD51+ /geminin+ cells is shown. Bars represent mean ± SEM (n = 3). $^ { \star } P < 0 . 0 5$ by one-way ANOVA followed by Tukey’s multiple comparisons test.

## Discussion

The clinical adoption of PARPi for adjuvant treatment of locally advanced or metastatic breast cancer in patients with germline BRCA1/2 mutations was established as the standard of care in 2018 (53). Since then, efforts to expand the clinical utility of PARPi have centered on three key areas. First, identifying sensitive patient populations beyond those with advanced germline BRCA1/2+ disease is a major focus of ongoing clinical trials. Notably, in the neoadjuvant setting, PARPi monotherapy has shown efficacy; a single-agent, targeted therapy (talazoparib) achieved pCR as first-line treatment in patients with germline BRCA1/2 mutated breast cancer, without the need for chemotherapy (24). Additionally, the SWOG S1416 trial showed clinical benefit in patients with BRCA-like molecular profiles, even in the absence of germline BRCA1/2 mutations (54). Second, the development of more effective and better-tolerated agents is underway. A next-generation, selective PARP1 inhibitor (AZD5305) has demonstrated improved safety and tolerability, along with enhanced tumor control, compared to first-generation PARP1/2 inhibitors (55, 56). Third, there remains an urgent need for strategies to identify and overcome both intrinsic and acquired mechanisms of PARPi resistance (12).

PARPi resistance has been shown to arise through restoration of HR repair and/or by stabilizing replication forks (7–9). These resistance mechanisms can be either BRCA1/2-dependent or BRCA1/2- independent. BRCA1/2-dependent mechanisms include somatic reversion or restoration of BRCA1/2 open reading frames, epigenetic reversion of BRCA1 promoter hypermethylation, and upregulation of hypomorphic BRCA1/2 alleles (22, 57). BRCA1/2-independent mechanisms include loss of factors that block end resection, including 53BP1 and components of the Shieldin complex, or through activation of microhomology-mediated end joining (52, 58–60). PARPi resistance can also result from replication fork protection by limiting excessive nucleolytic degradation at stalled replication forks (10, 11). Additional mechanisms include upregulation of the P-glycoprotein drug efflux transporter, loss of PAR glycohydrolase, and downregulation or mutation of PARP1 itself (5, 61–63). It is important to note that most of these resistance mechanisms have been identified and validated through various genetic and functional screens conducted in established cancer cell lines.

Our current understanding of PARPi resistance mechanisms in patient tumors is derived from a small number of clinical trials involving patients who had received extensive prior treatment before initiating PARPi therapy (12). As a result, attributing specific resistance mechanisms solely to PARPi exposure is challenging, since these tumors were subjected to selective pressures from multiple therapies, some of which share overlapping resistance mechanisms with PARPi (13–15). In this context, BRCA1/2 reversion mutations, which restore HR repair, have emerged as the most commonly reported mechanism of resistance (16–23).

A  
C  
<!-- image-->

<!-- image-->

B  
<!-- image-->

D  
<!-- image-->

E  
<!-- image-->

<!-- image-->  
F

<!-- image-->

<!-- image-->

<!-- image-->

G  
<!-- image-->

H  
<!-- image-->  
Fig. 6.   Intrinsic talazoparib resistance in PDX27 is driven by the expansion of a rare tumor subclone lacking SHLD2 expression. (A) Signature 3 analysis of homologous recombination deficiency (HRD) using deconstructSigs across all PDX models. PDX27 samples are highlighted with black rectangles. (B) Signature 3 analysis using SigMA across all PDX models, with PDX27 samples indicated by black rectangles. (C) Large-scale state transition analysis across all PDX models to assess genomic instability. PDX27 samples are marked with black rectangles. (D) Weighted genome instability index analysis of all PDX models, highlighting PDX27 with black rectangles. (E) PyClone analysis of clonal dynamics in PDX27 tumors. Distinct subclones are indicated by different colors. (F) Scatter plot comparing gene expression between PDX27_S and PDX27_B. Log2-transformed TPM values are plotted. Genes upregulated in PDX27_S and consistent with a talazoparib-resistant phenotype are shown in green; those inconsistent with resistance are shown in red; others are shown in gray. Genes with matching copy number and expression changes consistent with resistance are circled in red. SHLD2 is highlighted with a black rectangle. (G) Quantification of human SHLD2 mRNA in PDX27_B and PDX27_S tumors by qPCR (n = 4 for PDX27_B, n = 2 detectable samples for PDX27_S). \*P < 0.05 by unpaired two-tailed Student’s t test. (H) Model illustrating two distinct mechanisms of PARPi resistance in the neoadjuvant setting: i) a BRN2-driven mechanism involving activation of STAT3 and ATR/RAD51 pathways, resulting in HR repair restoration and PARPi resistance, and ii) expansion of a subclone with SHLD2 loss leading to restored HR repair and PARPi resistance. Figure created with BioRender (https://BioRender.com/2uc1jso).

Resistance mechanisms specific to the neoadjuvant setting of PARPi monotherapy remain poorly understood. To date, only two published clinical trials have evaluated PARPi monotherapy in the neoadjuvant setting and both trials enrolled patients with germline BRCA1/2 mutant breast tumors. The first trial was a feasibility study (64), and the second was a Phase II trial that assessed tumor response following six months of talazoparib monotherapy (24). As part of the Phase II trial, tumor biopsies collected from patients both before and after treatment were subjected to genomic and transcriptomic profiling (26) and were used to establish PDX models (this study). Importantly, these tumors offer a unique opportunity to investigate mechanisms of PARPi resistance in the absence of confounding effects from prior therapies.

In a previous study, we examined transcriptomes of pretreatment patient tumors from the phase II trial and found that those resistant to PARPi exhibited either reduced SHLD2 expression, a hypoxia-associated gene signature, or a stem-like transcriptional profile (26). However, validation of these candidate resistance mechanisms was limited by the small quantity of tumor tissue available from patients. Notably, we did not observe restoration of BRCA1/2 function or expression of ABCB1 as a mechanism of resistance in these clinical samples.

In this study, we performed outlier analysis on pretreatment breast tumors and identified BRN2 overexpression as a correlate of resistance to talazoparib. Survival analysis revealed that patients with breast cancer who have high tumor BRN2 expression had significantly worse outcomes compared to those with low BRN2 expression. Consistently, breast cancer cell lines with the highest BRN2 levels were significantly more resistant to talazoparib. Our functional studies conducted in PDX tumors from patient 18 and established TNBC cell lines suggest a causal role for BRN2 in mediating PARPi resistance. In support of this, BRN2 was undetectable in PDX tumors derived from patients classified as pCR or RCB-1, all of whom were sensitive to talazoparib, but was readily detected in the two PDX tumors derived from patients clinically classified as RCB-II (Patient 27) and RCB-III (Patient 18) both of whom were resistant to talazoparib (SI Appendix, Table S1). In PDX models derived from Patient 18, BRN2 was enriched in the posttreatment tumor compared to the pretreatment tumor, suggesting selection for BRN2 expressing cells following talazoparib exposure. Although BRN2 was detected in the pretreatment tumor in the case of PDX models established from Patient 27, it was not detected in the post treatment tumor. Our analysis indicates that, in this case, PARPi resistance was driven by the expansion of a preexisting SHLD2-deficient subclone which outcompeted BRN2-high tumor cells under selection pressure from PAPRi treatment.

While BRN2 is poorly studied in breast cancer, it is known to promote aggressiveness in tumors of neural or neuroendocrine origins (28, 29). In melanoma, BRN2 has been shown to drive migration and invasion (65–67), suppress both anoikis and apoptosis (68), and may exert noncanonical functions in DNA repair regulation (30). Higher BRN2 expression in melanoma also corresponds to drug resistance (30). Furthermore, BRN2 plays a key role in neural stem cell identity and self-renewal (69), and facilitates the conversion of nonstem glioblastoma cells into glioblastoma stem cells (70). In this study, we identified a feedback loop between BRN2 and STAT3 that promotes breast cancer stemness. Moreover, we demonstrated that BRN2 activates transcription of ATR/RAD51 pathway components, thereby restoring HR repair and leading to PARPi resistance (Fig. 6H). Importantly, targeting ATR or STAT3 sensitized BRN2-high tumors to talazoparib, highlighting potential therapeutic strategies for overcoming resistance in BRN2-high TNBC.

In support of our findings, preclinical studies have shown that inhibiting STAT3 with WP1066 restores doxorubicin sensitivity by disrupting the STAT3/OCT-4/c-Myc stemness pathway in TNBC cells (71). Furthermore, while BRCA-deficient, PARPi resistant cells rely on the ATR pathway for replication fork stabilization and HR repair (42, 72), our results showed that ATR inhibition using VE-822 sensitized both BRCA1-mutant and BRCA1-wild type TNBC cell lines to PARPi. Finally, ongoing clinical trials are evaluating combinations of PARPi with STAT3 (73) or ATR (74, 75) inhibitors, or with conventional therapies in TNBC. Some have shown promising effects in overcoming chemoresistance (73–75), supporting the translational potential of our findings in BRN2-high TNBC.

In addition to establishing serial PDX models from the baseline and surgical tumors of patient 18, we successfully generated pretreatment and posttreatment PDX models from the tumors of patient 27. Our analysis revealed that expansion of a preexisting SHLD2- deficient subclone drove PARPi resistance (Fig. 6H). SHLD2 is a component of the Shieldin complex, which functions downstream of 53BP1 to promote cNHEJ by protecting the ends of DNA-DSBs from excessive resection. In BRCA1-deficient cells, which are already impaired in HR repair, the 53BP1/Shieldin pathway restricts resection, enforcing reliance on error-prone cNHEJ. Loss of SHLD2 removes this restriction, allowing end resection to proceed and enabling partial restoration of HR repair, ultimately leading to PARPi resistance (51, 52). While we were not able to perform a comparative analysis using the patient 27 tumor, due to insufficient material, a common feature that predicted PARPi resistance in pretreatment tumors from patients enrolled in the neoadjuvant clinical trial of single-agent talazoparib was the loss of SHLD2 expression (26). These findings suggest that reduced SHLD2 expression may be a common mechanism of intrinsic resistance in BRCA-deficient breast cancers treated with neoadjuvant PARPi monotherapy and emphasize the importance of incorporating functional biomarkers like SHLD2 into future patient stratification strategies.

This study highlights clinically relevant mechanisms of PARPi resistance in the neoadjuvant setting, focusing on BRN2 overexpression and SHLD2 deficiency. These findings underscore the importance of tumor heterogeneity and clonal evolution under therapeutic pressure and provide a rationale for developing biomarkerdriven strategies to overcome resistance. The identification of the BRN2–STAT3–ATR axis as a driver of resistance reveals therapeutic vulnerabilities, offering potential avenues for combination therapies in BRN2-high TNBC.

## Materials and Methods

Collection of Patient Samples. All research performed using human patient samples followed the Health Insurance Portability and Accountability Act privacy and security rules (76) and the Common Rule (http://www.hhs.gov/ohrp/humansubjects/commonrule/). We also obtained informed consent from all patients who gave samples for establishing the PDX model. Patients were enrolled in trial NCT03499353 an MD Anderson Cancer Center IRB-approved protocol (2014-0045). Results from the trial have been published (24, 26). In brief, 20 patients diagnosed with breast cancer (stage I-III), who also had a germline BRCA1 or BRCA2 pathogenic variant, were enrolled in the study. Patients were on talazoparib alone (1 mg/day) by oral route for six months. The surgery took place within five weeks of completion of talazoparib doses. Tumor tissue obtained prior to treatment (baseline) and at the time of surgery was placed in DMEM/F12 media (HyClone, Cat. No. SH30023.01) containing antibiotics (100 units/mL penicillin, 100 µg/mL streptomycin, 0.25 µg/ mL amphotericin B) (Corning cat # MT30004CI) and was kept on ice during transport to the laboratory. In general, tumor cells were implanted orthotopically into mice within 1 to 2 h after the tumor arrived in the laboratory for processing.

Mice. All experiments were done using Female NOD/SCID mice (NOD.CB17- Prkdcscid/NcrCrl), purchased from Charles River, National Cancer Institute colony. All mouse experiments were approved by the Institutional Animal Care and Use

Committee (IACUC) at MD Anderson Cancer Center (IACUC protocol 00000978). Ends for mouse experiments were decided in agreement with IACUC-approved criteria when tumors reached 1,000 mm3 in diameter. Mice were humanely killed according to NIH and AAALAC guidelines by exposing them to carbon dioxide, followed by cervical dislocation.

PDX Establishment. PDX models were established as described previously (77, 78). Briefly, the 4th mammary fat pads (MFPs) of 4- to 5-week-old NOD/ SCID female mice were prehumanized for 3 to 4 wk with immortalized human mammary stromal fibroblasts (EG cells), labeled with green fluorescent protein (GFP), which were kindly provided by Dr. Charlotte Kupperwasser (Tufts Medical School). Patient tumor tissues were digested using complete DMEM/F12 media with collagenase (3 mg/mL) (Roche, Cat. No. 1088793) and hyaluronidase (250 U/mL) (Sigma, Cat. No. H-3506) and kept at 37 °C inside a rotator for 30 to 90 min. Samples were washed and incubated in red blood cell lysis buffer for 3 min (Sigma, Cat. No. R7757). Cell pellets were washed and kept in DMEM/ F12 with 5% bovine calf serum (BCS) and Matrigel (50/50; Corning, Cat. No. 354234) before injecting into the right 4th MFPs of humanized mice. When tumors reached \~1,000 mm3 they were collected for further passaging in new cohorts of mice. Models were considered established if they could be passaged three consecutive times in mice. All models were validated by short-tandem repeat (STR) DNA fingerprinting, qPCR, and PCR as described before (78).

RNA Extraction and Sequencing. RNA extraction and sequencing for the collected tumor samples were performed as described previously (79).

RNA-seq Data Analysis. The RNA-Seq data were processed as previously described (26). Detailed methods can be found in the SI Appendix.

Gene Expression Outlier Analysis of patient tumor samples. The mean (µ0) and SD (σ0) of each gene in patient responders were used to calculate Z scores. For each gene, Z scores were calculated by subtracting µ0 from the transcripts per million (TPM) value and dividing that result by σ0 for each sample. If a sample had a Z score greater than 3 or less than −3, it was considered to be an outlier sample. The genes with at least two outlier samples in nonresponders and no outlier samples in responders were considered candidate resistance genes. We further prioritized the candidate genes by the decreasing order of the variance of Z scores in nonresponders. The top 20 most variable candidate genes were selected.

Survival Analysis With TCGA Data. We downloaded the normalized RNA-Seq gene expression data and clinical outcomes for the TCGA BRCA dataset (80) from the Broad Firehose database. We selected the primary tumors and discretized them into BRN2-high and BRN2-low cohorts by examining the distribution of the gene expression values and identifying a natural break in the data. We then compared the overall survival of the patients with a Kaplan–Meier analysis.

Drug Sensitivity Correlations. We obtained drug screen data from the Genomics of Drug Sensitivity in Cancer database (81) and curated and harmonized the gene expression and drug sensitivity data using custom scripts. Detailed methods can be found in the SI Appendix.

DNA-seq Data Analysis. The DNA-Seq data were processed as previously described (26). Detailed methods can be found in the SI Appendix.

Genomic Analysis of HR Deficiency (HRD) and Clonal Architecture. We estimated the degree of HRD from both somatic variants and copy number changes as described previously (26). Detailed methods can be found in the SI Appendix.

Cell Lines, Antibodies, and Drugs. The detailed information for cell lines, antibodies, and drugs can be found in the SI Appendix.

Preclinical Studies to Test the Talazoparib Response. Talazoparib was freshly prepared weekly in 10% dimethyl adipimidate (ACROS Organics, Cat. No. B00M1642) and 5% Solutol HS 15 (Sigma Aldrich, cat # BCBL1570V), and 85% PBS at 0.0413 mg/mL and stored at 4 °C in the dark. The right 4th MFPs of mice were engrafted with 5 × 105 tumor cells. When tumors reached approximately \~150 mm3 , mice were randomly assigned to the indicated groups. Talazoparib solution (0.165 mg/kg) or vehicle control were administered by oral gavage daily. Tumor volume was measured by caliper in two dimensions, and volumes were estimated using the equation [tumor volume = ½ × (length × width2 )]. Caliper measurements were obtained twice a week.

IHC Staining. The staining procedure for IHC was performed as described previously (79). The quantification of IHC images was conducted using Fiji software (82).

PDX-Derived Organoid Culture. Organoid culture was established as described before (83), with modifications. In brief, when tumors reached \~1000 mm3 , they were harvested and processed as described above. Single cell suspensions were subjected to magnetic-activated cell sorting using the mouse cell depletion kit (Miltenyi Biotec, Cat. No. 130-104-694) to eliminate mouse cells. We performed qPCR for all PDX tumors as previously described (84) to assess the human-tomouse DNA content and validate the purification process. Finally, at least 100,000 cells were embedded into 150 ul of matrigel/well in a 6-well ultralow attachment plate and incubated at 37 °C with 5%CO and 5% O . Fresh media were added every 2 to 3 d. Organoid cells were recovered from the matrigel matrix by incubating them with cell recovery solution (Corning, Cat. No. 354253) on ice for approximately 30 min, with frequent pipetting.

Lentiviral Transduction for BRN2 Overproduction and Knockdown Studies. For BRN2 overproduction studies, control lentivirus (Cat. No. PS100092) and lentiviruses encoding human BRN2 (Cat. No. RC205330) were purchased from OriGene. For knockdown experiments, lentivirus containing BRN2 shRNAs (Cat. No. TRCN0000019329, shRNA #1; and Cat. No. TRCN0000019332, shRNA #2) and a nontargeting control (Cat. No. SHC007) were obtained from Sigma Chemical Company. Cells were transduced at a multiplicity of infection (MOI) of 2 in the presence of 10 μg/mL polybrene (Sigma, Cat. No. TR-1003-G), and the medium was replaced the following day. After recovery—two days for established cell lines and seven days for organoid cultures—transduced cells were selected with 1 μg/mL puromycin (Life Technologies, Cat. No. A11138-03) for one to two weeks.

Detailed methods for western blotting, cell viability assay, clonogenic assay, flow cytometry and cell sorting analysis, ALDEFLUOR assay, mammosphere assay, immunofluorescence, and qPCR can be found in the SI Appendix.

Statistical Analysis. Statistical analyses were performed using GraphPad Prism 10 (GraphPad Software Inc.) by the unpaired t test, two-way ANOVA followed by Sidak’s or Tukey’s multiple comparisons test, or unpaired two-tailed Student’s t test with a Welch correction for unequal variances, as indicated in the figure legends. Dose–response curves were plotted and IC50 values were calculated using GraphPad Prism 10. The CI values were calculated using CompuSyn software (41). Synergistic combinations CI < 1, and additive combinations: CI = 1.

1. T. Hanscom, M. McVey, Regulation of error-prone DNA double-strand break repair and its impact on genome evolution. Cells 9, 1657 (2020).

2. H. E. Bryant et al., Specific killing of BRCA2-deficient tumours with inhibitors of poly(ADP-ribose) polymerase. Nature 434, 913–917 (2005).

3. H. Farmer et al., Targeting the DNA repair defect in BRCA mutant cells as a therapeutic strategy. Nature 434, 917–921 (2005).

4. D. C. Janysek, J. Kim, P. H. G. Duijf, E. Dray, Clinical use and mechanisms of resistance for PARP inhibitors in homologous recombination-deficient cancers. Transl. Oncol. 14, 101012 (2021).

5. A. D. D’Andrea, Mechanisms of PARP inhibitor sensitivity and resistance. DNA Repair (Amst.) 71, 172–176 (2018).

6. C. J. Lord, A. Ashworth, Mechanisms of resistance to therapies targeting BRCA-mutant cancers. Nat. Med. 19, 1381–1388 (2013).

7. C. J. Lord, A. Ashworth, PARP inhibitors: Synthetic lethality in the clinic. Science 355, 1152–1158 (2017).

8. T. A. Hopkins et al., PARP1 trapping by PARP inhibitors drives cytotoxicity in both cancer cells and healthy bone marrow. Mol. Cancer Res. 17, 409–419 (2019).

9. K. Cong et al., Replication gaps are a key determinant of PARP inhibitor synthetic lethality with BRCA deficiency. Mol. Cell 81, 3227 (2021).

10. A. Ray Chaudhuri et al., Replication fork stability confers chemoresistance in BRCA-deficient cells. Nature 535, 382–387 (2016).

11. X. Ding et al., Synthetic viability by BRCA2 and PARP1/ARTD1 deficiencies. Nat. Commun. 7, 12425 (2016).

12. S. M. Noordermeer, H. van Attikum, PARP inhibitor resistance: A tug-of-war in BRCA-mutated cells. Trends Cell Biol. 29, 820–834 (2019).

13. S. Akashi-Tanaka et al., BRCAness predicts resistance to taxane-containing regimens in triple negative breast cancer during neoadjuvant chemotherapy. Clin. Breast Cancer 15, 80–85 (2015).

14. M. McMullen, K. Karakasis, A. Madariaga, A. M. Oza, Overcoming platinum and PARP-inhibitor resistance in ovarian cancer. Cancers (Basel) 12, 1607 (2020).

15. J. Michels et al., Cisplatin resistance associated with PARP hyperactivation. Cancer Res. 73, 2271–2280 (2013).

16. J. Goodall et al., Circulating cell-free DNA to guide prostate cancer treatment with PARP inhibition. Cancer Discov. 7, 1006–1017 (2017).

17. E. Harvey-Jones et al., Longitudinal profiling identifies co-occurring BRCA1/2 reversions, TP53BP1, RIF1 and PAXIP1 mutations in PARP inhibitor-resistant advanced breast cancer. Ann. Oncol. 35, 364–380 (2024).

18. O. Kondrashova et al., Secondary somatic mutations restoring RAD51C and RAD51D associated with acquired resistance to the PARP inhibitor rucaparib in high-grade ovarian carcinoma. Cancer Discov. 7, 984–998 (2017).

Data, Materials, and Software Availability. RNAseq/DNAseq data have been deposited in GEO repository (GSE298644) (85).

ACKNOWLEDGMENTS. We are grateful to the patients who provided tumor biopsies for omic analysis and for PDX model establishment. We thank members of the H.P.-W. laboratory for their helpful comments throughout the course of this study. We also thank David J. Tweardy’s laboratory at MD Anderson Cancer Center for providing the STAT3 inhibitor (TTI-101). The research reported in this publication was supported by the generous philanthropic support of the Cazalot family, the Toomim Family Fund, VICTORY Houston, Inc, and The University of Texas MD Anderson Cancer Center Moon Shots Program™. It was also supported by the National Cancer Institute of the NIH under award number U54CA209978 (J.T.C.); the Cancer Prevention and Research Institute of Texas Grants RP160710 (H.P.-W. and J.T.C.) and RP170668 (J.T.C.). The MD Anderson Research Histology Core Laboratory, the Advanced Technology Genomics Core, and the Cytogenetics and Cell Authentication Core are supported in part by NCI Grant P30CA016672. H.P.-W. is an ACS Research Professor.

Author affiliations: a Department of Experimental Radiation Oncology, The University of Texas MD Anderson Cancer Center, Houston, TX 77030; b Department of Bioinformatics and Computational Biology, The University of Texas MD Anderson Cancer Center, Houston, TX 77030; c Department of Integrative Biology and Pharmacology, Institute of Molecular Medicine, The University of Texas Health Science Center at Houston, Houston, TX 77030; and d Department of Breast Medical Oncology, The University of Texas MD Anderson Cancer Center, Houston, TX 77030

Author contributions: N.M.A., Y.J., Y.Q., J.T.C., and H.P.-W. designed research; N.M.A., Y.J., X.Z., S.C., J.S., S.J.-J., A.L.R., and C.-C.C. performed research; J.S. and J.K.L. contributed new reagents/analytic tools; N.M.A., Y.J., Y.Q., X.L., F.H., J.T.C., and H.P.-W. analyzed data; J.K.L. and J.T.C. acquired funding; H.P.-W. supervised research Acquired funding; and N.M.A., Y.J., J.T.C., and H.P.-W. wrote the paper.

Reviewers: L.M.H., Oregon Health and Science University Hospital; and L.Z., Duke University. Competing interest statement: Dr. Litton is on the advisory board of Gilead (uncompensated). Dr. Litton receives research support (to her Institution) from Medivation, Pfizer, Merck, Zenith, EMD-Serono, Genentech, Astra-Zeneca.

19. K. K. Lin et al., BRCA reversion mutations in circulating tumor DNA predict primary and acquired resistance to the PARP inhibitor rucaparib in high-grade ovarian carcinoma. Cancer Discov. 9, 210–219 (2019).

20. S. J. Pettitt et al., Clinical BRCA1/2 reversion analysis identifies hotspot mutations and predicted neoantigens associated with therapy resistance. Cancer Discov. 10, 1475–1488 (2020).

21. D. Quigley et al., Analysis of circulating cell-free DNA identifies multiclonal heterogeneity of BRCA2 reversion mutations associated with resistance to PARP inhibitors. Cancer Discov. 7, 999–1005 (2017).

22. W. Sakai et al., Secondary mutations as a mechanism of cisplatin resistance in BRCA2-mutated cancers. Nature 451, 1116–1120 (2008).

23. L. Tobalina, J. Armenia, E. Irving, M. J. O’Connor, J. V. Forment, A meta-analysis of reversion mutations in BRCA genes identifies signatures of DNA end-joining repair mechanisms driving therapy resistance. Ann. Oncol. 32, 103–112 (2021).

24. J. K. Litton et al., Neoadjuvant talazoparib for patients with operable breast cancer with a germline BRCA pathogenic variant. J. Clin. Oncol. 38, 388–394 (2020).

25. C. Liedtke et al., Response to neoadjuvant therapy and long-term survival in patients with triplenegative breast cancer. J. Clin. Oncol. 26, 1275–1281 (2008).

26. X. Liu et al., Identification of biomarkers of response to preoperative talazoparib monotherapy in treatment naive gBRCA+ breast cancers. NPJ Breast Cancer 8, 64 (2022).

27. R. P. Miskin et al., Integrin alpha3beta1 promotes invasive and metastatic properties of breast cancer cells through induction of the Brn-2 transcription factor. Cancers (Basel) 13, 480 (2021).

28. E. Schreiber et al., Astrocytes and glioblastoma cells express novel octamer-DNA binding proteins distinct from the ubiquitous Oct-1 and B cell type Oct-2 proteins. Nucleic Acids Res. 18, 5495–5503 (1990).

29. J. L. Bishop et al., The master neural transcription factor BRN2 is an androgen receptor-suppressed driver of neuroendocrine differentiation in prostate cancer. Cancer Discov. 7, 54–71 (2017).

30. K. Herbert et al., BRN2 suppresses apoptosis, reprograms DNA damage repair, and is associated with a high somatic mutation burden in melanoma. Genes Dev. 33, 310–332 (2019).

31. M. J. Garnett et al., Systematic identification of genomic markers of drug sensitivity in cancer cells. Nature 483, 570–575 (2012).

32. B. D. Lehmann et al., Identification of human triple-negative breast cancer subtypes and preclinical models for selection of targeted therapies. J. Clin. Invest. 121, 2750–2767 (2011).

33. J. G. Tate et al., COSMIC: The catalogue of somatic mutations in cancer. Nucleic Acids Res. 47, D941–D947 (2019).

34. Y. H. Ibrahim et al., PI3K inhibition impairs BRCA1/2 expression and sensitizes BRCA-proficient triple-negative breast cancer to PARP inhibition. Cancer Discov. 2, 1036–1047 (2012).

35. A. Juvekar et al., Phosphoinositide 3-kinase inhibitors induce DNA damage through nucleoside depletion. Proc. Natl. Acad. Sci. U.S.A. 113, E4338–E4347 (2016).

36. O. Liska et al., TFLink: An integrated gateway to access transcription factor-target gene interactions for multiple species. Database (Oxford) 2022, baac083 (2022).

37. L. Liu et al., ALDH1A1 contributes to PARP inhibitor resistance via enhancing DNA repair in BRCA2−/−ovarian cancer cells. Mol. Cancer Ther. 19, 199–210 (2020).

38. V. Azzoni et al., BMI1 nuclear location is critical for RAD51-dependent response to replication stress and drives chemoresistance in breast cancer stem cells. Cell Death Dis. 13, 96 (2022).

39. Y. Liu et al., RAD51 mediates resistance of cancer stem cells to PARP inhibition in triple-negative breast cancer. Clin. Cancer Res. 23, 514–522 (2017).

40. A. M. Tsimberidou et al., Phase I trial of TTI-101, a first-in-class oral inhibitor of STAT3, in patients with advanced solid tumors. Clin. Cancer Res. 31, 965–974 (2025).

41. N. Zhang, J. N. Fu, T. C. Chou, Synergistic combination of microtubule targeting anticancer fludelone with cytoprotective panaxytriol derived from Panax ginseng against MX-1 cells in vitro: Experimental design and data analysis using the combination index method. Am. J. Cancer Res. 6, 97–104 (2016).

42. S. A. Yazinski et al., ATR inhibition disrupts rewired homologous recombination and fork protection pathways in PARP inhibitor-resistant BRCA-deficient cancer cells. Genes Dev. 31, 318–332 (2017).

43. E. Fokas et al., Targeting ATR in vivo using the novel inhibitor VE-822 results in selective sensitization of pancreatic tumors to radiation. Cell Death Dis. 3, e441 (2012).

44. H. Li et al., PARP inhibitor resistance: The underlying mechanisms and clinical implications. Mol. Cancer 19, 107 (2020).

45. P. Polak et al., A mutational signature reveals alterations underlying deficient homologous recombination repair in breast cancer. Nat. Genet. 49, 1476–1486 (2017).

47. E. Manie et al., Genomic hallmarks of homologous recombination deficiency in invasive breast carcinomas. Int. J. Cancer 138, 891–900 (2016).

48. T. Popova et al., Ploidy and large-scale genomic instability consistently identify basal-like breast carcinomas with BRCA1/2 inactivation. Cancer Res. 72, 5454–5462 (2012).

49. D. Endesfelder et al., Chromosomal instability selects gene copy-number variants encoding core regulators of proliferation in ER+ breast cancer. Cancer Res. 74, 4853–4863 (2014).

50. A. Roth et al., Pyclone: Statistical inference of clonal population structure in cancer. Nat. Methods 11, 396–398 (2014).

51. H. Dev et al., Shieldin complex promotes DNA end-joining and counters homologous recombination in BRCA1-null cells. Nat. Cell Biol. 20, 954–965 (2018).

52. S. M. Noordermeer et al., The shieldin complex mediates 53BP1-dependent DNA repair. Nature 560, 117–121 (2018).

53. L. Cortesi, H. S. Rugo, C. Jackisch, An overview of PARP inhibitors for the treatment of breast cancer. Target. Oncol. 16, 255–282 (2021).

54. E. Rodler et al., Cisplatin with veliparib or placebo in metastatic triple-negative breast cancer and BRCA mutation-associated breast cancer (S1416): A randomised, double-blind, placebo-controlled, phase 2 trial. Lancet Oncol. 24, 162–174 (2023).

55. G. Illuzzi et al., Preclinical characterization of AZD5305, a next-generation, highly selective PARP1 inhibitor and trapper. Clin. Cancer Res. 28, 4724–4736 (2022).

56. T. A. Yap et al., “PETRA: First in class, first in human trial of the next generation PARP1-selective inhibitor AZD5305 in patients (pts) with BRCA1/2, PALB2 or RAD51C/D mutations” in Proceedings of the American Association for Cancer Research Annual Meeting (2022), vol. 82.

57. S. L. Edwards et al., Resistance to therapy caused by intragenic deletion in BRCA2. Nature 451, 1111–1115 (2008).

58. R. Gupta et al., DNA repair network analysis reveals Shieldin as a key regulator of NHEJ and PARP inhibitor sensitivity. Cell 173, 972–988 e923 (2018).

59. R. Ceccaldi et al., Homologous-recombination-deficient tumours are dependent on Polthetamediated repair. Nature 518, 258–262 (2015).

60. P. A. Mateos-Gomez et al., Mammalian polymerase theta promotes alternative NHEJ and suppresses recombination. Nature 518, 254–257 (2015).

61. A. Vaidyanathan et al., ABCB1 (MDR1) induction defines a common resistance mechanism in paclitaxel- and olaparib-resistant ovarian cancer cells. Br. J. Cancer 115, 431–441 (2016).

62. S. J. Pettitt et al., Genome-wide and high-density CRISPR-Cas9 screens identify point mutations in PARP1 causing PARP inhibitor resistance. Nat. Commun. 9, 1849 (2018).

63. E. Gogola et al., Selective loss of PARG restores PARylation and counteracts PARP inhibitor-mediated synthetic lethality. Cancer Cell 33, 1078–1093.e1012 (2018).

64. J. K. Litton et al., A feasibility study of neoadjuvant talazoparib for operable breast cancer patients with a germline BRCA mutation demonstrates marked activity. NPJ Breast Cancer 3, 49 (2017).

65. I. Berlin et al., Phosphorylation of BRN2 modulates its interaction with the Pax3 promoter to control melanocyte migration and proliferation. Mol. Cell. Biol. 32, 1237–1247 (2012).

66. G. M. Boyle et al., Melanoma cell invasiveness is regulated by miR-211 suppression of the BRN2 transcription factor. Pigment Cell Melanoma Res. 24, 525–537 (2011).

67. S. Pinner et al., Intravital imaging reveals transient changes in pigment production and Brn2 expression during metastatic melanoma dissemination. Cancer Res. 69, 7969–7977 (2009).

68. C. J. Pierce et al., BRN2 expression increases anoikis resistance in melanoma. Oncogenesis 9, 64 (2020).

69. M. A. F. Soares et al., Hierarchical reactivation of transcription during mitosis-to-G1 transition by Brn2 and Ascl1 in neural stem cells. Genes Dev. 35, 1020–1034 (2021).

70. M. L. Suva et al., Reconstructing and reprogramming the tumor-propagating potential of glioblastoma stem-like cells. Cell 157, 580–594 (2014).

71. C. C. Cheng et al., Stat3/Oct-4/c-Myc signal circuit for regulating stemness-mediated doxorubicin resistance of triple-negative breast cancer cells and inhibitory effects of WP1066. Int. J. Oncol. 53, 339–348 (2018).

72. H. Kim et al., Targeting the ATR/CHK1 axis with PARP inhibition results in tumor regression in BRCA-mutant ovarian cancer models. Clin. Cancer Res. 23, 3097–3108 (2017).

73. J. J. Qin, L. Yan, J. Zhang, W. D. Zhang, STAT3 as a potential therapeutic target in triple negative breast cancer: A systematic review. J. Exp. Clin. Cancer Res. 38, 195 (2019).

74. J. Jin, Z. Tao, J. Cao, T. Li, X. Hu, DNA damage response inhibitors: An avenue for TNBC treatment. Biochimica et Biophysica Acta (BBA) 1875, 188521 (2021).

75. A. Ring et al., Olaparib and ceralasertib (AZD6738) in patients with triple-negative advanced breast cancer: Results from cohort E of the plasmaMATCH trial (CRUK/15/010). Clin. Cancer Res. 29, 4751–4759 (2023).

76. Anonymous, U.A. Department of Health and Human Services. Combined Text of All Rules (http:// www.hhs.gov/ocr/privacy/hipaa/administrative/combined/index.html).

77. L. E. Dobrolecki et al., Patient-derived xenograft (PDX) models in basic and translational breast cancer research. Cancer Metastasis Rev. 35, 547–573 (2016).

78. G. V. Echeverria et al., Predictors of success in establishing orthotopic patient-derived xenograft models of triple negative breast cancer. NPJ Breast Cancer 9, 2 (2023).

79. R. T. Powell et al., Targeting neddylation and sumoylation in chemoresistant triple negative breast cancer. NPJ Breast Cancer 10, 37 (2024).

80. N. Cancer Genome Atlas, Comprehensive molecular portraits of human breast tumours. Nature 490, 61–70 (2012).

81. W. Yang et al., Genomics of drug sensitivity in cancer (GDSC): A resource for therapeutic biomarker discovery in cancer cells. Nucleic Acids Res. 41, D955–D961 (2013).

82. J. Schindelin et al., Fiji: An open-source platform for biological-image analysis. Nat. Methods 9, 676–682 (2012).

83. N. Sachs et al., A living biobank of breast cancer organoids captures disease heterogeneity. Cell 172, 373–386.e310 (2018).

84. G. V. Echeverria et al., High-resolution clonal mapping of multi-organ metastasis in triple negative breast cancer. Nat. Commun. 9, 5079 (2018).

85. N. M. Abdulkareem et al., Data from “Resistance to neoadjuvant talazoparib in triple-negative breast cancer mediated by BRN2-induced ATR/STAT3 pathways or Shieldin 2 subclone expansion.” NCBI GEO. Available at https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE298644. Deposited 2 June 2025.