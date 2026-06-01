RESEARCH

Open Access

# Optimizing treatment and sequencing strategies for maximal survival and net health benefits in ALK-positive NSCLC: a systematic review and reconstructed individual patient data meta-analysis

<!-- image-->

Mingye Zhao1,2†, Jiaqi Li1,2†, Yunlin Jiang4 , Hanqiao Shao1,2, Jin Huang3\* and Wenxi Tang1,2\*

## Abstract

Methods Related data from phase Ⅱ-Ш clinical trials targeting ALK-positive NSCLC was identified through a systematic search of PubMed, EMBASE, the Cochrane Library, and ClinicalTrials.gov. Progression-free survival (PFS) and overall survival (OS) estimates were derived from Kaplan-Meier curves using individual participant data. Life-year gained (LYG) was the main efficacy outcome. Safety was evaluated by all-cause grade 3 + adverse events. Survival outcomes across treatment sequences were projected using a clock-reset semi-Markov model. Quality-adjusted life year (QALY) was used as the metric for NHB to evaluate the comprehensive value of treatment effectiveness and safety. Sensitivity and scenario analyses were conducted to validate our findings.

Results A total of 27 studies were included. Lorlatinib maximized LYG and NHB as both first-line and post-crizotinib second-line therapy. Alectinib led LYG and NHB after chemotherapy resistance, while brigatinib topped after alectinib resistance. Chemotherapy followed by alectinib or brigatinib, resulted in the highest LYG for first-line to second-line PFS, with the alectinib-brigatinib sequence delivering the highest NHB. For first-line to third-line PFS, the chemotherapy-alectinib-brigatinib sequence maximized survival, while alectinib-brigatinib-lorlatinib was optimal for NHB. Frontline second-generation ALK-TKI enhanced boost survival and NHB, using first-generation ALK-TKI before chemotherapy had little impact on survival but improved initial NHB. Safety profiles emphasized alectinib as the safest first-line option, with iruplinalkib being the most favorable option after crizotinib resistance. Uncertainty analysis indicated that the findings were robust.

Conclusions According to current analyses, lorlatinib is an optimal first-line therapy. Alectinib and brigatinib are effective subsequent treatments in cases of non-lorlatinib resistance. First-line ALK-TKIs optimize patient benefits, and carefully sequenced treatments offer substantial survival and NHB across all stages of therapy.

Keywords ALK-TKIs, Non-small-cell lung cancer, Systemic therapy, Sequential therapy, Net health benefit

## Introduction

About 50–60% of non-small-cell lung cancer (NSCLC) cases present with known driver mutations, which benefit from targeted therapy [1, 2]. In recent decades, progress in translational research and drug discovery has enabled the molecular classification of NSCLC, particularly adenocarcinomas, by identifying oncogenic drivers with activating mutations in EGFR or fusions involving ALK, RET, and ROS1 kinases [1, 2]. Anaplastic lymphoma kinase (ALK) gene fusion characterizes a distinct molecular subtype of NSCLC [3]. This chromosomal rearrangement on chromosome 2 leads to the aberrant expression and constitutive activation of the ALK tyrosine kinase domain. ALK-positive lung cancers depend on ALK signaling and generally respond to inhibition via ALK-tyrosine kinase inhibitors (ALK-TKIs) [4–6].

As of December 2023, five ALK-TKIs have been approved by the U.S. Food and Drug Administration (FDA), and an additional three have been approved by the National Medical Products Administration (NMPA) for the treatment of advanced ALK-positive NSCLC [5–17], including crizotinib, ceritinib, lectinib, brigatinib, ensartinib, envonalkib, iruplinalkib, and lorlatinib (Notably, iruplinalkib, ensartinib, and envonalkib have not yet been approved by the FDA for the treatment of ALK-positive NSCLC). Crizotinib, as a first-generation ALK-inhibitor, was the first to receive approveby the U.S. Food and Drug Administration (FDA) in August 2011. In first-line treatment, compared to chemotherapy, crizotinib improved the median progression-free survival (PFS) from 7.0 months (95% confidence interval [CI], 6.8–8.2) to 10.9 (8.3–13.9) [14]. Nevertheless, the median PFS for patients treated with crizotinib is limited to 8–11 months, with central nervous system (CNS) relapse occurring due to inadequate drug penetration of the blood-brain barrier. Several second-generation ALK TKIs, including ceritinib, alectinib, and brigatinib, have shown efficacy in the CNS and overcome crizotinib-refractory ALK resistance mutations. Compared with chemotherapy, ceritinib increased the PFS from 8.1 months (5.8–11.1) to 16.6 months (12.6–27.2). The results of the ALEX trial confirmed that alectinib significantly improved PFS (hazards ratios [HR], 0.43 [95% CI, 0.32–0.58]) and overall survival (OS) (0.67 [0.46–0.98]) compared to crizotinib [18]. Similarly, the ALTA-1  L results also demonstrated the significant advantage of brigatinib over crizotinib in improving PFS (0.48 [0.35–0.66]) [19]. Lorlatinib is a third-generation macrocyclic ALK TKI with strong activity against wild-type ALK and most resistance mutations, including ALKG1202R. The CROWN showed significantly longer PFS (HR 0.28) and reduced CNS progression risk (HR 0.07) compared to crizotinib, leading to first-line approval in 2021 [15]. The latest American Society of Clinical Oncology (ASCO) meeting reported 5-year update results from the CROWN study, showing a 60-month PFS of 60% for lorlatinib, compared to only 8% for crizotinib [20]. Additionally, ensartinib and envonalkib, as second-generation ALK-TKIs, have also demonstrated significant superiority over crizotinib in PFS [17, 21]. For patients resistant to crizotinib, second and third-generation ALK-TKIs have also significantly improved survival. Median PFS was 5.4 months for ceritinib, 10.9 for alectinib, 19.3 for brigatinib, 19.8 for iruplinalkib, 9.6 for ensartinib, and not reached for lorlatinib, all surpassing chemotherapy at 1.6 months, significantly enhancing survival [11, 22–26].

Identifying the optimal treatment sequence for survival is critical in clinical practice. The IFCT-1302 CLINALK study retrospectively analyzed ALK-positive NSCLC patients treated with crizotinib followed by second-generation ALK-TKIs like ceritinib or alectinib, revealing a median OS of 89.6 months [27]. The WJOG 9516 L study reported an OS benefit of 88.4 months for crizotinib followed by alectinib [28]. U.S. real-world data showed an OS of 86 months with this sequence [29]. Collectively, these studies suggest that starting with first-generation ALK inhibitors and transitioning to second-generation ALK-TKIs can result in a median OS of over 7 years.

Navigating treatment options and sequencing is complex. The optimal strategy should be based on a comprehensive evaluation of efficacy and safety, synthesized from data across phase Ⅱ-Ⅲ RCTs and broad patient cohorts [30]. Trials like PROFILE 1014, ALEX, ALTA-1 L, CROWN, and others provide critical insights into crizotinib’s performance, but a comprehensive aggregate analysis is still lacking. Current clinical evidence on optimal treatment sequencing is limited, primarily from real-world studies. Further exploration of alternative sequences is necessary. Treatment decisions should balance the comprehensive value of drugs, integrating both safety and efficacy metrics to guide clinical choices.

In this study, we addressed three key challenges: the complexity of selecting and sequencing treatments, the lack of comprehensive data synthesis from phase Ⅱ-Ⅲ RCTs, and the scarcity of clinical evidence on optimal treatment sequencing [31–34]. We conducted a meta-analysis using reconstructed individual patient data (IPD) from clinical trials to obtain precise survival metrics, including median survival and interval-specific survival rates, while evaluating the safety of different regimens. This method accounts for censored data and evaluates long-term outcomes, tasks that previous traditional meta-analyses could not achieve [35]. Additionally, we employed a time-reset microsimulation model with reconstructed IPD to estimate survival outcomes for various treatment sequences, allowing for re-analysis via Kaplan-Meier and Cox regression [36–38]. Finally, we assessed the comprehensive value of treatments and sequences using Net Health Benefit (NHB).Specifically, NHB is a comprehensive metric that combines safety and efficacy to measure the overall impact of a medical intervention, balancing positive outcomes (e.g., improved survival rates, quality of life) against negative outcomes (e.g., side effects) [39].

## Methods

## Protocol and Search strategy

The literature review was conducted adhering to the PRISMA-IPD guidelines for systematic reviews of IPD [30]. Our study protocol has been registered with PROS-PERO (CRD42024498685, https://www.crd.york.ac.u k/prospero/). Details of the search methodology can be found in Additional File Part 1. The completed Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) checklist is available in Additional File 2. In summary, through December 2023, two investigators, Zhao and Li, performed a comprehensive search of databases including PubMed, EMBASE, the Cochrane Library, and ClinicalTrials.gov to identify related clinical trials. Search terms employed encompassed “ALK”, “Anaplastic Lymphoma Kinase”, “non-small-cell lung cancer”, “NSCLC”, “randomized controlled trials”, and “RCT”. The Languages were restricted to English.

## Study selection and data extraction

Titles and abstracts from the selected studies were first evaluated by two independent researchers, Zhao and Li. Should discrepancies arise, an oncology specialist convened for resolution. The inclusion criteria were based on the PICOS structure, detailed as follows:

(1)Population: Adults diagnosed with ALK-positive NSCLC via histology or cytology, including advanced-stage patients, without limitations on demographic or individual traits.

(2)Interventions and comparisons: Systematic interventions under consideration included medical, surgical, radiotherapeutic, and multimodal treatments.

(3)Outcomes: The study focused on PFS, OS, and adverse events (AEs, [grade 3 or above]).

(4)Study design: The research primarily included phase Ⅱ-Ⅲ clinical trials that provided the most current and comprehensive data, excluding older or redundant studies. Case reports, retrospective analyses, and real-world studies were not considered.

## Data extraction

Two independent investigators were tasked with data extraction. We compiled details such as the characteristics of the eligible studies, demographic information of the study populations, and aspects of the intervention programs.

## Statistical analyses

To enable a more thorough comparison, we analyzed all-cause grade 3 or higher AEs using a random-effects model from the Meta package to combine their incidence rates, since they are more frequently reported than treatment-related AEs in this area. In terms of survival estimation, IPDs were acquired utilizing the approach developed by Guyot, and Kaplan-Meier curves reported in publications were digitized using version 2.24 of the GetData Graph Digitizer software [40]. Once the IPD had been reconstructed, a pooled estimate of the survival was conducted. This analysis applied the MetaSurv method, where survival probabilities, transformed via the arcsine method, were combined through a random-effects model, culminating in a distribution-free aggregated survival curve [41]. Life-year gain (LYG) and landmark survival rates were used to describe survival. LYG represents the area under the curve (AUC) over a specific time period, similar to Restricted Mean Survival Time (RMST), as both reflect the AUC of KM curves over defined intervals [42–44]. Heterogeneity across studies was evaluated through the I2 statistic, presented visually in a forest plot. An I2 statistic exceeding 40% was deemed indicative of substantial heterogeneity, whereas a value below that threshold suggested low heterogeneity [45]. Additionally, we conducted multiple sensitivity analyses, including the exclusion of phase Ⅱ trials and comparison of phase Ⅱ and Ш trial results. Furthermore, for long-term survival projections, we employed parametric models to fit and extrapolate the aforementioned survival curves using reconstructed IPD. The considered parametric models included exponential, gamma, Gompertz, Weibull, generalized gamma, log-normal, log-logistic, fractional polynomial (FP), restricted cubic spline (RCS), and Royston-Parmar spline (RP) models. The goodnessof-fit criteria for model selection were evaluated based on the Akaike information criterion (AIC). Additionally, we visually inspected whether the survival curves conformed to clinical expectations, such as the presence or absence of a plateau phase [46]. Publication bias was assessed via Begg’s test using objective response rate, as HRs were often unavailable in single-arm trials.

To calculate and forecast the effectiveness of sequential treatment paths, we implemented an advanced clock-reset semi-Markov model using microsimulation to precisely determine survival probabilities and state transitions. The core advantage of this model lies in its consideration of memory: unlike the memoryless assumption of traditional Markov models, it is capable of capturing the relationship between the individual state transition probabilities and both the current state and the duration of time spent in that state. This method is crucial for capturing the temporal details of state transitions, especially when the duration of an individual in each state plays a decisive role in the overall dynamics of the system and in the cost-effectiveness analysis [35, 47, 48]. Through microsimulation, we can customize unique characteristics and historical trajectories for each individual, and record and analyze all relevant events and state transitions that occur during the simulation process. This method provides a deep understanding of complex health interventions and their long-term impacts and is an indispensable part of research [35, 49]. In addition, the virtual patient IPD generated by the microsimulation model provides us with a rich data foundation for conducting Kaplan-Meier analysis and Cox proportional hazards (Cox-PH) modelling, thereby enhancing the depth and breadth of our analysis. For more details, please refer to our previously published research [35]. Patients without progression or who died censored. Given the unavailability of reported time to progression (TTP) curves, we were compelled to infer probabilities of progression and non-progression directly from the available PFS curves. This assumption was reasonable, according to the INTELLECT study, where the PFS curve for the ALK-TKI was almost identical to the TTP curve [50]. The probability of death was determined by the information from the OS curve. Limited by the data available for analysis, this study analyzed four types of sequential paths: PFS 1–2, PFS 1–3, PFS 1 + OS 2, and PFS 1–2 + OS 3. The detailed definitions of the sequential paths are provided in Additional File Part 2. For each part, we constructed a cohort of 10,000 patients using Monte Carlo simulation. Based on this, we performed Kaplan-Meier analysis and compared the relative effects of different pathways using the Cox-PH model [51]. In evaluating the effectiveness of sequential treatment pathways, we performed multiple scenario analyses to confirm the robustness of our results. This included Scenario 1: in which the observation period was extended from 10 years to 40 years to achieve the effect of a lifetime simulation; Scenario 2: in which phase Ⅱ trials were excluded to avoid the impact of single-center or small-sample trials on the results; Scenario 3: in which phase Ⅱ trials and trials focusing on Asian populations were excluded.

To obtain NHB, clinical and safety outcomes were integrated to calculate a measure called quality-adjusted life year (QALY), as recommended by the National Institute for Health and Care Excellence (NICE) [52, 53]. The calculation method for the indicator was the LYG multiplied by the utility value, minus the disutility caused by adverse reactions. The utility values and the disutilities caused by adverse reactions are derived from a NICE guideline [54]. A discount of 3% (range: 0–5%) was applied for the calculation of NHB [55]. Additionally, probabilistic sensitivity analysis (PSA) was performed to verify the impact of parameter uncertainty on the results. Parameter ranges were set to their respective 95% CIs or when not available, assumed to vary within ± 5% of the mean [55]. For details on the parameter values, sources, and fluctuation ranges, see Additional File, Table S1.

## Results

## Characteristics of the included studies

Flowcharts detailing the selection process are available in Fig.  1. The search across the aforementioned databases yielded a total of 2005 records. Of these, we initially excluded 1760 records for not meeting our selection criteria. Subsequently, 245 studies were deemed potentially relevant and subjected to a thorough full-text examination. After applying the inclusion criteria, our network analysis incorporated 27 studies, comprising 14 phase Ⅲ trials [4–7, 9–13, 15, 17, 18, 22] and 13 phase Ⅱ trials [25, 26, 50, 56–65]. The treatments included in these studies were chemotherapy, crizotinib, alectinib, brigatinib, ceritinib, ensartinib, envonalkib, iruplinalkib, and lorlatinib. Additional details on the characteristics and publication information of the included studies are compiled in the Additional File, Table S2. Treatment regimens and evidence for sequential paths are shown in Fig.  2. No publication bias was detected by Begg’s test (z = -0.09, p = 0.931); the corresponding funnel plot is shown in Additional File, Figure S1.

## Pooled survival analysis across treatment regimens

In terms of first-line OS, the 12-month survival rates (Table  1) from highest to lowest were as follows: brigatinib (94.8%), alectinib (92.2%), envonalkib (90.6%), lorlatinib (89.3%), ensartinib (88.2%), crizotinib (87.8%), ceritinib (84.1%), and chemotherapy (78.7%). Regarding the 120-month LYG (Fig.  3A), the performance from highest to lowest was lorlatinib (87.06 months), ensartinib (80.2), alectinib (79.45), brigatinib (79.04), crizotinib (72.99), chemotherapy (57.15), and ceritinib (56.65). The sensitivity analysis results were consistent, see Table  1; Fig. 3A for more details on LYG (heterogeneity, and clinical evidence and sample size for survival estimates, etc.).

<!-- image-->  
Fig. 1 PRISMA study flow chart

Goodness-of-fit results for the survival curves of each treatment regimen can be found in Table S4. The NHBs at 120 months from highest to lowest were lorlatinib (5.15 QALYs; 97.8% probability of being best), alectinib (4.53), ensartinib (4.52), brigatinib (4.43), crizotinib (3.9), ceritinib (3.14), and chemotherapy (2.95). For more details, see Table  2. For first-line PFS, the 12-month survival rates (Table  1) from highest to lowest were brigatinib (85.9%), alectinib (77.5%), lorlatinib (75.7%), envonalkib (73.1%), ensartinib (65.8%), ceritinib (63%), crizotinib (49%), and chemotherapy (22.3%). For the 120-month LYG (Fig. 3B), the performance from highest to lowest was lorlatinib (77.97 months), alectinib (53.85), ensartinib (51.19), brigatinib (47.13), envonalkib (32.85), crizotinib (27.21), ceritinib (25.33), and chemotherapy (9.81). More details including the sensitivity analysis results can be seen in Table S3 and Fig.  3. The NHB results at 120 months (Table  2) indicated that lorlatinib (4.76 QALYs; 100% probability of being the best) remained the best option, followed by alectinib (3.39), ensartinib (3.23), brigatinib (2.99), envonalkib (2.12), crizotinib (1.77), ceritinib (1.65), and chemotherapy (0.65).

For second-line therapies resistant to crizotinib, in terms of PFS, 12-month survival rates (Table  1) from highest to lowest were lorlatinib (64.8%), iruplinalkib (56.9%), brigatinib (54.1%), alectinib (49.8%), ensartinib (38.4%), ceritinib (26%), and chemotherapy (5.7%). The 24-month LYGs (Fig.  3D) from highest to lowest were lorlatinib (16.33 months), iruplinalkib (15.66), brigatinib (14.88), alectinib (13.64), and ceritinib (9.39). For OS, 12-month survival rates (Table  1) from highest to lowest were lorlatinib (95.1%), iruplinalkib (85.2%), brigatinib (75%), alectinib (68.3%), chemotherapy (61.1%), crizotinib (60.7%). The 24-month LYGs (Fig.  3C) from highest to lowest were lorlatinib (23.27 months), brigatinib (19.25), alectinib (18.57), and chemotherapy (17.69). Table S3 and Fig.  3 provide more details, including the sensitivity analysis results. The NHB results suggested that for PFS, the top three were lorlatinib (1.33 QALYs; 58.1% probability of being the best), alectinib (1.32), and brigatinib (1.23). Similarly, for OS, lorlatinib (3.21 QALYs; 99.9% probability of being the best) remained the best option, followed by brigatinib (2.74). The complete results can be found in Table 2.

<table><tr><td rowspan=1 colspan=1>First-line (Evidence)</td><td rowspan=1 colspan=1>Second-line (Evidence)</td><td rowspan=1 colspan=1>Third-line (Evidence)</td></tr><tr><td rowspan=12 colspan=1>Chemotherapy(PROFILE 1014/PROFILE1029/ASCEND 4)</td><td rowspan=3 colspan=1>Alectinib(AF-001JP)</td><td rowspan=1 colspan=1>Brigatinib(J-ALTA)</td></tr><tr><td rowspan=1 colspan=1>Ceritinib(ASCEND-9)</td></tr><tr><td rowspan=1 colspan=1>Lorlatinib(exp 3B/NCT0390997 cohort2)</td></tr><tr><td rowspan=7 colspan=1>Crizotinib(Profile 1007)</td><td rowspan=1 colspan=1>Brigatinib(KIM 2017/ALTA-3L/ALTA)</td></tr><tr><td rowspan=1 colspan=1>Ceritinib(ASCEND 2/ASCEND 5/ASCEND-6)</td></tr><tr><td rowspan=1 colspan=1>Lorlatinib(exp 2-3A/NCT0390997 cohort1)</td></tr><tr><td rowspan=1 colspan=1>Alectinib (ALUR/ALTA-3L/Sai-Hong2015)</td></tr><tr><td rowspan=1 colspan=1>Ensartinib(Yang2017)</td></tr><tr><td rowspan=1 colspan=1>Iruplinalkib(INTELLECT)</td></tr><tr><td rowspan=1 colspan=1>Chemotherapy (ALUR/ASCEND 5)</td></tr><tr><td rowspan=1 colspan=1>Chemotherapy(Profile 1007)</td><td></td></tr><tr><td rowspan=1 colspan=1>Ceritinib (ASCEND 3)</td><td rowspan=1 colspan=1>Lorlatinib(exp 3B/NCT0390997 cohort2)</td></tr><tr><td rowspan=7 colspan=1>Crizotinib (PROFILE 1014/PROFILE1029/ALEX/ALESIA/J-ALEX/ALTA-1L/CROWN/eXalt3/TQ-B3139)</td><td rowspan=1 colspan=1>Brigatinib(KIM 2017/ALTA-3L/ALTA)</td><td rowspan=6 colspan=1>Lorlatinib(EXP4)</td></tr><tr><td rowspan=1 colspan=1>Ceritinib(ASCEND 2/ASCEND 5/ASCEND-6)</td></tr><tr><td rowspan=1 colspan=1>Lorlatinib(exp 2-3A/NCT0390997 cohort1)</td></tr><tr><td rowspan=1 colspan=1>Alectinib (ALUR/ALTA-3L/Sai-Hong2015)</td></tr><tr><td rowspan=1 colspan=1>Ensartinib(Yang2017)</td></tr><tr><td rowspan=1 colspan=1>Iruplinalkib(INTELLECT)</td></tr><tr><td rowspan=1 colspan=1>Chemotherapy (ALUR/ASCEND 5)</td><td rowspan=1 colspan=1>Lorlatinib(exp 2-3A/NCT0390997 cohort1)</td></tr><tr><td rowspan=3 colspan=1>Alectinib(ALEX/ALESIA/J-ALEX/AF-001JP)</td><td rowspan=1 colspan=1>Brigatinib(J-ALTA)</td><td rowspan=3 colspan=1>Lorlatinib(EXP4)</td></tr><tr><td rowspan=1 colspan=1>Ceritinib(ASCEND-9)</td></tr><tr><td rowspan=1 colspan=1>Lorlatinib(exp 3B/NCT0390997 cohort2)</td></tr><tr><td rowspan=1 colspan=1>Ensartinib(eXalt3)</td><td rowspan=5 colspan=1></td><td rowspan=5 colspan=1>/</td></tr><tr><td rowspan=1 colspan=1>Envonalkib(TQ-B3139)</td></tr><tr><td rowspan=1 colspan=1>Brigatinib(ALTA-1L)</td></tr><tr><td rowspan=1 colspan=1>Ceritinib(ASCEND4/ASCEND-8)</td></tr><tr><td rowspan=1 colspan=1>Lorlatinib(CROWN/EXP1)</td></tr></table>

Fig. 2 Visualization and evidence synthesis for treatment strategies and sequential pathways. Note: Evidence source refer to Table S2

For second-line therapies following chemotherapy resistance, in terms of PFS, the 24-month LYGs (Table 2) from highest to lowest were alectinib (21.83 months), ceritinib (16.51), crizotinib (9.91), and chemotherapy (5.98). For OS, the 24-month LYGs from highest to lowest were alectinib (23.35 months), ceritinib (21.53), chemotherapy (18.42), and crizotinib (18.15). Detailed results can be found in Table 2; Fig. 3E-F. NHB results indicated that alectinib was the best option for both OS and PFS, and sensitivity analysis showed that the probability of being the best reached 100%. More details can be found in Table 2. For PFS of second-line treatment options after developing resistance to alectinib, the 24-month LYGs (Fig.  3G) from highest to lowest were brigatinib (10.14 months), lorlatinib (8.82), and ceritinib (5.72). The NHB results showed that the performance from best to worst was brigatinib (0.91 QALY), lorlatinib (0.56), and ceritinib (0.30). The complete results can be found in Table 2.

Figure 3 displays the pooled survival outcomes for different regimens, as well as the differences in pooled survival between phase Ⅱ and Ⅲ clinical trials, indicating variance in the performance of ALK-TKIs across phase Ⅱ-Ⅲ clinical trials but overall consistency (see “Overall difference” in Fig.  4). Additionally, in the abovementioned survival meta-analyses, all sections exhibited low heterogeneity (see Table 1).

## Pooled survival analysis across sequential treatment pathways

In terms of sequential therapies, for PFS 1–2, 13 sequential pathways were considered (Table  2). The results indicated that alectinib-brigatinib (median survival, 56 months) and chemotherapy-alectinib (66 months) were the best choices, followed by crizotinib-iruplinalkib (HR vs. chemotherapy-alectinib, 1.11), alectinib-lorlatinib (1.12), and crizotinib-lorlatinib (1.36). More details can be seen in Fig.  5A. In terms of NHB (Table  2), the best performance was observed for alectinib-brigatinib (3.88 QALYs, 77.78% probability of being the best), followed by chemotherapy-alectinib (3.56 QALYs). After excluding phase Ⅱ studies, 6 sequential pathways were included. Crizotinib-alectinib was the best choice (HR vs. chemotherapy-chemotherapy, 0.39), followed by crizotinibbrigatinib (0.40), more details are presented in Table S6. In terms of NHB, crizotinib-alectinib (2.97 QALYs, 97.76% probability of being the best) and crizotinibbrigatinib (2.71 QALYs) were also the best choices (Table

Table 1 Pooled survival data: results from MetaSurv methodology
<table><tr><td>Treatment</td><td>Studies</td><td>Pa- tients, N</td><td>Median survival (month,95% CI)</td><td>12-month survival rate (%, 95% Cl)</td><td>24-month LYG*(month)</td><td>48-month LYG*(month)</td><td>2 (%)</td></tr><tr><td colspan="8">OS of first-line</td></tr><tr><td>Alectinib</td><td>ALEX, ALESIA, J-ALEX, AF-001JP</td><td>427</td><td>NR</td><td>92.2</td><td>22.99</td><td>40.98</td><td>8.1</td></tr><tr><td>Alectinib(600 mg BID)</td><td>J-ALEX, AF-001 JP</td><td>150</td><td>NR</td><td>93.1</td><td>23.20</td><td>40.17</td><td>3.9</td></tr><tr><td>Alectinib(1200 mg BID)</td><td>ALEX, ALESIA</td><td>277</td><td>NR</td><td>91.4</td><td>22.88</td><td>41.42</td><td>4.3</td></tr><tr><td>Brigatinib</td><td>ALTA-1 L</td><td>137</td><td>NR</td><td>94.8</td><td>21.73</td><td>38.81</td><td>0</td></tr><tr><td>Ensartinib</td><td>eXalt3</td><td>121</td><td>NR</td><td>88.2</td><td>22.03</td><td>38.95</td><td>0</td></tr><tr><td>Lorlatinib</td><td>CROWN</td><td>149</td><td>NR</td><td>89.3</td><td>22.61</td><td>41.23</td><td>0</td></tr><tr><td>Crizotinib</td><td>PROFILE 1014,PROFILE 1029,ALEX, ALESIA, J-ALEX,</td><td>901</td><td>63.39(33.91-NR)</td><td>87.8</td><td>21.80</td><td>37.50</td><td>18.7</td></tr><tr><td>Chemotherapy</td><td>ALTA-1 L, CROWN, eXalt3 PROFILE 1014,PROFILE</td><td>358</td><td>42.82 (22.89-44.09) 78.7</td><td></td><td>19.77</td><td>31.48</td><td>12.8</td></tr><tr><td>Ceritinib</td><td>1029,ASCEND 4 ASCEND 4</td><td>189</td><td>NR(29.3-NR)</td><td>84.1</td><td>21.11</td><td>34.62</td><td>0</td></tr><tr><td>Envonalkib</td><td>TQ-B3139</td><td>131</td><td>NR</td><td>90.6</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td colspan="8">PFS of first-line</td></tr><tr><td>Alectinib</td><td>ALEX, ALESIA, J-ALEX, AF-001JP</td><td>427</td><td>37.42 (20.78-40.7)</td><td>77.5</td><td>19.93</td><td>32.33</td><td>18.4</td></tr><tr><td>Alectinib(600 mg BID)</td><td>J-ALEX, AF-001 JP</td><td>150</td><td>43.42 (17.18-44.22)</td><td>78.2</td><td>20.32</td><td>33.41</td><td>3.1</td></tr><tr><td>Alectinib(1200 mg BID)</td><td>ALEX, ALESIA</td><td>277</td><td>31.72 (NR-NR)</td><td>73.9</td><td>18.72</td><td>NA</td><td>4.8</td></tr><tr><td>Brigatinib</td><td>ALTA-1 L</td><td>137</td><td>24.0 (18.5-43.2)</td><td>85.9</td><td>18.11</td><td>28.68</td><td>0</td></tr><tr><td>Ensartinib</td><td>eXalt3</td><td>121</td><td>25.8 (21.8-NR)</td><td>73.1</td><td>18.76</td><td>30.26</td><td>0</td></tr><tr><td>Lorlatinib</td><td>CROWN, NCT01970865 PROFILE 1014,PROFILE</td><td>179</td><td>NR</td><td>75.7</td><td>19.99</td><td>35.31</td><td>0</td></tr><tr><td>Crizotinib</td><td>1029,ALEX, ALESIA, J- ALEX, ALTA-1 L, CROWN,</td><td>1156</td><td>11.71 (9.9712.97)</td><td>49.0</td><td>14.12</td><td>18.99</td><td>8.1</td></tr><tr><td>Chemotherapy</td><td>eXalt3,TQ-B3139 PROFILE 1014,PROFILE 1029,ASCEND 4</td><td>358</td><td>7.22 (5.81-8.63)</td><td>22.3</td><td>8.94</td><td>NA</td><td>7.7</td></tr><tr><td>Ceritinib</td><td>ASCEND 4,ASCEND 8</td><td>387</td><td>17.99 (12.8522.58) 63.0</td><td></td><td>16.55</td><td>NA</td><td>0</td></tr><tr><td>Ceritinib(450 mg fed)</td><td>ASCEND 8</td><td>73</td><td>NR (11.8-NR)</td><td>66.5</td><td>17.43</td><td>NA</td><td>0</td></tr><tr><td>Ceritinib(600 mg fed)</td><td>ASCEND 8</td><td>51</td><td>17.0 (10.1-NR)</td><td>62.4</td><td>16.38</td><td>NA</td><td>0</td></tr><tr><td>Ceritinib(750 mg fasted)</td><td>ASCEND 4,ASCEND 8</td><td>263</td><td>16.50 (11.14-19.64) 58.4</td><td></td><td>15.72</td><td>NA</td><td>0</td></tr><tr><td>Envonalkib</td><td>TQ-B3139</td><td>131</td><td>24.87 (15.64-30.36) 65.8</td><td></td><td>17.72</td><td>NA</td><td>0</td></tr><tr><td colspan="8">OS of second-line (crizotinib resistance)</td></tr><tr><td>Alectinib</td><td>ALUR</td><td>79</td><td>27.8 (18.2-NR)</td><td>68.3</td><td>18.57</td><td>NA</td><td>0</td></tr><tr><td>Brigatinib</td><td>NCT01449461,ALTA</td><td>444</td><td>34.23 (NR-NR)</td><td>75.0</td><td>19.25</td><td>NA</td><td>3.2</td></tr><tr><td>Brigatinib (90 mg daily)</td><td>NCT01449461,ALTA</td><td>224</td><td>32.17 (NR-NR)</td><td>69.4</td><td>18.0</td><td>NA</td><td>0</td></tr><tr><td>Brigatinib (180 mg daily)</td><td>NCT01449461,ALTA</td><td>220</td><td>35.4 (NR-NR)</td><td>79.3</td><td>20.2</td><td>NA</td><td>0</td></tr><tr><td>Lorlatinib</td><td>NCT01970865</td><td>21</td><td>NR</td><td>95.1</td><td>23.27</td><td>NA</td><td>0 0</td></tr><tr><td>Ceritinib</td><td>ASCEND 2,ASCEND 6</td><td>243</td><td>NR</td><td>60.7</td><td>NA</td><td>NA</td><td></td></tr><tr><td>Iruplinalkib</td><td>INTELLECT</td><td>146</td><td>NR</td><td>85.2</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td>Chemotherapy</td><td>ALUR</td><td>40</td><td>NR (8.6-NR)</td><td>61.1</td><td>17.69</td><td>NA</td><td>0</td></tr><tr><td colspan="8">PFS of second-line (crizotinib resistance)</td></tr><tr><td>Alectinib</td><td>ALUR, ALTA-3 L, Sai-Hong 2015 333</td><td></td><td>11.77 (5.63-16.98)</td><td>49.8</td><td>13.64</td><td>NA</td><td>16.7</td></tr><tr><td>Brigatinib</td><td>NCT01449461,ALTA, ALTA-3 L</td><td>569</td><td>15.02 (9.57-18.69)</td><td>54.1</td><td>14.88</td><td>NA</td><td>23.5</td></tr><tr><td>Brigatinib (90 mg daily)</td><td>NCT01449461,ALTA</td><td>224</td><td>12.67 (9.4616.46)</td><td>46.7</td><td>13.48</td><td>NA</td><td>0</td></tr><tr><td>Brigatinib (180 mg daily)</td><td>NCT01449461,ALTA, ALTA-3 L</td><td>345</td><td>17.08 (12.83-20.67)</td><td>61.1</td><td>16.04</td><td>NA</td><td>18.4</td></tr><tr><td>Lorlatinib</td><td>NCT01970865,NCT0390997</td><td>126</td><td>NR</td><td>64.8</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td>Ceritinib</td><td>ASCEND 2,ASCEND 5,ASCEND</td><td>358</td><td>6.68 (4.157.83)</td><td>26</td><td>9.39</td><td>NA</td><td>28.2</td></tr><tr><td>Iruplinalkib</td><td>6 INTELLECT</td><td>146</td><td>14.5 (11.7-20.0)</td><td>56.9</td><td>15.66</td><td>NA</td><td>0</td></tr><tr><td>Treatment</td><td>Studies</td><td>Pa- tients, N</td><td>Median survival (month,95% CI)</td><td>12-month survival rate (%,</td><td>24-month LYG*(month)</td><td>48-month LYG*(month)</td><td>{ (%)</td></tr><tr><td>Ensartinib</td><td>NCT03215693</td><td>156</td><td>9.6 (7.4-11.6)</td><td>95% CI) 38.4</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td>Chemotherapy</td><td>ALUR, ASCEND 5</td><td>151</td><td>1.4 (1.21.6)</td><td>5.7</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td colspan="8">OS of second-line (chemotherapy resistance)</td></tr><tr><td>Alectinib</td><td>AF-001JP</td><td>46</td><td>NR</td><td>93.6</td><td>23.35</td><td>41.78</td><td>0</td></tr><tr><td>Ceritinib</td><td>ASCEND 3</td><td>124</td><td>51.3 (42.7-55.3)</td><td>88.9</td><td>21.53</td><td>37</td><td>0</td></tr><tr><td>Crizotinib</td><td>PROFILE 1007</td><td>173</td><td>20.3</td><td>70.1</td><td>18.15</td><td>NA</td><td>0</td></tr><tr><td>Chemotherapy</td><td>PROFILE 1007</td><td>174</td><td>22.8</td><td>72.3</td><td>18.42</td><td>NA</td><td>0</td></tr><tr><td colspan="8">PFS of second-line (chemotherapy resistance)</td></tr><tr><td>Alectinib</td><td>AF-001JP</td><td>46</td><td>NR (33.1-NR)</td><td>83.6</td><td>21.83</td><td>36.81</td><td>0</td></tr><tr><td>Ceritinib</td><td>ASCEND 3</td><td>124</td><td>16.6 (11.0-23.2)</td><td>62.2</td><td>16.51</td><td>25.38</td><td>0</td></tr><tr><td>Crizotinib</td><td>PROFILE 1007</td><td>173</td><td>7.7</td><td>31.5</td><td>9.91</td><td>NA</td><td>0</td></tr><tr><td>Chemotherapy</td><td>PROFILE 1007</td><td>174</td><td>3</td><td>12.1</td><td>5.98</td><td>NA</td><td>0</td></tr><tr><td colspan="8">PFS of second-line (alectinib resistance)</td></tr><tr><td>Brigatinib</td><td>J-ALTA</td><td>47</td><td>7.3 (3.7-9.3)</td><td>32.9</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td>Lorlatinib#</td><td>NCT01970865,NCT0390997</td><td>71</td><td>5.93 (2.93-7.91)</td><td>31.9</td><td>NA</td><td>NA</td><td>0</td></tr><tr><td>Ceritinib</td><td>ASCEND 9</td><td>20</td><td>3.7 (1.9-5.3)</td><td>12.7</td><td>NA</td><td>NA</td><td>0</td></tr></table>

NR not reported, NA not available, OS overall survival, PFS progression-free survival  
#, resistance to second-generation ALK-TKIs in trials  
\*, LYG, Life-year Gain

S5). For PFS 1–3, a total of 19 sequential pathways were included (see Table 2). The top three ranked regimens are chemotherapy-alectinib-brigatinib (median survival, 84 months), chemotherapy-alectinib-brigatinib (77 months), and alectinib-brigatinib-lorlatinib (75 months), complete results are provided in Fig. 5B. In terms of NHB (Table 2), alectinib-brigatinib-lorlatinib (4.6 QALYs, 94.07% probability of being the best) was the best choice, followed by alectinib-ceritinib-lorlatinib (4.05 QALYs) and chemotherapy-alectinib-brigatinib (3.96 QALYs). After excluding phase Ⅱ studies, 4 sequential pathways were included (see Table S5-6), with chemotherapy-crizotinib-alectinib being the choice with the highest efficacy and net benefit, followed by chemotherapy-crizotinib-brigatinib. The above findings indicated that the frontline use of secondgeneration ALK-TKI may yield greater survival benefits and NHB (sequential treatment paths with alectinib as the first-line therapy were the optimal choice for both survival time and NHB). The sequence of first-generation ALK-TKI and chemotherapy use appeared to have little impact on overall sequential survival outcomes, while frontline use of ALK-TKIs may deliver higher NHB (for instance, chemotherapy-crizotinib and crizotinibchemotherapy both achieved a 17-month median survival in PFS 1–2, with NHBs of 1.18 and 1.94 QALYs, respectively).

For PFS 1 + OS 2, 9 sequential pathways were included (Fig.  5C). The top three in terms of efficacy were chemotherapy-alectinib (HR vs. alectinib-lorlatinib, 0.78), crizotinib-lorlatinib (0.99), and alectinib-lorlatinib;

alectinib-lorlatinib (4.37 QALYs, 94.07% probability of being the best) had the highest NHB, followed by crizotinib-lorlatinib (4.25 QALYs). The complete results can be seen in Table  2. After excluding phase Ⅱ studies, 4 sequential pathways were included in the study, with crizotinib-chemotherapy being the choice with the highest efficacy and NHB (Table S5-6). In terms of PFS 1–2 + OS 3, 7 sequential pathways were considered (Fig.  5D). The top three were crizotinibalectinib-lorlatinib (median survival, 110 months), crizotinib-chemotherapy-lorlatinib (90 months), and chemotherapy-crizotinib-lorlatinib (81 months). Crizotinib-chemotherapy-lorlatinib (4.37 QALYs, 53.81% probability of being the best) and crizotinib-alectinib-lorlatinib (4.36 QALYs) were the sequences with the highest NHB, with complete results presented in Table  2. After excluding phase Ⅱ studies, chemotherapy-crizotinibchemotherapy was the choice with the highest effectiveness and NHB. Complete results can be found in Table S5-6. The results of treatment pathways over a 40-year observation period were consistent with the base-case analysis, as detailed in Figure S2 and Table S7. Additionally, the results for Scenario Three were consistent with those for Scenario Two, as detailed in Table S8.

## Pooled safety analysis across treatment regimens

The results of the meta-analyses for safety are summarized in Fig.  6. For first-line therapy, the incidence rates among different targeted therapy regimens from best to worst were as follows: alectinib (0.5, 95% CI [0.44–0.56]), ensartinib (0.5, 0.41–0.58), chemotherapy (0.53, 0.45–0.61), crizotinib (0.53, 0.48–0.58), ceritinib (0.71, 0.62–0.79), brigatinib (0.73, 0.65–0.8), and lorlatinib (0.76, 0.68–0.82). For crizotinib-resistant scenarios, from best to worst, the treatments were follows: iruplinalkib (0.31, 0.23–0.39), alectinib (0.5, 0.44–0.56), chemotherapy (0.43, 0.27–0.61), lorlatinib (0.58, 0.46–0.69), and ceritinib (0.69, 0.62–0.74). For patients resistant to chemotherapy, the safety profiles of treatments from best to worst were as follows: chemotherapy (0.46, 0.38–0.53), crizotinib (0.56, 95% CI [0.49–0.64]), and ceritinib (0.88, 0.81–0.93). The choices after resistance to alectinib, from best to worst, were lorlatinib (0.48, 0.33–0.62), brigatinib (0.64, 0.52–0.75), and ceritinib (0.7, 0.46–0.88). In this section, high heterogeneity was observed in the first-line treatments with alectinib, crizotinib, and ceritinib.

A  
<!-- image-->  
C

B  
<!-- image-->  
D

<!-- image-->  
E

<!-- image-->

<!-- image-->

F  
<!-- image-->

G  
<!-- image-->  
Fig. 3 Survival estimation based on parametric modelling. (A First-line OS; B First-line PFS; C Second-line OS, crizotinib resistance; D Second-line PFS, crizotinib resistance; E Second-line OS, chemotherapy resistance; F Second-line PFS, chemotherapy resistance; G Second-line PFS, alectinib resistance; LYs, life-years gain; PFS, progression-free survival; OS, overall survival)

Table 2 Results of net health benefits for all treatments and sequential therapies
<table><tr><td>1st-line PFS</td><td>Lor</td><td>Ale</td><td>Ens</td><td>Bri</td><td>Cri</td></tr><tr><td>NHB (QALY)</td><td>4.76</td><td>3.39</td><td>3.23</td><td>2.99</td><td>1.77</td></tr><tr><td>Proability of being best</td><td>100%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>1 st-line PFS (Continued)</td><td>Env</td><td>Cer</td><td>Che</td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>2.12</td><td>1.65</td><td>0.65</td><td></td><td></td></tr><tr><td>Proability of being best</td><td>0%</td><td>0%</td><td>0%</td><td></td><td></td></tr><tr><td>1 st-line OS</td><td>Lor</td><td>Cer</td><td>Ale</td><td>Bri</td><td>Ens</td></tr><tr><td>NHB (QALY)</td><td>5.15</td><td>3.14</td><td>4.53</td><td>4.43</td><td>4.52</td></tr><tr><td>Proability of being best</td><td>97.84%</td><td>0.00%</td><td>0.43%</td><td>0.64%</td><td>0.88%</td></tr><tr><td>1st-line OS (Continued)</td><td>Cri</td><td>Che</td><td></td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>3.9</td><td>2.95</td><td></td><td></td><td></td></tr><tr><td>Proability of being best</td><td>0.21%</td><td>0.00%</td><td></td><td></td><td></td></tr><tr><td>2st-line PFS (crizotinib resistance)</td><td>Ale</td><td>Bri</td><td>Ens</td><td>Che</td><td>Lor</td></tr><tr><td>NHB (QALY)</td><td>1.32</td><td>1.23</td><td>1.03</td><td>0.25</td><td>1.33</td></tr><tr><td>Proability of being best</td><td>41.10%</td><td>0.60%</td><td>0.00%</td><td>0.00%</td><td>58.11%</td></tr><tr><td>2st-line PFS (crizotinib resistance, continued)</td><td>Cer</td><td>Iru</td><td></td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>0.62</td><td>1.21</td><td></td><td></td><td></td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.19%</td><td></td><td></td><td></td></tr><tr><td>2st-line OS (crizotinib resistance)</td><td>Ale</td><td>Bri</td><td>Che</td><td>Lor</td><td></td></tr><tr><td>NHB (QALY)</td><td>2.16</td><td>2.74</td><td>2.64</td><td>3.21</td><td></td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.01%</td><td>0.00%</td><td>99.99%</td><td></td></tr><tr><td>2st-line PFS (chemotherapy resistance)</td><td>Ale</td><td>Che</td><td>Cri</td><td>Cer</td><td></td></tr><tr><td>NHB (QALY)</td><td>3.13</td><td>0.41</td><td>0.55</td><td>2.17</td><td></td></tr><tr><td>Proability of being best</td><td>100%</td><td>0%</td><td>0%</td><td>0%</td><td></td></tr><tr><td>2st-line OS (chemotherapy resistance)</td><td>Ale</td><td>Bri</td><td>Ens</td><td>Che</td><td></td></tr><tr><td>NHB (QALY)</td><td>3.89</td><td>2.47</td><td>1.68</td><td>2.47</td><td></td></tr><tr><td>Proability of being best</td><td>100%</td><td>0%</td><td>0%</td><td>0%</td><td></td></tr><tr><td>2st-line PFS (alectinib resistance)</td><td>Bri</td><td>Lor</td><td>Cer</td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>0.911</td><td>0.56</td><td>0.298</td><td></td><td></td></tr><tr><td>Proability of being best</td><td>100%</td><td>0%</td><td>0%</td><td></td><td></td></tr><tr><td>PFS 1-2</td><td>Ale + Bri</td><td>Ale +Cer</td><td>Ale + Lor</td><td>Che + Ale</td><td>Che+Cer</td></tr><tr><td>NHB (QALY)</td><td>3.88</td><td>3.56</td><td>3.69</td><td>3.56</td><td>2.62</td></tr><tr><td>Proability of being best</td><td>77.78%</td><td>0.00%</td><td>0.00%</td><td>22.22%</td><td>0.00%</td></tr><tr><td>PFS 1-2 (Continued)</td><td>Che+Che</td><td>Che + Crz</td><td>Crz +Ale</td><td>Crz+Bri</td><td>Crz+Cer</td></tr><tr><td>NHB (QALY)</td><td>1.36</td><td>1.18</td><td>2.79</td><td>2.79</td><td>2.26</td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>PFS 1-2 (Continued)</td><td>Crz+Che</td><td>Crz+Iru</td><td>Crz+Lor</td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>1.94</td><td>3.44</td><td>3.02</td><td></td><td></td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td></td><td></td></tr><tr><td>PFS 1+OS 2</td><td>Ale + Lor</td><td>Che +Ale</td><td>Che+Cer</td><td>Che+Che</td><td>Che+Crz</td></tr><tr><td>NHB (QALY)</td><td>4.37</td><td>4.21</td><td>3.04</td><td>2.95</td><td>2.26</td></tr><tr><td>Proability of being best</td><td>65.41%</td><td>33.96%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>PFS 1 + OS 2 (Continued)</td><td>Crz+Ale</td><td>Crz+Bri</td><td>Crz+Che</td><td>Crz+Lor</td><td></td></tr><tr><td>NHB (QALY)</td><td>3.49</td><td>3.86</td><td>3.75</td><td>4.25</td><td></td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.63%</td><td></td></tr><tr><td>PFS 1-3</td><td>Ale + Bri+Lor</td><td>Ale+Cer+Lor</td><td>Che+Ale+Bri</td><td>Che +Ale+Cer</td><td>Che+Ale+Lor</td></tr><tr><td>NHB (QALY)</td><td>4.6</td><td>4.05</td><td>3.96</td><td>3.76</td><td>3.86</td></tr><tr><td>Proability of being best</td><td>94.07%</td><td>0.00%</td><td>5.93%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>PFS 1-3 (Continued)</td><td>Che+Cer+Lor</td><td>Che+Crz+Ale</td><td>Che+Crz+Bri</td><td>Che+Crz+Cer</td><td>Che+Crz+Che</td></tr><tr><td>NHB (QALY)</td><td>3.01</td><td>2.37</td><td>2.31</td><td>1.79</td><td>1.44</td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>PFS 1-3 (Continued)</td><td>Che+Crz+Ens</td><td>Che+Crz+Iru</td><td>Che+Crz+Lor</td><td>Crz+Ale+Lor</td><td>Crz+Bri+Lor</td></tr><tr><td>NHB (QALY)</td><td>2.12</td><td>3.15</td><td>2.6</td><td>3.32</td><td>3.33</td></tr><tr><td>Proability of being best</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>PFS 1-3 (Continued)</td><td>Crz+Cer+Lor</td><td>Crz+Che+Lor</td><td>Crz+Ens+Lor</td><td>Crz+Iru+Lor</td><td></td></tr><tr><td>NHB (QALY)</td><td>2.95</td><td>3.19</td><td>3.16</td><td>3.96</td><td></td></tr><tr><td>Proability of being best</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td></td></tr><tr><td>PFS 1-2 + OS 3</td><td>Che+Cer+Lor</td><td>Che + Crz+Ale</td><td>Che +Crz+Bri</td><td>Che +Crz+Che</td><td>Che + Crz+Lor</td></tr><tr><td>NHB (QALY)</td><td>3.73</td><td>3.12</td><td>3.53</td><td>3.41</td><td>4.01</td></tr><tr><td>Proability of being best</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr><tr><td>PFS 1-2 + OS 3 (Continued)</td><td>Che+Ale+Lor</td><td>Crz+Che+Lor</td><td></td><td></td><td></td></tr><tr><td>NHB (QALY)</td><td>4.36</td><td>4.37</td><td></td><td></td><td></td></tr><tr><td>Proability of being best</td><td>46.19%</td><td>53.81%</td><td></td><td></td><td></td></tr></table>

Ale Alectinib, Bri Brigatinib, Cer Ceritinib, Che Chemotherapy, Cri Crizotinib, Ens Ensartinib, Env Envonalkib, Iru Iruplinalkib, Lor Lorlatinib, NHB net health benefit, QALY quality-adjusted life-year, PFS progression-free survival, OS, overall survival

<!-- image-->  
Fig. 4 Comparison of survival estimates across phase Ⅱ and Ⅲ Trials. OS, overall survival; PFS, progression-free survival

## Discussion

## Main findings

In this large systematic review and meta-analysis of 27 trials, we reconstructed IPD to provide robust survival and safety estimates for all systemic therapies and sequential treatment pathways for ALK-positive NSCLC. The main findings of this study were as follows:

For first-line treatments, brigatinib had the highest 12-month survival rate for both PFS and OS, while lorlatinib showed the greatest LYG at 120 months. The NHB indicated that lorlatinib was the optimal treatment for both PFS and OS. For second-line treatments after crizotinib resistance, lorlatinib ranked highest in 12-month survival rate and 24-month LYG for both PFS and OS. Additionally, lorlatinib had the best NHB outcomes for both PFS and OS. For second-line treatments after chemotherapy resistance, alectinib had the highest 24-month

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 5 Modeled relative efficacy between sequential therapies based on survival data. A PFS 1–2; B PFS 1–3; C PFS 1 + OS 2; D PFS 1–2 + OS 3. Ale, Alectinib; Bri, Brigatinib; Cer, Ceritinib; Che, Chemotherapy; Cri, Crizotinib; Ens, Ensartinib; Env, Envonalkib; Iru, Iruplinalkib; Lor, Lorlatinib; PFS, progression-free survival; OS, overall survival

LYG for both PFS and OS. Regarding NHB, the probability of alectinib being the optimal choice reaches 100%. For second-line treatments after alectinib resistance, brigatinib had the highest LYG at 24 months for PFS. The NHB results also indicated brigatinib as the best option.

Regarding sequential treatment pathways, for PFS 1–2, chemotherapy-alectinib and alectinib-brigatinib ranked highest for median survival, and alectinib-brigatinib had the greatest NHB. When excluding phase Ⅱ studies, crizotinib-alectinib led in both survival and NHB. For PFS 1–3, the sequence of chemotherapy-alectinibbrigatinib had the longest median survival. Alectinibbrigatinib-lorlatinib offered the highest NHB. Without phase Ⅱ studies, chemotherapy-crizotinib-alectinib was the optimal choice both in survival and NHB. For PFS 1 + OS 2, chemotherapy-alectinib and alectinib-lorlatinib were most effective, with the latter providing the best NHB. Post-phase Ⅱ study exclusion, crizotinib-chemotherapy remained the leading choice. For PFS 1–2 + OS 3, crizotinib-alectinib-lorlatinib was the most effective, with crizotinib-chemotherapy-lorlatinib yielding the highest NHB. After removing phase Ⅱ studies, chemotherapycrizotinib-chemotherapy showed the best results. The results over a 40-year observation period were consistent with the primary analysis. The findings indicated that using second-generation ALK-TKIs as frontline therapy enhanced survival and NHB; the sequencing of first-generation ALK-TKI and chemotherapy had minimal impact on sequential survival, while frontline ALK-TKIs provided a higher NHB. Additionally, Scenario Three yielded results consistent with Scenario Two. The clinical trial evidence underpinning these sequential therapy pathways is robust, and uncertainty analysis indicates that the results of this section are relatively reliable [66].

Regarding safety, alectinib had the lowest incidence of AEs among the first-line treatments, followed by ensartinib, chemotherapy, crizotinib, ceritinib, brigatinib, and lorlatinib. Post-crizotinib resistance, iruplinalkib was the safest, followed by alectinib, chemotherapy, lorlatinib, and ceritinib. In chemotherapy-resistant patients, chemotherapy led in safety, followed by crizotinib and ceritinib. For alectinib resistance, lorlatinib was the safest, with brigatinib and ceritinib thereafter.

<table><tr><td>Treatment</td><td>Evidence</td><td>I2</td><td>Mean Difference (95% CI)</td></tr><tr><td>First-line</td><td></td><td></td><td></td></tr><tr><td>Crizotinib</td><td>PROFILE1014/ALEX/ALESIA/J-ALEX/ ALTA-1L/CROWN/eXalt3/TQ-B3139</td><td>0.57</td><td>0.53 (0.48 to 0.58)</td></tr><tr><td>Alectinib</td><td>ALEX/ALESIA/J-ALEX</td><td>0.87</td><td>0.38 (0.26 to 0.52)</td></tr><tr><td>Alectinib(600mg BID)</td><td>J-ALEX</td><td>NA</td><td>0.26 (0.18 to 0.36)</td></tr><tr><td>Alectinib(1200mg BID)</td><td>ALEX/ALESIA</td><td>0</td><td>0.50 (0.44 to 0.56)</td></tr><tr><td>Brigatinib</td><td>ALTA-1L</td><td>NA</td><td>0.73 (0.65 to 0.80)</td></tr><tr><td>Ensartinib</td><td>eXalt3</td><td>NA</td><td>0.50 (0.41 to 0.58)</td></tr><tr><td>Chemotherapy</td><td>PROFILE 1014</td><td>NA</td><td>0.53 (0.45 to 0.61)</td></tr><tr><td>Lorlatinib</td><td>CROWN</td><td>NA</td><td>0.76 (0.68 to 0.82)</td></tr><tr><td>Ceritinib</td><td>ASCEND-4/ASCEND-8</td><td>0.78</td><td>0.71 (0.62 to 0.79)</td></tr><tr><td>Envonalkib</td><td>TQ-B3139</td><td>NA</td><td>0.63 (0.54 to 0.72)</td></tr><tr><td>Ceritinib(450mg fed)</td><td>ASCEND-8</td><td>NA</td><td>0.65 (0.55 to 0.74)</td></tr><tr><td>Ceritinib(600mg fed)</td><td>ASCEND-8</td><td>NA</td><td>0.79 (0.69 to 0.87)</td></tr><tr><td>Ceritinib(750mg fasted)</td><td>ASCEND-4/ASCEND-8</td><td>0.89</td><td>0.71 (0.53 to 0.84)</td></tr><tr><td>Crizotinib Resistance</td><td></td><td></td><td></td></tr><tr><td>Iruplinalkib</td><td>INTELLECT</td><td>NA</td><td>0.31 (0.23 to 0.39)</td></tr><tr><td>Alectinib</td><td>ALUR</td><td>NA</td><td>0.38 (0.27 to 0.49)</td></tr><tr><td>Ceritinib</td><td>ASCEND-2/ASCEND-6</td><td>0.11</td><td>0.69 (0.62 to 0.74) TH</td></tr><tr><td>Chemotherapy</td><td>ALUR</td><td>NA</td><td>0.43 (0.27 to 0.61)</td></tr><tr><td>Lorlatinib</td><td>NCT0390997</td><td>NA</td><td>0.58 (0.46 to 0.69)</td></tr><tr><td>Chemotherapy Resistance</td><td></td><td></td><td></td></tr><tr><td>Chemotherapy</td><td>PROFILE 1007 NA</td><td></td><td>0.46 (0.38 to 0.53)</td></tr><tr><td>Crizotinib</td><td>PROFILE 1007 NA</td><td></td><td>0.56 (0.49 to 0.64)</td></tr><tr><td>Ceritinib</td><td>ASCEND-3 NA</td><td></td><td>0.88 (0.81 to 0.93)</td></tr><tr><td>Alectinib Resistance</td><td></td><td></td><td></td></tr><tr><td>Brigatinib J-ALTA</td><td>NA</td><td></td><td>0.64 (0.52 to 0.75)</td></tr><tr><td>Lorlatinib</td><td>NCT0390997 NA</td><td></td><td>0.48 (0.33 to 0.62)</td></tr><tr><td>Ceritinib ASCEND-9</td><td>NA</td><td></td><td>0.70 (0.46 to 0.88)</td></tr><tr><td></td><td>0 0.2</td><td>0.5 0.8</td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>&lt;</td><td>→ Lower Higher</td><td></td></tr></table>

Fig. 6 Summary of pooled safety outcomes. NA, Not available

According to the latest ASCO, European Society for Medical Oncology (ESMO), and Chinese Society of Clinical Oncology (CSCO) guidelines, there are some differences in recommendations for treating ALK-positive NSCLC. ASCO guidelines recommend alectinib/ brigatinib and lorlatinib as first-line treatments, with ceritinib and crizotinib as alternatives. ESMO also endorses alectinib and brigatinib/lorlatinib, with ceritinib and crizotinib as secondary options. CSCO prioritizes alectinib, brigatinib, and lorlatinib, considering alternatives like ensartinib in specific cases. For subsequent treatments, switching to another ALK-TKI is advised after first-line failure. ASCO favors alectinib and brigatinib, with lorlatinib as a secondary option. CSCO suggests using second- and third-generation ALK-TKIs after resistance to first-generation TKIs, with lorlatinib as the first choice after resistance to second-generation TKIs, and chemotherapy as another option for ALK-TKI resistance. ESMO aligns with CSCO, recommending lorlatinib after second-generation ALK-TKI resistance and advising against other ALK-TKIs after lorlatinib. After first-generation resistance, alectinib, brigatinib, and ceritinib are preferred [67–69].

The NSCLC treatment landscape has advanced with targeted therapies offering personalized options [70]. Our study evaluated these therapies based on efficacy and net health benefit (NHB), balancing clinical benefits and quality of life [53]. Brigatinib and alectinib showed favorable 12-month OS rates as first-line treatments. However, the CROWN trial’s 5-year results highlighted lorlatinib’s superior PFS rate (60%), the highest for any single-agent targeted therapy in advanced NSCLC [20]. Long-term modeling suggested lorlatinib’s highest LYG at 120 months, underscoring the importance of strategic therapy selection based on both immediate and longterm survival benefits [71]. Lorlatinib’s superior NHB also indicated potential quality-of-life improvements, critical for patients prioritizing both life extension and well-being [53]. Resistance to first-line treatments like crizotinib necessitates optimizing second-line therapies [72, 73]. Lorlatinib, with the highest PFS and OS postcrizotinib, proves robust in resistant-tumor settings [74].

For patients facing chemotherapy resistance, alectinib has emerged as a superior survival option, with its optimal NHB further affirming its patient-friendly profile given the adverse effects commonly linked to chemotherapy. The sequential treatment pathways present a complex scenario in which clinicians must navigate the best course of action for long-term patient management [72]. The combination of chemotherapy followed by alectinib or brigatinib had a moderate effect on survival. The transition from a non-targeted to a targeted therapy approach capitalizes on the initial broad-spectrum effects of chemotherapy while subsequently leveraging the precision of targeted therapies. This finding was consistent with that of Lee [75], who indicated that frontline use of ALK-TKIs did not significantly increase survival. However, since ALK-TKIs can prolong the survival time of first-line PFS [75], the utility of first-line PFS is better than that after progression [54]. Therefore, under the same treatment combination, the earlier use of ALK-TKIs may increase more NHB. Personalizing treatment sequences to the patient’s specific genetic and clinical profile is increasingly important for optimal efficacy [76]. Continuous monitoring and the ability to adjust treatment plans in response to changes in the patient’s disease status are critical for keeping the treatment aligned with the patient’s needs [77]. This strategic, flexible approach to sequential treatment allows for sustained disease control, extends survival, and prioritizes the patient’s overall wellbeing throughout the treatment journey [78, 79]. The exclusion of phase Ⅱ studies in our scenario analysis serves to focus the results on more definitive data, which are typically obtained from larger, more diverse patient populations in phase 3 trials. This approach enhances the reliability of the findings, providing clearer guidance for clinical decision-making.

Our study, a first in using a reconstructed IPD metaanalysis in this field, revealed negligible heterogeneity and high-quality data, providing strong survival projections crucial for future clinical trials [79]. Our study also explored sequential treatment pathways, showing no significant difference in efficacy between first-generation followed by second-generation ALK inhibitors and direct second-generation therapy. We have previously compared the safety, efficacy, and quality of life of ALK-TKIs in first- and second-line settings for NSCLC in a network meta-analysis [80]. This study further expands on this basis, incorporating more clinical data and broadening the research framework and depth. To the best of our knowledge, there are no clinical trials in the field of ALK NSCLC based on sequential treatment, with only some retrospective study evidence available. Wei et al. [81] reported there was no significant difference in efficacy between first-generation sequential second-generation ALK-TKIs and direct therapy with second-generation ALK-TKI regimens. Kentaro et al. [28] showed that there was no significant difference in OS between crizotinib sequential alectinib and alectinib sequential crizotinib, but the former performed better in terms of time-totreatment failure; Kentaro et al. [82] indicated that the OS performance of alectinib monotherapy was not as good as that of crizotinib sequential alectinib. Potential gaps in the current study landscape should be acknowledged, including the lack of direct comparisons between second and third-generation ALK-TKIs. Future research should focus on head-to-head trials to provide clearer clinical guidance.

## Limitation

The study’s limitations include: (1) The lack of clinical data after resistance to lorlatinib [80] prevented us from analyzing the sequential pathway of lorlatinib as the first-line treatment. (2) We used QALY as an indicator to calculate NHB. However, the possibility of recurring AEs cannot be excluded, which may introduce some bias in quantifying the safety indicator [83]. Additionally, we derived utility values from the ATLA-1  L study, lacking comprehensive data from all trials [19]. (3) Our reliance on reconstructed IPD, which included only survival information, introduced potential inconsistencies across patient baselines and contributed to heterogeneity in areas such as AEs. The risk of this limitation remained, despite extensive uncertainty analyses. (4) The analysis included only clinical trials with selective patient enrolment and discontinuation protocols, necessitating validation in real-world clinical settings [84]. (5) Our analysis did not differentiate specific types of AEs, which may obscure the nuanced effects of these toxicities on patients’ quality of life. Comparing high-grade AEs alone can lead to unclear results regarding the impact on quality of life, as the toxicity profiles of the drugs are very different. For instance, while alectinib may cause mild gastrointestinal issues, lorlatinib might lead to severe neurological side effects. This lack of differentiation can result in an incomplete understanding of the overall impact on patient quality of life. Therefore, a comprehensive evaluation of both the frequency and nature of AEs is essential for accurately assessing their broader implications.

## Conclusion

Lorlatinib is highlighted as the best first-line therapy and remains superior after crizotinib resistance. Sequential therapies, particularly chemotherapy followed by alectinib or brigatinib, yield the highest LYG and NHB, with the chemotherapy-alectinib-brigatinib sequence notably maximizing benefits in more advanced stages. Frontline second-generation ALK-TKIs likely improve survival and NHB, while the sequence of first-generation ALK-TKI and chemotherapy has minimal impact on survival, with ALK-TKIs enhancing NHB. This findings underscores the value of strategic ALK-TKI sequencing in treatment progression.

## Supplementary Information

The online version contains supplementary material available at https://doi.or g/10.1186/s12885-026-15916-4.

Supplementary Material 1.

Supplementary Material 2.

## Authors’ contributions

Prof. Tang, Mr Zhao, Mr Li, Mr Shao and Prof. Huang had full access to all of the data in the study and take responsibility for the integrity of the data and the accuracy of the data analysis. Mr Zhao, Mr Li contributed equally to this work. Concept and design: Tang; Acquisition of data: Zhao, Li, Jiang, Shao; Analysis and interpretation of data: Zhao, Huang, Li; Drafting of manuscript: Zhao, Li; Critical revision of the manuscript for important intellectual content: Huang, Jiang, Shao; Statistical analysis: Zhao, Li, Huang; Obtaining funding: Tang; Administrative and technical support: Tang; Supervision: Tang, Huang.

## Funding

This research was supported by the General Program of National Natural Science Foundation of China (Grant no. 72174207) and the Postgraduate Research and Practice Innovation Program of Jiangsu Province (Grant no.3322500029).

## Data availability

Data sharing statement Full data set is available, on request from the corresponding author, e-mail, tokammy@cpu.edu.cn.

## Declarations

Ethics approval and consent to participate Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Author details

1 Department of Pharmacoeconomics, School of International   
Pharmaceutical Business, China Pharmaceutical University, Nanjing,   
Jiangsu, China   
2 Center for Pharmacoeconomics and Outcomes Research & Department   
of Public Affairs Management, School of International Pharmaceutical   
Business, China Pharmaceutical University, Nanjing, Jiangsu, China   
3 Department of Oncology, Xiangya Hospital, Central South University,   
Changsha, Hunan 410008, China   
4 Yueyang Hospital of Integrated Traditional Chinese and Western   
Medicine, Shanghai University of Traditional Chinese Medicine, Shanghai,   
China

Received: 16 September 2024 / Accepted: 23 March 2026   
Published online: 29 March 2026

## References

1. Pao W, Girard N. New driver mutations in non-small-cell lung cancer. Lancet Oncol. 2011;12(2):175–80.

2. Sung H, Ferlay J, Siegel RL, et al. Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries. CA Cancer J Clin. 2021;71(3):209–49.

3. Duma N, Santana-Davila R, Molina JR. Non-small cell lung cancer: epidemiology, screening, diagnosis, and treatment. Mayo Clin Proc. 2019;94(8):1623–40.

4. Solomon BJ, Kim DW, Wu YL, et al. Final overall survival analysis from a study comparing first-line Crizotinib versus chemotherapy in ALK-mutation-positive non-small-cell lung cancer. J Clin Oncol. 2018;36(22):2251–8.

5. Soria JC, Tan D, Chiari R, et al. First-line ceritinib versus platinum-based chemotherapy in advanced ALK-rearranged non-small-cell lung cancer (ASCEND-4): a randomised, open-label, phase 3 study. Lancet. 2017;389(10072):917–29.

6. Wu YL, Lu S, Lu Y, et al. Results of PROFILE 1029, a Phase III comparison of firstline Crizotinib versus chemotherapy in East Asian Patients with ALK-positive advanced non-small cell lung cancer. J Thorac Oncol. 2018;13(10):1539–48.

7. Hida T, Nokihara H, Kondo M, et al. Alectinib versus crizotinib in patients with ALK-positive non-small-cell lung cancer (J-ALEX): an open-label, randomised phase 3 trial. Lancet. 2017;390(10089):29–39.

8. Peters S, Camidge DR, Shaw AT, et al. Alectinib versus Crizotinib in untreated ALK-positive non-small-cell lung cancer. N Engl J Med. 2017;377(9):829.

9. Zhou C, Kim SW, Reungwetwattana T, et al. Alectinib versus crizotinib in untreated Asian patients with anaplastic lymphoma kinase-positive nonsmall-cell lung cancer (ALESIA): a randomised phase 3 study. Lancet Resp Med. 2019;7(5):437–46.

10. Camidge DR, Kim HR, Ahn MJ, et al. Brigatinib versus Crizotinib in ALKpositive non-small-cell lung cancer. N Engl J Med. 2018;379(21):2027–39.

11. Shaw AT, Kim TM, Crino L, et al. Ceritinib versus chemotherapy in patients with ALK-rearranged non-small-cell lung cancer previously given chemotherapy and crizotinib (ASCEND-5): a randomised, controlled, open-label, phase 3 trial. Lancet Oncol. 2017;18(7):874–86.

12. Shaw AT, Kim DW, Nakagawa K, et al. Crizotinib versus chemotherapy in advanced ALK-positive lung cancer. N Engl J Med. 2013;368(25):2385–94.

13. Horn L, Wang Z, Wu G, et al. Ensartinib vs Crizotinib for patients with anaplastic lymphoma kinase-positive non-small cell lung cancer: a randomized clinical trial. JAMA Oncol. 2021;7(11):1617–25.

14. Solomon BJ, Mok T, Kim DW, et al. First-line crizotinib versus chemotherapy in ALK-positive lung cancer. N Engl J Med. 2014;371(23):2167–77.

15. Shaw AT, Bauer TM, de Marinis F, et al. First-line Lorlatinib or Crizotinib in advanced ALK-positive lung cancer. N Engl J Med. 2020;383(21):2018–29.

16. Yang J, Lu S, Burotto M. 319O ALTA-3: a randomized trial of brigatinib (BRG) vs alectinib (ALC) in crizotinib (CRZ)-refractory advanced ALK+ NSCLC. 2022.

17. Yang Y, Min J, Yang N, et al. Envonalkib versus crizotinib for treatment-naive ALK-positive non-small cell lung cancer: a randomized, multicenter, openlabel, phase III trial. Signal Transduct Target Ther. 2023;8(1):301.

18. Mok T, Camidge DR, Gadgeel SM, et al. Updated overall survival and final progression-free survival data for patients with treatment-naive advanced ALK-positive non-small-cell lung cancer in the ALEX study. Ann Oncol. 2020;31(8):1056–64.

19. Camidge DR, Kim HR, Ahn MJ, et al. Brigatinib versus Crizotinib in ALK inhibitor-naive advanced ALK-positive NSCLC: final results of phase 3 ALTA-1L trial. J Thorac Oncol. 2021;16(12):2091–108.

20. Solomon BJ, Liu G, Felip E, et al. Lorlatinib vs crizotinib in treatmentnaïve patients with advancedALK + non-small cell lung cancer: 5-year progression-free survival and safety from the CROWN study. J Clin Oncol. 2024;42(17suppl):LBA8503.

21. Yang Y, Min J, Yang N, et al. Envonalkib versus crizotinib for treatment-naive ALK-positive non-small cell lung cancer: a randomized, multicenter, openlabel, phase III trial. Signal Transduct Target Ther. 2023;8(1):301.

22. Wolf J, Helland A, Oh IJ, et al. Final efficacy and safety data, and exploratory molecular profiling from the phase III ALUR study of alectinib versus chemotherapy in crizotinib-pretreated ALK-positive non-small-cell lung cancer. ESMO Open. 2022;7(1):100333.

23. Yang JC, Liu G, Lu S, et al. Brigatinib versus Alectinib in ALK-Positive NSCLC after disease progression on Crizotinib: results of phase 3 ALTA-3 trial. J Thorac Oncol. 2023;18(12):1743–55.

24. Shi Y, Chen J, Zhang H, et al. Efficacy and safety of iruplinalkib (WX-0593) in ALK-positive crizotinib-resistant advanced non-small cell lung cancer patients: a single-arm, multicenter phase II study (INTELLECT). BMC Med. 2023;21(1):72.

25. Yang Y, Zhou J, Zhou J, et al. Efficacy, safety, and biomarker analysis of ensartinib in crizotinib-resistant, ALK-positive non-small-cell lung cancer: a multicentre, phase 2 trial Lancet Respir Med. 2020;8(1):45–53.

26. Lu S, Zhou Q, Liu X, et al. Lorlatinib for previously treated ALK-positive advanced NSCLC: primary efficacy and safety from a phase 2 study in People’s Republic of China. J Thorac Oncol. 2022;17(6):816–26.

27. Duruisseaux M, Besse B, Cadranel J, et al. Overall survival with crizotinib and next-generation ALK inhibitors in ALK-positive non-small-cell lung cancer (IFCT-1302 CLINALK): a French nationwide cohort retrospective study. Oncotarget. 2017;8(13):21903–17.

28. Ito K, Yamanaka T, Hayashi H, et al. Sequential therapy of crizotinib followed by alectinib for non-small cell lung cancer harbouring anaplastic lymphoma kinase rearrangement (WJOG9516L): a multicenter retrospective cohort study. Eur J Cancer. 2021;145:183–93.

29. Pacheco JM, Gao D, Smith D, et al. Natural history and factors associated with overall survival in stage IV ALK-rearranged non-small cell lung cancer. J Thorac Oncol. 2019;14(4):691–700.

30. Tan D, Tang A, Lim WH, et al. Survival trends in sorafenib for advanced hepatocellular carcinoma: a reconstructed individual patient data meta-analysis of randomized trials. Liver Cancer. 2023;12(5):445–56.

31. Stewart LA, Tierney JF. To IPD or not to IPD? Advantages and disadvantages of systematic reviews using individual patient data. Eval Health Prof. 2002;25(1):76–97.

32. Tseng CH, Hsu YC, Chen TH, et al. Hepatocellular carcinoma incidence with tenofovir versus entecavir in chronic hepatitis B: a systematic review and meta-analysis. Lancet Gastroenterol Hepatol. 2020;5(12):1039–52.

33. Cheung KS, Mak LY, Liu SH, et al. Entecavir vs Tenofovir in hepatocellular carcinoma prevention in chronic hepatitis b infection: a systematic review and meta-analysis. Clin Transl Gastroenterol. 2020;11(10):e236.

34. Choi WM, Choi J, Lim YS. Effects of Tenofovir vs Entecavir on risk of hepatocellular carcinoma in patients with chronic HBV infection: a systematic review and meta-analysis. Clin Gastroenterol Hepatol. 2021;19(2):246–58.

35. Zhao M, Shao T, Chi Z, et al. Effectiveness and cost-effectiveness analysis of 11 treatment paths, seven first-line and three second-line treatments for Chinese patients with advanced wild-type squamous non-small cell lung cancer: a sequential model. Front Public Health. 2023;11:1051484.

36. Tierney JF, Stewart LA, Ghersi D, et al. Practical methods for incorporating summary time-to-event data into meta-analysis. Trials. 2007;8:16.

37. Wiksten A, Hawkins N, Piepho HP, et al. Nonproportional hazards in network meta-analysis: efficient strategies for model building and analysis. Value Health. 2020;23(7):918–27.

38. Freeman SC, Cooper NJ, Sutton AJ, et al. Challenges of modelling approaches for network meta-analysis of time-to-event outcomes in the presence of non-proportional hazards to aid decision making: application to a melanoma network. Stat Methods Med Res. 2022;31(5):839–61.

39. Schnipper LE, Davidson NE, Wollins DS, et al. American Society of Clinical Oncology Statement: a conceptual framework to assess the value of cancer treatment options. J Clin Oncol. 2015;33(23):2563–77.

40. Guyot P, Ades AE, Ouwens MJ, et al. Enhanced secondary analysis of survival data: reconstructing the data from published Kaplan-Meier survival curves. BMC Med Res Methodol. 2012;12:9.

41. Jackson D, White IR, Thompson SG. Extending DerSimonian and Laird’s methodology to perform multivariate random effects meta-analyses. Stat Med. 2010;29(12):1282–97.

42. Royston P, Parmar MK. Restricted mean survival time: an alternative to the hazard ratio for the design and analysis of randomized trials with a time-toevent outcome. BMC Med Res Methodol. 2013;13:152.

43. Uno H, Claggett B, Tian L, et al. Moving beyond the hazard ratio in quantifying the between-group difference in survival analysis. J Clin Oncol. 2014;32(22):2380–5.

44. Zhao L, Claggett B, Tian L, et al. On the restricted mean survival time curve in survival analysis. Biometrics. 2016;72(1):215–21.

45. Zhao B, Han Y, Wang Y, et al. A Bayesian network meta-analysis regarding the comparative efficacy of therapeutics for ALK-positive, brain metastatic nonsmall cell lung cancer. Pharmacol Res. 2021;174:105931.

46. Shao T, Zhao M, Liang L, et al. Impact of extrapolation model choices on the structural uncertainty in economic evaluations for cancer immunotherapy: a case study of checkmate 067. Pharmacoecon Open. 2023;7(3):383–92.

47. Ivanics T, Murillo PC, Claasen M, et al. Dynamic risk profiling of HCC recurrence after curative intent liver resection. Hepatology. 2022;76(5):1291–301.

48. Carta A, Conversano C. On the Use of Markov Models in pharmacoeconomics: pros and cons and implications for policy makers. Front Public Health. 2020;8:569500.

49. Smare C, Lakhdari K, Doan J, et al. Evaluating Partitioned Survival and Markov Decision-Analytic modeling approaches for use in cost-effectiveness analysis: estimating and comparing survival outcomes. PharmacoEconomics. 2020;38(1):97–108.

50. Shi Y, Chen J, Zhang H, et al. Efficacy and safety of iruplinalkib (WX-0593) in ALK-positive crizotinib-resistant advanced non-small cell lung cancer patients: a single-arm, multicenter phase II study (INTELLECT). BMC Med. 2023;21(1):72.

51. Yang Y, Min J, Yang N, et al. Envonalkib versus crizotinib for treatment-naive ALK-positive non-small cell lung cancer: a randomized, multicenter, openlabel, phase III trial. Signal Transduct Target Ther. 2023;8(1):301.

52. Excellence N I F H. Guide to the Methods of Technology Appraisal 2013. London: National Institute for Health and Care Excellence (NICE); 2013.

53. Schnipper LE, Davidson NE, Wollins DS, et al. American Society of Clinical Oncology statement: a conceptual framework to assess the value of cancer treatment options. J Clin Oncol. 2015;33(23):2563–77.

54. Brigatinib for ALK-positive advanced nonsmall-cell lung cancer that has not been previously treated with an ALK inhibitor [EB/OL]. [2024-03-12]. https://w ww.nice.org.uk/guidance/ta670/evidence/​​f​​i​nal-appraisal-determination-com mittee-papers-pdf-8964111853.

55. Cabibbo G, Reig M, Celsa C, et al. First-Line immune checkpoint inhibitorbased sequential therapies for advanced hepatocellular carcinoma: rationale for future trials. Liver Cancer. 2022;11(1):75–84.

56. Tamura T, Kiura K, Seto T, et al. Three-year follow-up of an Alectinib Phase I/ II study in ALK-positive non-small-cell lung cancer: AF-001JP. J Clin Oncol. 2017;35(14):1515–21.

57. Ou SH, Ahn JS, De Petris L, et al. Alectinib in Crizotinib-Refractory ALK-Rearranged non-small-cell lung cancer: a Phase II Global Study. J Clin Oncol. 2016;34(7):661–8.

58. Huber RM, Hansen KH, Paz-Ares RL, et al. Brigatinib in Crizotinib-Refractory ALK+ NSCLC: 2-Year follow-up on systemic and intracranial outcomes in the Phase 2 ALTA trial. J Thorac Oncol. 2020;15(3):404–15.

59. Crino L, Ahn MJ, De Marinis F, et al. Multicenter Phase II study of whole-body and intracranial activity with Ceritinib in patients with ALK-rearranged nonsmall-cell lung cancer previously treated with chemotherapy and Crizotinib: results From ASCEND-2. J Clin Oncol. 2016;34(24):2866–73.

60. Nishio M, Felip E, Orlov S, et al. Final overall survival and other efficacy and safety results from ASCEND-3: Phase II study of Ceritinib in ALKi-naive patients with ALK-rearranged NSCLC. J Thorac Oncol. 2020;15(4):609–17.

61. Wu YL, Shi Y, Tan D, et al. Phase 1/2 study of ceritinib in Chinese patients with advanced anaplastic lymphoma kinase-rearranged non-small cell lung cancer previously treated with crizotinib: Results from ASCEND-6. Lung Cancer. 2020;150:240–6.

62. Hida T, Seto T, Horinouchi H, et al. Phase II study of ceritinib in alectinibpretreated patients with anaplastic lymphoma kinase-rearranged metastatic non-small-cell lung cancer in Japan: ASCEND-9. Cancer Sci. 2018;109(9):2863–72.

63. Nishio M, Yoshida T, Kumagai T, et al. Brigatinib in Japanese patients with ALK-Positive NSCLC previously treated with alectinib and other tyrosine kinase inhibitors: outcomes of the phase 2 J-ALTA Trial. J Thorac Oncol. 2021;16(3):452–63.

64. Kim DW, Tiseo M, Ahn MJ, et al. Brigatinib in patients with Crizotinibrefractory anaplastic lymphoma kinase-positive non-small-cell lung cancer: a randomized, multicenter phase II Trial. J Clin Oncol. 2017;35(22):2490–8.

65. Solomon BJ, Besse B, Bauer TM, et al. Lorlatinib in patients with ALK-positive non-small-cell lung cancer: results from a global phase 2 study. Lancet Oncol. 2018;19(12):1654–67.

66. Liao D, Yu L, Shangguan D, et al. Recent advancements of monotherapy, combination, and sequential treatment of EGFR/ALK-TKIs and ICIs in nonsmall cell lung cancer. Front Pharmacol. 2022;13:905947.

67. Owen DH, Ismaila N, Freeman-Daily J, et al. Therapy for stage IV non–small cell lung cancer with driver alterations: ASCO living guideline, version 2024.1. J Clin Oncol. 2024;42(20):e44–59.

68. Hendriks LE, Kerr KM, Menis J, et al. Oncogene-addicted metastatic nonsmall-cell lung cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. Ann Oncol. 2023;34(4):339–57.

69. Chinese Society of Clinical Oncology Guidelines Working Committee. Chinese Society of Clinical Oncology (CSCO) Guidelines for the diagnosis and treatment of non-small cell lung cancer, 2024 Edition. Beijing: People’s Medical Publishing House; 2024.

70. Carper MB, Claudio PP. Clinical potential of gene mutations in lung cancer. Clin Transl Med. 2015;4(1):33.

71. Hendriks LE, Kerr KM, Menis J, et al. Non-oncogene-addicted metastatic non-small-cell lung cancer: ESMO clinical practice guideline for diagnosis, treatment and follow-up. Ann Oncol. 2023;34(4):358–76.

72. Lin YT, Chiang CL, Hung JY, et al. Resistance profiles of anaplastic lymphoma kinase tyrosine kinase inhibitors in advanced non-small-cell lung cancer: a multicenter study using targeted next-generation sequencing. Eur J Cancer. 2021;156:1–11.

73. Bejarano L, Jordao M, Joyce JA. Therapeutic targeting of the tumor microenvironment. Cancer Discov. 2021;11(4):933–59.

74. Shiba-Ishii A, Johnson TW, Dagogo-Jack I, et al. Analysis of lorlatinib analogs reveals a roadmap for targeting diverse compound resistance mutations in ALK-positive lung cancer. Nat Cancer. 2022;3(6):710–22.

75. Lee YC, Hsieh CC, Lee YL, et al. Which should be used first for ALK-positive non-small-cell lung cancer: chemotherapy or targeted therapy? A metaanalysis of five randomized trials. Medicina (Kaunas). 2019;55(2):29.

76. Itchins M, Pavlakis N. The quantum leap in therapeutics for advanced ALK + non-small cell lung cancer and pursuit to cure with precision medicine. Front Oncol. 2022;12:959637.

77. Yanagitani N, Uchibori K, Koike S, et al. Drug resistance mechanisms in Japanese anaplastic lymphoma kinase-positive non-small cell lung cancer and the clinical responses based on the resistant mechanisms. Cancer Sci. 2020;111(3):932–9.

78. Lin YT, Yu CJ, Yang JC, et al. Anaplastic Lymphoma Kinase (ALK) Kinase Domain Mutation Following ALK inhibitor(s) failure in advanced ALK positive non-small-cell lung cancer: analysis and literature review. Clin Lung Cancer. 2016;17(5):e77–94.

79. Pinto JA, Raez LE, Domingo G. Clinical consequences of resistance to ALK inhibitors in non-small cell lung cancer. Expert Rev Respir Med. 2020;14(4):385–90.

80. Zhao M, Shao T, Shao H, et al. Identifying optimal ALK inhibitors in first- and second-line treatment of patients with advanced ALK-positive non-small-cell lung cancer: a systematic review and network meta-analysis. BMC Cancer. 2024;24(1):186.

81. Wei J, Zhou H, Song Z. Sequential therapy with crizotinib and a secondgeneration ALK inhibitor versus direct therapy of a second-generation ALK inhibitor in ALK-positive advanced lung cancer: a real-world study. J Thorac Dis. 2023;15(5):2425–37.

82. Ito K, Hataji O, Kobayashi H, et al. Sequential therapy with Crizotinib and Alectinib in ALK-rearranged non-small cell lung cancer-a multicenter retrospective study. J Thorac Oncol. 2017;12(2):390–6.

83. Mott DJ, Schirrmacher H, Al-Janabi H, et al. Modelling spillover effects on informal carers: the carer QALY trap. PharmacoEconomics. 2023;41(12):1557–61.

84. Riley RD, Lambert PC, Abo-Zaid G. Meta-analysis of individual participant data: rationale, conduct, and reporting. BMJ. 2010;340:c221.

## Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.