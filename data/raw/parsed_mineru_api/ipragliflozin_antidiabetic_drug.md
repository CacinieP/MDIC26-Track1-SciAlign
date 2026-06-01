Review

# Evaluating the Comparative Effectiveness of Sodium-Glucose Transporter 2 Inhibitors (SGLT-2i) on Liver Enzymes in Patients With Nonalcoholic Fatty Liver Disease: A Comprehensive Systematic Review and Bayesian Network Meta-Analysis of Randomized Controlled Trials

<!-- image-->

Ibrahim Khalil, MBBS 1, \* , Md Imran Hossain, MBBS 2 , Mahmuda Akter, MBBS 2

1 Dhaka Medical College and Hospital, Dhaka, Bangladesh

2 Manikganj Medical College and Hospital, Manikganj, Bangladesh

## a r t i c l e i n f o

Article history:   
Received 30 April 2025   
Received in revised form   
12 June 2025   
Accepted 18 August 2025   
Available online 22 August 2025   
Key words:   
SGLT-2 inhibitors   
nonalcoholic fatty liver disease   
Bayesian Network Meta-Analysis   
liver enzymes   
metabolic outcomes

## a b s t r a c t

Objective: This study aimed to conduct the first network meta-analysis (NMA) comparing the effectiveness of sodium-glucose transporter 2 (SGLT-2) inhibitorsddapagliflozin, empagliflozin, and ipragliflozindin improving liver-related and metabolic outcomes in patients with nonalcoholic fatty liver disease (NAFLD), utilizing a robust Bayesian NMA framework. Methods: We conducted a systematic review and Bayesian NMA of randomized controlled trials (RCTs) up to December 31, 2024, following Preferred Reporting Items for Systematic Reviews and Network Meta-Analyses guidelines. Databases (PubMed, Cochrane Library, Scopus, Embase) were searched for RCTs involving NAFLD patients (with or without type 2 diabetes) treated with SGLT-2 inhibitors versus placebo/standard treatments. Outcomes included alanine aminotransferase, aspartate aminotransferase, gamma-glutamyl transferase, fibrosis-4 score, body weight, and fasting plasma glucose. A random-effects Bayesian NMA was performed using a Markov Chain Monte Carlo method, with treatments ranked via Surface Under the Cumulative Ranking Curve (SUCRA) scores. Results: Eleven RCTs (805 patients) were included. Dapagliflozin led in alanine aminotransferase (mean difference [MD]: 11.35 IU/L, 95% CrI: 18.39 to 4.19, SUCRA: 84.87%), aspartate aminotransferase (MD: 7.96 IU/L, 95% CrI: 15.69 to 0.18, SUCRA: 81.70%), and body weight reduction (MD: 3.60 kg, 95% CrI: 5.92 to 1.64, SUCRA: 88.88%). Ipragliflozin excelled in gamma-glutamyl transferase (MD: 15.19 IU/L, 95% CrI: 31.25 to 2.11, SUCRA: 81.35%) and fasting plasma glucose reduction (MD: 2.20 mmol/L, 95% CrI: 9.88 to 5.30, SUCRA: 59.79%). Empagliflozin topped fibrosis-4 score reduction (MD: 0.12, 95% CrI: 0.42 to 0.13, SUCRA: 73.27%). Conclusion: SGLT-2 inhibitors significantly improve liver and metabolic outcomes in NAFLD, with dapagliflozin, ipragliflozin, and empagliflozin offering distinct benefits, supporting personalized treatment strategies.

© 2025 American Association of Clinical Endocrinology. Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

Abbreviations: ALT, alanine aminotransferase; AST, aspartate aminotransferase; CrI, credible interval; FIB-4, fibrosis-4 (score); FPG, fasting plasma glucose; GGT, gamma-glutamyl transferase; MCMC, Markov Chain Monte Carlo; MD, mean difference; NAFLD, nonalcoholic fatty liver disease; NASH, nonalcoholic steatohepatitis; NMA, network meta-analysis; RCT, randomized controlled trial; SGLT-2, sodium-glucose transporter 2; SUCRA, surface under the cumulative ranking curve; T2DM, type 2 diabetes mellitus.

\* Address correspondence to Dr Ibrahim Khalil, Dhaka Medical College and Hospital, Secretariat Road, Dhaka 1000, Bangladesh.

E-mail address: ibrahim124904@gmail.com (I. Khalil).

## Introduction

Nonalcoholic fatty liver disease (NAFLD) is a global health challenge, affecting approximately 25% to 30% of adults and up to 70% to 90% of those with type 2 diabetes mellitus (T2DM) or obesity.1 Characterized by hepatic fat accumulation, NAFLD ranges from simple steatosis to nonalcoholic steatohepatitis (NASH), which can progress to fibrosis, cirrhosis, and hepatocellular carcinoma.2 Its association with insulin resistance, dyslipidemia, and cardiovascular disease underscores the need for effective therapies targeting both liver and metabolic outcomes.3,4 Current management relies heavily on lifestyle interventions, such as weight loss, but their limited sustainability highlights the role of pharmacological treatments.5

Sodium-glucose transporter 2 (SGLT-2) inhibitors, including dapagliflozin, empagliflozin, and ipragliflozin, offer promise for NAFLD due to their effects on glucose metabolism, body weight, and inflammation.6 By inhibiting renal glucose reabsorption, these agents reduce fasting plasma glucose (FPG) and hemoglobin A1c, while also promoting weight loss and potentially improving liver enzymes like alanine aminotransferase (ALT), aspartate aminotransferase (AST), and gamma-glutamyl transferase (GGT).7 Clinical trials suggest SGLT-2 inhibitors may decrease hepatic fat and fibrosis markers, such as the fibrosis-4 (FIB-4) score, particularly in NAFLD patients with T2DM.8-10 For instance, dapagliflozin has been shown to lower ALT and body weight, while empagliflozin may improve fibrosis indices.9,10 However, the comparative effectiveness of these agents remains unclear due to heterogeneous trial outcomes and a lack of head-to-head comparisons.11-13

Traditional meta-analyses have evaluated individual SGLT-2 inhibitors against placebo but cannot rank multiple treatments across diverse outcomes.12,13 Bayesian network meta-analysis (NMA) addresses this gap by integrating direct and indirect evidence, enabling robust comparisons and probabilistic rankings. 14 No prior Bayesian NMA has comprehensively assessed dapagliflozin, empagliflozin, and ipragliflozin for NAFLD-specific outcomes. This study aimed to compare the effectiveness of SGLT-2 inhibitors in reducing ALT, AST, GGT, FIB-4 score, body weight, and FPG in NAFLD patients using Bayesian NMA. By synthesizing randomized controlled trial data, we sought to guide clinical decisionmaking and inform future research for this prevalent disease.

## Methods

This Bayesian network meta-analysis was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Network Meta-Analyses guidelines to ensure methodological rigor and transparency.15 The primary objective was to evaluate and compare the effectiveness of SGLT-2 inhibitors, including dapagliflozin, empagliflozin, and ipragliflozin, in improving liver-related and metabolic parameters in patients with NAFLD. These parameters included reductions in alanine aminotransferase (ALT), aspartate aminotransferase (AST), gamma-glutamyl transferase (GGT), FIB-4 score, body weight, and fasting plasma glucose (FPG). The study was registered with international prospective register of systematic reviews to ensure transparency in the study design and methodology.16

## Study Selection Criteria

## Eligibility Criteria

Predefined inclusion and exclusion criteria were applied to select eligible studies. Only randomized controlled trials (RCTs) were included.17,18 Studies were required to involve adult participants (aged 18 years) diagnosed with NAFLD, with or without concurrent T2DM. The interventions consisted of any SGLT-2 inhibitor, including but not limited to dapagliflozin, empagliflozin, and ipragliflozin, administered as monotherapy or in combination with standard treatments (eg, metformin, insulin). The comparator group included placebo or standard treatments without SGLT-2 inhibitors. Primary outcomes encompassed changes in ALT (IU/L), AST (IU/L), GGT (IU/L), FIB-4 score, body weight (kg), and FPG (mmol/L). Studies published in English were eligible, with no

## Highlights

 Bayesian network meta-analysis evaluated sodium-glucose transporter 2 inhibitors effects on liver and metabolic outcomes in nonalcoholic fatty liver disease (NAFLD) patients

Treatments were ranked using Surface Under the Cumulative Ranking Curve (SUCRA) scores for comparative efficacy across multiple outcomes

 Dapagliflozin led alanine aminotransferase reduction (mean difference [MD]: 11.35 IU/L, SUCRA: 84.87%) and body weight reduction (MD: 3.60 kg, SUCRA: 88.88%) in NAFLD

 Ipragliflozin excelled in gamma-glutamyl transferase reduction (MD: 15.19 IU/L, SUCRA: 81.35%) and fasting plasma glucose reduction (MD: 2.20 mmol/L, SUCRA: 59.79%) in NAFLD

 Empagliflozin topped fibrosis-4 score reduction (MD: 0.12, SUCRA: 73.27%), indicating superior anti-fibrotic effects in NAFLD

## Clinical Relevance

Sodium-glucose transporter 2 inhibitors, including dapagliflozin, empagliflozin, and ipragliflozin, significantly improve liverrelated (alanine aminotransferase, aspartate aminotransferase, gamma-glutamyl transferase (GGT), fibrosis-4 score) and metabolic (body weight, fasting plasma glucose [FPG]) outcomes in nonalcoholic fatty liver disease patients. Dapagliflozin s superiority in reducing liver enzymes and body weight, ipragliflozin s efficacy in GGT and FPG, and empagliflozin s impact on fibrosis markers support personalized treatment strategies.

restrictions on publication dates up to December 31, 2024, to capture the most recent evidence.

## Information Sources

A comprehensive literature search was conducted across major electronic databases, including PubMed, Cochrane Library, Scopus, and Embase, covering studies from inception to December 31, 2024.19 The search strategy utilized Medical Subject Headings and keywords relevant to the target population (“nonalcoholic fatty liver disease,” “NAFLD,” “steatosis”), interventions (“sodiumglucose transporter 2 inhibitors,” “dapagliflozin,” “empagliflozin,” “ipragliflozin”), and study design (“randomized controlled trial,” “RCT”). All records were managed using EndNote software, and duplicates were removed prior to screening.20 Detailed search strategy is provided in Supplementary Table 1.

## Study Selection Process

Two independent reviewers screened the titles and abstracts of all identified records based on the eligibility criteria. Full-text articles of potentially eligible studies were retrieved for further evaluation.19 Discrepancies during screening or full-text review were resolved through discussion, with a third reviewer consulted if consensus could not be reached. A Preferred Reporting Items for Systematic Reviews and Meta-Analyses flow diagram was generated to summarize the study selection process (Fig. 1).15

## PRISMA 2020 flow diagram for Study Selection Process

<!-- image-->  
Fig. 1. Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 flow diagram for systematic reviews which included searches of databases and registers.

## Data Extraction

Data extraction was performed independently by 2 reviewers using a standardized, pre-piloted form.18 Extracted data included study characteristics (eg, authors, publication year, country, study design, funding sources), participant-level characteristics (eg, sample size, age, sex distribution, baseline NAFLD severity, T2DM status, concurrent medications), and intervention details (eg, type of SGLT-2 inhibitor, dosage, treatment duration). Control group characteristics, including placebo or standard treatment, were also extracted.21,22 Outcome data included mean differences (MD) for ALT (IU/L), AST (IU/L), GGT (IU/L), FIB-4 score, body weight (kg), and FPG (mmol/L) compared to baseline or placebo.

## Data Analysis

## Network Meta-Analysis

A Bayesian network meta-analysis (NMA) was conducted using R (version 4.4.3).21,23,24 A random-effects model was employed to account for between-study heterogeneity, using a Markov Chain

Monte Carlo (MCMC) method.25 Non-informative normal priors were applied for treatment effects, and weakly informative priors were used for variance components.26 Model convergence was assessed using convergence diagnostics, including the Gelman-Rubin Diagnostic, Deviance Information Criterion, and potential scale reduction factor.27-30 The MCMC process involved 10 000 adaptation steps, a burn-in period of 20 000 iterations, and 250 000 iterations to ensure robust estimates.25 Mean differences (MD) compared to placebo were calculated for continuous outcomes (ALT, AST, GGT, FIB-4 score, body weight, FPG). Results were reported as posterior medians with 95% credible intervals (CrI). Surface Under the Cumulative Ranking Curve (SUCRA) values were computed to rank treatments, with higher SUCRA values indicating greater effectiveness.14

## Model Specifications and Parameters

A Bayesian MCMC model was used to estimate treatment effects across the network.25 Convergence was evaluated using trace plots, Gelman-Rubin statistics, and Deviance Information Criterion to ensure stable estimates.27,30 Sensitivity analyses tested the robustness of findings by varying model assumptions, such as prior distributions.26

Statistical Significance and Uncertainty

Results were expressed as posterior median estimates with 95% CrI.29 SUCRA values ranked treatments for each outcome, with values closer to 100% indicating higher efficacy.14 Uncertainty was quantified through the width of CrI and posterior distributions.30

## Risk of Bias Assessment

The risk of bias for each included study was evaluated using the Cochrane Risk of Bias Tool (RoB 2.0),22 assessing domains including random sequence generation, allocation concealment, blinding of participants and personnel, blinding of outcome assessment, incomplete outcome data, and selective reporting. 31,32 Studies were classified as low, unclear, or high risk of bias.32,33

## Reporting

The Bayesian NMA results were reported in accordance with Preferred Reporting Items for Systematic Reviews and Network Meta-Analyses guidelines.15 A Preferred Reporting Items for Systematic Reviews and Meta-Analyses flow diagram detailed the study selection process (Fig. 1), and findings were presented using forest plots, network diagrams (Fig. 2), and SUCRA rankings to illustrate the relative effectiveness of SGLT-2 inhibitors, including dapagliflozin, empagliflozin, and ipragliflozin, versus placebo across liver-related and metabolic outcomes (Figs. 3 and 4). 14

Result

## Baseline Characteristics of Included Studies

## Effect on Alanine Aminotransferase (ALT)

This Bayesian network meta-analysis included 11 RCTs involving 805 patients with nonalcoholic fatty liver disease (NAFLD).9,10,34e42 The studies evaluated dapagliflozin, empagliflozin, and ipragliflozin effects on liver enzymes, FIB-4 score, body weight, and FPG compared to placebo or standard treatments (Table 1). Participant numbers ranged from 38 to 160, with intervention groups of 18e80 and control groups of 15e80. Dapagliflozin (5e10 mg) was used in 5 studies, empagliflozin (10e25 mg) in four, and ipragliflozin (50 mg) in two. Control groups included placebo (6 studies), metforminbased regimens (two studies), standard treatments (two studies), or diet/exercise therapy (one study). Mean ages in intervention groups ranged from 29 ± 11 to 65 ± 8 years, and in control groups from 31 ± 14 to 62 ± 7 years. Treatment durations varied from 12 to 72 weeks, with most lasting 12e24 weeks. Risk of bias of included studies are provided in Supplementary Fig. 1. Network Plots of Interventions were shown in Fig. 2.

For the reduction in alanine aminotransferase (ALT) levels in patients with NAFLD, this Bayesian NMA demonstrated that Dapagliflozin achieved the greatest efficacy in reducing ALT compared to Placebo, with a mean difference (MD) of 11.35 IU/L (95% credible interval [CrI]: 18.39 to 4.19; Surface Under the Cumulative Ranking Curve [SUCRA]: 84.87%). Empagliflozin followed, with an MD of 8.07 IU/L (95% CrI: 16.60 to 0.18; SUCRA: 61.77%) versus Placebo (Figs. 3 and 5 A). Ipragliflozin exhibited an MD of 6.05 IU/L (95% CrI: 17.95 to 4.83; SUCRA: 48.50%)

<!-- image-->  
D

<!-- image-->  
E

<!-- image-->

<!-- image-->

F  
<!-- image-->

<!-- image-->  
Fig. 2. Network Plots of Interventions for Outcomes in NAFLD Patients. Network plots illustrate direct comparisons between dapagliflozin, empagliflozin, ipragliflozin, and placebo for outcomes in nonalcoholic fatty liver disease (NAFLD) patients, with node sizes reflecting the number of participants and edge thickness indicating the number of studies (noted on edges). (A). ALT, (B). AST, (C). GGT, (D). Fibrosis-4 (FIB-4) score, (E). Body weight (BW), (F). Fasting plasma glucose (FPG).

<!-- image-->

D  
<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

F  
<!-- image-->

<!-- image-->  
Fig. 3. Forest plots, SUCRA plots, and rank plots for liver enzyme outcomes in NAFLD patients treated with SGLT-2 Inhibitors. This figure presents the Bayesian network metaanalysis results for dapagliflozin, empagliflozin, ipragliflozin, and placebo in nonalcoholic fatty liver disease (NAFLD) patients. A-C. Forest plots showing mean differences (MD) in IU/L with 95% credible intervals (CrI) relative to placebo for: (A). Alanine Aminotransferase (ALT), (B). Aspartate Aminotransferase (AST), (C). Gamma-Glutamyl Transferase (GGT). D-F. Surface Under the Cumulative Ranking Curve (SUCRA) plots displaying the probability of each treatment achieving higher rankings (smaller outcome values) for: (D). ALT, (E). AST, (F). GGT. G-I. Rank plots illustrating the probability of each treatment achieving specific ranks (1e4, with 1 being the best) for: (G). ALT, H. AST, I. GGT.

compared to Placebo, which served as the reference (SUCRA: 4.86%).

## Effect on Aspartate Aminotransferase (AST)

For the reduction in aspartate aminotransferase (AST) levels in patients with NAFLD, this Bayesian NMA demonstrated that Dapagliflozin achieved the greatest efficacy in reducing AST compared to Placebo, with a mean difference (MD) of 7.96 IU/L (95% CrI: 15.69 to 0.18; SUCRA: 81.70%). Empagliflozin followed, with an MD of 6.68 IU/L (95% CrI: 16.17 to 2.32; SUCRA: 72.43%) versus Placebo. Ipragliflozin exhibited an MD of 0.01 IU/L (95% CrI: 12.39 to 12.02; SUCRA: 26.28%) compared to Placebo (Figs. 3 and 5 B), which served as the reference (SUCRA: 19.58%).

## Effect on Gamma-Glutamyl Transferase (GGT)

For the reduction in gamma-glutamyl transferase (GGT) levels in patients with NAFLD, this Bayesian NMA demonstrated that Ipragliflozin achieved the greatest efficacy in reducing GGT compared to Placebo, with a mean difference (MD) of 15.19 IU/L (95% CrI: 31.25 to 2.11; SUCRA: 81.35%). Empagliflozin followed, with an MD of 11.56 IU/L (95% CrI: 27.37 to 4.25; SUCRA: 62.29%) versus Placebo (Fig. 3, Supplemental Fig. 2). Dapagliflozin exhibited an MD of 9.52 IU/L (95% CrI: 22.28 to 2.77; SUCRA: 52.15%) compared to Placebo, which served as the reference (SUCRA: 4.20%).

## Effect on FIB-4 Score

For the reduction in FIB-4 score in patients with NAFLD, data from this NMA demonstrated that Empagliflozin achieved the greatest efficacy in reducing FIB-4 score compared to Placebo, with a mean difference (MD) of 0.12 (95% CrI: 0.42 to 0.13; SUCRA: 73.27%). Dapagliflozin followed, with an MD of 0.09 (95% CrI: 0.44 to 0.26; SUCRA: 57.55%) versus Placebo (Fig. 4, Supplemental Fig. 3). Placebo served as the reference (SUCRA: 19.18%).

## Effect on Body Weight

For the reduction in body weight in patients with NAFLD, data this Bayesian NMA demonstrated that Dapagliflozin achieved the greatest efficacy in reducing body weight compared to Placebo, with a mean difference (MD) of 3.60 kg (95% CrI: 5.92 to 1.64; SUCRA: 88.88%). Ipragliflozin and Empagliflozin followed, both with an MD of 2.13 kg (95% CrI: 5.91 to 1.31 for Ipragliflozin; 95% CrI: 4.60 to 0.38 for Empagliflozin; SUCRA: 53.63% and 53.24%, respectively) versus Placebo (Fig. 4, Supplemental Fig. 4). Placebo served as the reference (SUCRA: 4.25%).

## Effect on Fasting Plasma Glucose

For the reduction in fasting plasma glucose (FPG) in patients with NAFLD, data from this Bayesian NMA demonstrated that Ipragliflozin achieved the greatest efficacy in terms of mean difference in reducing FPG compared to Placebo, with a mean difference (MD) of 2.20 mmol/L (95% CrI: 9.88 to 5.30; SUCRA: 59.79%). Dapagliflozin followed, with an MD of 2.10 mmol/L (95%

<!-- image-->

D  
<!-- image-->

<!-- image-->

<!-- image-->

E  
<!-- image-->

<!-- image-->

<!-- image-->

F  
<!-- image-->

<!-- image-->  
Fig. 4. Forest plots, SUCRA plots, and rank plots for fibrosis and metabolic outcomes in NAFLD patients treated with SGLT-2 inhibitors. This figure presents Bayesian network metaanalysis results for dapagliflozin, empagliflozin, ipragliflozin, and placebo in nonalcoholic fatty liver disease (NAFLD) patients, focusing on fibrosis and metabolic outcomes. A-C. Forest plots showing mean differences (MD) with 95% credible intervals (CrI) relative to placebo for: A. FIB-4 score, B. Body weight (BW, in kg), C. Fasting plasma glucose (FPG, in mmol/L). D-F. Surface Under the Cumulative Ranking Curve (SUCRA) plots displaying the probability of each treatment achieving higher rankings (smaller outcome values) for: (D). FIB-4 score, E. BW, F. FPG. G-I. Rank plots illustrating the probability of each treatment achieving specific ranks (1e4, with 1 being the best) for: G. FIB-4 score, H. BW, I. FPG. FIB-4 ¼ fibrosis-4.

CrI: 9.71 to 1.29; SUCRA: 64.98%) versus Placebo (Fig. 4, Supplemental Fig. 5). Empagliflozin exhibited an MD of 1.98 mmol/L (95% CrI: 10.41 to 5.56; SUCRA: 55.67%) compared to Placebo, which served as the reference (SUCRA: 19.57%).

## Discussion

Nonalcoholic fatty liver disease (NAFLD) represents a pressing global health challenge, with a prevalence of 25% to 30% in the general adult population and up to 70% to 90% among individuals with T2DM or obesity.1,2 Characterized by excessive hepatic fat accumulation, NAFLD encompasses a spectrum ranging from benign steatosis to nonalcoholic steatohepatitis (NASH), which can progress to fibrosis, cirrhosis, and hepatocellular carcinoma.2,3 Its intricate association with insulin resistance, dyslipidemia, and cardiovascular disease underscores the critical need for therapies that address both hepatic and metabolic dysfunction.3 ,4 While lifestyle interventions, such as weight loss through diet and exercise, remain the cornerstone of NAFLD management, their limited long-term sustainability has driven the exploration of pharmacological interventions.5 Sodium-glucose transporter 2 (SGLT-2) inhibitorsddapagliflozin, empagliflozin, and ipragliflozindhave emerged as promising therapeutic agents, leveraging their multifaceted effects on glucose metabolism, body weight, and inflammation.6,7 This Bayesian network meta-analysis (NMA), the first to comprehensively compare these three SGLT-2 inhibitors in NAFLD patients, evaluates their comparative effectiveness in improving liver-related outcomes (alanine aminotransferase [ALT], aspartate aminotransferase [AST], gamma-glutamyl transferase [GGT], and FIB-4 score) and metabolic parameters (body weight and fasting plasma glucose [FPG]). By synthesizing data from 11 RCTs involving 805 patients, our findings delineate distinct efficacy profiles for each SGLT-2 inhibitor (Table 2), offering critical insights for personalized treatment strategies while highlighting methodological limitations and avenues for future research.

## Liver Enzyme Reductions

Liver enzymes, including ALT, AST, and GGT, serve as surrogate markers of hepatocyte injury, hepatic fat accumulation, and oxidative stress in NAFLD.3 Elevated levels of these enzymes are indicative of underlying liver pathology, making their reduction a primary therapeutic target.3 Our Bayesian NMA demonstrates that dapagliflozin achieves the most substantial reductions in ALT (mean difference [MD]: 11.35 IU/L, 95% credible interval [CrI]: 18.39 to 4.19, Surface Under the Cumulative Ranking Curve [SUCRA]: 84.87%) and AST (MD: 7.96 IU/L, 95% CrI: 15.69 to 0.18, SUCRA: 81.70%) compared to placebo.9 These findings position dapagliflozin as the most effective SGLT-2 inhibitor for mitigating hepatocyte injury, likely through mechanisms such as reduced de novo lipogenesis and enhanced b-oxidation, which decrease hepatic fat content.7 The high SUCRA scores reflect dapagliflozin’s robust performance, making it a preferred choice for patients with early NAFLD characterized by significant steatosis and elevated liver enzymes. Empagliflozin follows with meaningful reductions in ALT (MD: 8.07 IU/L, 95% CrI: 16.60 to 0.18, SUCRA: 61.77%) and AST (MD: 6.68 IU/L, 95% CrI: 16.17 to 2.32, SUCRA: 72.43%), indicating a solid but less pronounced effect compared to dapagliflozin.8 Ipragliflozin, however, demonstrates a more modest reduction in ALT (MD: 6.05 IU/L, 95% CrI: 17.95 to 4.83, SUCRA:

able 1 Population Baseline Characteristics of Included Studies with References
<table><tr><td>Studies</td><td>No. of participants Total</td><td>No. of participants (Intervention/Control)</td><td>Intervention</td><td>Intervention dose</td><td>Intervention</td><td> ± e  ± y Control</td><td></td><td>Control</td><td>Treatment Duration (wks)</td><td>Country</td></tr><tr><td>Han et al,34</td><td>44</td><td>(29/15)</td><td>Ipragliflozin</td><td>50 mg</td><td>56 ± 8</td><td>57 ±9</td><td>Placebo controlled</td><td>Metformin + PPoglitazone</td><td>24</td><td>Korea</td></tr><tr><td>Eriksson et al,9</td><td>40</td><td>(20/20)</td><td>Dapagliflozin</td><td>10 mg</td><td>65 ± 6</td><td>61 ± 6</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>12</td><td>Sweden</td></tr><tr><td>Elhini et al,35</td><td>160</td><td>(80/80)</td><td>Empagliflozin</td><td>25 mg</td><td>47 ± 7</td><td>46 ± 8</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>24</td><td>Egypt</td></tr><tr><td>Shi et al, 36</td><td>78</td><td>(40/38)</td><td>Dapagliflozin + eformin</td><td>10 mg</td><td>49 ± 9</td><td>47 ± 10</td><td>Placebo controlled</td><td>Metformin + antidiabetic treatment</td><td>24</td><td>China</td></tr><tr><td>Hussain et al,37</td><td>138</td><td>(67/71)</td><td>Dapagliflozin</td><td>5-10 mg</td><td>29 ± 11</td><td>31 ± 14</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>12</td><td>Pakistan</td></tr><tr><td>Phruksotsai et lt,38</td><td>38</td><td>(18/20)</td><td>Dapagliflozin</td><td>10 mg</td><td>57 ± 6</td><td>62 ± 7</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>12</td><td>Thailand</td></tr><tr><td>Chehrehgosha et al,9</td><td>72</td><td>(35/37)</td><td>Empagliflozin</td><td>10 mg</td><td>65 ± 8</td><td>61 ± 8</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>24</td><td>Iran</td></tr><tr><td>Taheri et al,40</td><td>90</td><td>(43/47)</td><td>Empagliflozin</td><td>10 mg</td><td>43 ± 8</td><td>41 ± 9</td><td>Double blinded, placebo controlled</td><td>Placebo</td><td>24</td><td>Iran</td></tr><tr><td>Kuchay et al,10</td><td>42</td><td>(22/20)</td><td>Empagliflozin</td><td>10 mg</td><td>49 ± 9</td><td>41 ± 10</td><td>Placebo controlled</td><td>Standard treatment</td><td>20</td><td>India</td></tr><tr><td>Takaashi et al,4</td><td>46</td><td>(21/25)</td><td>Ipragliflozin</td><td>50 mg</td><td>55 ± 8</td><td>57 ±9</td><td>Open-label randomized controlled trial</td><td>Diet/exercise therapy, antidiabetic drugs</td><td>72</td><td>Japan</td></tr><tr><td>Aso et al,42</td><td>57</td><td>(33/24)</td><td>Dapagliflozin</td><td>5 mg</td><td>50 ± 8</td><td>51 ± 9</td><td>Placebo controlled</td><td>Standard treatment without SGLT-2 inhibitors</td><td>24</td><td>Japan</td></tr></table>

48.50%) and a negligible effect on AST (MD: 0.01 IU/L, 95% CrI: 12.39 to 12.02, SUCRA: 26.28%), suggesting it may be less effective in addressing acute hepatocyte injury.1

In contrast, ipragliflozin excels in reducing GGT, achieving the greatest efficacy with an MD of 15.19 IU/L (95% CrI: 31.25 to 2.11, SUCRA: 81.35%) compared to placebo.11 GGT, a marker of oxidative stress and inflammation, is particularly relevant in NAFLD, as these processes contribute to disease progression.3,7 Ipragliflozin’s superiority in this domain may reflect its ability to modulate inflammatory pathways, potentially through reduced oxidative stress, making it particularly suitable for patients with NAFLD driven by these mechanisms.7 Empagliflozin (MD: 11.56 IU/L, 95% CrI: 27.37 to 4.25, SUCRA: 62.29%) and dapagliflozin (MD: 9.52 IU/L, 95% CrI: 22.28 to 2.77, SUCRA: 52.15%) also reduce GGT, but their effects are less pronounced, reinforcing ipragliflozin’s unique role in this outcome.8,9 These differential effects on liver enzymes highlight the complementary strengths of SGLT-2 inhibitors, with dapagliflozin addressing hepatocyte injury and ipragliflozin targeting oxidative stress, enabling clinicians to tailor therapy based on the dominant pathophysiological features of NAFLD.

## Fibrosis Marker Reduction

Liver fibrosis, a hallmark of NAFLD progression, is a critical determinant of long-term outcomes, including the risk of cirrhosis and hepatocellular carcinoma.2,3 The FIB-4 score, a non-invasive marker, provides a reliable estimate of fibrosis severity, guiding clinical decision-making.3 Our NMA identifies empagliflozin as the most effective SGLT-2 inhibitor for reducing FIB-4 scores (MD: 0.12, 95% CrI: 0.42 to 0.13, SUCRA: 73.27%), followed by dapagliflozin (MD: 0.09, 95% CrI: 0.44 to 0.26, SUCRA: 57.55%).10 Empagliflozin’s anti-fibrotic effect may be driven by its ability to reduce hepatic stellate cell activation and collagen deposition, mediated by anti-inflammatory properties and improvements in insulin sensitivity.6,7 This positions empagliflozin as the preferred agent for patients with advanced NAFLD and suspected or confirmed fibrosis, where preventing progression to cirrhosis is a priority. Dapagliflozin’s modest effect on FIB-4 suggests a secondary role in fibrosis management, potentially due to its primary focus on reducing hepatic fat rather than directly targeting fibrotic pathways.9 The limited data on ipragliflozin for FIB-4 outcomes reflect a gap in the literature, particularly in studies focusing on fibrosis markers, which warrants further investigation.11 These findings underscore the potential of SGLT-2 inhibitors to address NAFLD progression, with empagliflozin offering a targeted approach to fibrosis mitigation.

## Body Weight and FPG Reductions

Metabolic dysfunction, encompassing obesity and hyperglycemia, is a central driver of NAFLD pathogenesis, contributing to hepatic fat accumulation and disease progression.4 Our NMA highlights dapagliflozin’s superiority in body weight reduction (MD: 3.60 kg, 95% CrI: 5.92 to 1.64, SUCRA: 88.88%), significantly outperforming ipragliflozin and empagliflozin, both with an MD of 2.13 kg (95% CrI: 5.91 to 1.31 for ipragliflozin; 95% CrI: 4.60 to 0.38 for empagliflozin; SUCRA: 53.63% and 53.24%, respectively).9 This robust weight loss, likely driven by caloric loss through glycosuria, reduces visceral and hepatic fat, amplifying dapagliflozin’s hepatic benefits by decreasing steatosis and lipotoxicity.6 The comparable but less pronounced effects of ipragliflozin and empagliflozin suggest they still contribute meaningfully to weight management, but dapagliflozin’s dominance makes it the preferred choice for patients where weight reduction is a primary therapeutic goal.

<!-- image-->  
Fig. 5. League Table with Heatmap Comparing Effects of SGLT-2 Inhibitors on Liver Enzymes in NAFLD. Values represent mean differences (MD) in IU/L with 95% credible intervals (CrI). Color intensity indicates the magnitude and direction of effect: green for significant reductions (favoring the treatment in the column), red for increases (favoring the comparator in the row), and gray for no comparison (diagonal). (A). Alanine aminotransferase (ALT): Dapagliflozin showed the largest reduction versus placebo (MD: 11.35 IU/L, 95% CrI: 18.39 to 4.19). (B). Aspartate aminotransferase (AST): Dapagliflozin again led with a reduction of 7.96 IU/L (95% CrI: 15.69 to 0.18) compared to placebo.

For FPG, ipragliflozin leads with an MD of 2.20 mmol/L (95% CrI: 9.88 to 5.30, SUCRA: 59.79%), closely followed by dapagliflozin (MD: 2.10 mmol/L, 95% CrI: 9.71 to 1.29, SUCRA: 64.98%) and empagliflozin (MD: 1.98 mmol/L, 95% CrI: 10.41 to 5.56, SUCRA: 55.67%).11 The tight clustering of FPG reductions indicates that all three SGLT-2 inhibitors effectively improve glycemic control, with ipragliflozin’s slight advantage possibly attributable to its pharmacokinetic profile, which may enhance sustained glucose excretion.7 This makes ipragliflozin particularly appealing for NAFLD patients with T2DM or prediabetes, where glycemic control is critical. Dapagliflozin’s strong performance in both weight and FPG reduction positions it as a versatile option for patients with concurrent metabolic challenges, while empagliflozin’s consistent but slightly less potent effect supports its role in comprehensive metabolic management.

Comparison of SGLT-2 Inhibitor Effects Across Glucose Tolerance Status

The efficacy of SGLT-2 inhibitors varies across glucose tolerance status, influencing their clinical application in NAFLD. In patients with T2DM, dapagliflozin’s significant reductions in ALT, AST, and body weight (MD: 11.35 IU/L, 7.96 IU/L, and 3.60 kg, respectively) and ipragliflozin’s efficacy in GGT and FPG (MD: 15.19 IU/L and 2.20 mmol/L) are particularly pronounced.9,11 These effects likely stem from the heightened insulin resistance and metabolic dysfunction in T2DM, which amplify the glycosuria-driven benefits of SGLT-2 inhibitors.6 Empagliflozin’s reduction in FIB-4 score (MD: 0.12) is also notable In T2DM cohorts, reflecting its antifibrotic potential in this high-risk group.10 In patients with prediabetes and metabolic syndrome, the effects are attenuated, as less severe insulin resistance may reduce the metabolic impact of SGLT-2 inhibitors.40 For those with normal glucose tolerance, data are sparse, but the benefits on liver enzymes and FPG appear diminished due to lower baseline hyperglycemia, limiting glycosuriadriven effects.42 These variations underscore the importance of tailoring SGLT-2 inhibitor therapy to the patient’s metabolic profile, with T2DM patients deriving the greatest benefit due to synergistic effects on glucose and lipid metabolism.

Comparative Effectiveness of SGLT-2 Inhibitors (Dapagliflozin, Empagliflozin, Ipragliflozin) versus Placebo on Liver and Metabolic Outcomes in NAFLD Patients: Results from this Bayesian Network Meta-Analysis
<table><tr><td>Outcome</td><td>Intervention</td><td>Mean difference (MD)</td><td>95% credible interval (Crl)</td><td>SUCRA (%)</td></tr><tr><td>Alanine aminotransferase (AL, IU/L)</td><td>Dapagliflozin</td><td>-11.35</td><td>-18.39 to -4.19</td><td>84.87</td></tr><tr><td></td><td>Empagliflozin</td><td>-8.07</td><td>-16.60 to 0.18</td><td>61.77</td></tr><tr><td></td><td>Ipragliflozin</td><td>-6.05</td><td>-17.95 to 4.83</td><td>48.50</td></tr><tr><td></td><td>Placebo</td><td>Reference</td><td></td><td>4.86</td></tr><tr><td>Aspartate aminotransferase (AST, IU/L)</td><td>Dapagliflozin</td><td>-7.96</td><td>-15.69 to −0.18</td><td>81.70</td></tr><tr><td></td><td>Empagliflozin</td><td>-6.68</td><td>−16.17 to 2.32</td><td>72.43</td></tr><tr><td></td><td>Ipragliflozin</td><td>0.01</td><td>12.39 to 12.02</td><td>26.28</td></tr><tr><td rowspan="3">Gamma-glutamyl transferase (GGT, IU/L)</td><td>Pacebo</td><td>Reference</td><td></td><td>19.58</td></tr><tr><td>Ipragliflozin</td><td>-15.19</td><td>−31.25 to −2.11</td><td>81.35</td></tr><tr><td>Empagliflozn</td><td>-11.56</td><td>27.37 to 4.25</td><td>62.29</td></tr><tr><td></td><td>Dapagliflozin</td><td>-9.52</td><td>22.28 to 2.77</td><td>52.15</td></tr><tr><td>FIB-4 score</td><td>Placebo</td><td>Reference</td><td></td><td>4.20</td></tr><tr><td></td><td>Empagliflozin</td><td>-0.12</td><td>-0.42 to 0.13</td><td>73.27</td></tr><tr><td></td><td>Dapagliflozin</td><td>-0.09</td><td>-0.44 to 0.26</td><td>57.55</td></tr><tr><td></td><td>Placebo</td><td>Reference</td><td></td><td>19.18</td></tr><tr><td>Body weight (kg)</td><td>Dapagliflozin</td><td>-3.60</td><td>−5.92 to -1.64</td><td>88.88</td></tr><tr><td></td><td>Ipragliflozin</td><td>-2.13</td><td>−5.91 to 1.31</td><td>53.63</td></tr><tr><td></td><td>Empagliflozin</td><td>-2.13</td><td>−4.60 to 0.38</td><td>53.24</td></tr><tr><td></td><td>Placebo</td><td>Reference</td><td></td><td>4.25</td></tr><tr><td>Fasting plasma glucose (FPG, mmol/L)</td><td>Ipragliflozin</td><td>-2.20</td><td>-9.88 to 5.30</td><td>59.79</td></tr><tr><td></td><td>Dapaglflozin</td><td>-2.10</td><td>9.71 to 1.29</td><td>64.98</td></tr><tr><td></td><td>Empagliflozin</td><td>-1.98</td><td>-10.41 to 5.56</td><td>55.67</td></tr><tr><td></td><td>Placebo</td><td>Reference</td><td></td><td>19.57</td></tr></table>

## Study Limitations

This NMA has several limitations that warrant careful consideration. First, the sample size of 805 patients across 11 RCTs, while substantial, may limit statistical power, particularly for less-studied outcomes like FIB-4, with trial sizes ranging from 38 to 160 participants.9,10,34-42 Second, the exclusion of other SGLT-2 inhibitors (eg, canagliflozin, sotagliflozin, ertugliflozin) due to insufficient RCT data restricts the generalizability of findings to the broader class of SGLT-2 inhibitors.12 Third, heterogeneity in baseline NAFLD severity, T2DM prevalence, and ethnicity (eg, Asian vs non-Asian cohorts) may introduce confounding, despite the use of a randomeffects model to account for between-study variability.14 Fourth, the predominance of short-term trials (12e24 weeks) may underestimate the long-term effects of SGLT-2 inhibitors on fibrosis progression or regression, as fibrosis changes often require extended periods to manifest.9,10 Fifth, the reliance on indirect comparisons, due to the absence of head-to-head trials, introduces potential inconsistency, although the Bayesian NMA framework mitigates this through robust statistical methods.15 Sixth, the lack of histological outcomes, such as steatosis or NASH resolution, limits insights into direct hepatic effects, which are critical for assessing disease modification.3 Finally, the restriction to Englishlanguage publications may exclude relevant non-English studies, potentially introducing selection bias. 19

## Implications and Future Directions

The findings of this Bayesian NMA have significant implications for clinical practice in NAFLD management. Dapagliflozin’s dominance in reducing ALT, AST, and body weight (MD: 11.35 IU/ L, 7.96 IU/L, and 3.60 kg, respectively) positions it as the optimal choice for patients with early NAFLD and significant steatosis, where mitigating hepatocyte injury and visceral fat accumulation is paramount.9 Ipragliflozin’s superiority in GGT and FPG reduction (MD: 15.19 IU/L and 2.20 mmol/L) makes it ideal for patients with elevated oxidative stress markers or those requiring robust glycemic control, particularly in Asian populations where its use is prevalent.11 Empagliflozin’s lead in FIB-4 score reduction (MD: 0.12) suggests it is the preferred agent for patients with advanced NAFLD and suspected fibrosis, offering a targeted approach to prevent progression to cirrhosis.10 Clinicians should tailor treatment based on patient-specific factors, including T2DM status, baseline liver enzyme levels, fibrosis risk, and regional drug availability, to optimize therapeutic outcomes.

Future research must address the identified limitations to refine the role of SGLT-2 inhibitors in NAFLD management. First, larger RCTs with diverse populations, including non-T2DM and normoglycemic NAFLD patients, are essential to enhance generalizability and clarify efficacy across glucose tolerance states.3 Second, trials incorporating additional SGLT-2 inhibitors, such as canagliflozin, sotagliflozin, and ertugliflozin, would provide a more comprehensive comparison of the class.12 Third, extending trial durations beyond 24 weeks is critical to evaluate long-term effects on fibrosis and histological outcomes, such as NASH resolution or steatosis regression, using gold-standard methods like liver biopsy or magnetic resonance imaging-proton density fat fraction.5 Fourth, head-to-head trials comparing dapagliflozin, ipragliflozin, and empagliflozin would eliminate reliance on indirect comparisons, providing clearer evidence of relative efficacy.14 Fifth, meta-regression analyses exploring covariates such as ethnicity, NAFLD severity, and glucose tolerance status could elucidate heterogeneity and identify subgroups with optimal responses.15 Finally, integrating multiomics approaches, including genomics and metabolomics, could uncover the molecular mechanisms underlying differential responses to SGLT-2 inhibitors, paving the way for precision medicine in NAFLD management.6

## Conclusion

This Bayesian NMA provides robust evidence that SGLT-2 inhibitorsddapagliflozin, ipragliflozin, and empagliflozindsignificantly improve liver enzymes, fibrosis markers, body weight, and FPG in patients with NAFLD. Each inhibitor offers distinct benefits: dapagliflozin excels in reducing ALT, AST, and body weight, making it ideal for early NAFLD with significant steatosis; ipragliflozin leads in GGT and FPG reduction, suitable for patients with oxidative stress or glycemic control needs; and empagliflozin tops FIB-4 score reduction, positioning it as the preferred choice for advanced NAFLD with fibrosis risk. These complementary profiles support personalized treatment strategies tailored to patient-specific clinical and metabolic characteristics. Future studies should prioritize larger, longerterm RCTs, include additional SGLT-2 inhibitors, and incorporate histologic and multiomics data to confirm long-term benefits and optimize therapeutic approaches. By addressing these gaps, SGLT-2 inhibitors can be fully integrated into NAFLD management, offering hope for improved outcomes in this prevalent and progressive disease.

## Author Contributions

I.K., MBBS, did study concept or design, data collection, data analysis or interpretation, writing the paper. Md. I.H., MBBS, draft writing, review and edit. M.A., MBBS, data extraction, draft review and edit.

## Data Availability

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Registration

The study was registered with international prospective register of systematic reviews to ensure transparency and adherence to methodological rigor (Registration ID: CRD420251034426).

## Disclosure

The authors have no conflicts of interest to disclose.

## References

1. Younossi ZM, Koenig AB, Abdelatif D, Fazel Y, Henry L, Wymer M. Global epidemiology of nonalcoholic fatty liver disease-meta-analytic assessment of prevalence, incidence, and outcomes. Hepatology (Baltimore, Md.). 2016;64(1): 73e84. https://doi.org/10.1002/hep.28431.

2. Younossi ZM, Golabi P, Paik JM, Henry A, Van Dongen C, Henry L. The global epidemiology of nonalcoholic fatty liver disease (NAFLD) and nonalcoholic steatohepatitis (NASH): a systematic review. Hepatology (Baltimore, Md.). 2023;77(4):1335e1347. https://doi.org/10.1097/HEP.0000000000000004.

3. Chalasani N, Younossi Z, Lavine JE, et al. The diagnosis and management of nonalcoholic fatty liver disease: practice guidance from the American Association for the study of liver diseases. Hepatology (Baltimore, Md.). 2018;67(1): 328e357. https://doi.org/10.1002/hep.29367.

4. Targher G, Byrne CD, Tilg H. NAFLD and increased risk of cardiovascular disease: clinical associations, pathophysiological mechanisms and pharmacological implications. Gut. 2020;69(9):1691e1705. https://doi.org/10.1136/gutjnl-2020-320622.

5. Vilar-Gomez E, Martinez-Perez Y, Calzadilla-Bertot L, et al. Weight loss through lifestyle modification significantly reduces features of nonalcoholic steatohepatitis. Gastroenterology. 2015;149(2):367e378.e5. https://doi.org/10.1053/ j.gastro.2015.04.005.

6. Scheen AJ. Sodium-glucose cotransporter type 2 inhibitors for the treatment of type 2 diabetes mellitus. Nat Reviews. Endocrinol. 2020;16(10):556e577. https://doi.org/10.1038/s41574-020-0392-2.

7. Heerspink HJ, Perkins BA, Fitchett DH, Husain M, Cherney DZ. Sodium glucose cotransporter 2 inhibitors in the treatment of diabetes mellitus: cardiovascular

and kidney effects, potential mechanisms, and clinical applications. Circulation. 2016;134(10):752e772. https://doi.org/10.1161/CIRCULATIONAHA.116.021 887.

8. Kahl S, Gancheva S, Straßburger K, et al. Empagliflozin effectively lowers liver fat content in well-controlled type 2 diabetes: a randomized, Double-blind, phase 4, placebo-controlled trial. Diabetes Care. 2020;43(2):298e305. https:// doi.org/10.2337/dc19-0641.

9. Eriksson JW, Lundkvist P, Jansson PA, et al. Effects of dapagliflozin and n-3 carboxylic acids on non-alcoholic fatty liver disease in people with type 2 diabetes: a double-blind randomised placebo-controlled study. Diabetologia. 2018;61(9):1923e1934. https://doi.org/10.1007/s00125-018-4675-2.

10. Kuchay MS, Krishan S, Mishra SK, et al. Effect of empagliflozin on liver fat in patients with type 2 diabetes and nonalcoholic fatty liver disease: a randomized controlled trial (E-LIFT trial). Diabetes Care. 2018;41(8):1801e1808. https://doi.org/10.2337/dc18-0165.

11. Ohki T, Isogawa A, Toda N, Tagawa K. Effectiveness of ipragliflozin, a sodiumglucose Co-transporter 2 inhibitor, as a second-line treatment for non-alcoholic fatty liver disease patients with type 2 diabetes mellitus who do not respond to incretin-based therapies including glucagon-like Peptide-1 analogs and dipeptidyl Peptidase-4 inhibitors. Clin Drug Invest. 2016;36(4):313e319. https://doi.org/10.1007/s40261-016-0383-1.

12. Mantovani A, Byrne CD, Scorletti E, Mantzoros CS, Targher G. Efficacy and safety of anti-hyperglycaemic drugs in patients with non-alcoholic fatty liver disease with or without diabetes: an updated systematic review of randomized controlled trials. Diabetes Metab. 2020;46(6):427e441. https://doi.org/10.1016/ j.diabet.2019.12.007.

13. Martínez-Vizcaíno V, Díez-Fernandez A, Alvarez-Bueno C, Martínez-Alfonso J,  Cavero-Redondo I. Safety and efficacy of SGLT2 inhibitors: a multiple-treatment meta-analysis of clinical decision indicators. J Clinical Med. 2021;10(12): 2713. https://doi.org/10.3390/jcm10122713.

14. Salanti G, Ades AE, Ioannidis JP. Graphical methods and numerical summaries for presenting results from multiple-treatment meta-analysis: an overview and tutorial. J Clinical Epidemiology. 2011;64(2):163e171. https://doi.org/10.1016/ j.jclinepi.2010.03.016.

15. Hutton B, Salanti G, Caldwell DM, et al. The PRISMA extension statement for reporting of systematic reviews incorporating network meta-analyses of health care interventions: checklist and explanations. Ann Internal Med. 2015;162(11):777e784. https://doi.org/10.7326/M14-2385.

16. Booth A, Clarke M, Dooley G, Ghersi D, Moher D, Petticrew M, Stewart L. The nuts and bolts of PROSPERO: an international prospective register of systematic reviews. Syst Rev. 2012;1:2. https://doi.org/10.1186/2046-4053-1-2.

17. Shea BJ, Reeves BC, Wells G, Thuku M, Hamel C, Moran J, et al. Amstar 2: a critical appraisal tool for systematic reviews that include randomised or nonrandomised studies of healthcare interventions, or both. BMJ. 2017;358:j4008. https://doi.org/10.1136/bmj.j4008.

18. Higgins JP, Li T, Deeks JJ. Choosing effect measures and computing estimates of effect. In: Higgins JPT, Thomas J, Chandler J, et al., eds. Cochrane Handbook for Systematic Reviews of Interventions. Wiley Online Library, John Wiley & Sons; 2019.

19. Lefebvre C, Glanville J, Briscoe S, et al. Searching for and selecting studies. In: Higgins JPT, Thomas J, Chandler J, et al., eds. Cochrane Handbook for Systematic Reviews of Interventions. Wiley Online Library, John Wiley & Sons; 2019.

20. Bramer WM, Milic J, Mast F. Reviewing retrieved references for inclusion in systematic reviews using EndNote. J Med Libr Assoc. 2017;105(1):84e87. https://doi.org/10.5195/jmla.2017.111.

21. Li T, Puhan MA, Vedula SS, Singh S, Dickersin K, Ad Hoc Network Meta-analysis Methods Meeting Working Group. Network meta-analysis-highly attractive but more methodological research is needed. BMC Med. 2011;9:79. https:// doi.org/10.1186/1741-7015-9-79.

22. Higgins JP, Altman DG, Gøtzsche PC, et al. The Cochrane Collaboration's tool for assessing risk of bias in randomised trials. BMJ (Clinical Research ed.). 2011;343: d5928. https://doi.org/10.1136/bmj.d5928.

23. R Core Team. R: A language and environment for statistical computing. R foundation for statistical computing. https://www.R-project.org/; 2024. Accessed April 15, 2025.

24. Beliveau A, Boyne DJ, Slater J, Brenner D, Arora P. BUGSnet: an R package to  facilitate the conduct and reporting of Bayesian network meta-analyses. BMC Med Res Methodol. 2019;19(1):196. https://doi.org/10.1186/s12874-019-0829- 2.

25. Dias S, Sutton AJ, Ades AE, Welton NJ. Evidence synthesis for decision making 2: a generalized linear modeling framework for pairwise and network metaanalysis of randomized controlled trials. Med Decis Making. 2013;33(5): 607e617. https://doi.org/10.1177/0272989X12458724.

26. Gelman A, Carlin JB, Stern HS, et al. Bayesian data analysis. 3rd ed. Chapman and Hall/CRC; 2013. https://doi.org/10.1201/b16018.

27. Brooks SP, Gelman A. General methods for monitoring convergence of iterative simulations. J Comput Graphical Stat. 1998;7(4):434e455. https://doi.org/ 10.1080/10618600.1998.10474787.

28. van Valkenhoef G, Kuiper J. Gemtc: network meta-analysis using bayesian methods. R Package Version 1.0-1. https://cran.r-project.org/package gemtc; 2021. Accessed April 15, 2025.

29. Dias S, Welton NJ, Sutton AJ, Ades AE. Evidence synthesis for decision making 1: introduction. Med Decis Making. 2013;33(5):597e606. https://doi.org/ 10.1177/0272989X13487604.

30. Spiegelhalter DJ, Best NG, Carlin BP. Angelika Van Der Linde, Bayesian Measures of Model Complexity and Fit. J R Stat Soc Ser B: Stat Methodol. 2002;64(4): 583e639. https://doi.org/10.1111/1467-9868.00353.

31. Chaimani A, Caldwell DM, Li T, Higgins JP, Salanti G. Undertaking network meta-analyses. In: Higgins JPT, Thomas J, Chandler J, et al., eds. Cochrane Handbook for Systematic Reviews of Interventions. Wiley Online Library, John Wiley & Sons; 2019.

32. Sterne JAC, Savovic J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019;366:l4898. https://doi.org/10.1136/ bmj.l4898.

33. Higgins JPT, Sterne JAC, Savovic J, et al. A revised tool for assessing risk of bias in randomized trials. Cochrane Database Syst Rev. 2016;10(Suppl 1):29e31.

34. Han E, Lee YH, Lee BW, Kang ES, Cha BS. Ipragliflozin additively ameliorates non-alcoholic fatty liver disease in patients with type 2 diabetes controlled with metformin and pioglitazone: a 24-Week randomized controlled trial. J Clinical Medicine. 2020;9(1):259. https://doi.org/10.3390/jcm9010259.

35. Elhini SH, Wahsh EA, Elberry AA, et al. The impact of an SGLT2 inhibitor versus ursodeoxycholic acid on liver steatosis in diabetic patients. Pharmaceuticals (Basel, Switzerland). 2022;15(12):1516. https://doi.org/10.3390/ph15121516.

36. Shi M, Zhang H, Wang W, et al. Effect of dapagliflozin on liver and pancreatic fat in patients with type 2 diabetes and non-alcoholic fatty liver disease. J Diabetes Complications. 2023;37(10):108610. https://doi.org/10.1016/ j.jdiacomp.2023.108610.

37. Hussain M, Babar MZM, Tariq S, et al. Therapeutic outcome of dapagliflozin on various parameters in non-alcoholic fatty liver disease (NAFLD) patients. Int J Diabetes Dev Ctries. 2022;42:290e296. https://doi.org/10.1007/s13410-021- 00980-2.

38. Phrueksotsai S, Pinyopornpanish K, Euathrongchit J, et al. The effects of dapagliflozin on hepatic and visceral fat in type 2 diabetes patients with nonalcoholic fatty liver disease. J Gastroenterol Hepatol. 2021;36:2952e2959. https://doi.org/10.1111/jgh.15580.

39. Chehrehgosha H, Sohrabi MR, Ismail-Beigi F, et al. Empagliflozin improves liver steatosis and fibrosis in patients with non-alcoholic fatty liver disease and type 2 diabetes: a randomized, Double-blind, placebo-controlled clinical trial. Diabetes Ther. 2021;12:843e861. https://doi.org/10.1007/s13300-021-01011-3.

40. Taheri H, Malek M, Ismail-Beigi F, et al. Effect of empagliflozin on liver steatosis and fibrosis in patients with non-alcoholic fatty liver disease without diabetes: a randomized, Double-blind, placebo-controlled trial. Adv Therapy. 2020;37(11):4697e4708. https://doi.org/10.1007/s12325-020-01498-5.

41. Takahashi H, Kessoku T, Kawanaka M, et al. Ipragliflozin improves the hepatic outcomes of patients with diabetes with NAFLD. Hepatol Commun. 2022;6(1): 120e132. https://doi.org/10.1002/hep4.1696.

42. Aso Y, Sagara M, Niitani T, et al. Serum high-molecular-weight adiponectin and response to dapagliflozin in patients with type 2 diabetes and non-alcoholic fatty liver disease. J Investigative Medicine. 2021;69(7):1324e1329. https:// doi.org/10.1136/jim-2020-001621.