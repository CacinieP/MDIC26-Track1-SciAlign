# Exploratory Analysis of Biomarkers and Treatment Outcomes from the COLUMBUS Study in BRAF V600E/K–Mutant Advanced or Metastatic Melanoma

<!-- image-->

Reinhard Dummer1 , Shibing Deng2 , Tao Xie2 , Nuzhat Pathan2 , Hedieh Saffari3 , Caroline Robert4 , Ana Arance5 , Jan Willem B. de Groot6 , Claus Garbe7 , Helen J. Gogas8 , Ralf Gutzmer9 , Ivana Krajsov´a10, Gabriella Liszkay11 , Carmen Loquai12, Mario Mandala13, Dirk Schadendorf14,15, Naoya Yamazaki16, Paolo A. Ascierto17, Craig B. Davis2 , Khyati Shah2 , Phineas Hamilton2 , Alessandra di Pietro18, and Keith Flaherty19

## ABSTRACT

Purpose: Treatment with encorafenib ± binimetinib is associated with improved survival versus vemurafenib in patients with BRAF V600E/K–mutant advanced melanoma. We retrospectively analyzed genomic and transcriptomic data from the phase III COLUMBUS trial to identify molecular correlates of benefit with encorafenib ± binimetinib.

Experimental Design: In COLUMBUS, patients with BRAF V600E/K–mutant locally advanced, unresectable, or metastatic melanoma (n ¼ 921) were randomized to receive encorafenib plus binimetinib, encorafenib, or vemurafenib. We used whole-exome sequencing (n ¼ 666), wholetranscriptome sequencing (RNA sequencing; n ¼ 514), and assessment of circulating tumor DNA (ctDNA) at baseline (n ¼ 336) and on treatment (cycle 2 day 1, n ¼ 184) to evaluate biomarker associations with progression-free and overall survival.

## Introduction

BRAF V600 mutations occur in approximately 50% of patients with cutaneous melanoma (1–3). COLUMBUS (NCT01909453) was a randomized, two-part, multicenter, open-label, phase III study that assessed the safety and efficacy of the BRAF inhibitor encorafenib plus the MEK inhibitor binimetinib versus monotherapy with the BRAF inhibitors vemurafenib or encorafenib in patients with BRAF V600E/K–mutant locally advanced, unresectable, or metastatic melanoma (4). COLUMBUS led to the approval of the combination of encorafenib plus binimetinib in this population based on

Results: Survival benefits with encorafenib plus binimetinib versus vemurafenib were greatest in patients with higher tumor mutational burden (TMB) and those with evidence of tumor immune infiltration (i.e., higher cytolytic score, PD-L1 expression, or IFNγ gene signature scores). Clustering of gene expression profiles identified three tumor subgroups, including an “immune” subgroup associated with improved survival. Detection of BRAF V600 alterations in baseline ctDNA was associated with shorter survival; clearance of BRAF V600 alterations at cycle 2 day 1 was associated with improved survival across arms.

Conclusions: The greatest benefits of encorafenib plus binimetinib were observed in patients with evidence of high TMB and/or tumor-immune infiltration, suggesting potential immune contributions to efficacy, which were not observed with vemurafenib. BRAF V600 detectability in ctDNA seems to have utility as a marker of prognosis and response in this population.

improved progression-free [PFS; 14.9 vs. 7.3 months; hazard ratio (HR), 0.51] and overall survival (OS; 33.6 vs. 16.9 months; HR, 0.67) versus vemurafenib (2, 4–8).

Despite the demonstrated benefits of encorafenib plus binimetinib, primary and acquired resistance mechanisms remain significant clinical challenges (9). Since the approval based on COLUMBUS, resistance mechanisms and validated novel biomarkers for treatment optimization have been elucidated. Demonstrated mechanisms of resistance include alternate activation of the MAPK pathway through activating mutations in NRAS, KRAS, or MAP2K1 and activating mutations in the PI3K pathway involving AKT,

This open access article is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

©2026 The Authors; Published by the American Association for Cancer Research

## Translational Relevance

The phase III COLUMBUS trial previously demonstrated that encorafenib plus binimetinib and encorafenib monotherapy improved progression-free survival (PFS) and overall survival (OS) versus vemurafenib in patients with BRAF V600E/K–mutant locally advanced, unresectable, or metastatic melanoma. Patients were either treatment-na¨ıve or had progressed after first-line immunotherapy and had not received prior BRAF or MEK inhibitors. The combination of encorafenib plus binimetinib provided the best clinical outcome for this patient population. In this study, we found that the greatest survival benefits with encorafenib plus binimetinib were seen in patients with evidence of preexisting immune cell infiltration and higher tumor mutational burden. Associations between detectability of BRAF alterations in circulating tumor DNA (ctDNA) at baseline and during treatment and PFS and OS suggest ctDNA as a potential marker of prognosis and benefit in BRAF V600E/K– mutant advanced melanoma.

PTEN, and MTOR (10). Beyond genetic alterations, single-cell analysis has revealed that drug-tolerant transcriptional states can arise in response to treatment (11), whereas specific cancer cell phenotypic or tumor microenvironment (TME) features may also confer primary resistance (12). Examples include MITF, which exhibits dual resistance functions through MITF-high/AXL-low versus MITFlow/AXL-high phenotypic switching (13), and POSTN, which fosters resistance by promoting emergence of tumor cell–protective macrophages that directly shield melanoma cells from treatment-induced cell death (12). Importantly, signatures of immune infiltration have been associated with increased benefit from BRAF plus MEK inhibition, with treatment promoting enhanced CD8+ T-cell infiltration and improved antigen presentation (14). Circulating tumor DNA (ctDNA) has also emerged as a biomarker for monitoring treatment response, detecting resistance an average of 3.6 months earlier than conventional imaging (15). Although current clinical practice guidelines acknowledge biomarker importance, comprehensive biomarker evaluation beyond BRAF mutation testing has not yet been incorporated into standard practice recommendations (8).

In this study, we evaluate whether the addition of binimetinib to encorafenib led to increased benefit in specific biomarker molecularly defined subgroups and whether encorafenib alone confers increased benefit versus vemurafenib in specific subgroups. This leveraged analysis of long-term 7-year PFS and OS, along with comprehensive genomic and transcriptomic profiling of patients treated in COLUMBUS, to better understand the correlates of benefit with BRAF inhibition ± MEK inhibition in BRAF V600E– mutant melanoma. Analyses of whole-exome sequencing (WES) and whole-transcriptome sequencing [RNA sequencing (RNA-seq)] were performed, as was ctDNA profiling of somatic mutations at baseline and on treatment, representing the largest cohort of BRAFmutant melanoma samples comprehensively characterized to date.

## Materials and Methods

## COLUMBUS study

COLUMBUS (NCT01909453) is a randomized, two-part, multicenter, open-label, phase III study (4, 5, 16–18). The COLUMBUS study design, primary analysis, and 5- and 7-year updates have been published previously (4, 5, 17, 18). Briefly, eligible patients were treatment-na¨ıve or had progressed after first-line immunotherapy, had an Eastern Cooperative Oncology Group performance status of 0 or 1, and had not had prior therapy with a BRAF inhibitor and/or MEK inhibitor. In COLUMBUS part 1, 577 patients were randomized 1:1:1 to receive encorafenib 450 mg once daily plus binimetinib 45 mg twice daily, encorafenib 300-mg once-daily monotherapy, or vemurafenib 960-mg twice-daily monotherapy. In COLUMBUS part 2, 344 patients were randomized 3:1 to receive encorafenib 300 mg once daily plus binimetinib 45 mg twice daily or encorafenib 300 mg once-daily monotherapy (Supplementary Fig. S1).

This exploratory biomarker analysis was performed in enrolled patients with available samples for WES, RNA-seq, and/or ctDNA analyses. The study protocol was approved by independent ethics committees or site institutional review boards. The conduct of the study conformed to Good Clinical Practice guidelines and the ethical requirements outlined in the Declaration of Helsinki. Written informed consent was obtained from all patients before screening.

## Endpoints

This exploratory biomarker analysis evaluated genomic and transcriptomic correlates of the patients’ clinical outcomes. PFS was assessed by blinded independent central review and was defined as the time from the date of randomization to the date of the first documented disease progression or death due to any cause, whichever occurred first. OS was defined as the time from the date of randomization to the date of death due to any cause. PFS and OS data from the 7-year analysis (data cutoff: January 13, 2023) were analyzed by treatment groups and the presence of specific genetic alterations or transcriptomic features at baseline.

Data from COLUMBUS parts 1 and 2 were pooled for the encorafenib plus binimetinib arm (part 1, encorafenib 450 mg once daily; part 2, encorafenib 300 mg once daily) and for encorafenib monotherapy (300 mg once daily in both parts) to increase the power for biomarker analysis.

## WES, whole-transcriptome sequencing, and analysis

Baseline tumor samples were analyzed using the ACE ImmunoID NeXT WES/RNA-seq assays (Personalis Inc.). WES and RNA-seq of formalin-fixed, paraffin-embedded (FFPE) blocks or slide samples were performed by Personalis using the ImmunoID NeXT platform and sequenced on the Illumina NovaSeq Sequencing system. DNA and RNA were dual-isolated from FFPE blocks or slides using the AllPrep DNA/RNA FFPE Kit (Qiagen). WES capture was performed using SureSelect Clinical Research Exome v.2 (Agilent Technologies) according to the manufacturer’s recommendations. Additional supplementation with Personalis proprietary target probes was performed to enhance coverage in difficult-to-sequence regions within sets of biomedically and medically relevant genes. For WES, Personalis proxy normal and custom filters were used to remove germline variants. Matched normal controls were unavailable; hence, variants were filtered for presumptive somatic status based on Personalis’ internal control pipeline. Somatic mutations with variant allele frequency (VAF) above 0.05 were reported. For RNA-seq, Personalis provided gene-level read counts and transcript per million (TPM)-normalized gene expression values. Samples with fewer than 25M mapped reads were excluded from further analyses.

Analyses of gene expression were based on a log2 (x + 1) transformation of TPM values. Unsupervised clustering and estimation of tumor cell type compositions using K-means clustering and xCell were performed to identify candidate molecular subtypes and potential cell type contributions to subtypes, respectively (19). Clustering on gene expression and global analyses of gene expression with outcomes were performed after filtering genes to exclude those with a standard deviation in log expression <1 across samples.

## Biomarker assessments

Tumor mutational burden (TMB) [mutations (mut)/Mb] was determined by Personalis’ proprietary bioinformatics pipeline based on WES. The cytolytic score was determined as the average logtransformed GZMA and PRF1 TPM (20). PD-L1 (encoded by CD274) expression levels were evaluated as log TPM. The GO-BP IFNγ gene expression signature was used to calculate an IFNγ gene expression score as the mean of log TPM values of signature genes. The PI3K pathway was considered mutated if mutations were detected in PIK3CA, PTEN, AKT (AKT1, 2, and 3), or MTOR genes. MITF and AXL gene expression levels were evaluated from log TPM. For patient stratification for TMB, cytolytic score, PD-L1 expression, IFNγ signature, and ERBB2 expression, biomarker-high subgroups were defined as those with biomarker levels above the median for the population, and biomarker-low subgroups as those with levels at or below the median. BRAF mutation status (V600E or V600K) was taken from local test results reported at patient enrollment; in one case in which both BRAF V600E and V600K were reported, V600K was considered to be present.

## ctDNA analysis

Plasma samples were collected for ctDNA analysis at screening, cycle 1 day 1 (C1D1, and C2D1, with the C1D1 values taken as baseline. Samples were sequenced using the GuardantOMNI assay (Guardant Health Inc.) to evaluate somatic alterations. Variants were detected and reported based on a threshold of ≥0.01% VAF, as determined by Guardant’s proprietary bioinformatics pipeline. As study patients were known to have BRAF V600 alterations, BRAF V600 alteration VAF was used as the metric for ctDNA burden in the analysis.

## Statistical analysis

Median durations of follow-up for PFS and OS were estimated by reverse Kaplan–Meier analysis. HR were estimated using Cox proportional hazard regression models and presented along with 95% confidence intervals (CI). Cluster analysis was performed using the K-means clustering method, with the optimal number of k clusters determined by the average silhouette width. Recursive partitioning was conducted based on preselected predictor variables using the rpart R package, including only cases with complete data for each variable. Unless otherwise indicated, adjustments correcting for multiple testing were not performed, and all results should thus be interpreted as hypothesis-generating. All analyses were performed using R v4.1.0 or above (RRID: SCR_001905).

## Results

## Study cohort

In the COLUMBUS study, a total of 921 patients with locally advanced unresectable or metastatic BRAF V600E/K–mutant melanoma were randomized. In part 1 of COLUMBUS, 577 patients were randomized to receive encorafenib plus binimetinib (n ¼ 192), vemurafenib monotherapy (n ¼ 191), or encorafenib monotherapy (n ¼ 194). In COLUMBUS part 2, an additional 344 patients were randomized to receive encorafenib plus binimetinib (n ¼ 258) or encorafenib monotherapy (n ¼ 86; Supplementary Fig. S1). Overall, 668 patients had WES or RNA-seq data (Supplementary Fig. S2); 666 patients had WES, 514 patients had RNA-seq, 336 patients had baseline ctDNA, and 184 patients had on-treatment ctDNA successfully profiled. Baseline characteristics by biomarker status are shown in Table 1 for tumor tissue biomarkers and were similar between the biomarker set and the overall study population.

## TMB and benefit from encorafenib ± binimetinib versus vemurafenib

The range for TMB was 5.28 to 33.56 mut/Mb. Patients were considered to have low or high baseline TMB based on the median TMB value among patients profiled in the study (8.64 mut/Mb). Encorafenib plus binimetinib resulted in a PFS benefit versus vemurafenib regardless of the TMB group [HR, 0.55 (95% CI, 0.38–0.80) for high TMB and HR, 0.53 (95% CI, 0.37–0.76) for low TMB]; however, patients in the TMB-high group had a longer PFS versus patients in the TMB-low group for both treatment arms [HR, 0.71 (95% CI, 0.55–0.93) with encorafenib plus binimetinib (high vs. low TMB) and HR, 0.74 (95% CI, 0.48–1.15) with vemurafenib (high vs. low TMB)]. In contrast, encorafenib monotherapy provided an improved PFS benefit versus vemurafenib in the TMB-low group [HR, 0.63 (95% CI, 0.43–0.94)] but not in the TMB-high group [HR, 0.88 (95% CI, 0.59–1.31)]. No difference in PFS was observed between patients in the TMB-high and TMB-low groups treated with encorafenib monotherapy [HR, 1.01 (95% CI, 0.71–1.42); Fig. 1A].

Encorafenib plus binimetinib or encorafenib monotherapy resulted in a greater OS benefit versus vemurafenib in the TMBhigh group compared with the TMB-low group (Fig. 1B). OS was improved with both encorafenib plus binimetinib [HR, 0.58 (95% CI, 0.41–0.81)] and encorafenib monotherapy [HR, 0.65 (95% CI, 0.45–0.94)] versus vemurafenib in the TMB-high group, with no OS benefits observed versus vemurafenib observed in the TMB-low group.

Additionally, TMB was elevated in patients with BRAF V600K (n ¼ 79) versus BRAF V600E (n ¼ 586) mutations [median, 10.60 vs. 8.47 mut/Mb; P < 0.001 (t test)]; however, adjusting for BRAF mutation type in models did not affect the increased OS benefit of encorafenib and encorafenib plus binimetinib versus vemurafenib observed in the TMB-high group (adjusted HR, 0.65 and 0.58, respectively).

## Transcriptional correlates of PFS and OS with encorafenib plus binimetinib or encorafenib monotherapy versus vemurafenib

The range for cytolytic scores was 0.12 to 6.87 log2 TPM. Patients were considered to have low or high cytolytic scores based on the median score values. For patients in the high cytolytic score group, encorafenib plus binimetinib resulted in greater PFS (Fig. 1C) and OS (Fig. 1D) benefits versus vemurafenib compared with patients in the low cytolytic score group [PFS HR, 0.32 (95% CI, 0.21–0.50) for high cytolytic score and 0.64 (95% CI, 0.42–0.98) for low cytolytic score; OS HR, 0.60 (95% CI, 0.40–0.90) for high cytolytic score and 0.73 (95% CI, 0.51–1.04) for low cytolytic score]. Lower PFS or OS benefits were observed with encorafenib monotherapy versus vemurafenib [PFS HR, 0.65 (95% CI, 0.42–1); OS HR, 0.99 (95% CI, 0.64–1.52)]. In the low cytolytic score group, although PFS was significantly longer with encorafenib plus binimetinib versus vemurafenib [HR, 0.64 (95% CI, 0.42–0.98)], no PFS benefit was observed with encorafenib monotherapy versus vemurafenib [HR, 0.92 (95% CI, 0.59–1.43)]. Similar trends were observed when grouping patients by PD-L1 (CD274) expression as well as the IFNγ gene signature score based on their median values (Supplementary Fig. S3A–S3D), with PFS and OS benefits with encorafenib plus binimetinib and encorafenib monotherapy versus vemurafenib numerically greatest in patients with high PD-L1 (CD274) expression or high IFNγ. As expected, these RNA-derived metrics of tumor immune infiltration were highly correlated across patients (r > 0.75; Supplementary Fig. S3E).

Table 1. Baseline patient characteristics by biomarker status.
<table><tr><td></td><td>Overall</td><td colspan="2">Biomarker set</td><td></td></tr><tr><td>Variable</td><td>(N = 921)</td><td>No (n = 253)</td><td>Yes (n = 668)</td><td>P value</td></tr><tr><td>Age, years</td><td></td><td></td><td></td><td></td></tr><tr><td>Median (range)</td><td>56 (47-66)</td><td>55 (46-65)</td><td>57 (47-66)</td><td>0.2</td></tr><tr><td>Sex, n (%)</td><td></td><td></td><td></td><td></td></tr><tr><td>Female</td><td>392 (43)</td><td>105 (42)</td><td>287 (43)</td><td></td></tr><tr><td>Male</td><td>529 (57)</td><td>148 (58)</td><td>381 (57)</td><td></td></tr><tr><td>Race, n (%)</td><td></td><td></td><td></td><td>0.022</td></tr><tr><td>Missing</td><td>1 (0.1)</td><td>1 (0.4)</td><td>0 (0)</td><td></td></tr><tr><td>Asian</td><td>41 (4.5)</td><td>6 (2.4)</td><td>35 (5.2)</td><td></td></tr><tr><td>Black</td><td>1 (0.1)</td><td>1 (0.4)</td><td>0 (0)</td><td></td></tr><tr><td>White</td><td>838 (91)</td><td>229 (91)</td><td>609 (91)</td><td></td></tr><tr><td>Native American</td><td>4 (0.4)</td><td>1 (0.4)</td><td>3 (0.4)</td><td></td></tr><tr><td>Other</td><td>9 (1)</td><td>5 (2)</td><td>4 (0.6)</td><td></td></tr><tr><td>Unknown</td><td>27 (2.9)</td><td>10 (4)</td><td>17 (2.5)</td><td></td></tr><tr><td>Treatment, n (%)</td><td></td><td></td><td></td><td></td></tr><tr><td>Untreated</td><td>10 (1.1)</td><td>10 (4)</td><td>0 (0)</td><td></td></tr><tr><td>Encorafenib (part 1)</td><td>192 (21)</td><td>72 (28)</td><td>120 (18)</td><td></td></tr><tr><td>Encorafenib (part 2)</td><td>84 (9.1)</td><td>6 (2.4)</td><td>78 (12)</td><td></td></tr><tr><td>Encorafenib 300 mg + binimetinib</td><td>257 (28)</td><td>33 (13)</td><td>224 (34)</td><td></td></tr><tr><td>Encorafenib 450 mg + binimetinib</td><td>192 (21)</td><td>76 (30)</td><td>116 (17)</td><td></td></tr><tr><td>Vemurafenib</td><td>186 (20)</td><td>56 (22)</td><td>130 (19)</td><td></td></tr><tr><td>BRAF screening, n (%)</td><td></td><td></td><td></td><td>0.4</td></tr><tr><td>Missing</td><td>2 (0.2)</td><td>1 (0.4)</td><td>1 (0.1)</td><td></td></tr><tr><td>V600E</td><td>815 (88)</td><td>227 (90)</td><td>588 (88)</td><td></td></tr><tr><td>V600K</td><td>104 (11)</td><td>25 (9.9)</td><td>79 (12)</td><td></td></tr></table>

Taken together, these analyses suggest the greatest treatment benefit from encorafenib plus binimetinib versus vemurafenib for patients with evidence of potential antitumor immune responses that included higher TMB, cytolytic score, PD-L1 expression level, and IFNγ gene expression signature scores (Fig. 1; Supplementary Fig. S3). Although qualitatively similar effects were generally observed for encorafenib monotherapy versus vemurafenib, these effects were generally not as strong and did not always reach statistical significance, suggesting a greater importance of immune contexture to the effects of encorafenib plus binimetinib than encorafenib alone.

Other gene expression patterns reflecting potentially targetable cell phenotypes were also observed. For example, patients with high ERBB2 expression showed reduced benefit with encorafenib plus binimetinib versus vemurafenib compared with those with low ERBB2 expression for PFS [Fig. 2A; PFS HR, 0.60 (95% CI, 0.39–0.92) for high ERBB2 and 0.36 (95% CI, 0.24–0.55) for low ERBB2] and OS [Fig. 2B; OS HR, 0.75 (95% CI, 0.52–1.1) for high ERBB2 and 0.56 (95% CI, 0.38–0.83) for low ERBB2]. Thus, although patients with high ERBB2 expression still derived a PFS benefit from encorafenib plus binimetinib versus vemurafenib, this was substantially reduced compared with the ERBB2-low group, and, unlike in the ERBB2-low group, an OS benefit was not significant.

Previous gene expression analyses have found melanoma to segregate into invasive and proliferative phenotypes, differentiated by the expression of AXL and MITF, respectively (21). In this study, MITF and AXL expression were negatively correlated across samples (r ¼ �0.44; P < 0.001). The benefits of encorafenib ± binimetinib were largely consistent across patients with above versus below median expression of MITF or AXL (Supplementary Fig. S4A–S4D), although increased MITF, but not AXL, expression was associated with decreased PFS [HR, 1.44 (95% CI, 1.16–1.79)] and OS [HR, 1.27 (95% CI, 1.03–1.57)] when pooling across arms, with no significant interaction across arms (PFS curves for individual arms shown in Supplementary Fig. S4A and S4C). Expression of AXL was not significantly associated with OS (Supplementary Fig. S4D), and the ratio of MITF/AXL expression (based on the median of log2 MITF TPM - log2 AXL TPM) was not more strongly associated with outcome than MITF expression alone [PFS HR, 1.26 (95% CI, 1.02– 1.57); OS HR, 1.26 (95% CI, 1.02–1.55)].

## Gene expression–based molecular subgroups

To perform unbiased subgroup discovery in COLUMBUS, we used K-means clustering to identify candidate tumor molecular subgroups, with three presumptive subgroups identified (Supplementary Fig. S5). For consistency with prior subtyping systems (21), these were labeled as “immune” based on the expression of immune-related genes (n ¼ 122), “invasive” based on low expression of MITF and higher expression of AXL (n ¼ 150), and “proliferative” based on higher MITF expression (n ¼ 242; Fig. 3A). Interestingly, AXL expression was also relatively elevated in the immune subgroup. Estimation of the abundances of key cell types in the TME using xCell (19) corroborated high scores for lymphocytes in the immune subgroup and revealed higher keratinocyte scores in the invasive subtype. The immune subgroup was also significantly associated with biopsy sites (Fisher exact test; $P < 0 . 0 0 1 )$ , with the invasive subtype enriched in skin biopsies and the immune subtype in lymph node metastases (Fig. 3B), thus suggesting gene expression clusters may be representative of biopsy site rather than intrinsic features of the tumors. Furthermore, samples originating from the skin were not classified as primary or metastatic lesions; therefore, it is unclear to what extent the observed differences between skin and other sites reflect the biology of metastatic disease. Nonetheless, differences were observed between the three clusters that were not dependent on biopsy site, and comparative analysis of relative contributions to OS suggested that the gene expression cluster contributed substantially more than biopsy site, with the effect of cluster approximately 28-fold greater. As suggested by preceding analyses, the immune cluster was associated with improved survival compared with the invasive and proliferative clusters, with significantly longer OS for patients with an immune versus an invasive tumor subtype [HR, 0.69 (95% CI, 0.51–0.94); Fig. 3C].

Additional analyses of biomarkers, including cytolytic score and ERBB2 and MITF expression, demonstrated that expression of these cluster-specific features was largely independent of biopsy site (Supplementary Fig. S6). For example, samples in the immune cluster showed higher cytolytic scores than other subtypes across biopsy sites. In contrast, invasive cluster samples had increased ERBB2 expression, whereas proliferative cluster samples expressed higher levels of MITF. These patterns were largely independent of biopsy site.

To corroborate these targeted findings, we also performed global analyses of gene expression associations with OS, including z-scored expression values for each measured gene in univariable Cox models. Consistent with the preceding analyses, key markers of lymphocyte infiltration were associated with improved OS in the encorafenib plus binimetinib arm, with CD38, LAG3, and CD8A among the genes most strongly associated with OS; in contrast, these associations were attenuated in the encorafenib arm alone and largely absent in the vemurafenib arm. In the encorafenib plus binimetinib arm, the expression of SOX6 was also strongly associated with increased risk. Gene-set enrichment analysis of hallmark gene sets using genes ranked by associations with OS in each arm further corroborated this interpretation, with immune processes (e.g., allograft rejection and IFNγ signaling) dominating the signals recovered from the encorafenib plus binimetinib arm and, to a lesser extent, the encorafenib arm (Fig. 1E).

## PI3K pathway mutations and benefit with encorafenib ± binimetinib

Given the described role of PI3K pathway mutations in resistance to BRAF ± MEK inhibition (22), we tested for associations between pathway alterations and outcome. For patients with mutations in the PI3K pathway, the PFS (Fig. 2C) and OS (Fig. 2D) benefits with encorafenib plus binimetinib versus vemurafenib were reduced compared with patients who were wild-type (WT) for the PI3K pathway [PFS HR, 0.69 (95% CI, 0.40–1.17) for PI3K pathway mutations and 0.51 (95% CI, 0.38–0.69) for WT PI3K pathway; OS HR, 0.83 (95% CI, 0.52–1.33) for PI3K pathway mutations and 0.68 (95% CI, 0.52–0.89) for WT PI3K pathway]. However, in contrast to encorafenib plus binimetinib, encorafenib monotherapy showed numerically longer PFS and significantly longer OS [HR, 0.55 (95% CI, 0.32–0.93)] in patients with PI3K pathway mutations, compared with those without mutations.

## BRAF V600 alteration detectability in ctDNA at baseline and on treatment as a prognostic marker for PFS and OS

Detection of BRAF V600 alterations in ctDNA at baseline was associated with reduced PFS (Fig. 4A) and OS (Fig. 4B) compared with nondetection, regardless of the treatment arm. This effect was more pronounced for OS (HR of detection vs. nondetection ranged from 2.3 to 3.5 across arms; P < 0.01; Fig. 4A) than for PFS (HR, 1.9–2.3; P < 0.05; Fig. 4B). On-treatment change in BRAF V600 ctDNA detectability was evaluated in the encorafenib and encorafenib plus binimetinib arms and was also prognostic for survival outcomes, despite a limited sample size. For patients with BRAF V600 alterations detectable at baseline, those who transitioned to nondetectable at C2D1 of treatment with encorafenib plus binimetinib or encorafenib monotherapy had evidence of improved PFS [HR, 0.36 (P ¼ 0.023) in the encorafenib arm; and 0.59 $( P = 0 . 0 8 7 )$ in the encorafenib plus binimetinib arm; Fig. 4C] and OS [HR, 0.24 (P ¼ 0.0016); 0.60 (P ¼ 0.094), respectively; Fig. 4D] compared with patients for whom ctDNA remained detectable. Detectability of BRAF V600 alterations in ctDNA at baseline was also strongly associated with serum lactate dehydrogenase (LDH) levels. Among ctDNA-evaluable patients with greater than the upper limit of normal (ULN) for LDH (mean, 639.2 U/L in ctDNAevaluable cases), >99% had a BRAF V600 alteration detected, with only a single case with nondetection (n ¼ 103/104 detected). Conversely, 68.1% (158/232) of patients with the ULN or lower for LDH (mean, 168.7 U/L) had an alteration detected [P < 0.0001 (Fisher exact test)]. As expected, baseline LDH was strongly prognostic for both PFS and OS in ctDNA-evaluable cases, with higher risk in >ULN groups (HR ranged from 2.3 to 4.9 across arms for PFS and 3–3.3 for OS; all P < 0.001), with no evidence of differential effects across arms (Supplementary Fig. S7).

To better interpret the relative associations of the above factors with patient outcomes, we examined the correlation among these variables and used recursive partitioning to model OS in the encorafenib and encorafenib plus binimetinib arms. This analysis included LDH, cytolytic score, BRAF V600 VAF/ detection in baseline ctDNA, TMB, and MITF and ERBB expression as predictors. Correlations were based on continuous marker values and recursive partitioning based on the cutpoints tested above and included only patients with complete data for these markers. Correlation analysis (n ¼ 161 across arms) was consistent with previous observations, with the strongest correlation observed between ctDNA BRAF V600 allele frequency and LDH (r ¼ 0.52), followed by more modest negative correlations among gene expression features that reflected previous clustering analyses (Supplementary Fig. S8). Survival analysis largely recapitulated previous univariable analyses, with LDH ranked as the most important factor in both arms; in the encorafenib plus binimetinib arm (n ¼ 67), the longest survival was observed in patients with ≤ULN LDH, high cytolytic scores, and high TMB (median OS, 97.4 months; Supplementary Fig. S9), in contrast to patients with >ULN LDH and high ERBB2 expression (median OS, 10.8 months). In the encorafenib arm (n ¼ 54), the longest survival was observed in patients with ≤ULN LDH and low MITF expression (median OS, 46.4 months), in contrast to patients in the >ULN LDH group (median OS, 9.89 months).

A  
<!-- image-->

C  
<!-- image-->

B  
<!-- image-->

D  
<!-- image-->

E  
<!-- image-->

<!-- image-->

<!-- image-->

F  
<!-- image-->  
Figure 1.  
PFS and OS for encorafenib plus binimetinib or encorafenib vs. vemurafenib by (A and B) TMB and (C and D) cytolytic score. E, Volcano plots of univariable gene expression associations with OS in each arm based on z-scored gene expression values. F, Gene-set enrichment analysis of gene expression associations against hallmark gene signatures; signatures with greatest average NES across arms shown. Bini, binimetinib; BM, biomarker; CYT, cytotoxic score; Enco, encorafenib; NES, normalized enrichment scores; Vemu, vemurafenib.

<!-- image-->

C  
<!-- image-->

B  
<!-- image-->

D  
<!-- image-->  
Figure 2.  
PFS and OS for encorafenib plus binimetinib or encorafenib vs. vemurafenib by (A and B) ERBB2 expression level and (C and D) PI3K pathway mutation status. Bini, binimetinib; BM, biomarker; Enco, encorafenib; Vemu, vemurafenib.

## Discussion

Exploratory analyses based on the 7-year follow-up of the COLUMBUS study indicate that survival benefits from encorafenib plus binimetinib were observed across most molecular subgroups in BRAF V600E/K–mutant melanoma, and no subgroups showed inferior outcomes when treated with encorafenib plus binimetinib versus vemurafenib. Benefits with encorafenib monotherapy versus vemurafenib were less pronounced than with encorafenib plus binimetinib, supporting the use of the BRAF inhibitor ± MEK inhibitor combination over a singleagent BRAF inhibitor.

The PFS and/or OS benefits with encorafenib plus binimetinib versus vemurafenib were greater among patient subgroups with evidence of potential for antitumor immune response at study entry (e.g., higher TMB, cytolytic score, PD-L1 expression, and IFNγ gene expression signature scores) compared with subgroups with low levels of these biomarkers. Notably, although PFS was improved with encorafenib plus binimetinib versus vemurafenib regardless of immune-related biomarker levels, an OS benefit was only observed for patients in the high TMB, cytolytic score, PD-L1 expression, and IFNγ gene expression signature groups.

In contrast to the aforementioned patient subgroups, patients with PI3K pathway mutations seem to have a smaller benefit with encorafenib plus binimetinib, but this benefit remains superior to vemurafenib. As has been previously suggested (22), this suggests a potential role for the PI3K pathway in intrinsic or acquired resistance to encorafenib plus binimetinib. Dysregulation of the PI3K pathway as a factor contributing to acquired resistance to BRAF inhibitors in melanoma has been documented in previous studies (23, 24). It was notable that the same effect was not observed with encorafenib monotherapy, in which patients with PI3K pathway mutations instead seemed to have improved outcomes. The driver of this potential disparity remains unclear, and additional work with larger sample sizes will be required to confirm the effect. The reduced treatment benefits over vemurafenib in patients with mutations in the PI3K pathway may support a potential role for the PI3K pathway in resistance to treatment that warrants follow-up.

Reduced survival benefits with encorafenib plus binimetinib versus vemurafenib were also observed for patient subgroups with high ERBB2 (HER2) expression, compared with those who had low ERBB2 expression, suggesting a potential role ERBB2 in resistance to encorafenib plus binimetinib. Melanoma is not typically considered to be a candidate for HER2-targeting therapies due to substantially lower HER2 positivity rates and expression levels than observed in cancers that are commonly HER2-amplified (25). However, expression (measured via RNA-seq) was elevated in invasive subgroups, and potential for synergistic therapies that target lower levels of expression may be possible. Resistance associated with HER2 overexpression may also be mediated by downstream PI3K pathway activation (26). Resistance to BRAF inhibitors remains a clinical problem in the BRAF V600E/K–mutant metastatic melanoma landscape (23), and patients with PI3K pathway mutations or those with higher ERBB2 expression may benefit from the addition of other therapies to encorafenib plus binimetinib.

A  
<!-- image-->

<!-- image-->

<!-- image-->  
Figure 3.  
Characterization of tumor samples to identify candidate molecular subtypes by K-means clustering and distribution of subtypes by biopsy site. A, Heatmap showing K-means cluster and the expression of key marker genes (AXL and MITF) and cell type scores generated by xCell. B, Distribution of K-means subgroups across biopsy sites. C, OS by K-means subgroup and treatment arm. Bini, binimetinib; Vemu, vemurafenib.

The identification and characterization of tumor subtypes—immune, invasive, and melanocytic/proliferative—based on gene expression and biomarker analyses are consistent with prior classification of melanomas as invasive versus proliferative and further delineate a subgroup with markedly higher immune infiltration. Consistent with the analysis of individual biomarkers, the immune subtype demonstrated the longest OS. Associations between proliferative and invasive melanoma markers (27), such as MITF and AXL, respectively, and survival outcomes suggest that melanocyte plasticity may influence therapeutic response. The overall negative prognostic impact of high levels of MITF on PFS and OS across the encorafenib plus binimetinib, encorafenib monotherapy, and vemurafenib treatment arms is consistent with previous suggestions that MITF expression is associated with resistance to targeted therapy (28).

The observation that encorafenib plus binimetinib resulted in a more pronounced treatment benefit versus vemurafenib in patients with tumors with evidence of immune infiltration is consistent with previous biomarker analyses that reported a benefit of BRAF inhibitor ± MEK inhibitor combinations for patients with BRAFmutant melanoma with an elevated IFNγ signature and an immune signature that included GZMA (a component of the cytolytic score), among other genes (29, 30). It also parallels a beneficial effect of a high cytolytic score observed in patients with BRAF-mutant colorectal cancer treated with encorafenib plus binimetinib (plus cetuximab) in the BEACON study (31), suggesting that immunologic correlates of benefit from encorafenib plus binimetinib may be observable in multiple cancer types.

<!-- image-->

C  
<!-- image-->

B  
<!-- image-->

D  
<!-- image-->  
PFS and OS by detection of BRAF V600 alterations in ctDNA at (A and B) baseline and (C and D) on treatment. Only patients with BRAF V600 alteration detections at baseline are shown in C and D. Bini, binimetinib; D, detectable; Enco, encorafenib; ND, nondetectable; Vemu, vemurafenib.

Whereas patients historically received BRAF inhibitor plus MEK inhibitor combinations as first-line therapy for BRAF V600–mutant melanoma, treatment paradigms have fundamentally shifted following recent clinical trial results. The DREAMseq trial showed superior outcomes with immunotherapy-first approaches, with 2-year OS of 72% versus 52% for targeted-therapy-first approaches (32). Current practice guidelines now recommend immunotherapy as first-line treatment for most patients with BRAF V600–mutant melanoma, reserving BRAF/MEK inhibitors for second-line therapy after immunotherapy failure or in specific clinical scenarios requiring rapid disease control (8). Our results suggest that an immune-infiltrated TME may lead to increased benefit from encorafenib plus binimetinib, which might be potentiated by prior immunotherapy. However, the SECOMBIT study found numerically lower response rates to encorafenib plus binimetinib after progression on nivolumab plus ipilimumab than in first-line therapy, suggesting that other factors may overcome a priming effect of immunotherapy, if present (33). Due to the era of this study, very few patients had been previously treated with immune checkpoint blockade, and we were unable to robustly evaluate this possibility in this study (4, 17). Furthermore, similar preclinical and clinical findings suggesting that BRAF inhibitors and/or MEK inhibitors engage or exploit the immune system have led to multiple (34) phase II and III trials, including COMBI-I, IMspire150, and KEYNOTE-022, that explored the combination of BRAF inhibitors/MEK inhibitors and immune checkpoint blockade. The results of these studies have so far failed to lead to a recommendation of combination triplet therapies for BRAFmutant melanoma in routine clinical practice (4, 35, 36). Observations of the expected immunostimulatory effects of MEK inhibition alone have led to trials such as IMspire170, which combined an MEK inhibitor (cobimetinib) with immune checkpoint blockade in BRAF-WT melanoma, but failed to demonstrate clear benefit. The ongoing

STARBOARD and PORTSIDE studies combine encorafenib and binimetinib with pembrolizumab or nivolumab plus ipilimumab, respectively, and may help clarify the potential for immune synergies suggested (37, 38). The detectability of BRAF V600 alterations in ctDNA at baseline and changes in detectability during treatment were associated with PFS and OS across treatment arms, with effect sizes largely consistent with those observed in a meta-analysis of metastatic melanoma studies (39). Detection of BRAF V600 alterations at baseline was highly correlated with serum LDH, but alterations were still frequently detectable in patients with LDH below the ULN, suggesting potential value for ctDNA profiling in patients with lower LDH levels. Thus, these results are in accord with the use of ctDNA as a marker of survival and/ or response in BRAF V600E/K–mutant advanced or metastatic melanoma that warrants further validation.

This analysis pooled data from the encorafenib plus binimetinib arms in COLUMBUS part 1 (encorafenib 450 mg once daily) and part 2 (encorafenib 300 mg once daily), which limits conclusions regarding encorafenib dosing in the combination regimen and potentially biomarker comparisons among arms in this study. Furthermore, as this was a retrospective analysis, it was not able to address all hypotheses of interest with sufficient or equivalent power, and further prospective analyses are needed to validate the findings proposed here. These analyses corroborated a greater benefit of encorafenib plus binimetinib versus vemurafenib across genetic and transcriptional biomarker subgroups and did not identify any subgroups of patients who had improved outcomes with vemurafenib versus encorafenib plus binimetinib. Increased benefit was most notable in tumors with evidence of immune infiltration or potential for antitumor immune response (e.g., with elevated TMB), thus supporting the hypothesis that encorafenib plus binimetinib might show synergistic effects when combined with immunotherapies.

In conclusion, survival benefit from encorafenib ± binimetinib was observed across the majority of molecular subgroups, and this benefit was most pronounced in patients treated with encorafenib plus binimetinib with heightened signatures of immune infiltration and elevated TMB.

## Data Availability

Upon request, and subject to review, Pfizer will provide the data that support the findings of this study. Subject to certain criteria, conditions, and exceptions, Pfizer may also provide access to the related individual deidentified participant data. See https://www.pfizer.com/science/clinical-trials/trialdata-and-results for more information and for instructions on how to submit a request.

## Authors’ Disclosures

R. Dummer has intermittent, project-focused consulting and/or advisory relationships with Novartis, MSD, Bristol Myers Squibb, Roche, Amgen, Takeda, Pierre Fabre, Sun Pharma, Sanofi, CatalYm, Second Genome, Regeneron, T3 Pharma, MaxiVAX SA, Pfizer, Simcere, and Iovance outside the submitted work; is a senior medical advisor of Oncobit; and has participated on Derma2go outside the submitted work. S. Deng reports employment, stock, and other ownership interests with Pfizer. C. Robert reports personal fees from Pierre Fabre, Bristol Myers Squibb, MSD, Merck, Roche, Pfizer, Sun Pharma, Regeneron, Maat Pharma, Iovance, Moderna, and Immatics outside the submitted work. A. Arance reports other support from BioNTech, Bristol Myers Squibb, Genmab, MSD, Biontech, HUYABIO International, Immunocore, IO Biotech, Iovance Biotherapeutics, Novartis, Pierre Fabre, Replimune, and Sairopa outside the submitted work. C. Garbe reports personal fees from CeCaVa, MSD, NeraCare, and Philogen outside the submitted work. H.J. Gogas reports grants from ARRAY during the conduct of the study; grants and personal fees from Bristol Myers Squibb, MSD, and Regeneron; and grants from Pfizer and Replimmune outside the submitted work.

R. Gutzmer reports other support from Novartis during the conduct of the study; grants from Amgen, Sanofi, Regeneron, Kyowa-Kirin, Almirall, SUN Pharma, and Recordati; and personal fees from Bristol Myers Squibb, Novartis, MSD, Almirall, Pierre Fabre, Merck, SUN Pharma, Sanofi, Regeneron, Immunocore, Delcath, Kyowa-Kirin, Incyte, and Janssen outside the submitted work. C. Loquai reports advisory board membership, travel reimbursement, and honoraria from Bristol Myers Squibb, Merck, BioNTech, Regeneron, Lilly, Pfizer, Sanofi, MSD, Novartis, and Almirall Hermal. M. Mandala reports grants and personal fees from Novartis and personal fees from Regeneron, Bristol Myers Squibb, Sun Pharma, MSD, and Immunocore outside the submitted work. D. Schadendorf reports personal fees, nonfinancial support, and other support from Regeneron and Pierre Fabre; grants, personal fees, nonfinancial support, and other support from MSD; grants, personal fees, and other support from Bristol Myers Squibb; personal fees from Novartis; personal fees and other support from Immatics, Immunocore, IOBioTech, Philogen, and BioNTech; and personal fees from Allmiral, Boehringer Ingelheim, ImCheck, Iovance, Neracare, SkylineDX, Merck-Serono, Moderna, EeBeTe, and Ipsen during the conduct of the study. N. Yamazaki reports personal fees from ONO; grants and personal fees from Bristol Myers Squibb, MSD, and Novartis; and grants from HUYA and Regeneron outside the submitted work. P.A. Ascierto reports grants and personal fees from Bristol Myers Squibb, Roche-Genentech, and Medicenna; personal fees and other support from Pierre Fabre, Pfizer, Bio AI Health, Replimmune, Philogen, and MSD; and personal fees from Novartis, Sun Pharma, Immunocore, Italfarmaco, Boehringer Ingelheim, Regeneron, Nouscom, ValoTx, Erasca, IO-Biontech, Anaveon, Genmab, Menarini, Incyte, and ImCheck Therapeutics outside the submitted work. K. Shah reports employment, stock, and other ownership interests with Pfizer. P. Hamilton reports employment, stock, and other ownership interests with Pfizer. A. di Pietro reports employment, stock, and other ownership interests with Pfizer. K.T. Flaherty reports other support from Khora Therapeutics, Clovis Oncology, Kinnate Biopharma, Checkmate Pharmaceuticals, Strata Oncology, Scorpion Therapeutics, PIC Therapeutics, Apricity, Parabalis, Tvarrdi, xCures, Monopteros, Vibliome, ALX Oncology, Karkinos, Soley Therapeutics, Alterome, IntrECate, PreDICTA, Tasca Therapeutics, Genentech, Takeda, Transcode Therapeutics, Nextech Invest, and Novartis during the conduct of the study. No disclosures were reported by the other authors.

## Authors’ Contributions

R. Dummer: Conceptualization, data curation, supervision, validation, visualization, investigation, methodology, writing–original draft, writing–review and editing. S. Deng: Data curation, formal analysis, writing–original draft, writing–review and editing. T. Xie: Data curation, formal analysis, writing–review and editing. N. Pathan: Conceptualization, writing–review and editing. H. Saffari: Data curation, formal analysis, writing–review and editing. C. Robert: Investigation, writing–review and editing. A. Arance: Investigation, writing–review and editing. J.W.B. de Groot: Investigation, writing–review and editing. C. Garbe: Investigation, writing–review and editing. H.J. Gogas: Investigation, writing–review and editing. R. Gutzmer: Investigation, writing–review and editing. I. Krajsova´: Investigation, writing–review and editing. G. Liszkay: Validation, investigation, writing–review and editing. C. Loquai: Investigation, writing–review and editing. M. Mandala: Investigation, writing–review and editing. D. Schadendorf: Investigation, writing–review and editing. N. Yamazaki: Investigation, writing–review and editing. P.A. Ascierto: Investigation, writing–review and editing. C.B. Davis: Conceptualization, formal analysis, writing–original draft, writing–review and editing. K. Shah: Writing– original draft, writing–review and editing. P. Hamilton: Data curation, formal analysis, writing–original draft, writing–review and editing. A. di Pietro: Conceptualization, writing–original draft, writing–review and editing. K. Flaherty: Investigation, writing–review and editing.

## Acknowledgments

The authors thank the participants and their families, as well as the staff at the participating sites. This study was sponsored by Array BioPharma, which was acquired by Pfizer in July 2019. Medical writing support was provided by Blaise Low, PhD, Tina Wasmeier, PhD, and Eleanor Porteous, MSc, at Nucleus Global, an Inizio company, and was funded by Pfizer.

## Note

Supplementary data for this article are available at Clinical Cancer Research Online (http://clincancerres.aacrjournals.org/).

Received September 23, 2025; revised November 19, 2025; accepted January 12, 2026; posted first January 15, 2026.

## References

1. Davies H, Bignell GR, Cox C, Stephens P, Edkins S, Clegg S, et al. Mutations of the BRAF gene in human cancer. Nature 2002;417:949–54.

2. Schadendorf D, van Akkooi ACJ, Berking C, Griewank KG, Gutzmer R, Hauschild A, et al. Melanoma. Lancet 2018;392:971–84.

3. Siroy AE, Boland GM, Milton DR, Roszik J, Frankian S, Malke J, et al. Beyond BRAF(V600): clinical mutation panel testing by next-generation sequencing in advanced melanoma. J Invest Dermatol 2015;135:508–15.

4. Dummer R, Ascierto PA, Gogas HJ, Arance A, Mandala M, Liszkay G, et al. Encorafenib plus binimetinib versus vemurafenib or encorafenib in patients with BRAF-mutant melanoma (COLUMBUS): a multicentre, open-label, randomised phase 3 trial. Lancet Oncol 2018;19:603–15.

5. Schadendorf D, Dummer R, Flaherty KT, Robert C, Arance A, de Groot JWB, et al. COLUMBUS 7-year update: a randomized, open-label, phase III trial of encorafenib plus binimetinib versus vemurafenib or encorafenib in patients with BRAF V600E/K-mutant melanoma. Eur J Cancer 2024;204:114073.

6. NCCN. NCCN guidelines for patients: melanoma. Plymouth Meeting (PA): NCCN; 2025 [cited 2024 Sept 26]. Available from: https://www.nccn.org/ patients/guidelines/content/PDF/melanoma-patient.pdf.

7. Gouda MA, Subbiah V. Precision oncology for BRAF-mutant cancers with BRAF and MEK inhibitors: from melanoma to tissue-agnostic therapy. ESMO Open 2023;8:100788.

8. Amaral T, Ottaviano M, Arance A, Blank C, Chiarion-Sileni V, Donia M, et al. Cutaneous melanoma: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. Ann Oncol 2025;36:10–30.

9. Ascierto PA, Dummer R, Gogas HJ, Flaherty KT, Arance A, Mandala M, et al. Update on tolerability and overall survival in COLUMBUS: landmark analysis of a randomised phase 3 trial of encorafenib plus binimetinib vs vemurafenib or encorafenib in patients with BRAF V600-mutant melanoma. Eur J Cancer 2020;126:33–44.

10. Shi H, Hugo W, Kong X, Hong A, Koya RC, Moriceau G, et al. Acquired resistance and clonal evolution in melanoma during BRAF inhibitor therapy. Cancer Discov 2014;4:80–93.

11. Rambow F, Rogiers A, Marin-Bejar O, Aibar S, Femel J, Dewaele M, et al. Toward minimal residual disease-directed therapy in melanoma. Cell 2018; 174:843–55.e19.

12. Vasilevska J, Cheng PF, Lehmann J, Ramelyte E, Gomez ´ JM, Dimitriou F, et al. Monitoring melanoma patients on treatment reveals a distinct macrophage population driving targeted therapy resistance. Cell Rep Med 2024;5:101611.

13. Muller ¨ J, Krijgsman O, Tsoi J, Robert L, Hugo W, Song C, et al. Low MITF/ AXL ratio predicts early resistance to multiple targeted drugs in melanoma. Nat Commun 2014;5:5712.

14. Frederick DT, Piris A, Cogdill AP, Cooper ZA, Lezcano C, Ferrone CR, et al. BRAF inhibition is associated with enhanced melanoma antigen expression and a more favorable tumor microenvironment in patients with metastatic melanoma. Clin Cancer Res 2013;19:1225–31.

15. Haselmann V, Gebhardt C, Brechtel I, Duda A, Czerwinski C, Sucker A, et al. Liquid profiling of circulating tumor DNA in plasma of melanoma patients for companion diagnostics and monitoring of BRAF inhibitor therapy. Clin Chem 2018;64:830–42.

16. Dummer R, Ascierto PA, Gogas HJ, Arance A, Mandala M, Liszkay G, et al. Overall survival in patients with BRAF-mutant melanoma receiving encorafenib plus binimetinib versus vemurafenib or encorafenib (COLUMBUS): a multicentre, open-label, randomised, phase 3 trial. Lancet Oncol 2018;19: 1315–27.

17. Dummer R, Flaherty KT, Robert C, Arance A, de Groot JWB, Garbe C, et al. COLUMBUS 5-year update: a randomized, open-label, phase III trial of encorafenib plus binimetinib versus vemurafenib or encorafenib in patients with BRAF V600-mutant melanoma. J Clin Oncol 2022;40:4178–88.

18. Ascierto PA, Dummer R, Gogas HJ, Arance A, Mandala M, Liszkay G, et al. Contribution of MEK inhibition to BRAF/MEK inhibitor combination treatment of BRAF-mutant melanoma: part 2 of the randomized, open-label, phase III COLUMBUS trial. J Clin Oncol 2023;41:4621–31.

19. Aran D, Hu Z, Butte AJ. xCell: digitally portraying the tissue cellular heterogeneity landscape. Genome Biol 2017;18:220.

20. Rooney MS, Shukla SA, Wu CJ, Getz G, Hacohen N. Molecular and genetic properties of tumors associated with local immune cytolytic activity. Cell 2015; 160:48–61.

21. Tirosh I, Izar B, Prakadan SM, Wadsworth MH 2nd, Treacy D, Trombetta JJ, et al. Dissecting the multicellular ecosystem of metastatic melanoma by singlecell RNA-seq. Science 2016;352:189–96.

22. Irvine M, Stewart A, Pedersen B, Boyd S, Kefford R, Rizos H. Oncogenic PI3K/ AKT promotes the step-wise evolution of combination BRAF/MEK inhibitor resistance in melanoma. Oncogenesis 2018;7:72.

23. Zhong J, Yan W, Wang C, Liu W, Lin X, Zou Z, et al. BRAF inhibitor resistance in melanoma: mechanisms and alternative therapeutic strategies. Curr Treat Options Oncol 2022;23:1503–21.

24. Proietti I, Skroza N, Bernardini N, Tolino E, Balduzzi V, Marchesiello A, et al. Mechanisms of acquired BRAF inhibitor resistance in melanoma: a systematic review. Cancers (Basel) 2020;12:2801.

25. Yan M, Schwaederle M, Arguello D, Millis SZ, Gatalica Z, Kurzrock R. HER2 expression status in diverse cancers: review of results from 37,992 patients. Cancer Metastasis Rev 2015;34:157–64.

26. Pan L, Li J, Xu Q, Gao Z, Yang M, Wu X, et al. HER2/PI3K/AKT pathway in HER2-positive breast cancer: a review. Medicine (Baltimore) 2024;103:e38508.

27. Hoek KS, Eichhoff OM, Schlegel NC, Dobbeling ¨ U, Kobert N, Schaerer L, et al. In vivo switching of human melanoma cells between proliferative and invasive states. Cancer Res 2008;68:650–6.

28. Tangella LP, Clark ME, Gray ES. Resistance mechanisms to targeted therapy in BRAF-mutant melanoma - a mini review. Biochim Biophys Acta Gen Subj 2021;1865:129736.

29. Dummer R, Brase JC, Garrett J, Campbell CD, Gasal E, Squires M, et al. Adjuvant dabrafenib plus trametinib versus placebo in patients with resected, BRAFV600-mutant, stage III melanoma (COMBI-AD): exploratory biomarker analyses from a randomised, phase 3 trial. Lancet Oncol 2020;21:358–72.

30. Wongchenko MJ, McArthur GA, Dr´eno B, Larkin J, Ascierto PA, Sosman J, et al. Gene expression profiling in BRAF-mutated melanoma reveals patient subgroups with poor outcomes to vemurafenib that may be overcome by cobimetinib plus vemurafenib. Clin Cancer Res 2017;23:5238–45.

31. Kopetz S, Murphy DA, Pu J, Ciardiello F, Desai J, Van Cutsem E, et al. Molecular profiling of BRAF-V600E-mutant metastatic colorectal cancer in the phase 3 BEACON CRC trial. Nat Med 2024;30:3261–71.

32. Atkins MB, Lee SJ, Chmielowski B, Tarhini AA, Cohen GI, Truong TG, et al. Combination dabrafenib and trametinib versus combination nivolumab and ipilimumab for patients with advanced BRAF-mutant melanoma: the DREAMseq trial-ECOG-ACRIN EA6134. J Clin Oncol 2023;41:186–97.

33. Ascierto PA, Mandala \` M, Ferrucci PF, Guidoboni M, Rutkowski P, Ferraresi V, et al. Sequencing of ipilimumab plus nivolumab and encorafenib plus binimetinib for untreated BRAF-mutated metastatic melanoma (SECOM-BIT): a randomized, three-arm, open-label phase II trial. J Clin Oncol 2023; 41:212–21.

34. Liu Y, Zhang X, Wang G, Cui X. Triple combination therapy with PD-1/PD-L1, BRAF, and MEK inhibitor for stage III-IV melanoma: a systematic review and meta-analysis. Front Oncol 2021;11:693655.

35. Gutzmer R, Stroyakovskiy D, Gogas H, Robert C, Lewis K, Protsenko S, et al. Atezolizumab, vemurafenib, and cobimetinib as first-line treatment for unresectable advanced BRAFV600 mutation-positive melanoma (IMspire150): primary analysis of the randomised, double-blind, placebo-controlled, phase 3 trial. Lancet 2020;395:1835–44.

36. Ferrucci PF, Di Giacomo AM, Del Vecchio M, Atkinson V, Schmidt H, Schachter J, et al. KEYNOTE-022 part 3: a randomized, double-blind, phase 2 study of pembrolizumab, dabrafenib, and trametinib in BRAF-mutant melanoma. J Immunother Cancer 2020;8:e001806.

37. Dudnichenko O, Penkov K, McKean M, Mandala \` M, Kukushkina M, Panella T, et al. First-line encorafenib plus binimetinib and pembrolizumab for advanced BRAF V600-mutant melanoma: safety lead-in results from the randomized phase III STARBOARD study. Eur J Cancer 2024;213:115070.

38. Schadendorf D, Dummer R, Ribas A, Robert C, Sullivan RJ, King A, et al. 1180TiP Randomized phase II trial (PORTSIDE) evaluating encorafenib (enco) and binimetinib (bini) plus pembrolizumab (pembro) versus nivolumab (nivo) and ipilimumab (ipi) for the treatment of advanced BRAF-mutant melanoma. Ann Oncol 2023;34:S700.

39. Gracie L, Pan Y, Atenafu EG, Ward DG, Teng M, Pallan L, et al. Circulating tumour DNA (ctDNA) in metastatic melanoma, a systematic review and metaanalysis. Eur J Cancer 2021;158:191–207.