Check for updates

## OPEN ACCESS

EDITED BY   
Andreas Nüssler,   
University Hospital and Faculty of   
Medicine, University of Tübingen,   
Germany   
REVIEWED BY   
Sabrina Ehnert,   
University Hospital and Faculty of   
Medicine, University of Tübingen,   
Germany   
Lokman Hekim Tanriverdi,   
İnönü University, Türkiye

\*CORRESPONDENCE Min Song, sm@gszy.edu.cn Yongjia Song, syj@gszy.edu.cn

† These authors have contributed equally to this work and share first authorship

RECEIVED 19 January 2026   
REVISED 02 March 2026   
ACCEPTED 11 March 2026   
PUBLISHED 07 April 2026

## CITATION

Liu X, Gong Y, Liu L, Wang X, Hu K, Song M and Song Y (2026) Real-world pharmacovigilance of drug-induced osteoporosis: a focus on antiretroviral therapy and toxicological mechanisms in the elderly. Front. Pharmacol. 17:1790867. doi: 10.3389/fphar.2026.1790867

## COPYRIGHT

© 2026 Liu, Gong, Liu, Wang, Hu, Song and Song. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# Real-world pharmacovigilance of drug-induced osteoporosis: a focus on antiretroviral therapy and toxicological mechanisms in the elderly

Xiaoyu Liu 1† , Yanlong Gong 2† , Lu Liu 1 , Xiaomin Wang 1 , Kangyi Hu1 , Min Song1 \* and Yongjia Song1 \*

1 Clinical College of Chinese Medicine, Gansu University of Chinese Medicine, Lanzhou, Gansu, China, 2 Minimally Invasive Spine Orthopedics, Affiliated Hospital of Gansu University of Chinese Medicine, Lanzhou, Gansu, China

Background: Osteoporosis and bone density reduction are significant health concerns in elderly populations. While aging is a primary factor, drug-induced bone loss—particularly associated with antiviral agents, proton pump inhibitors (PPIs), and immunomodulatory drugs—has become a growing issue in patients managing multiple conditions.

Objective: This study aims to comprehensively assess adverse drug reactions (ADRs) related to bone density reduction and osteoporosis in elderly patients using the FDA Adverse Event Reporting System (FAERS). A specific focus is placed on HIV patients using antiretroviral therapy (ART), alongside an exploration of gender differences and toxicological mechanisms of high-risk drugs.

Methods: Data from FAERS (2004-Q2 2025) were analyzed using disproportionality analysis (DPA) to calculate Reporting Odds Ratios (RORs) and 95% confidence intervals (CIs). Toxicological analysis was conducted on high-risk drugs (e.g., Tenofovir Disoproxil) using PubChem, GeneCards, and GO/ KEGG pathway enrichment to identify disrupted biological processes.

Results: Antiretroviral drugs exhibited the most significant risk signals. For decreased bone density, Emtricitabine/Tenofovir Disoproxil (ROR = 713.48, 95% CI: 648.66–784.79) and Tenofovir Disoproxil (ROR = 665.79, 95% CI: 611.91–724.42) showed extreme associations. For osteoporosis, significant signals were also identified for these antivirals, as well as for Esomeprazole (ROR = 12.23, 95% CI: 11.27–13.28) and Adalimumab (ROR = 2.16, 95% CI: 1.99–2.35). Gender-specific differences indicated men are at higher risk from antiviral drugs, whereas women are more affected by bone metabolic and immunomodulatory regulators. Toxicological analyses suggest these drugs disrupt vitamin D metabolism, calcium homeostasis, and parathyroid hormone (PTH) signaling.

Conclusion: Long-term use of antiretroviral drugs, PPIs, and immunomodulators is strongly linked to bone metabolic disorders in the elderly. Although pharmacovigilance studies utilizing FAERS are limited by spontaneous reporting bias and the inability to establish direct causality, these quantitative findings and toxicological insights provide robust real-world evidence for enhancing clinical monitoring and personalized risk management.

decreased bone density, genderdifferences, induction time analysis, osteoporosis, pharmacovigilance analysis, toxicological analysis

## 1 Introduction

Decreased bone density and osteoporosis are among the most common bone metabolic diseases in the elderly, characterized primarily by bone mass reduction, trabecular structure degradation, and increased bone fragility, leading to a significant rise in fracture risk (Isganaitis, 2019). These conditions not only impair the patient’s quality of life but also cause chronic pain, decreased mobility, and long-term disability risks. In clinical practice, osteoporosis is often regarded as a natural consequence of aging. However, recent studies have shown that drug-induced bone density loss in the elderly population is also of significant clinical concern (Di et al., 2025). If drug-induced bone metabolic disorders are not promptly recognized and intervened, they may exacerbate bone loss, increase fracture risk, and lead to treatment interruptions and escalating medical costs, posing a potential threat to elderly patients’ health management and drug safety.

In long-term medication therapy for elderly patients, several commonly used drugs have been found to be associated with decreased bone density and osteoporosis. Antiviral medications, such as Tenofovir disoproxil and its fixed-dose combinations, have been shown to reduce bone mineral content and increase fracture risk (Dumitrescu et al., 2025). Proton pump inhibitors (PPIs), such as Esomeprazole, interfere with calcium absorption and bone remodeling, thereby increasing the risk of osteoporosis and hip fractures (Lespessailles and Toumi, 2022). Moreover, antitumor and immunomodulatory drugs, such as Adalimumab, while improving symptoms of inflammatory diseases, may indirectly affect bone metabolism by inhibiting osteoblast function or enhancing osteoclast activity (Ran et al., 2025). Additionally, the long-term use of aromatase inhibitors (e.g., Anastrozole, Letrozole) in postmenopausal women is closely associated with bone loss (Robertson et al., 2016). However, existing studies are mostly limited to specific drugs or single-center clinical observations, lacking systematic drug risk spectrum analyses based on real-world data.

Elderly populations exhibit significant individual differences in drug metabolism, physiological reserves, and bone metabolic responses. With age, factors such as renal function decline, decreased endocrine levels, and calcium-phosphate metabolism disorders may amplify the effects of medications on bone metabolism (Irsik et al., 2021). At the same time, the presence of multiple chronic diseases and polypharmacy complicates drug interactions, increasing the probability of adverse bone metabolic reactions (Almodovar and Nahata, 2019). However, systematic research on drug-related bone density loss and osteoporosis risk characteristics in the elderly population is still limited, particularly in areas such as high-risk drug identification, gender differences analysis, and the patterns of drug-induced time variation. This lack of quantitative evidence restricts the clinical individualized medication risk prevention and control in elderly patients.

In recent years, the osteoporosis risk in HIV patients has also gained attention. The relationship between HIV infection and decreased bone density has been confirmed in multiple studies, especially among patients using antiretroviral therapy (ART) for extended periods. These medications can significantly impact bone metabolism, leading to an increased incidence of osteoporosis (Biver, 2022).

Based on this, the present study relies on the U.S. Food and Drug Administration (FDA) Adverse Event Reporting System (FAERS) database to systematically analyze adverse event reports related to drug-induced bone density loss and osteoporosis in the elderly population from Q1 2004 to Q2 2025 (Yu et al., 2021). The study employs disproportionate analysis methods, such as reporting odds ratios (ROR), to identify potential high-risk drugs, with gender subgroup comparisons to evaluate signal differences across different groups. A potential toxicological analysis of high-risk drugs in HIV patients is also conducted. Finally, external validation is performed using the Canadian CVARDD database to ensure the robustness and credibility of the results (Thiruchelvam et al., 2025). This study aims to systematically reveal the risk spectrum, gender differences, and temporal characteristics of drug-related bone density loss and osteoporosis in the elderly population, providing real-world evidence for clinical drug safety management, and offering scientific reference for accurately identifying high-risk groups and optimizing medication strategies for elderly patients.

## 2 Materials and methods

## 2.1 Data source and process

The adverse event data used in this study were sourced from the FAERS database (https://fis.fda.gov/extensions/FPD-QDE-FAERS/ FPD-QDE-FAERS.html). This database has been publicly available since 2004, and the data for adverse event reports from Q1 2004 to Q2 2025 were downloaded from the ASCII FAERS database.

For data downloaded from the FAERS database with the same “caseid” (report code), only the most recent report based on the date was retained, and duplicate reports were removed. Drug names were standardized using the RxNorm drug normalization naming system to standardize the drug names in the FAERS database. The international medical terminology dictionary version 27.1 (MedDRA 27.1) was used to match the primary terms (PT) for adverse events related to “bone density reduction and osteoporosis”.

After standardizing the drug names and adverse event names, the adverse event reports for the primary suspected (PS) drugs related to bone density reduction and osteoporosis were collected. These adverse event reports were characterized by gender, age, weight, indications, reporting country, and outcomes.

## 2.2 Signal analysis algorithm

In this study, the disproportionality analysis (DPA) algorithm, commonly used in pharmacovigilance studies, was employed to detect potential signals for adverse events related to bone density reduction and osteoporosis. The disproportionality analysis algorithm is a widely used data mining method that analyzes the correlation between drugs and adverse reactions by comparing the observed frequency ratios in exposed and unexposed populations using a 2 × 2 contingency table, as shown in Supplementary Table S1. In this study, the Reporting Odds Ratio (ROR) was used to calculate the signal strength (Rothman et al., 2004). A risk signal was considered present when the lower limit of the 95% confidence interval (CI) of the ROR was greater than 1 and the frequency (a)

<!-- image-->  
FIGURE 1 Disproportionality analysis process for drug-related bone density reduction and osteoporosis adverse events. Abbreviations: Faers, fda adverse event reporting system; SMQ, standardised MedDRA queries; PS, primary suspected; CVARDD, Canada vigilance adverse reaction online database; GO, gene ontology; KEGG, kyoto encyclopedia of genes and genomes.

was greater than 3. To control the risk of false discoveries in multiple comparisons, the Benjamini–Hochberg method was applied using the “p.adjust” function in the “stats” package of R. A two-tailed test was performed, and statistical significance was set at a false discovery rate (FDR) adjusted p-value (FDR p) below 0.05 (Jing et al., 2022). Effective signals were determined as new adverse event signals when they were not mentioned in the FDA drug label (https://www. accessdata.fda.gov/scripts/cder/daf/index.cfm). All data in this study were processed and analyzed using R4.4.0 and MS Excel software. The data extraction and analysis process is illustrated in Figure 1.

## 2.3 Toxicological analysis

To further investigate the mechanisms of high-risk drugs associated with bone density reduction and osteoporosis, we conducted a toxicological analysis of Tenofovir Disoproxil and Emtricitabine Tenofovir Disoproxil. First, we extracted known target information for these two drugs from the PubChem and SwissTarget Prediction databases, and combined it with data from the GeneCards database to filter out toxicity targets related to “druginduced osteoporosis” and “osteotoxicity.”

Using a Venn diagram analysis, we identified the intersection of toxicity targets associated with these drugs and osteoporosis, revealing their potential mechanisms of action. After target screening, we performed Gene Ontology (GO) analysis and KEGG pathway enrichment analysis of the intersecting targets using the DAVID database to explore their potential biological processes.

## 3 Results

## 3.1 Population characteristics of drugrelated bone density reduction and osteoporosis adverse events

As of Q2 2025, the FAERS database reported 5,954 adverse events related to decreased bone density. As shown in Figure 2, 11,818 adverse events related to osteoporosis were recorded. From 2004 to 2025, the number of adverse event reports generally showed a fluctuating trend rather than a linear increase proportional to the database size.

Notably, a disproportionate surge was observed between 2020 and 2021, where reports of ’Decreased bone density’ increased by 87% (from 540 to 1,010 cases) and ’Osteoporosis’ peaked at 1,176 cases.

Subsequently, a distinct downward trend occurred from 2022 to 2024, diverging from the continued expansion of the FAERS database. This ’peak-and-fall’ pattern suggests that the reported events were driven by specific pharmacovigilance signals or clinical factors during the peak period, rather than being an artifact of overall database growth.

<!-- image-->  
Trend of adverse reaction reporting between drug related bone density reduction and osteoporosis.

Table 1 shows the characteristics of the populations for bone density reduction and osteoporosis adverse events in the elderly. Among the reports for decreased bone density, 65.1% were female, 34.0% were male, and 0.8% had unknown gender. Regarding age distribution, the group aged 65–85 years (54.3%) accounted for the largest proportion of known-age reports. Weight was primarily concentrated in the 50–100 kg range (17.4%), but 78.8% of the population had unknown weight. Notably, HIV infection (36.9%) was the most common indication, followed by osteoporosis (20.8%) and postmenopausal osteoporosis (5.0%). The countries with the highest number of reports were the United States (70.0%), Canada (5.5%), and China (1.6%). For osteoporosis, 76.5% of the reports were from females, 22.7% from males, and 0.8% had unknown gender. In terms of age, the group aged 18–65 years (59.4%) accounted for the largest proportion of known-age reports. Weight was primarily concentrated in the 50–100 kg range (29.9%), but 63.9% of the population had unknown weight. Notably, rheumatoid arthritis (13.6%) was the most common indication, followed by HIV infection (11.8%) and osteoporosis (5.3%). The countries with the highest number of reports were the United States (56.2%), Canada (12.3%), and Germany (2.1%).

## 3.2 Risk drug analysis in the elderly population

There are 18 drugs associated with adverse events related to drug-induced bone density reduction, as shown in Figure 3A. The top five drugs are Tenofovir Disoproxil (N = 984), Emtricitabine Tenofovir Disoproxil (N = 783), Efavirenz Emtricitabine Tenofovir Disoproxil (N = 488), Esomeprazole (N = 106), and Anastrozole (N = 67). As detailed in Table 2, the top five drugs associated with decreased bone density, ranked by the number of reports, all exhibited highly robust risk signals. These include Tenofovir Disoproxil (N = 984, ROR = 665.79, 95% CI: 611.91–724.42), Emtricitabine Tenofovir Disoproxil (N = 783, ROR = 713.48, 95% CI: 648.66–784.79), Efavirenz Emtricitabine Tenofovir Disoproxil (N = 488, ROR = 691.12, 95% CI: 613.48–778.59), Esomeprazole (N = 106, ROR = 3.98, 95% CI: 3.28–4.82), and Anastrozole (N = 67, ROR = 8.44, 95% CI: 6.63–10.75). The drugs were further classified according to the ATC classification system, as shown in Figure 3B, where Anti-infectives for Systemic Use (N = 2,366) was the most prevalent drug category, followed by Antineoplastic and Immunomodulating Agents (N = 126).

Further comparison with the drug labels revealed that eight drugs, including Esomeprazole (N = 106, ROR = 3.98), Leflunomide (N = 31, ROR = 6), Salmeterol (N = 14, ROR = 1.94), Lamivudine (N = 7, ROR = 6.18), and Lopinavir Ritonavir (N = 5, ROR = 6.33), did not directly mention bone density reduction as an adverse event in the product labeling. These newly identified adverse event signals are worth further clinical attention, as detailed in Supplementary Table S2.

For osteoporosis-related adverse events, 63 drugs were identified as risk drugs, as shown in Figure 3C. The top five drugs are Tenofovir Disoproxil (N = 667), Esomeprazole (N = 612), Adalimumab (N = 570), Emtricitabine Tenofovir Disoproxil (N = 514), and Etanercept (N = 447). For osteoporosis-related adverse events, the top five drugs ranked by report count (Table 2) also demonstrated significant associations. The leading drugs were Tenofovir Disoproxil (N = 667, ROR = 167.20, 95% CI: 152.77–182.98), followed by Esomeprazole (N = 612, ROR = 12.23, 95% CI: 11.27–13.28), Adalimumab (N = 570, ROR = 2.16, 95% CI: 1.99–2.35), Emtricitabine Tenofovir Disoproxil (N = 514, ROR = 172.62, 95% CI: 155.75–191.32), and

TABLE 1 Population characteristics of adverse events related to drug-induced Decreased bone density and osteoporosis.
<table><tr><td rowspan=1 colspan=1>Characteristics</td><td rowspan=1 colspan=2>Decreased bone density</td><td rowspan=1 colspan=2>Osteoporosis</td></tr><tr><td rowspan=1 colspan=1>Number of events</td><td rowspan=1 colspan=2>5954</td><td rowspan=1 colspan=2>11,818</td></tr><tr><td rowspan=1 colspan=1>Gender, number (%)</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Female</td><td rowspan=1 colspan=2>3878 (65.1%)</td><td rowspan=1 colspan=2>9039 (76.5%)</td></tr><tr><td rowspan=1 colspan=1>Male</td><td rowspan=1 colspan=2>2027 (34.0%)</td><td rowspan=1 colspan=2>2686 (22.7%)</td></tr><tr><td rowspan=1 colspan=1>Miss</td><td rowspan=1 colspan=2>49 (0.8%)</td><td rowspan=1 colspan=2>93 (0.8%)</td></tr><tr><td rowspan=1 colspan=1>Age, number (%)</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Median age</td><td rowspan=1 colspan=2>67</td><td rowspan=1 colspan=2>70</td></tr><tr><td rowspan=1 colspan=1>60-85</td><td rowspan=1 colspan=2>5778 (97.10%)</td><td rowspan=1 colspan=2>11,285 (95.5%)</td></tr><tr><td rowspan=1 colspan=1>&gt;85</td><td rowspan=1 colspan=2>176 (3.0%)</td><td rowspan=1 colspan=2>533 (4.5%)</td></tr><tr><td rowspan=1 colspan=1>Weight (KG), number (%)</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>&lt;50</td><td rowspan=1 colspan=2>151 (2.50%)</td><td rowspan=1 colspan=2>473 (4.0%)</td></tr><tr><td rowspan=1 colspan=1>50~100</td><td rowspan=1 colspan=2>1035 (17.40%)</td><td rowspan=1 colspan=2>3532 (29.9%)</td></tr><tr><td rowspan=1 colspan=1>&gt;100</td><td rowspan=1 colspan=2>77 (1.30%)</td><td rowspan=1 colspan=2>267 (2.3%)</td></tr><tr><td rowspan=1 colspan=1>Miss</td><td rowspan=1 colspan=2>4692 (78.80%)</td><td rowspan=1 colspan=2>7546 (63.9%)</td></tr><tr><td rowspan=5 colspan=1>Top 5 indication, number(%)</td><td rowspan=1 colspan=1>HIV INFECTION</td><td rowspan=1 colspan=1>2201 (36.9%)</td><td rowspan=1 colspan=1>RHEUMATOID ARTHRITIS</td><td rowspan=1 colspan=1>1614(1614,13.6%)</td></tr><tr><td rowspan=1 colspan=1>OSTEOPOROSIS</td><td rowspan=1 colspan=1>1239 (20.8%)</td><td rowspan=1 colspan=1>HIV INFECTION</td><td rowspan=1 colspan=1>1404 (11.8%)</td></tr><tr><td rowspan=1 colspan=1>OSTEOPOROSISPOSTMEHOPAUSAL</td><td rowspan=1 colspan=1>303 (5.0%)</td><td rowspan=1 colspan=1>OSTEOPOROSIS</td><td rowspan=1 colspan=1>627 (5.3%)</td></tr><tr><td rowspan=1 colspan=1>RHEUMATOID ARTHRITIS</td><td rowspan=1 colspan=1>192 (3.2%)</td><td rowspan=1 colspan=1>GASTROOESOPHAGEAL REFLUXDISEASE (420)</td><td rowspan=1 colspan=1>420 (3.5%)</td></tr><tr><td rowspan=1 colspan=1>OSTEOPENIA</td><td rowspan=1 colspan=1>81 (1.3%)</td><td rowspan=1 colspan=1>MULTIPLE SCLEROSIS</td><td rowspan=1 colspan=1>234 (1.9%)</td></tr><tr><td rowspan=5 colspan=1>Top 5 Reported Countries, number (%)</td><td rowspan=1 colspan=1>United States</td><td rowspan=1 colspan=1>4170 (70.0%)</td><td rowspan=1 colspan=1>United States</td><td rowspan=1 colspan=1>6666 (56.2%)</td></tr><tr><td rowspan=1 colspan=1>Canada</td><td rowspan=1 colspan=1>328 (5.5%)</td><td rowspan=1 colspan=1>Canada</td><td rowspan=1 colspan=1>1459 (12.3%)</td></tr><tr><td rowspan=1 colspan=1>CHINA</td><td rowspan=1 colspan=1>97 (1.6%)</td><td rowspan=1 colspan=1>GERMANY</td><td rowspan=1 colspan=1>256 (2.1%)</td></tr><tr><td rowspan=1 colspan=1>JAPAN</td><td rowspan=1 colspan=1>86 (1.4%)</td><td rowspan=1 colspan=1>BRAZIL</td><td rowspan=1 colspan=1>253 (2.1%)</td></tr><tr><td rowspan=1 colspan=1>GREAT BRITAIN</td><td rowspan=1 colspan=1>36 (0.6%)</td><td rowspan=1 colspan=1>GREAT BRITAIN</td><td rowspan=1 colspan=1>215 (1.8%)</td></tr></table>

Etanercept (N = 447, ROR = 1.31, 95% CI: 1.19–1.44). According to the ATC classification system (Figure 3D), the largest drug category was Antineoplastic and Immunomodulating Agents (N = 2,805). Notably, after correcting for terminology variations, ’Anti-infectives for systemic use’ emerged as the second-largest category with 1,636 reports. This was followed by Alimentary Tract and Metabolism (N = 907). The high prevalence of anti-infectives is consistent with the significant signals observed for antiretroviral drugs in our specific drug analysis.

Further comparison with the drug labels revealed that 32 drugs, including Adalimumab (N = 570, ROR = 2.16), Etanercept (N = 447, ROR = 1.31), Tofacitinib (N = 279, ROR = 1.9), Methotrexate (N = 221, ROR = 2.12), and Tocilizumab (N = 167, ROR = 4.51), did not directly mention osteoporosis as an adverse event in the product labeling. These newly identified adverse event signals are also worth further clinical attention, as detailed in Supplementary Table S2.

## 3.3 Gender differences in risk drugs for bone density reduction and osteoporosis

To elucidate gender-specific susceptibilities to drug-induced bone toxicity, we performed a stratified disproportionality analysis. Regarding bone density reduction (Figure 4), a stark dichotomy in drug risk profiles between genders emerged. Male patients exhibited overwhelmingly dominant risk signals associated almost exclusively with antiretroviral therapies. Notably, Tenofovir Disoproxil demonstrated an extreme association with bone density reduction in men (N = 702, ROR = 1139.82, 95% CI: 1021.29–1272.11), which was substantially higher than the signal observed in women (N = 281, ROR = 445.15, 95% CI: 383.58–516.60). Conversely, while female patients also demonstrated significant risks from antiviral agents, they uniquely presented a broader risk spectrum driven by bone metabolic regulators, such as Denosumab (N = 779, ROR =

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Analysis of Drug-Related Bone Density Reduction and Osteoporosis Risk Signals in the General Population. (A) Bar chart of top risk signal drugs for bone density reduction; (B) Donut chart of ATC classifications for bone density reduction risk signals; (C) Bar chart of top risk signal drugs for osteoporosis; (D) Donut chart of ATC classifications for osteoporosis risk signals.

10.91, 95% CI: 10.08–11.80) and Teriparatide (N = 659, ROR =   
12.50, 95% CI: 11.49–13.59).

Heatmap analysis of the shared risk signals (Figure 6A) further illustrates these nuances: while Tenofovir Disoproxil and Emtricitabine Tenofovir Disoproxil (male ROR = 965.86, 95% CI: 858.38–1086.80) had profoundly higher toxicities in men, complex fixed-dose combinations like Efavirenz/Emtricitabine/Tenofovir Disoproxil (female ROR = 925.60, 95% CI: 731.37–1171.39) and Cobicistat/Elvitegravir/Emtricitabine/Tenofovir Disoproxil (female ROR = 486.20, 95% CI: 248.58–950.93) exhibited stronger signal intensities in women, indicating that gender plays a critical modulating role even within the same antiretroviral drug class.

This gender-dependent risk pattern was mirrored in osteoporosis events (Figure 5). Tenofovir Disoproxil again showed a disproportionately higher risk in men (N = 424, ROR = 318.27, 95% CI: 283.15–357.74) compared to women (N = 242, ROR = 145.52, 95% CI: 124.96–169.47). However, the osteoporosis risk spectrum in female patients was distinctly expanded to include strong signals from proton pump inhibitors and immunomodulators, driven primarily by Esomeprazole (N = 502, ROR = 11.03, 95% CI: 10.07–12.09) and Adalimumab (N = 508, ROR = 2.09, 95% CI: 1.91–2.28).

The corresponding heatmap for shared osteoporosis signals (Figure 6B) visually reinforces this dichotomy. It highlights that fundamental antiretrovirals like Tenofovir Disoproxil and Emtricitabine Tenofovir Disoproxil (male ROR = 275.51, 95% CI:

241.81–313.90) remain heavily male-predominant risks. In contrast, female vulnerabilities are elevated across certain combination therapies (e.g., Emtricitabine/Tenofovir Disoproxil: female ROR = 238.63, 95% CI: 198.03–287.55; Efavirenz/Emtricitabine/Tenofovir Disoproxil: female ROR = 224.71, 95% CI: 177.14–285.04) alongside a wider array of anti-inflammatory and metabolic medications.

## 3.4 Toxicological analysis

Tenofovir Disoproxil and Emtricitabine Tenofovir Disoproxil are the drugs with the highest number of reported events and the highest ROR values, with both being used for the treatment of HIV. To further explore their potential risks in osteoporosis, we conducted a toxicological analysis. Target information for these drugs was retrieved from the PubChem and SwissTarget Prediction databases, while toxicity targets related to “drug-induced osteoporosis” and “osteotoxicity” were obtained from the GeneCards database.

As shown in the Venn diagram in Figure 7A, Tenofovir Disoproxil has three intersecting toxicity targets with osteoporosis, while Emtricitabine Tenofovir Disoproxil has four intersecting targets. Further Gene Ontology (GO) and KEGG enrichment analyses were performed using the DAVID database.

Figure 7B shows that the intersecting targets of Tenofovir Disoproxil are highly focused on key endocrine regulatory axes in bone metabolism. The GO_BP (biological process) enrichment primarily highlights processes related to vitamin D/calcitriol metabolism and response (e.g., vitamin D metabolic/catabolic process, calcitriol biosynthetic process, response to vitamin D), further pointing to calcium ion homeostasis maintenance. At the KEGG pathway level, significant enrichment was found in the synthesis, secretion, and action pathways of parathyroid hormone (PTH), along with associations to steroid biosynthesis. These results suggest that Tenofovir Disoproxil may disrupt the “vitamin D—calcium homeostasis—PTH” regulatory network, leading to metabolic imbalance in bone mass and increasing the risk of osteoporosis.

TABLE 2 Disproportionality analysis of top 10 drugs associated with decreased bone density and osteoporosis in older adults reported to the FAERS database (2004–2025 Q2).
<table><tr><td rowspan=1 colspan=1>Adverse event</td><td rowspan=1 colspan=1>Drug</td><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1>ROR (95% CI)</td><td rowspan=1 colspan=1>p value p adjust</td><td rowspan=1 colspan=1>p value p adjust</td></tr><tr><td rowspan=10 colspan=1>Decreased bone density</td><td rowspan=1 colspan=1>TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>984</td><td rowspan=1 colspan=1>665.79 (611.91724.42)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>783</td><td rowspan=1 colspan=1>713.48 (648.66784.79)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>488</td><td rowspan=1 colspan=1>691.12 (613.48778.59)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>ESOMEPRAZOLE *</td><td rowspan=1 colspan=1>106</td><td rowspan=1 colspan=1>3.98 (3.284.82)</td><td rowspan=1 colspan=1>1.48E-51</td><td rowspan=1 colspan=1>4.41E-49</td></tr><tr><td rowspan=1 colspan=1>ANASTROZOLE *</td><td rowspan=1 colspan=1>67</td><td rowspan=1 colspan=1>8.44 (6.6310.75)</td><td rowspan=1 colspan=1>4.68E-94</td><td rowspan=1 colspan=1>1.39E-91</td></tr><tr><td rowspan=1 colspan=1>COBICISTAT ELVITEGRAVIR EMTRICITABINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>54</td><td rowspan=1 colspan=1>348.17 (254.01-477.24)</td><td rowspan=1 colspan=1>1.19E-111</td><td rowspan=1 colspan=1>3.54E-109</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE RILPIVIRINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>49</td><td rowspan=1 colspan=1>302.61 (218.67-418.77)</td><td rowspan=1 colspan=1>6.02E-99</td><td rowspan=1 colspan=1>1.80E-96</td></tr><tr><td rowspan=1 colspan=1>LEFLUNOMIDE *</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>6.00 (4.218.55)</td><td rowspan=1 colspan=1>1.67E-28</td><td rowspan=1 colspan=1>4.97E-26</td></tr><tr><td rowspan=1 colspan=1>ADEFOVIR</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>40.41 (25.8063.30)</td><td rowspan=1 colspan=1>3.23E-25</td><td rowspan=1 colspan=1>9.62E-23</td></tr><tr><td rowspan=1 colspan=1>MELOXICAM *</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>10.24 (6.5815.92)</td><td rowspan=1 colspan=1>4.77E-14</td><td rowspan=1 colspan=1>1.42E-11</td></tr><tr><td rowspan=10 colspan=1>Osteoporosis</td><td rowspan=1 colspan=1>TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>667</td><td rowspan=1 colspan=1>167.20 (152.77-182.98)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>ESOMEPRAZOLE *</td><td rowspan=1 colspan=1>612</td><td rowspan=1 colspan=1>12.23 (11.27-13.28)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>ADALIMUMAB *</td><td rowspan=1 colspan=1>570</td><td rowspan=1 colspan=1>2.16 (1.99-2.5)</td><td rowspan=1 colspan=1>2.64E-75</td><td rowspan=1 colspan=1>1.76E-72</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>514</td><td rowspan=1 colspan=1>172.62 (155.75191.32)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>ETANERCEPT *</td><td rowspan=1 colspan=1>447</td><td rowspan=1 colspan=1>1.31 (1.19-1.44)</td><td rowspan=1 colspan=1>2.28E-08</td><td rowspan=1 colspan=1>1.53E-05</td></tr><tr><td rowspan=1 colspan=1>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>295</td><td rowspan=1 colspan=1>154.34 (135.09176.33)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>TOFACITINIB *</td><td rowspan=1 colspan=1>279</td><td rowspan=1 colspan=1>1.90 (1.69-2.14)</td><td rowspan=1 colspan=1>6.61E-27</td><td rowspan=1 colspan=1>4.42E-24</td></tr><tr><td rowspan=1 colspan=1>METHOTREXATE *</td><td rowspan=1 colspan=1>221</td><td rowspan=1 colspan=1>2.12 (1.852.42)</td><td rowspan=1 colspan=1>2.72E-29</td><td rowspan=1 colspan=1>1.82E-26</td></tr><tr><td rowspan=1 colspan=1>TOCILIZUMAB *</td><td rowspan=1 colspan=1>167</td><td rowspan=1 colspan=1>4.51 (3.87-5.26)</td><td rowspan=1 colspan=1>3.81E-98</td><td rowspan=1 colspan=1>2.55E-95</td></tr><tr><td rowspan=1 colspan=1>ANASTROZOLE *</td><td rowspan=1 colspan=1>164</td><td rowspan=1 colspan=1>10.57 (9.0512.35)</td><td rowspan=1 colspan=1>8.88E-298</td><td rowspan=1 colspan=1>5.94E-295</td></tr></table>

a = number of reports; ROR, reporting odds ratio; CI, confidence interval.  
Asterisks (\*) denote new disproportionality signals not previously documented in the respective drug labeling.

Figure 7C shows that the intersecting targets of Emtricitabine Tenofovir Disoproxil also focus on endocrine regulation of bone metabolism. The GO_BP enrichment is significantly related to vitamin D/calcitriol metabolism and response, calcium ion homeostasis, and estrogen response, indicating that its potential effects may extend to sex hormone regulation. In addition to significant enrichment in the PTH pathway and steroid biosynthesis, the KEGG pathways also associate with osteoclast differentiation. Overall, this combination drug may disrupt the “vitamin D—calcium homeostasis—PTH/sex hormones” regulatory network and influence osteoclast-related bone remodeling processes, thus promoting bone homeostasis imbalance and increasing the risk of osteoporosis.

## 3.5 External validation with the canadian database

To further ensure the accuracy of the study results, we analyzed adverse event reports related to bone density reduction and osteoporosis in the Canadian CVARDD database. Among the reports related to bone density reduction, Esomeprazole, Leflunomide, and Meloxicam exhibited risk signals for bone density reduction in both databases. Regarding osteoporosisrelated adverse events, 33 common risk signals for osteoporosis were reported consistently in both the FAERS and CVARDD databases, which further validates the robustness of the results.

As shown in Figure 8, Esomeprazole (FAERS = 612, CVARDD = 3) shows a relatively low risk in both databases, indicating consistent adverse event risk in both datasets. Adalimumab (FAERS = 570, CVARDD = 140) exhibited a high risk in both databases, suggesting that the risk distribution for this drug is consistent across databases, further supporting the reliability of the study findings. Etanercept (FAERS = 447, CVARDD = 10) showed a higher risk in the FAERS database but a lower risk in the CVARDD database, which could be attributed to differences in data sources or geographic factors. Tofacitinib (FAERS = 279, CVARDD = 7) displayed moderate risk in both databases, further enhancing the consistency and robustness of the results. Methotrexate (FAERS = 221, CVARDD = 1073) showed a high risk in both databases, with the CVARDD database indicating an even more prominent risk, suggesting that the impact of this drug on bone density has been validated across both databases.

<table><tr><td>DRUG</td><td></td><td>ROR(95% CI)</td><td></td><td></td><td></td><td>ROR</td></tr><tr><td></td><td></td><td>N</td><td></td><td></td><td></td><td></td></tr><tr><td>Male</td><td>702</td><td>1139.82 (1021.29-1272.11)</td><td></td><td></td><td></td><td>1139.82</td></tr><tr><td>TENOFOVIR DISOPROXIL EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>555</td><td>965.86 (858.38-1086.8)</td><td></td><td></td><td></td><td>965.86</td></tr><tr><td>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>335</td><td>813.86 (704.61-940.04)</td><td></td><td></td><td></td><td>813.86</td></tr><tr><td></td><td>48</td><td>12.09 (9.06-16.12)</td><td></td><td></td><td></td><td>12.09</td></tr><tr><td>TERIPARATIDE</td><td></td><td>366.56 (253.55-529.93)</td><td></td><td></td><td></td><td></td></tr><tr><td>COBICISTAT ELVITEGRAVIR EMTRICITABINE TENOFOVIR DISOPROXIL38 DENOSUMAB</td><td></td><td>3.04 (2.12-4.36)</td><td></td><td></td><td></td><td>366.56</td></tr><tr><td>EMTRICITABINE RILPIVIRINE TENOFOVIR DISOPROXIL</td><td>30 27</td><td>306.11 (199.57-469.54)</td><td></td><td></td><td></td><td>3.04 306.11</td></tr><tr><td>ALENDRONIC ACID</td><td>21</td><td>14.43 (9.36-22.23)</td><td></td><td></td><td></td><td>14.43</td></tr><tr><td>ZOLEDRONIC ACID</td><td>19</td><td>2.76 (1.75-4.33)</td><td>H</td><td></td><td></td><td>2.76</td></tr><tr><td>ESOMEPRAZOLE</td><td>18</td><td>2.66 (1.67-4.23)</td><td></td><td></td><td></td><td></td></tr><tr><td>ADEFOVIR</td><td>16</td><td></td><td></td><td></td><td></td><td>2.66</td></tr><tr><td>Female</td><td></td><td>69.22 (41.7-114.91)</td><td></td><td></td><td></td><td>→ 69.22</td></tr><tr><td>DENOSUMAB</td><td></td><td>10.91 (10.08-11.8)</td><td>HH</td><td></td><td></td><td></td></tr><tr><td>TERIPARATIDE</td><td>779 659</td><td>12.5 (11.49-13.59)</td><td>H</td><td></td><td></td><td>10.91</td></tr><tr><td>TENOFOVIR DISOPROXIL</td><td>281</td><td>445.15 (383.58-516.6)</td><td></td><td></td><td></td><td>12.5</td></tr><tr><td>EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>225</td><td>773.71 (642.6-931.57)</td><td></td><td></td><td></td><td>445.15</td></tr><tr><td>ALENDRONIC ACID</td><td>220</td><td>13.46 (11.74-15.44)</td><td></td><td></td><td></td><td>*773.71</td></tr><tr><td>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>153</td><td>925.6 (731.37-1171.39)</td><td></td><td></td><td></td><td>13.46</td></tr><tr><td>RALOXIFENE</td><td>145</td><td>35.47 (29.94-42.02)</td><td></td><td></td><td></td><td>925.6</td></tr><tr><td>ZOLEDRONIC ACID</td><td>144</td><td>5.82 (4.93-6.88)</td><td></td><td></td><td></td><td>35.47</td></tr><tr><td>ESOMEPRAZOLE</td><td>86</td><td>4.15 (3.35-5.14)</td><td></td><td></td><td></td><td>5.82</td></tr><tr><td>ANASTROZOLE</td><td>66</td><td>7.29 (5.71-9.31)</td><td>H</td><td></td><td></td><td>4.15</td></tr><tr><td>IBANDRONIC ACID</td><td>58</td><td>6.3 (4.86-8.18)</td><td></td><td></td><td></td><td>7.29</td></tr><tr><td></td><td>52</td><td>11.79 (8.95-15.54)</td><td></td><td></td><td></td><td>6.3</td></tr><tr><td>ROMOSOZUMAB</td><td>31</td><td>7.02 (4.92-10.01)</td><td></td><td></td><td></td><td>11.79</td></tr><tr><td>LEFLUNOMIDE RISEDRONIC ACID</td><td>29</td><td>7.15 (4.95-10.32)</td><td></td><td></td><td></td><td>7.02</td></tr><tr><td>EMTRICITABINE RILPIVIRINE TENOFOVIR DISOPROXIL</td><td>22</td><td>374.29 (224.57-623.85)</td><td></td><td></td><td></td><td>7.15</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>374.29</td></tr><tr><td>MELOXICAM</td><td>20</td><td>14.31 (9.19-22.3)</td><td>•</td><td></td><td></td><td>14.31</td></tr><tr><td>LETROZOLE</td><td>17</td><td>1.73 (1.08-2.79)</td><td></td><td></td><td></td><td>1.73</td></tr><tr><td>SALMETEROL</td><td>14</td><td>2.61 (1.55-4.42)</td><td>-</td><td></td><td></td><td>2.61</td></tr><tr><td>COBICISTAT ELVITEGRAVIR EMTRICITABINE TENOFOVIR DISOPROXIL14</td><td></td><td>486.2 (248.58-950.93)</td><td></td><td></td><td></td><td>486.2</td></tr><tr><td>EXEMESTANE</td><td>11</td><td>2.15 (1.19-3.88)</td><td>H 10</td><td>20</td><td></td><td>2.15</td></tr><tr><td colspan="4"></td><td>30</td><td>40</td><td>50</td></tr></table>

Forest Plot of gender differences in risk drugs for bone density reduction.

These results indicate that the findings from the FAERS and CVARDD databases mutually support each other, enhancing the reliability and accuracy of the study conclusions. Additionally, this suggests that the reporting of adverse drug reactions in different databases may be influenced by geographic or sample differences.

## 3.6 Induction time

The analysis of induction time for drug adverse reactions is of significant importance for drug safety monitoring, clinical medication guidance, regulatory decision-making, and drug development improvement. Due to the high rate of missing data for induction time in bone density reduction, we focused on analyzing the top 5 risk drugs for osteoporosis adverse events that were reported in both FAERS and CVARDD.

Weber distribution curve parameters are used for this analysis: when the shape parameter (β) is less than 1, with its 95% confidence interval (CI) less than 1, the adverse event (AE) incidence is considered to decrease over time (early failure-type curve). When β equals or is close to 1, and its 95% CI includes 1, the AE incidence continues to occur over time (random failure-type curve). When β is greater than 1, with its 95% CI not including 1, the AE incidence is considered to increase over time (wear-out failure-type curve).

As shown in Table 3, the results reveal significant differences in the induction time characteristics of the drugs. Tenofovir Disoproxil and its combination formulations have a longer time-to-onset (TTO) and exhibit a “wear-out failure-type curve” characteristic. The median induction time for Tenofovir Disoproxil was 1,272 days (β = 1.37, 95% CI: 1.22–1.52), indicating that as the medication duration increases, the adverse event incidence gradually rises. The findings were consistent in both male (β = 1.44) and female (β = 1.29) subgroups, suggesting that the risk of osteoporosis is closely related to cumulative medication duration. Similarly, Emtricitabine Tenofovir Disoproxil and its gender subgroups also had β values greater than 1 (1.30–1.49), showing a wear-out trend, which suggests that long-term medication use may lead to ongoing damage to bone structure.

Esomeprazole also showed significant wear-out failure-type characteristics. The median induction time was 1,374 days (β = 1.95, 95% CI: 1.48–2.43), indicating that the risk of osteoporosis significantly increases with prolonged use. This may be related to the long-term effects of acid suppression therapy on calcium absorption and bone metabolism disruption.

Adalimumab and Etanercept exhibited an “early failure-type curve.” The median induction time for Adalimumab was 354 days (β = 0.81, 95% CI: 0.70–0.93), and for Etanercept, it was 626 days (β = 0.80, 95% CI: 0.60–1.00), both suggesting that adverse events occur more frequently in the early stages of medication. This may be due to the early effects of immunomodulatory drugs on bone metabolic balance.

Overall, Tenofovir-class drugs are most prominently associated with wear-out risks related to long-term use, while Adalimumab and Etanercept may induce osteoporosis risk early in treatment. The Weber distribution curves further confirm this, with early failuretype curves appearing in Figures 9C,E, while wear-out failure-type curves are shown in Figures 9A,B,D,F–I.

<table><tr><td>DRUG</td><td>N</td><td>ROR(95% CI)</td></tr><tr><td>Male</td><td></td><td></td></tr><tr><td>TENOFOVIR DISOPROXIL</td><td>424</td><td>318.27 (283.15-357.74)</td></tr><tr><td>EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>322</td><td>275.51 (241.81-313.9)</td></tr><tr><td>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>179</td><td>228.19 (192.76-270.13)</td></tr><tr><td>ESOMEPRAZOLE</td><td>102</td><td>11.84 (9.7-14.45)</td></tr><tr><td>LEUPRORELIN</td><td>86</td><td>2.72 (2.2-3.38)</td></tr><tr><td>ADALIMUMAB</td><td>62</td><td>1.37 (1.06-1.76)</td></tr><tr><td>ZOLEDRONIC ACID</td><td>49</td><td>5.43 (4.09-7.21)</td></tr><tr><td>PREDNISONE</td><td>47</td><td>6.36 (4.76-8.5)</td></tr><tr><td>PREDNISOLONE</td><td>37</td><td>5.33 (3.85-7.38)</td></tr><tr><td>METHOTREXATE</td><td>33</td><td>1.95 (1.38-2.75)</td></tr><tr><td>SALBUTAMOL</td><td>28</td><td>5.53 (3.81-8.04)</td></tr><tr><td>TOFACITINIB</td><td>27</td><td>1.65 (1.13-2.41)</td></tr><tr><td>ALENDRONIC ACID</td><td>26</td><td>13.51 (9.15-19.93)</td></tr><tr><td>OMEPRAZOLE</td><td>25</td><td>3.35 (2.26-4.97)</td></tr><tr><td>EMTRICITABINE RILPIVIRINE TENOFOVIR DISOPROXIL</td><td>23</td><td>188.18 (119.56-296.19)</td></tr><tr><td>COBICISTAT ELVITEGRAVIR EMTRICITABINE TENOFOVIR DISOPROXIL23</td><td></td><td>146.84 (94.14-229.02)</td></tr><tr><td>ADEFOVIR</td><td>19</td><td>62.69 (39.28-100.07)</td></tr><tr><td>ROFECOXIB</td><td>19</td><td>2.82 (1.79-4.43)</td></tr><tr><td>METHYLPREDNISOLONE</td><td>19</td><td>4.18 (2.66-6.57)</td></tr><tr><td>PAMIDRONIC ACID</td><td>17</td><td>25.52 (15.73-41.41)</td></tr><tr><td>Female</td><td></td><td></td></tr><tr><td>ADALIMUMAB</td><td>508</td><td>2.09 (1.91-2.28)</td></tr><tr><td>ESOMEPRAZOLE</td><td>502</td><td>11.03 (10.07-12.09)</td></tr><tr><td>ETANERCEPT</td><td>410</td><td>1.18 (1.07-1.31)</td></tr><tr><td>DENOSUMAB</td><td>279</td><td>1.37 (1.21-1.54)</td></tr><tr><td>ALENDRONIC ACID</td><td>261</td><td>6.67 (5.89-7.55)</td></tr><tr><td>TOFACITINIB</td><td>250</td><td>1.58 (1.39-1.79)</td></tr><tr><td>TENOFOVIR DISOPROXIL</td><td>242</td><td>145.52 (124.96-169.47)</td></tr><tr><td>EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>192</td><td>238.63 (198.03-287.55)</td></tr><tr><td>TERIPARATIDE</td><td>191</td><td>1.3 (1.13-1.5)</td></tr><tr><td>METHOTREXATE</td><td>187</td><td>1.91 (1.65-2.21)</td></tr><tr><td>ZOLEDRONIC ACID</td><td>185</td><td>3.16 (2.73-3.65)</td></tr><tr><td>ANASTROZOLE</td><td>164</td><td>7.88 (6.74-9.21)</td></tr><tr><td>TOCILIZUMAB</td><td>159</td><td>4.37 (3.73-5.11)</td></tr><tr><td>ABATACEPT</td><td>136</td><td>1.7 (1.44-2.02)</td></tr><tr><td>ROFECOXIB</td><td>132</td><td>6.3 (5.3-7.5)</td></tr><tr><td>EFAVIRENZ EMTRICITABINE TENOFOVIR DISOPROXIL</td><td>115</td><td>224.71 (177.14-285.04)</td></tr><tr><td>INTERFERON BETA 1A</td><td>110</td><td>1.79 (1.48-2.16)</td></tr><tr><td>PREDNISONE</td><td>96</td><td>6.15 (5.02-7.53)</td></tr><tr><td>RITUXIMAB</td><td>85</td><td>1.93 (1.56-2.39)</td></tr><tr><td>BUDESONIDE FORMOTEROL</td><td>84</td><td>3.62 (2.91-4.49)</td></tr></table>

<!-- image-->  
FIGURE 5  
Forest Plot of gender differences in risk drugs for osteoporosis.

<!-- image-->

<!-- image-->  
FIGURE 6 Heatmap of shared risk signals for bone density reduction and osteoporosis in both men and Women. (A) Heatmap of ROR values for shared risk signals for bone density Reduction. (B) Heatmap of ROR values for shared risk signals for osteoporosis.

These results indicate that different drugs exhibit significant variations in the time distribution patterns of osteoporosis-related adverse reactions, suggesting that clinical monitoring and management of bone metabolism risks should be strengthened during long-term medication use.

<!-- image-->

<!-- image-->

<!-- image-->  
Toxicological analysis of high-risk signal drugs. (A) Venn diagram of the intersecting toxicity targets between high-risk drugs and osteoporosis; (B) GO and KEGG pathway enrichment analysis of the intersecting targets for Tenofovir Disoproxil; (C) GO and KEGG pathway enrichment analysis of the intersecting targets for Emtricitabine Tenofovir Disoproxil.

## 4 Discussion

Decreased bone density and osteoporosis are potential serious bone metabolism-related adverse drug reactions (ADRs) that can significantly affect the physiological function and quality of life of elderly patients, potentially leading to fractures and permanent damage (Rizzoli et al., 2011). With the widespread use of antiviral drugs, immunomodulatory drugs, and proton pump inhibitors, the associated bone metabolic risks have gradually gained attention. However, there is still limited systematic research on drug-related bone density reduction and osteoporosis in the elderly population, especially lacking multi-drug comparisons and gender stratification analysis based on real-world data.

This study, based on FAERS database data from 2004 to 2025, used disproportionality analysis (DPA) methods to systematically identify potential high-risk drugs, and its robustness was validated through the CVARDD database (Gibbons et al., 2025). Furthermore, the induction time modeling was combined to reveal the temporal evolution patterns of bone metabolism adverse reactions, providing real-world evidence for medication risk management in elderly patients.

## 4.1 Characteristics of vulnerable populations and clinical focus

Population characteristic analysis shows that women make up a significantly higher proportion of reports for adverse events related to bone density reduction (65.1%) and osteoporosis (76.5%), suggesting that women may be the primary susceptible group for drug-related bone metabolic damage. This difference may arise from multiple mechanisms: First, the decline in estrogen levels leads to decreased osteoblastic activity and increased osteoclastic activity, making women more prone to bone loss under pharmacological interventions (Eastell et al., 2019). Second, women have a higher prevalence of chronic diseases like osteoporosis and rheumatoid arthritis, which increases exposure to related adverse drug reactions due to long-term use of anti-inflammatory or immunomodulatory drugs (Buttgereit et al., 2024). Additionally, older women experience age-related declines in calcium absorption, vitamin D metabolism, and renal function reserves, which may further exacerbate the adverse effects of drugs on bone metabolism.

<!-- image-->  
Heatmap of risk drugs from FAERS, CVARDD, and combined data sources.

TABLE 3 Weibull distribution parameters for time-to-onset of drug-related osteoporosis.
<table><tr><td rowspan=1 colspan=6>Drug                      TTO (days)                                 Weibull distributionCase       Median      Scale parameter:      Shape parameter:        Typereports      (day)           a(9%C)               95%C)</td></tr><tr><td rowspan=1 colspan=1>TENOFOVIR DISOPROXIL</td><td rowspan=1 colspan=1>226</td><td rowspan=1 colspan=1>1272</td><td rowspan=1 colspan=1>1463.98 (1318.36~1609.60)</td><td rowspan=1 colspan=1>1.37 (1.22~1.52)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>ESOMEPRAZOLE</td><td rowspan=1 colspan=1>44</td><td rowspan=1 colspan=1>1374</td><td rowspan=1 colspan=1>1497.14 (1256.71~1737.58)</td><td rowspan=1 colspan=1>1.95 (1.48~2.43)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>ADALIMUMAB</td><td rowspan=1 colspan=1>125</td><td rowspan=1 colspan=1>354</td><td rowspan=1 colspan=1>625.48 (482.75~768.21)</td><td rowspan=1 colspan=1>0.81 (0.70~0.93)</td><td rowspan=1 colspan=1>Early failure</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE TENOFOVIRDISOPROXIL</td><td rowspan=1 colspan=1>177</td><td rowspan=1 colspan=1>1403.5</td><td rowspan=1 colspan=1>1522.51 (1355.64~1689.39)</td><td rowspan=1 colspan=1>1.41 (1.23~1.58)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>ETANERCEPT</td><td rowspan=1 colspan=1>46</td><td rowspan=1 colspan=1>626</td><td rowspan=1 colspan=1>851.19 (524.77~1177.61)</td><td rowspan=1 colspan=1>0.80 (0.60~1.00)</td><td rowspan=1 colspan=1>Early failure</td></tr><tr><td rowspan=1 colspan=1>TENOFOVIR DISOPROXIL(M)</td><td rowspan=1 colspan=1>133</td><td rowspan=1 colspan=1>1248.5</td><td rowspan=1 colspan=1>1468.48 (1302.05~1670.92)</td><td rowspan=1 colspan=1>1.44 (1.23~1.64)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>TENOFOVIR DISOPROXIL(F)</td><td rowspan=1 colspan=1>93</td><td rowspan=1 colspan=1>1435</td><td rowspan=1 colspan=1>1469.99 (1230.72~1709.25)</td><td rowspan=1 colspan=1>1.29 (1.07~1.51)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE TENOFOVIRDISOPROXIL(M)</td><td rowspan=1 colspan=1>104</td><td rowspan=1 colspan=1>1386</td><td rowspan=1 colspan=1>1578.37 (1365.05~1791.68)</td><td rowspan=1 colspan=1>1.49 (1.25~1.74)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr><tr><td rowspan=1 colspan=1>EMTRICITABINE TENOFOVIRDISOPROXIL(F)</td><td rowspan=1 colspan=1>73</td><td rowspan=1 colspan=1>1449</td><td rowspan=1 colspan=1>1517.81 (1242.37~1787.26)</td><td rowspan=1 colspan=1>1.30 (1.06~1.56)</td><td rowspan=1 colspan=1>Wear-out failurecurve</td></tr></table>

Abbreviation: TTO, time-to-onset; CI, confidence interval.

Age distribution results indicate that the 65–85 age group accounts for the largest proportion of adverse events in both categories, suggesting that older age is a high-risk period for drug-induced bone metabolic abnormalities. With aging, slower bone remodeling, degradation of trabecular microstructure, and polypharmacy are common, all of which may amplify the negative impact of drugs on bone density (Liu et al., 2025). Although the 50–100 kg weight group appeared most prevalent among reported cases, data on patient weight were missing in a significant proportion of reports (>60%). Given this high rate of missing data, we refrained from drawing definitive conclusions regarding dose-to-weight ratios or pharmacokinetic variations. This limitation highlights the critical need for more complete demographic recording in future real-world monitoring to facilitate precise risk assessment.

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Weber analysis of induction time for osteoporosis high-risk signal Drugs. (A) Tenofovir disoproxil induction time weber distribution curve (B) Esomeprazole induction time weber distribution curve (C) Adalimumab induction time weber distribution curve (D) Emtricitabine tenofovir disoproxil induction time weber distribution curve (E) Etanercept induction time weber distribution curve (F) Tenofovir disoproxil (male) induction time weber distribution curve (G) Tenofovir disoproxil (female) induction time weber distribution curve (H) Emtricitabine tenofovir disoproxil (male) induction time weber distribution curve (I) Emtricitabine tenofovir disoproxil (female) induction time weber distribution curve.

Indication analysis revealed that HIV infection accounted for the highest proportion of reports related to bone density reduction (36.9%), while rheumatoid arthritis (13.6%) and HIV infection (11.8%) were the leading indications for osteoporosis. This suggests that the immunosuppressive state and long-term antiviral therapy may jointly impact bone metabolic pathways, increasing the risk of drug-induced bone damage (Biver, 2022). Particularly, patients on antiretroviral therapy (ART) may experience chronic inflammation, tubular toxicity, and vitamin D metabolism abnormalities, which further exacerbate bone loss (Finnerty et al., 2017). The majority of reports came from the United States and Canada, reflecting the robustness of drug safety monitoring systems in North America, and highlighting the need for further global sharing and standardization of drug safety data.

In summary, elderly women, long-term users of antiviral or immunomodulatory drugs, and individuals over 65 years of age are key targets for the prevention and control of bone metabolic-related adverse reactions. Clinicians should enhance bone density monitoring and nutritional metabolic assessments during the early stages of treatment.

## 4.2 Gender differences and risk drug spectrum

This study revealed significant gender differences in drugrelated bone density reduction and osteoporosis. In bone density reduction events, antiviral drugs, especially Tenofovir Disoproxil (ROR = 1139.82) and its combination formulation Emtricitabine Tenofovir Disoproxil (ROR = 965.86), were the high-risk drugs for men, whereas women exhibited higher risks with bone metabolic regulators such as Denosumab (ROR = 10.91) and Teriparatide (ROR = 12.5). These differences not only reflect medication background variations but also illustrate the different mechanisms of action of drugs in gender-specific physiological and bone metabolic pathways.

In men, Tenofovir Disoproxil and its combination formulations induce mitochondrial dysfunction and renal proximal tubule damage by inhibiting mitochondrial DNA polymerase-γ (DNA polymerase-γ), resulting in phosphate loss, Fanconi syndrome, and hypophosphatemia, which ultimately lead to impaired bone mineralization and demineralization. Furthermore, Tenofovir downregulates osteoblast key transcription factors such as RUNX2 and osteocalcin, inhibiting bone formation, while enhancing osteoclast activity, thereby molecularly exacerbating bone density reduction (Mazon et al., 2018; Kimura et al., 2024). Many male HIV patients require long-term combination antiretroviral therapy (ART), and the cumulative effects of these drugs, along with kidney-bone axis damage mechanisms, may explain the high ROR values observed (Tomazic et al., 2007).

In women, Denosumab, a monoclonal RANKL antibody, effectively inhibits osteoclastogenesis by blocking the RANKL/ RANK signaling pathway. However, after discontinuation, the rebound effect of RANKL leads to a significant increase in bone resorption in the short term, resulting in rapid bone loss and increased fracture risk (Diab and Watts, 2014). Teriparatide (recombinant human parathyroid hormone 1–34) stimulates bone formation intermittently, but when used long-term or at inappropriate doses in elderly women with declining metabolic reserves, it may activate the RANKL pathway and cause excessive bone remodeling, leading to bone structure degeneration and decreased bone density under a state of bone metabolic imbalance (Blick et al., 2009). Additionally, estrogen deficiency downregulates estrogen receptor-α (ERα) signaling in female osteocytes, reducing the tolerance to drug-induced metabolic stress, thereby amplifying adverse drug effects on bone metabolism (Cui et al., 2024).

In osteoporosis-related events, male risk drugs were also primarily antiviral drugs (Tenofovir Disoproxil, ROR = 318.27; Emtricitabine Tenofovir Disoproxil, ROR = 275.51), while women’s risk drugs were represented by immunomodulatory drugs and proton pump inhibitors (PPIs) (Adalimumab, ROR = 2.09; Esomeprazole, ROR = 11.03). In men, long-term Tenofovir exposure may induce osteoporosis through energy metabolism disorders in bone cells and mechanisms of renal bone disease. The damage mechanisms include: ① impaired tubular reabsorption of phosphate; ② reduced synthesis of 1,25-dihydroxyvitamin D; ③ elevated serum alkaline phosphatase, leading to impaired bone matrix calcification (Kim et al., 2023).

Women taking PPIs show a significantly increased fracture risk. The molecular mechanisms include: decreased calcium solubility and impaired active absorption due to suppressed gastric acid secretion, downregulation of the calcium transporter TRPV6 in the intestine under long-term low-acid conditions (Moledina and Perazella, 2016); compensatory increases in parathyroid hormone (PTH) promoting bone resorption; and interference with the local microenvironment of bone remodeling via suppression of gastrinrelated signaling (Huang et al., 2024). Additionally, Esomeprazole may interfere with the Wnt/β-catenin signaling pathway, inhibiting osteoblast differentiation, thereby further impairing bone formation (Luk et al., 2013). For immunomodulatory agents like Adalimumab (anti-TNF-α monoclonal antibody), while improving arthritis symptoms, it can suppress TNF-α-mediated osteoblast activity recovery and bone remodeling, which may lead to bone metabolic imbalance with long-term use (Chan et al., 2015).

Gender differences are not only reflected in the types of drugs but also in the sensitivity of molecular pathways to responses. Male bone metabolism is primarily regulated by the androgen-IGF-1 axis, where a decrease in androgen levels reduces bone formation rate. In contrast, women’s bone metabolism is regulated by the estrogen-RANKL/OPG axis, where a decline in estrogen levels significantly enhances osteoclastic activity. This difference results in varying effects of the same drug on bone homeostasis through different hormone-dependent pathways, causing differences in ROR intensity (Ga et al., 2000). In conclusion, drug-induced bone metabolic damage exhibits distinct gender specificity, and the mechanisms involve endocrine regulation, mitochondrial energy metabolism, osteocyte signal transduction, and other biological processes. Clinical drug safety monitoring should incorporate gender, physiological, and metabolic status into stratified assessments for personalized risk management.

## 4.3 Exploration of potential risk drugs and mechanisms

This study identified 8 new risk signal drugs associated with bone density reduction and 32 with osteoporosis. These include Esomeprazole $\mathrm { ( R O R \ = \ } 3 . 9 8 \mathrm { ) }$ , Leflunomide $( \mathrm { R O R } \ = \ 6 . 0 0 )$ , Salmeterol $\begin{array} { l } { ( \mathrm { R O R } ~ = ~ 1 . 9 4 ) } \end{array}$ , Lamivudine $( \mathrm { R O R } \ = \ 6 . 1 8 )$ , and Lopinavir/Ritonavir (ROR = 6.33). These drugs were not listed in the product labeling as having adverse effects on bone metabolism, indicating potential risks.

From a pharmacological perspective, proton pump inhibitors (PPIs) inhibit gastric acid secretion, reducing intestinal calcium absorption and TRPV6 channel activity, and may interfere with the Wnt/β-catenin signaling pathway, inhibiting osteoblast differentiation. Immunomodulatory drugs like Leflunomide can suppress DHODH activity and downregulate BMP-2/Smad pathways, hindering bone formation and enhancing RANKLmediated bone resorption (Li et al., 2017). Antiviral drugs like Lamivudine and Lopinavir/Ritonavir inhibit mitochondrial DNA polymerase-γ, causing mitochondrial dysfunction, energy metabolism abnormalities, and renal hypophosphatemia, which leads to bone demineralization (Sikora et al., 2023). Beta-2 adrenergic agonists like Salmeterol can activate the cAMP/PKA pathway, upregulate RANKL expression, and promote osteoclast activation (Xie et al., 2020).

We further conducted toxicological analyses for Tenofovir Disoproxil (most reported) and Emtricitabine Tenofovir Disoproxil (highest ROR). The results showed that although the overlap in osteoporosis-related toxicity targets was small (3 and 4 targets, respectively), the functional enrichment revealed consistent and biologically directed bone metabolic pathways: both drugs significantly enriched processes related to vitamin D/ calcitriol metabolism and calcium ion homeostasis maintenance, and at the KEGG pathway level, they focused on PTH synthesis, secretion, and action pathways, along with steroid biosynthesis. Given that PTH is an important endocrine regulator maintaining blood calcium homeostasis, continuous activation of this pathway may lead to RANKL/OPG regulatory imbalance, enhanced osteoclast activity, and shift bone remodeling from dynamic balance to “net bone loss,” thereby increasing osteoporosis risk (De Leon-Oliva et al., 2023). Additionally, the combination drug further correlated with estrogen response and osteoclast differentiation pathways. Estrogen usually regulates the RANKL–OPG axis in osteoblasts/osteocytes (reducing RANKL, increasing OPG) to inhibit osteoclast differentiation and maturation. Disruption of this signaling may weaken physiological inhibition of bone resorption and promote osteoclast dominance (Cheng et al., 2022).

In conclusion, the findings suggest that the osteoporosis risk of HIV-related antiretroviral drugs may not only result from the previously emphasized kidney-bone metabolic axis disruption and phosphate-related bone demineralization but also from sustained disruption of the vitamin D–calcium homeostasis–PTH endocrine regulatory network, along with a cascade of sex hormone regulation imbalances and osteoclast activation. Based on these insights, it is recommended to include vitamin D metabolism markers, calcium-phosphate homeostasis, and PTH-related biochemical parameters in more targeted monitoring frameworks for drug vigilance and clinical risk management, and to use these as key references for future mechanistic validation and risk stratification.

## 4.4 Induction time characteristics and risk management

The time-to-onset (TTO) analysis revealed significant differences in the temporal distribution characteristics of druginduced bone metabolic adverse reactions. The study found that Tenofovir Disoproxil and its combination formulations (e.g., Emtricitabine Tenofovir Disoproxil) exhibited a typical “wearout failure curve” (β > 1), with a median TTO exceeding 1,200 days, indicating that the risk of osteoporosis gradually accumulates with prolonged use. This aligns with the mechanisms of renal tubular damage, phosphate loss, and bone demineralization induced by Tenofovir during long-term treatment. Esomeprazole also showed a significant wear-out failure-type curve (β = 1.95), indicating that long-term acid suppression therapy gradually weakens bone remodeling ability, with significant cumulative risk. In contrast, Adalimumab and Etanercept exhibited early failure-type curves with β values < 1 (0.81 and 0.80, respectively), suggesting that adverse reactions occur more frequently early in treatment, potentially related to the early interference of these drugs with bone metabolism balance and immune inflammation (Jamnitski et al., 2012).

These results suggest that in clinical risk management, differentiated strategies should be adopted based on the induction time characteristics of different drugs: for long-term antiviral medications, it is essential to focus on cumulative bone damage risks and recommend regular monitoring of bone density and serum phosphate levels; for immunomodulatory drugs, bone pain, muscle wasting, and other symptoms should be closely monitored in the early stages of treatment and intervened in a timely manner; for elderly women on long-term PPIs or aromatase inhibitors, baseline bone density should be established at the start of treatment, and medication adherence and safety should be evaluated dynamically.

## 4.5 Limitations

This study has several limitations that should be considered. First, the FAERS and CVARDD databases rely on voluntary reporting, which can lead to underreporting or incomplete data. This reporting bias may result in an incomplete representation of the true incidence of drug-related adverse events, particularly when critical information such as gender, age, or weight is missing from reports. Second, while the disproportionality analysis identifies associations between drugs and adverse events, it cannot establish causality. Confounding factors, such as underlying health conditions, co-medications, or genetic predispositions, may contribute to bone metabolism abnormalities but were not fully accounted for in this analysis. Lastly, the study primarily reflects data from the United States and Canada, which may not fully represent global populations. Geographic differences in healthcare systems, drug usage patterns, and genetic diversity could limit the generalizability of the results, highlighting the need for broader, more inclusive studies.

## 5 Conclusion

This study, by analyzing data from the U.S. FDA Adverse Event Reporting System (FAERS), systematically revealed the risk spectrum of drug-related bone density reduction and osteoporosis in the elderly population. The study found that antiviral drugs, immunomodulatory drugs, and proton pump inhibitors are closely related to bone metabolic abnormalities, and that gender plays a significant role in the risk of druginduced osteoporosis and bone density reduction. Specifically, for HIV patients, antiretroviral drugs such as Tenofovir and its combination formulations were identified as high-risk drugs for osteoporosis.

Through disproportionality analysis (DPA), we identified several potential high-risk drugs and further explored their mechanisms through toxicological analysis. The study results indicate that these drugs may promote the occurrence of osteoporosis by disrupting the vitamin D–calcium homeostasis–PTH regulatory network and sex hormone regulatory mechanisms. Meanwhile, we identified some drugs that were not explicitly listed in the product labeling as causing bone metabolic adverse reactions, providing new monitoring signals for clinical practice.

Additionally, induction time analysis revealed significant differences in the time-to-onset of bone density reduction and osteoporosis-related adverse reactions across different drugs. Specifically, long-term drugs like Tenofovir and its combination formulations exhibited a clear “wear-out failure curve,” suggesting that these drugs progressively increase the risk of osteoporosis over time. In contrast, immunomodulatory drugs tended to induce adverse reactions early in treatment.

In conclusion, this study provides strong evidence for the clinical risk management of drug-related bone metabolic abnormalities, particularly for elderly patients and HIV-infected individuals. The study emphasizes the importance of drug safety monitoring, especially for long-term medications, and suggests that clinicians should strengthen early monitoring and management of bone metabolic adverse reactions, implementing differentiated risk prevention strategies based on the induction time characteristics of the drugs.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary Material, further inquiries can be directed to the corresponding authors.

## Author contributions

XL: Writing – review and editing, Formal Analysis, Writing – original draft, Software, Methodology, Data curation, Visualization. YG: Visualization, Methodology, Formal Analysis, Writing – review and editing, Writing – original draft, Software. LL: Software, Writing – review and editing, Resources, Visualization, Methodology. XW: Writing – original draft, Software, Data curation, Methodology. KH: Data curation, Software, Methodology, Writing – review and editing. MS: Methodology, Supervision, Data curation, Writing – review and editing, Writing – original draft, Funding acquisition, Software. YS: Methodology, Software, Writing – original draft, Funding acquisition, Conceptualization, Supervision, Investigation, Writing – review and editing.

## Funding

The author(s) declared that financial support was received for this work and/or its publication. The work was supported by 2024 Gansu Province University Teacher Innovation Fund Project (2024A-087). Science Research and Innovation Fund Project of Gansu University of Traditional Chinese Medicine in 2023 (2023KCZD-8). National Natural Science Foundation of China Regional Project (81960878).

## References

Almodovar, A. S., and Nahata, M. C. (2019). Associations between chronic disease, polypharmacy, and medication-related problems among medicare beneficiaries. J. Manag. Care Spec. Pharm. 25 (5), 573–577. doi:10.18553/jmcp.2019.25.5.573

Biver, E. (2022). Osteoporosis and HIV infection. Calcif. Tissue Int. 110 (5), 624–640. doi:10.1007/s00223-022-00946-4

Blick, S. K., Dhillon, S., and Keam, S. J. (2009). Spotlight on teriparatide in osteoporosis. BioDrugs 23 (3), 197–199. doi:10.2165/00063030-200923030-00006

Buttgereit, F., Palmowski, A., Bond, M., Adami, G., and Dejaco, C. (2024). Osteoporosis and fracture risk are multifactorial in patients with inflammatory rheumatic diseases. Nat. Rev. Rheumatol. 20 (7), 417–431. doi:10.1038/s41584-024-01120-w

Chan, J. K., Glass, G. E., Ersek, A., Freidin, A., Williams, G. A., Gowers, K., et al. (2015). Low-dose TNF augments fracture healing in normal and osteoporotic bone by upregulating the innate immune response. EMBO Mol. Med. 7 (5), 547–561. doi:10.15252/ emmm.201404487

Cheng, C., Chen, L., and Chen, K. (2022). Osteoporosis due to hormone imbalance: an overview of the effects of estrogen deficiency and glucocorticoid overuse on bone turnover. Int. Journal Molecular Sciences 23 (3), 1376. doi:10. 3390/ijms23031376

## Acknowledgements

This study was performed using open-source data provided by the FAERS and CVARDD database, and we thank all those who provided information for this database.

## Conflict of interest

The author(s) declared that this work was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Generative AI statement

The author(s) declared that generative AI was not used in the creation of this manuscript.

Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2026.1790867/ full#supplementary-material

Cui, H., Li, J., Li, X., Su, T., Wen, P., Wang, C., et al. (2024). TNF-Alpha promotes osteocyte necroptosis by upregulating TLR4 in postmenopausal osteoporosis. Bone 182, 117050. doi:10.1016/j.bone.2024.117050

De Leon-Oliva, D., Barrena-Blázquez, S., Jiménez-álvarez, L., Fraile-Martinez, O., García-Montero, C., López-González, L., et al. (2023). The RANK-RANKL-OPG System: a multifaceted regulator of homeostasis, immunity, and cancer. Med. Kaunas. Lith. 59 (10), 1752. doi:10.3390/medicina59101752

Di, J., Yang, N., Zhao, Y., Chen, S., Guo, Z., He, D., et al. (2025). Evaluating the risk of osteoporosis-related adverse events with proton pump inhibitors: a pharmacovigilance study. Front. Pharmacol. 16, 1582908. doi:10.3389/fphar.2025.1582908

Diab, D. L., and Watts, N. B. (2014). Denosumab in osteoporosis. Expert Opin. Drug Saf. 13 (2), 247–253. doi:10.1517/14740338.2014.860133

Dumitrescu, F., Dragonu, L., Marcu, E. A., Pădureanu, V., Stoian, A. C., Rădoi-Troacă, C. L., et al. (2025). Bone mineral density in HIV-Infected people-the experience of Craiova regional Center. Biomedicines 13 (9), 2305. doi:10.3390/ biomedicines13092305

Eastell, R., Rosen, C. J., Black, D. M., Cheung, A. M., Murad, M. H., and Shoback, D. (2019). Pharmacological management of osteoporosis in postmenopausal women: an

Endocrine Society\* Clinical Practice Guideline. J. Clin. Endocrinol. Metab. 104 (5), 1595–1622. doi:10.1210/jc.2019-00221

Finnerty, F., Walker-Bone, K., and Tariq, S. (2017). Osteoporosis in postmenopausal women living with HIV. Maturitas 95, 50–54. doi:10.1016/j.maturitas.2016.10.015

Garnero, P., Sornay-Rendu, E., and Delmas, P. D. (2000). Low serum IGF-1 and occurrence of osteoporotic fractures in postmenopausal women. Lancet 355 (9207), 898–899. doi:10.1016/s0140-6736(99)05463-x

Gibbons, B., Lubsen, J., and Martonffy, A. I. (2025). Bone health in women. Prim. Care 52 (2), 353–370. doi:10.1016/j.pop.2025.01.008

Huang, J., Wu, T., Jiang, Y. R., Zheng, X. Q., Wang, H., Liu, H., et al. (2024). beta-Receptor blocker enhances the anabolic effect of PTH after osteoporotic fracture. Bone Res. 12 (1), 18. doi:10.1038/s41413-024-00321-z

Irsik, D. L., Bollag, W. B., and Isales, C. M. (2021). Renal contributions to age-related changes in mineral metabolism. JBMR Plus 5 (10), e10517. doi:10.1002/jbm4.10517

Isganaitis, E. (2019). Developmental programming of body composition: update on evidence and mechanisms. Curr. Diab Rep. 19 (8), 60. doi:10.1007/s11892-019-1170-1

Jamnitski, A., Krieckaert, C. L., Nurmohamed, M. T., Hart, M. H., Dijkmans, B. A., Aarden, L., et al. (2012). Patients non-responding to etanercept obtain lower etanercept concentrations compared with responding patients. Ann. Rheum. Dis. 71 (1), 88–91. doi:10.1136/annrheumdis-2011-200184

Jing, Y., Chen, X., Li, K., Liu, Y., Zhang, Z., Chen, Y., et al. (2022). Association of antibiotic treatment with immune-related adverse events in patients with cancer receiving immunotherapy. J. Immunother. Cancer 10 (1), e003779. doi:10.1136/jitc-2021-003779

Kim, E., Lee, H. W., Kim, S. S., Yoon, E., Jang, E. S., Chang, J. I., et al. (2023). Tenofovir disoproxil fumarate versus tenofovir alafenamide on risk of osteoporotic fracture in patients with chronic hepatitis B: a nationwide claims study in South Korea. Aliment. Pharmacol. Ther. 58 (11-12), 1185–1193. doi:10.1111/apt.17716

Kimura, S., Sunouchi, T., Watanabe, S., Hoshino, Y., Hidaka, N., Kato, H., et al. (2024). Latent metabolic bone disease, skeletal dysplasia and other conditions related to low bone formation among 38 patients with subtrochanteric femoral fractures: a retrospective observational study. Osteoporos. Int. 35 (9), 1633–1643. doi:10.1007/ s00198-024-07168-4

Lespessailles, E., and Toumi, H. (2022). Proton pump inhibitors and bone health: an update narrative review. Int. J. Mol. Sci. 23 (18), 10733. doi:10.3390/ijms231810733

Li, L., Sapkota, M., Gao, M., Choi, H., and Soh, Y. (2017). Macrolactin F inhibits RANKLmediated osteoclastogenesis by suppressing Akt, MAPK and NFATc1 pathways and promotes osteoblastogenesis through a BMP-2/smad/Akt/Runx2 signaling pathway. Eur. J. Pharmacol. 815, 202–209. doi:10.1016/j.ejphar.2017.09.015

Liu, L., Song, Y., Liu, X., Song, B., and Song, M. (2025). Sex differences in drug-induced osteoporosis: a pharmacovigilance study based on the FAERS database. Front. Public Health 13, 1630412. doi:10.3389/fpubh.2025.1630412

Luk, C. P., Parsons, R., Lee, Y. P., and Hughes, J. D. (2013). Proton pump inhibitorassociated hypomagnesemia: what do FDA data tell us?. Ann. Pharmacother. 47 (6), 773–780. doi:10.1345/aph.1R556

Mazon, M., Julien, J., Ung, R. V., Picard, S., Hamoudi, D., Tam, R., et al. (2018). Deletion of the Fanconi Anemia C gene in mice leads to skeletal anomalies and defective bone mineralization and microarchitecture. J. Bone Min. Res. 33 (11), 2007–2020. doi:10.1002/ jbmr.3546

Moledina, D. G., and Perazella, M. A. (2016). PPIs and kidney disease: from AIN to CKD. J. Nephrol. 29 (5), 611–616. doi:10.1007/s40620-016-0309-2

Ran, C., Tao, X., Shao, H., Liu, Y., and Tao, J. (2025). Different effects of tumor necrosis factor monoclonal antibody and receptor fusion protein on bone metabolism. Int. Immunopharmacol. 162, 115108. doi:10.1016/j.intimp.2025.115108

Rizzoli, R., Reginster, J. Y., Boonen, S., Bréart, G., Diez-Perez, A., Felsenberg, D., et al. (2011). Adverse reactions and drug-drug interactions in the management of women with postmenopausal osteoporosis. Calcif. Tissue Int. 89 (2), 91–104. doi:10.1007/ s00223-011-9499-8

Robertson, J., Bondarenko, I. M., Trishkina, E., Dvorkin, M., Panasci, L., Manikhas, A., et al. (2016). Fulvestrant 500 mg versus anastrozole 1 mg for hormone receptor-positive advanced breast cancer (FALCON): an international, randomised, double-blind, phase 3 trial. Lancet 388 (10063), 2997–3005. doi:10.1016/S0140-6736(16)32389-3

Rothman, K. J., Lanes, S., and Sacks, S. T. (2004). The reporting odds ratio and its advantages over the proportional reporting ratio. Pharmacoepidemiol Drug Saf. 13 (8), 519–523. doi:10.1002/pds.1001

Sikora, M., Smieszek, A., Pielok, A., and Marycz, K. (2023). MiR-21-5p regulates the dynamic of mitochondria network and rejuvenates the senile phenotype of bone marrow stromal cells (BMSCs) isolated from osteoporotic SAM/P6 mice. Stem Cell Res. Ther. 14 (1), 54. doi:10.1186/s13287-023-03271-1

Thiruchelvam, T., Lim, C. X., Munro, C., Chan, V., Jayasuria, G., Coulthard, K. P., et al. (2025). Adverse events and drug interactions associated with Elexacaftor/Tezacaftor/ Ivacaftor treatment: a descriptive Study across Australian, Canadian, and American adverse event databases. Life (Basel) 15 (8), 1256. doi:10.3390/life15081256

Tomazic, J., Ul, K., Volcansek, G., Gorensek, S., Pfeifer, M., Karner, P., et al. (2007). Prevalence and risk factors for osteopenia/osteoporosis in an HIV-infected male population. Wien Klin. Wochenschr 119 (21-22), 639–646. doi:10.1007/s00508-007- 0844-x

Xie, W., Li, F., Han, Y., Qin, Y., Wang, Y., Chi, X., et al. (2020). Neuropeptide Y1 receptor antagonist promotes osteoporosis and microdamage repair and enhances osteogenic differentiation of bone marrow stem cells via cAMP/PKA/ CREB pathway. Aging (Albany NY) 12 (9), 8120–8136. doi:10.18632/aging.103129

Yu, R. J., Krantz, M. S., Phillips, E. J., and Stone, C. A. (2021). Emerging causes of druginduced anaphylaxis: a review of anaphylaxis-associated reports in the FDA Adverse Event Reporting System (FAERS). J. Allergy Clin. Immunol. Pract. 9 (2), 819–829. doi:10. 1016/j.jaip.2020.09.021