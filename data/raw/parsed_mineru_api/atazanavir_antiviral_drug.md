# Development of a Physiologically Based Model of Bilirubin Metabolism in Health and Disease and Its Comparison With Real-World Data

Ahenk Zeynep Sayin1,2 | Lars Kuepfer1,2

1Institute for Systems Medicine With Focus on Organ Interaction, University Hospital RWTH Aachen, Aachen, Germany | 2Center for Computational Life Sciences, RWTH Aachen University, Aachen, Germany

Correspondence: Lars Kuepfer (lkuepfer@ukaachen.de)

Received: 19 April 2025 | Revised: 17 December 2025 | Accepted: 18 December 2025

Keywords: bilirubin | disorders of bilirubin metabolism | interindividual variability | PBPK | population simulation | real-world data

## ABSTRACT

Bilirubin is a breakdown product of erythrocytes and plays a crucial role in elimination of heme-containing proteins. After its synthesis in the reticuloendothelial system, unconjugated bilirubin is released into plasma and taken up into the liver. In hepatocytes, bilirubin is conjugated and excreted into the gastrointestinal tract via bile, where it is further converted to urobilinoids. There are various genetic factors causing abnormal bilirubin levels in plasma, such as Gilbert syndrome, Crigler-Najjar syndrome, Dubin-Johnson syndrome, and Rotor syndrome. To better understand bilirubin metabolism and its disorders, this study develops a physiologically based computational model incorporating published literature as well as real-world clinical data from the Explorys database. The model simulates bilirubin levels in both healthy individuals and patients with disorders of bilirubin metabolism. Population simulations show that Gilbert syndrome requires a substantial reduction in UDP-glucuronosyltransferase 1A1 activity, while Crigler-Najjar syndrome requires near-complete loss of its function. In contrast, Dubin-Johnson syndrome is characterized by a significant impairment of multidrug resistance-associated protein 2 activity. To also illustrate model behavior under targeted perturbations, we simulated administration of atazanavir in healthy individuals and patients with Gilbert syndrome to investigate its effect on bilirubin levels. Relative to baseline, unconjugated bilirubin maximum concentration $( C _ { \mathrm { m a x } } )$ increased by 34% in healthy individuals but by 67% in Gilbert syndrome. Overall, this study provides a conceptual and mechanistically informed framework for studying bilirubin homeostasis and the functional consequences of drug administration in health and disease.

## 1 | Introduction

Bilirubin is produced during heme degradation, mainly from the breakdown of hemoglobin in erythrocytes, with the remaining formed by degradation of hemoproteins. Heme is converted to biliverdin by heme oxygenase, which is then converted to unconjugated bilirubin (UB) by biliverdin reductase [1]. As UB is almost water-insoluble, it is transported to the liver bound to albumin in the bloodstream [2]. In the liver, bilirubin is conjugated by UDP-glucuronosyltransferase 1A1 (UGT1A1), which makes bilirubin hydrophilic. Conjugated bilirubin (CB) is then excreted into the bile and secreted into the duodenum. In the gastrointestinal tract, bilirubin is converted into urobilinoids through gut microbial enzymes. Most of the urobilinoids are excreted in the feces, while a smaller portion (\~1%) is reabsorbed into the enterohepatic circulation or excreted in urine [3, 4].

Disorders of bilirubin metabolism such as Gilbert syndrome, Crigler-Najjar syndrome, Dubin-Johnson syndrome, and Rotor syndrome result from genetic and metabolic conditions leading

## Study Highlights

• What is the current knowledge on the topic?

○ Bilirubin metabolism involves breakdown of heme into unconjugated bilirubin, which is then conjugated in the liver and excreted into the bile. Disorders such as Gilbert syndrome, Crigler-Najjar syndrome, Dubin-Johnson syndrome, and Rotor syndrome disrupt this process, leading to abnormal bilirubin levels.

• What question did this study address?

○ We developed a whole-body physiologically based computational model representing bilirubin metabolism to evaluate the bilirubin levels in health and bilirubin-related disorders, addressing interindividual variability, disorder-specific mechanistic alterations, and effects of dynamic perturbations.

• What does this study add to our knowledge?

○ The study presents functional analyses of bilirubin homeostasis and specific metabolic disorders. It is the first study to systematically compare simulations of bilirubin metabolism with real-world clinical data, providing insights into interindividual variability and disorder-specific patterns.

• How might this change drug discovery, development, and/or therapeutics?

○ The model provides a conceptual and mechanistic framework for investigation of drug-induced perturbations in bilirubin metabolism. The model can in particular be used to explore aberrant states in vulnerable patient subgroups with specific metabolic disorders at the population level.

to abnormal levels of bilirubin [5, 6]. Computational models may support a functional understanding of these disorders, which can significantly affect neurological and overall health status [7].

Existing models of bilirubin metabolism in the literature are largely based on compartmental modeling. For example, Berk et al. studied bilirubin kinetics in normal adults using a threecompartment model [8]. Similarly, Cobelli et al. focused on a two-compartment model of bilirubin kinetics in normal, hemolytic, and Gilbert's state [9]. Levitt and Levitt developed a pharmacokinetic model simulating plasma concentrations of both UB and CB in various hyperbilirubinemia pathologies based on the observation that double knockout of the organic anion-transporting polypeptide 1A (OATP1A) and organic anion-transporting polypeptide 1B (OATP1B) hepatic transporters in rats increases plasma CB approximately 400-fold [10]. Yang et al. used a physiologically based pharmacokinetic (PBPK) model, tuned with bilirubin levels from published studies on individuals with disorders of bilirubin metabolism, to distinguish drug-induced hyperbilirubinemia from liver injury-related hyperbilirubinemia [11]. Similarly, Dong et  al. applied PBPK modeling to assess the relative contributions of UGT1A1 and OATP1B1/3 inhibition by atazanavir in bilirubin elevation [12].

We here used PBPK modeling to create a physiologically based computational framework of bilirubin metabolism in health and disease (Figure  1). Generally, PBPK modeling describes physiological processes governing the distribution of drugs in the body at a large level of detail [13]. PBPK modeling can also be used to describe the distribution of endogenous molecules such as bile acids [14, 15] or proteins [16]. The primary goals of the study are to characterize bilirubin levels and to moreover explore the interindividual variability in healthy individuals and bilirubin-related disorders. To this end, population simulations were performed and compared to published and real-world data. Extending previous studies using controlled experiments, this work integrates real-world clinical data from multiple health institutions in the United States, made available by the Explorys database [17]. While model development focused on static conditions, we furthermore explored the potential for dynamic perturbations in bilirubin metabolism. Accordingly, the effect of the UGT1A1 and OATP1B1 inhibitor atazanavir [18] on bilirubin levels was evaluated using models for healthy individuals and patients with Gilbert syndrome. This work hence provides valuable mechanistic insights into the dynamics of bilirubin metabolism in health and disease.

## 2 | Methods

## 2.1 | Physiologically Based Pharmacokinetic Modeling

Physiologically based pharmacokinetic (PBPK) models predict the absorption, distribution, metabolism, and excretion (ADME) of drugs and endogenous molecules [13]. They rely on extensive physiological information such as organ volumes or organ blood flow rates, usually provided by the PBPK software. Organs are represented by plasma, intracellular, and interstitial compartments interconnected through vascular circulation. In PBPK modeling, tissue permeation and organ/plasma partitioning are calculated from physicochemical properties of a compound [13]. Together with active, protein-mediated processes, this allows a quantitative simulation of plasma and tissue time-concentration profiles.

Our model was developed with PK-Sim and MoBi from the open-source Open System Pharmacology (OSP) Suite (Version 11.1, www.open-systems-pharmacology.org) [19]. Details of the parameter identification and sensitivity analyses are provided in Text S1, and the methods used for calculating partition coefficients and permeabilities are described in Text S2.

## 2.2 | Physiologically Based Model of Bilirubin Metabolism

Reactions and active transport processes in the physiologically based model of bilirubin metabolism were modeled using Michaelis–Menten kinetics. Tubular secretion with Michaelis– Menten kinetics was selected for renal excretion, and OATP1B1 and MRP3 was assumed to be exclusively expressed on the basolateral surface of the hepatocytes. To reach the steady state in the model with bilirubin synthesis, simulations were run over an extended period to ensure calibration.

(a)  
<!-- image-->  
(b)  
FIGURE 1 | The systemic processes (a) and the specific reactions (b) in the physiologically based computational model of bilirubin metabolism. The model involves bilirubin synthesis, active transport processes via OATP1B1, MRP2, and MRP3, conjugation of bilirubin in the liver, intestinal reduction of bilirubin, as well as fecal and renal excretion. Unconjugated bilirubin (UB) is conjugated in the liver via UGT1A1. After the release of conjugated bilirubin (CB) into the small intestine, conjugated bilirubin is first reduced to unconjugated bilirubin and then further converted to urobilinogen (UBG) via gut microbial enzymes in the intestine. Some unconjugated bilirubin and a small portion of urobilinogen formed in the gut are reabsorbed into the enterohepatic circulation. A minor fraction of urobilinogen enters the systemic circulation, but it is not shown here for simplicity.

## 2.3 | Literature Data

Data points were digitized from published figures using WebPlotDigitizer [20]. Experimental studies involving administration of labeled bilirubin and time-resolved measurements were additionally considered for model development. In the corresponding simulation, only intravenous administration of

0.5 mg of exogenous bilirubin [21] was simulated, neglecting endogenous bilirubin metabolism.

## 2.4 | Explorys Data

The Explorys database is a commercial database comprising electronic health records collected from health institutions in the United States involving data of almost 1 million patients with liver-related health conditions [17]. Data was retrieved from the Explorys database in September 2024.

Details on cohort selection, exclusion criteria, and bilirubin measurement extraction from the Explorys database are provided in Text  S3. Descriptive information for each cohort, including number of patients, age, number of bilirubin observations, and summary statistics are provided in Section 3. All bilirubin measurements with the dimension of mass/volume were harmonized to mg/dL units. Statistics were calculated by excluding the top and bottom 2.5% of the data as there were some extreme outliers.

## 2.5 | Population Simulations

For the population simulations, the model was imported from MoBi into PK-Sim and a virtual population of 1000 individuals was created. PK-Sim randomly varies anatomical and physiological parameters according to their respective distributions [22]. To account for biological variability, a log-normal distribution of $V _ { \mathrm { m a x } }$ values was applied, with a geometric standard deviation of 1.6, based on Beal's characterization of typical genetic expressions variability [23]. For disease-specific cohorts, $V _ { \mathrm { m a x } }$ of the affected enzyme or transporter was scaled to reproduce the deficiency in each disorder. This top-down $V _ { \mathrm { m a x } }$ scaling approach was chosen to reflect alterations observed in real-world data while maintaining simplicity and computational efficiency. Additionally, the bottom and top 2.5% of the data were trimmed to ensure comparability with the Explorys data.

## 2.6 | Simulation of Atazanavir Administration

The atazanavir PBPK model from the OSP Suite PBPK Model library was used [24]. It includes metabolism by CYP3A4, mechanism-based inhibition of CYP3A4, mixed inhibition of UGT1A1, and glomerular filtration. Moreover, competitive inhibition of OATP1B1 by atazanavir $( K _ { \mathrm { i } } { = } 0 . 1 2 9 \mu \mathrm { M } )$ was incorporated [12]. Combined with the bilirubin metabolism model, 400 mg once daily oral administration of atazanavir for 30 days has been simulated in healthy individuals and patients with Gilbert syndrome.

## 3 | Results

In this study, we developed a physiologically based computational model of bilirubin metabolism, involving key enzymatic and transport processes. The study aimed to evaluate the bilirubin levels in health and bilirubin-related disorders, and to address interindividual variability using published and realworld data. Published data was used as the primary reference in the model calibration, while real-world data served as a second level of comparison to assess population-level variability. Furthermore, we also investigated the effect of the UGT1A1 and OATP1B1 inhibitor atazanavir in healthy individuals and patients with Gilbert syndrome.

## 3.1 | Model for Healthy Individuals and Rotor Syndrome

The physiologically based model includes bilirubin synthesis, hepatic uptake of both UB and CB by OATP1B1 [25–27], and bilirubin conjugation via UGT1A1 (Figure 1). Competitive inhibition between UB and CB for OATP1B1 was considered to capture the increase in UB levels in CB pathologies [10] and the $K _ { \mathrm { i } }$ values for the competing species were assumed to be equal to their $K _ { \mathrm { m } }$ for OATP1B1. The model also involves multidrug resistance-associated protein 2 (MRP2) mediated biliary excretion, multidrug resistance-associated protein 3 (MRP3) mediated systemic efflux, and reduction of CB to UB and further to urobilinogen via gut microbial enzymes. Additionally, the model accounts for fecal and urinary excretion, as well as enterohepatic circulation. An alternative OATP1B1- independent hepatic uptake of UB [10], represented as a firstorder process, was also included to account for basal uptake activity in patients with Rotor syndrome. Passive transport is explicitly represented in the underlying PBPK model. The high affinity of UB for albumin is represented in the model by an extremely low fraction unbound [28] (Table S1). Synthesis of UB was assumed to be 260 mg/day [21], modeled as a constant flux in venous plasma.

For the model development, intravenous administration of exogenous bilirubin was initially considered to describe timeresolved experimental data with labeled bilirubin studies (Figure 2a–d) [8, 9, 21]. Kinetic parameters in Table S2 were calibrated using published data from both healthy individuals and patients with Rotor syndrome (Table S3), following an approach similar to that of Levitt and Levitt [10], but additionally incorporating time-dependent data from labeled bilirubin studies by Cobelli et al. [9], Bloomer et al. [21], and Berk et al. [8] for healthy individuals. Data from healthy individuals and Rotor syndrome were used simultaneously in the calibration to inform the rate of OATP-independent hepatic uptake. In the model for Rotor syndrome, OATP1B1-mediated transport was excluded, while all other transport pathways were present. For steady state predictions (Figure  2e–k), the model including bilirubin synthesis was used, with absent OATP1B1 activity for Rotor syndrome.

In healthy state, the model could successfully describe the plasma levels of UB and CB (Figure 2a,b,e,f), including the CB fraction within the range reported in literature (Figure  2g). Moreover, the model reproduces the cumulative recovery of injected bilirubin in feces and urine from labeled bilirubin studies (Figure $^ { 2 \mathrm { c } , \mathrm { d } ) }$ . However, it overestimates the rate of fecal excretion of urobilinogen (Figure  2h), although the predicted rate of urinary excretion aligns with the literature (Figure 2i). The average rates reported in the literature range from 64 mg/day [21, 35] to 173 mg/day [21, 36] with individual excretion rates of 40.9–279.4 mg/day [35]. Our model estimates a fecal excretion rate of 255 mg/day, which remains within plausible limits.

Sensitivity analysis was performed on the healthy individual model to assess the effect of identified kinetic parameters on the model output. Although a formal identifiability analysis was not conducted due to computational cost, the sensitivity results provide insight into parameter identifiability. Parameters with high sensitivities are expected to be more identifiable as their variation strongly affects outputs. The parameter with the highest sensitivity is OATP1B1 $V _ { \mathrm { m a x } }$ of CB, followed by OATP1B1 $K _ { \mathrm { m } }$ and MRP2 $V _ { \mathrm { m a x } }$ of CB. In contrast, the renal excretion rate of urobilinogen shows the lowest sensitivity (Table S4).

<!-- image-->  
(b)

(e)  
<!-- image-->  
(f)

<!-- image-->

<!-- image-->  
(d)

(i)  
(j)  
<!-- image-->

(c)  
<!-- image-->

<!-- image-->

<!-- image-->  
(h)

(g)  
<!-- image-->

<!-- image-->

(k)  
<!-- image-->  
FIGURE 2 | Model predictions of the bilirubin metabolism model. Panels (a, b) show the predicted healthy plasma unconjugated bilirubin disappearance curves following bilirubin administration, presented as dimensionless (a) and per plasma volume (b), along with the measurements from Cobelli et al. [9], Bloomer et al. [21] and Berk et al. [8]. Panels (c, d) present simulated healthy cumulative recovery of injected bilirubin in feces and urine, respectively, in comparison to the measurements from Berk et al. [8]. Panels (e, f) show the healthy plasma unconjugated and conjugated bilirubin concentrations, respectively, with the measurements from Doumas and Wu [29] and Muraca et al. [30] plotted alongside model predictions at the steady state. For the data with error bars in these panels, the bars represent the upper and lower bounds of the range, while the height of the bar indicates the midpoint of this range. Panel (g) shows the model prediction of the healthy plasma conjugated bilirubin fraction, compared with the results from Berk et al. [8] and Muraca et al. [30]. Panels (h, i) display healthy fecal and urinary urobilinogen excretion rates, respectively, with the model outputs compared to data from Watson [31] and Ha and Bhagavan [32]. Panels (j, k) represent model outputs for plasma unconjugated and conjugated bilirubin concentrations in Rotor syndrome, respectively, in comparison to data from Namihisa and Yamaguchi [33] and van de Steeg et al. [34] with the error bars showing standard deviation.

In Rotor syndrome, the model captures the characteristic pattern, replicating the limited increase in UB (2.55-fold) while showing a higher elevation in CB (106.2-fold), with the simulated UB and CB concentrations being within the observed range (Figure 2j,k) [33, 34].

To also account for the interindividual variability in bilirubin metabolism, simulations were performed with a virtual population of 1000 individuals, which also serves as a validation of the model considering the range of plasma bilirubin levels.

Simulated population-level bilirubin levels in healthy individuals and Rotor syndrome were compared with the Explorys data and literature (see Section  2). To define a healthy bilirubin metabolism cohort in the Explorys database, the cases with

ICD-10 codes affecting bilirubin metabolism were excluded (see Text S3) and individuals aged 18–65 were considered in all cohorts (Table 1).

In healthy individuals, the median UB and total bilirubin (TB) levels from Explorys and the population simulation align with the literature means (Figure 3a–d). For both UB and TB, the range of Explorys is wider, though most individuals fall within the literature-reported ranges, whereas the population simulation results are completely within literature ranges. For the plasma CB, Explorys has higher concentrations than the literature-reported range, while the population simulation results fall mostly within the literature range. For the healthy CB ratio, Explorys and population simulation results generally exhibit higher values than literature, with the population simulation having the highest density slightly above but closer to the literature mean, while covering most of the range observed in the Explorys data. Sensitivity analysis of the rate constants indicates that hepatic uptake of CB and UB via OATP1B1 has the greatest impact on their plasma levels in healthy individuals (Table S4).

TABLE 1 | Statistics of bilirubin observations in the Explorys database for the healthy bilirubin metabolism cohort and cohorts with disorders of bilirubin metabolism.
<table><tr><td colspan="2"></td><td colspan="3">Unconjugated Total bilirubin</td></tr><tr><td colspan="2">Healthy</td><td>224,827</td><td>bilirubin 23,744</td><td>Conjugated bilirubin 73,132</td></tr><tr><td rowspan="10"></td><td>Number of patients</td><td></td><td></td><td></td></tr><tr><td>Age (years), mean ± SD</td><td>52.61 ± 10.10</td><td>51.82 ± 10.23</td><td>52.60±9.95</td></tr><tr><td>Age (years), range</td><td>18-65</td><td>18-65</td><td>18-65</td></tr><tr><td>Number of female patients, (%) Number of observations</td><td>127,323 (56.6%)</td><td>13,163 (55.4%)</td><td>40,548 (55.4%)</td></tr><tr><td>Observation,</td><td>2,469,047 0.58±0.40</td><td>65,979 0.43±0.34</td><td>265,663</td></tr><tr><td>mean ± SD (mg/dL)</td><td></td><td></td><td>0.37±0.46</td></tr><tr><td>Number of patients Age (years), mean ± SD</td><td>346 48.40±12.25</td><td>63</td><td>178</td></tr><tr><td></td><td>18-65</td><td>46.62±12.03</td><td>47.53±12.87</td></tr><tr><td>Age (years), range Number of female patients, (%)</td><td></td><td>18-65</td><td>18-65</td></tr><tr><td>Number of observations</td><td>83 (24.0%) 931</td><td>12 (19.0%)</td><td>38 (21.3%)</td></tr><tr><td>Observation,</td><td>2.82±2.45</td><td>81 1.79±0.81</td><td>260 0.80±0.75</td></tr><tr><td rowspan="6">Crigler-Najjar syndrome</td><td>mean ± SD (mg/dL)</td><td></td><td></td><td></td></tr><tr><td>Number of patients</td><td>1</td><td>/</td><td>/</td></tr><tr><td>Age (years), mean ± SD</td><td>30.00 ± 0.00</td><td>/</td><td>/</td></tr><tr><td>Age (years), range</td><td>/</td><td>/</td><td>/</td></tr><tr><td>Number of female patients, (%) Number of observations</td><td>0 (0.00%)</td><td>/</td><td>/</td></tr><tr><td>Observation,</td><td>2 4.8 ± 0.00</td><td>/ /</td><td>/</td></tr><tr><td rowspan="7">Dubin-Johnson and Rotor syndromes</td><td>mean ± SD (mg/dL)</td><td></td><td></td><td>/</td></tr><tr><td>Number of patients</td><td>7152</td><td>1280</td><td>3517</td></tr><tr><td>Age (years), mean ± SD</td><td>49.22 ± 11.94</td><td>47.69±12.29</td><td>48.01 ± 12.40</td></tr><tr><td>Age (years), range</td><td>18-65</td><td>18-65</td><td>18-65</td></tr><tr><td>Number of female patients, (%)</td><td>2825 (39.5%)</td><td>540 (42.2%)</td><td>1,1417 (40.3%)</td></tr><tr><td>Number of observations</td><td>52,761</td><td>2762</td><td>8819</td></tr><tr><td>Observation, mean ± SD (mg/dL)</td><td>8.02±7.84</td><td>2.61 ± 2.06</td><td>5.66 ±5.52</td></tr></table>

In Rotor syndrome, the Explorys data exhibit broad distribution; however, median UB, CB, and TB concentrations, as well as the CB ratio, align with the literature-reported means (Figure  3e–h). Population simulation predicts median CB and TB concentrations matching literature-reported means, while UB concentrations are lower but remain within the literature range. Some simulated CB ratios match the literature, although most simulation results cluster slightly at a higher range. In Rotor syndrome, the observed CB ratio is typically above 50% [33]. Based on sensitivity analysis of rate constants (Table  S4), MRP2 and OATP1B1-independent pathways primarily affect

CB and UB plasma levels in Rotor syndrome, respectively, suggesting that impaired hepatic uptake makes bilirubin disposition more dependent on passive diffusion and biliary excretion by MRP2.

## 3.2 | Other Disorders of Bilirubin Metabolism

Next, we investigated the functional consequences for various disorders of bilirubin metabolism, focusing on Gilbert syndrome, Crigler-Najjar syndrome, and Dubin-Johnson syndrome. In Gilbert syndrome and Crigler-Najjar syndrome, UGT1A1 activity is decreased, whereas MRP2 activity is reduced in Dubin-Johnson syndrome [5, 6]. A population simulation of 1000 individuals was performed, recalibrating only the mean $V _ { \mathrm { m a x } }$ of the affected enzyme or transporter for each disorder, focusing on the most affected bilirubin species, that is, UB for Gilbert syndrome and Crigler-Najjar syndrome, and CB for Dubin-Johnson syndrome. A geometric standard deviation of 1.6 [23] was applied to all $V _ { \mathrm { m a x } } .$ The results of population simulations for other disorders of bilirubin metabolism were compared to the bilirubin levels reported in the literature (Table  S5) and Explorys [10, 30, 37].

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
FIGURE 3 | Plasma unconjugated, conjugated, total bilirubin levels, and conjugated bilirubin ratio of population simulations in comparison to the literature and the Explorys data for the cohort of healthy bilirubin metabolism (a–d) and Rotor syndrome (e–h). These simulations were performed using the calibrated model without further parameter adjustment and therefore represent independent validation. For the healthy state, the literature means, ranges, and conjugated bilirubin ratio are reported in Muraca et al. [30]. For the Rotor syndrome, the literature means, ranges, and conjugated bilirubin ratio are reported in van de Steeg et al. [34].

For Gilbert syndrome, the mean $V _ { \mathrm { m a x } }$ of UGT1A1 was set to 4.60 μmol/L/min, which is 0.75% of the value in the healthystate reference model. Literature estimates UGT1A1 activity in Gilbert syndrome as 30%–50% of normal [38, 39]. Crigler-Najjar Type 2 is associated with UGT1A1 activity around 10% of the healthy reference [6, 39]. Crigler-Najjar Type 1, a more severe disorder, results from complete or near absence of UGT1A1. In our model, the mean $V _ { \mathrm { m a x } }$ of UGT1A1 for Crigler-Najjar syndrome was reduced to 0.55 μmol/L/min (0.09% of healthy-state value), which is consistent with literature [6]. In Dubin-Johnson syndrome, conjugated hyperbilirubinemia results from the absent or minimal MRP2 activity  [5, 6]. For the Dubin-Johnson syndrome, mean $V _ { \mathrm { m a x } }$ of MRP2 was decreased to 2.53 μmol/L/ min, representing 1.5% of the healthy-state value (Figure 4).

In Gilbert syndrome, the mean values in literature are reflected by the medians of the population simulation for UB, CB, and TB concentrations, as well as CB ratio (Figure  4a–d). In Explorys data, UB and TB align with the literature mean, while CB concentrations and ratios are higher than literature values. For UB, most of the concentrations from both Explorys and the population simulation remain within the literature-reported variation.

In Crigler-Najjar syndrome, the literature mean is well represented by the median of population simulation for all bilirubin concentrations and CB ratio (Figure 4e–h). The population simulations show a broad range of UB and TB levels, although Explorys data are limited to two TB measurements from the same patient, both below the literature mean. Sensitivity analysis of rate constants (Table  S4) shows that, in Gilbert and Crigler-Najjar syndromes, UB plasma levels are primarily influenced by UGT1A1, whereas CB levels are mostly affected by OATP1B1-mediated uptake. This indicates that under decreased UGT1A1 activity, the reduced conjugation rate is the major driver of UB accumulation, while OATP1B1 is the main pathway regulating CB levels.

For Dubin-Johnson syndrome, TB medians from both Explorys data and population simulations align with the literature mean (Figure  4i–l). The median of population simulation for CB matches the literature mean, whereas the median of the Explorys data is slightly higher. For UB, Explorys data and the literature mean are similar, while the simulation results are lower but still fall within the range of the Explorys data. The CB ratio is higher than the literature-reported mean for both Explorys data and the population simulation, while their peaks of the distributions are comparable. Sensitivity analysis of rate constants (Table S4) indicates that OATP1B1 pathway primarily affects plasma UB and CB levels in Dubin-Johnson syndrome, suggesting that impaired biliary excretion results in UB and CB levels being mainly influenced by hepatic uptake.

Overall, compared to real-world clinical data, population simulations reflect the central and most common values in clinical data, while real-world data generally show larger variability.

## 3.3 | Subject-Specific Bilirubin Profiles of Populations

To better understand individual-level bilirubin levels of these various populations, we examined absolute plasma concentrations of UB and CB for both real-world and simulated patients, underlying the ratios shown in Figures 3 and 4. This allows us to assess correlations between real-world UB and CB using linear regression in different states and to compare observed values with simulations.

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

(h)  
<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
FIGURE 4 | Plasma unconjugated, conjugated, total bilirubin levels, and conjugated bilirubin ratio of population simulations in comparison to the literature and the Explorys data for other disorders of bilirubin metabolism. Panels (a–d), (e–h), and (i–l) show the plasma bilirubin levels and conjugated bilirubin ratio in Gilbert syndrome, Crigler-Najjar syndrome, and Dubin-Johnson syndrome, respectively. For each disorder, only the $V _ { \mathrm { m a x } }$ of the affected enzyme or transporter was recalibrated to reproduce the levels of the most affected bilirubin species in each disorder (unconjugated bilirubin for Gilbert and Crigler-Najjar syndromes, conjugated bilirubin for Dubin-Johnson syndrome). The literature values are reported in Table S5 [10, 30, 37].

Figure 5 compares simulated and real-world CB versus UB levels under different conditions. In healthy individuals, CB and UB levels show a moderate positive correlation $\left( y = 0 . 3 9 x + 1 . 5 9 \right)$ , where small increases in UB are accompanied by a proportional rise in CB. In Rotor and Dubin-Johnson syndromes, both bilirubin species are elevated, with a stronger correlation $( y = 1 . 3 1 x + 2 9 . 9 9 )$ reflecting greater elevation of CB relative to UB. In Gilbert syndrome, UB levels are elevated, while CB remains low and weakly correlated $\left( y = 0 . 0 7 x + 1 0 . 4 1 \right)$ . The simulated individuals match the high-density regions of the real-world data although they do not capture the full observed variability.

## 3.4 | Atazanavir Administration in Healthy Individuals and Gilbert Syndrome

So far, only static cases have been considered with the physiologically based model. To illustrate its application for dynamic system-level perturbations, we simulated the time-dependent effect of atazanavir administration on time-concentration profiles of various bilirubin species. Atazanavir is an antiviral protease inhibitor used in the treatment of HIV [40]. It also inhibits UGT1A1 and OATP1B1, leading to hyperbilirubinemia in some patients [41]. Gilbert syndrome has been suggested as a potential risk factor for atazanavir-induced hyperbilirubinemia [41]. We here simulated the effect of atazanavir on a healthy individual compared to someone with Gilbert syndrome. The impact of 30-day atazanavir administration on plasma bilirubin levels in health and Gilbert syndrome is presented (Figure 6).

The results show that the atazanavir plasma concentration reached steady state within 30 days (Figure  6). In healthy individuals, UB $C _ { \mathrm { m a x } }$ increased by 34% and AUC by 15%, while remaining within the normal range [29]. In Gilbert syndrome, atazanavir caused a greater response in UB, increasing $C _ { \mathrm { m a x } }$ by 67% and AUC by 52%, while baseline UB levels were already above the normal range. In healthy individuals, CB $C _ { \mathrm { m a x } }$ and AUC rose by 50% and 25%, whereas individuals with Gilbert syndrome showed an elevation of 35% and 20%, respectively. In both individuals, CB was within the normal range [29]. Overall, the results indicate that atazanavir has a greater impact in Gilbert syndrome, potentially posing a clinical risk.

## 4 | Discussion

This study developed a physiologically based computational model simulating bilirubin metabolism in both healthy individuals and patients with disorders of bilirubin metabolism. The model involves key processes, including hepatic uptake of bilirubin, its conjugation, and its biliary excretion. It accurately replicated healthy plasma bilirubin levels and urinary excretion. However, the fecal excretion rate was overestimated. This discrepancy may reflect the variability in fecal excretion rates, affected by diet or bowel habits [35]. For Rotor syndrome, the plasma bilirubin levels with the typical pattern of limited increase in UB and a larger elevation in CB were reproduced.

(a)  
Healthy Conjugated vs. Unconjugated Bilirubin  
<!-- image-->  
(b)

Rotor Syndrome and Dubin Johnson Syndrome Conjugated vs. Unconjugated Bilirubin  
<!-- image-->  
(c)

Gilbert Syndrome Conjugated vs. Unconjugated Bilirubin  
<!-- image-->  
(d)

Crigler Najjar Syndrome Conjugated vs. Unconjugated Bilirubin  
<!-- image-->  
FIGURE 5 | Conjugated versus unconjugated bilirubin concentrations for individual patients. Panels (a–c) show both conjugated and unconjugated bilirubin levels of individuals from real-world clinical data (blue) and from simulations (yellow and red) representing healthy individuals, Rotor and Dubin-Johnson syndromes, and Gilbert syndrome, respectively. Rotor and Dubin-Johnson syndromes are shown in the same panel as they share the same ICD-10 code in the Explorys database. Panel (d) shows only the simulated bilirubin levels of patients with Crigler-Najjar syndrome since there is no Explorys data available. Dashed line represents the identity line, and the solid line represents the linear regression of real-world clinical data, with the corresponding equation provided in the legend.

Besides individual simulations of healthy reference and Rotor syndrome, a virtual population of 1000 individuals was simulated. Incorporating real-world clinical data, the study also reveals alterations in various disorders and allows comparisons with controlled-study values, showing less variability than clinical data. Moreover, our dynamic model enabled simulation of atazanavirinduced bilirubin changes, demonstrating its potential relevance for assessing risk in individuals with impaired bilirubin metabolism. For the disease-specific virtual populations, $V _ { \mathrm { m a x } }$ of the affected enzyme/transporter was scaled to reproduce characteristic bilirubin profiles. This top-down $V _ { \mathrm { m a x } }$ scaling is appropriate because each disorder is predominantly driven by a single enzymatic or transporter defect altering bilirubin kinetics [5, 6, 34, 42].

Comparison with the model of Levitt and Levitt [10] shows both consistencies and differences in bilirubin predictions across different conditions (Table S6). Our model is a whole-body dynamic framework that can simulate dynamic perturbations such as drug-induced hyperbilirubinemia, whereas Levitt and Levitt's model is a steady-state framework focused primarily on clinical bilirubin measurements. Both models capture baseline bilirubin in healthy individuals, with our population simulation yielding a higher median for CB. In disorders, both models reproduce expected trends, but in some cases differ quantitatively.

In a previous publication by Dong et al. [12] hyperbilirubinemia was analyzed as a result of UGT1A1 and OATP1B1/3 inhibition by atazanavir. For their study, the authors used a PBPK model which represented bilirubin synthesis through intravenous infusions. In this earlier work, different UGT1A1 phenotypes (extensive, intermediate and poor metabolizers, respectively) were considered instead of disease-specific populations. The different UGT1A1 metabolizer phenotypes in the publication by Dong et al. have been identified from three specific total bilirubin baseline levels. Also, the liver was modeled as a permeability-limited tissue and the published renal clearance rate for CB as well as in vitro UGT1A1 kinetics for UB were used as inputs for the elimination [12]. In contrast, our model accounts for both passive and active hepatic uptake, which is consistent with evidence for combined OATP1B1/3- mediated and passive transport [43, 44]. Moreover, in our model we assumed competitive inhibition between UB and CB for OATP1B1, supported by a rise in UB observed in CB pathologies [10]. Interestingly, the simulations in the publication by Dong et al. show larger effects on total bilirubin as well as an increase in unconjugated bilirubin after administration of atazanavir [12]. A major difference to the previous work is that in our model UGT1A1 activity in Gilbert syndrome only represents 0.75% of the healthy reference. Since the UGT1A1 phenotypes in Dong et  al. have a much larger activity, this could explain the lower sensitivity of our model towards atazanavir-mediated inhibition.

(a)  
<!-- image-->

(b)  
<!-- image-->

(c)  
<!-- image-->

d)Unconjugated Bilirubin:
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Cmax[μM]</td><td rowspan=1 colspan=1>Cmax[Fold ofRef.]</td><td rowspan=1 colspan=1>AUC[μM·h]</td><td rowspan=1 colspan=1>AUC[Fold ofRef.]</td></tr><tr><td rowspan=1 colspan=1>Healthy</td><td rowspan=1 colspan=1>4.80</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>3460.15</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>Gilbert</td><td rowspan=1 colspan=1>28.32</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>20394.43</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>Healthy + ATZ</td><td rowspan=1 colspan=1>6.45</td><td rowspan=1 colspan=1>1.34</td><td rowspan=1 colspan=1>3979.26</td><td rowspan=1 colspan=1>1.15</td></tr><tr><td rowspan=1 colspan=1>Gilbert + ATZ</td><td rowspan=1 colspan=1>47.36</td><td rowspan=1 colspan=1>1.67</td><td rowspan=1 colspan=1>30949.79</td><td rowspan=1 colspan=1>1.52</td></tr></table>

(e)Conjugated Bilirubin:
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Cmax[μM]</td><td rowspan=1 colspan=1>Cmax[Fold ofRef.]</td><td rowspan=1 colspan=1>AUC[μM·h]</td><td rowspan=1 colspan=1>AUC[Fold ofRef.]</td></tr><tr><td rowspan=1 colspan=1>Healthy</td><td rowspan=1 colspan=1>0.62</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>445.17</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>Gilbert</td><td rowspan=1 colspan=1>0.62</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>445.23</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>Healthy + ATZ</td><td rowspan=1 colspan=1>0.93</td><td rowspan=1 colspan=1>1.50</td><td rowspan=1 colspan=1>554.92</td><td rowspan=1 colspan=1>1.25</td></tr><tr><td rowspan=1 colspan=1>Gilbert + ATZ</td><td rowspan=1 colspan=1>0.84</td><td rowspan=1 colspan=1>1.35</td><td rowspan=1 colspan=1>536.80</td><td rowspan=1 colspan=1>1.20</td></tr></table>

FIGURE 6 | Simulated plasma bilirubin levels following atazanavir administration in a healthy individual and an individual with Gilbert syndrome. Panel (a) shows the simulated plasma atazanavir concentration. Panels (b, c) show the simulated plasma unconjugated and conjugated bilirubin levels in a healthy individual and an individual with Gilbert syndrome. Dashed lines indicate the bilirubin concentrations prior to atazanavir administration. Panels (d, e) show the maximum concentration $( C _ { \mathrm { m a x } } )$ and area under the curve (AUC) in both individuals, presented in absolute units and as fold-change relative to each individual's baseline model.

Our model describes the various syndromes of bilirubin metabolism mechanistically. Furthermore, our work is the first study on modeling of bilirubin metabolism to systematically compare simulation results with real-world data. Moreover, this is also the first whole-body model capable of describing time-resolved experimental data with labeled bilirubin.

Despite reasonably representing the bilirubin metabolism across different disorders, the model has some limitations. Most urobilinogen is oxidized to stercobilin for fecal excretion, with a smaller fraction forming urobilin excreted in urine. To avoid unnecessary model complexity, stercobilin and urobilin are represented as urobilinogen, with adjusted lipophilicity and solubility to match reported excretion rate. Additionally, data comparability across different institutions in the Explorys database presents another challenge. Although real-world data provides insights into the population-level variability, it may not always align with controlled clinical studies due to heterogeneity in data sources. Differences in protocols, lab methods, and recording standards may introduce inconsistencies in bilirubin data. Lastly, ICD-10 codes were used to identify the disorders of bilirubin metabolism. However, Rotor syndrome and Dubin-Johnson syndrome share the same code. While the cohort may include both, given the rarity of Rotor syndrome (0.0001% prevalence) [45], the cohort likely consists mainly of individuals with Dubin-Johnson syndrome.

Future work could extend the model to liver diseases like cirrhosis or cholestasis to study effects on bilirubin kinetics. Additionally, the model could also assess risks of complications like kernicterus in various pathological states.

In conclusion, this study presents a physiologically based computational model simulating bilirubin metabolism in healthy individuals and patients with bilirubin metabolism disorders. Disorders are represented by adjusting parameters from the healthy reference model. Using clinical and literature data, the model allows functional analyses across different conditions, despite some deviations in fecal excretion rates in the healthy state. Furthermore, its dynamic nature enables simulation of drug effects on bilirubin levels, allowing potential assessment of hyperbilirubinemia risk in high-risk cohorts under various conditions.

## Author Contributions

A.Z.S. and L.K. wrote the manuscript and designed the research. A.Z.S.   
performed the research and analyzed the data.

## Acknowledgment

Open Access funding enabled and organized by Projekt DEAL.

## Funding

This study was funded by the German Federal Ministry of Research, Technology and Space (BMFTR), grant number 03LW0304K.

## Conflicts of Interest

The authors declare no conflicts of interest.

## References

1. D. S. Pratt, “Chapter  73 – Liver Chemistry and Function Tests,” in Sleisenger and Fordtran's Gastrointestinal and Liver Disease, 9th ed., ed. M. Feldman, L. S. Friedman, and L. J. Brandt (W.B. Saunders, 2010), 1227–1237.e2.

2. S. B. Amin, “Narrative Review of Bilirubin Measurement and Binding,” Pediatric Medicine 4 (2021): 4.

3. J. F. Creeden, D. M. Gordon, D. E. Stec, and T. D. Hinds, Jr., “Bilirubin as a Metabolic Hormone: The Physiological Relevance of Low Levels,”

American Journal of Physiology. Endocrinology and Metabolism 320, no. 2 (2021): E191–e207.

4. E. Kuntz and H.-D. Kuntz, Hepatology Textbook and Atlas: History, Morphology, Biochemistry, Diagnostics, Clinic, Therapy, 3rd ed. (Springer, 2008).

5. J. M. Ascher Bartlett and J. Shah, “Disorders of Bilirubin Metabolism,” in Benign Hematologic Disorders in Children: A Clinical Guide, ed. D. M. Kamat and M. Frei-Jones (Springer International Publishing, 2021), 353–365.

6. S. Erlinger, I. M. Arias, and D. Dhumeaux, “Inherited Disorders of Bilirubin Transport and Conjugation: New Insights Into Molecular Mechanisms and Consequences,” Gastroenterology 146, no. 7 (2014): 1625–1638.

7. A. I. Pranty, S. Shumka, and J. Adjaye, “Bilirubin-Induced Neurological Damage: Current and Emerging iPSC-Derived Brain Organoid Models,” Cells 11, no. 17 (2022): 2647.

8. P. D. Berk, R. B. Howe, J. R. Bloomer, and N. I. Berlin, “Studies of Bilirubin Kinetics in Normal Adults,” Journal of Clinical Investigation 48, no. 11 (1969): 2176–2190.

9. C. Cobelli, M. Frezza, and C. Tiribelli, “Modeling, Identification and Parameter Estimation of Bilirubin Kinetics in Normal, Hemolytic and Gilbert's States,” Computers and Biomedical Research 8, no. 6 (1975): 522–537.

10. D. G. Levitt and M. D. Levitt, “Development of a Pharmacokinetic Model That Accounts for the Plasma Concentrations of Conjugated and Unconjugated Bilirubin Observed in a Variety of Disease States,” Clinical and Experimental Gastroenterology 16 (2023): 277–289.

11. K. Yang, C. Battista, J. L. Woodhead, et al., “Systems Pharmacology Modeling of Drug-Induced Hyperbilirubinemia: Differentiating Hepatotoxicity and Inhibition of Enzymes/Transporters,” Clinical Pharmacology and Therapeutics 101, no. 4 (2017): 501–509.

12. J. Dong, P. Sharma, R. Emara, et  al., “Inhibition of OATP1B1/3 Rather Than UGT1A1 May be the Major Cause of the Bilirubin Elevation After Atazanavir Administration,” Clinical Pharmacology & Therapeutics 118, no. 2 (2025): 497–509.

13. L. Kuepfer, C. Niederalt, T. Wendl, et al., “Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model,” CPT: Pharmacometrics & Systems Pharmacology 5, no. 10 (2016): 516–531.

14. V. Baier, H. Cordes, C. Thiel, et  al., “A Physiology-Based Model of Human Bile Acid Metabolism for Predicting Bile Acid Tissue Levels After Drug Administration in Healthy Subjects and BRIC Type 2 Patients,” Frontiers in Physiology 10 (2019): 1192.

15. B. Kister, A. Viehof, U. Rolle-Kampczyk, et  al., “A Physiologically Based Model of Bile Acid Metabolism in Mice,” iScience 26, no. 10 (2023): 107922.

16. P. Kalra, J. Brandl, T. Gaub, et al., “Quantitative Systems Pharmacology of Interferon Alpha Administration: A Multi-Scale Approach,” PLoS One 14, no. 2 (2019): e0209587.

17. Merative, “MarketScan Explorys Database,” https://www.merative. com/real-world-evidence/real-world-data-analytics.

18. J. H. Chang, E. Plise, J. Cheong, Q. Ho, and M. Lin, “Evaluating the In Vitro Inhibition of UGT1A1, OATP1B1, OATP1B3, MRP2, and BSEP in Predicting Drug-Induced Hyperbilirubinemia,” Molecular Pharmaceutics 10, no. 8 (2013): 3067–3075.

19. S. Willmann, J. Lippert, M. Sevestre, J. Solodenko, F. Fois, and W. Schmitt, “PK-Sim: A Physiologically Based Pharmacokinetic ‘Whole-Body’ Model,” Biosilico 1, no. 4 (2003): 121–124.

20. A. Rohatgi, “WebPlotDigitizer,” Version 4.7, https://automeris.io.

21. J. R. Bloomer, P. D. Berk, R. B. Howe, J. G. Waggoner, and N. I. Berlin, “Comparison of Fecal Urobilinogen Excretion With Bilirubin

Production in Normal Volunteers and Patients With Increased Bilirubin Production,” Clinica Chimica Acta 29, no. 3 (1970): 463–471.

22. S. Willmann, K. Höhn, A. Edginton, et  al., “Development of a Physiology-Based Whole-Body Population Model for Assessing the Influence of Individual Variability on the Pharmacokinetics of Drugs,” Journal of Pharmacokinetics and Pharmacodynamics 34, no. 3 (2007): 401–431.

23. J. Beal, “Biochemical Complexity Drives Log-Normal Variation in Genetic Expression,” Engineering Biology 1, no. 1 (2017): 55–60.

24. S. F. André Dallmann, “Atazanavir Model,” 2020, https://github. com/Open-Systems-Pharmacology/Atazanavir-Model?tab=readm e-ov-file.

25. O. Briz, M. A. Serrano, M. I. RI, J. Gonzalez-Gallego, and J. J. Marin, “Role of Organic Anion-Transporting Polypeptides, OATP-A, OATP-C and OATP-8, in the Human Placenta-Maternal Liver Tandem Excretory Pathway for Foetal Bilirubin,” Biochemical Journal 371, no. Pt 3 (2003): 897–905.

26. D. Keppler, “The Roles of MRP2, MRP3, OATP1B1, and OATP1B3 in Conjugated Hyperbilirubinemia,” Drug Metabolism and Disposition 42, no. 4 (2014): 561–565.

27. Y. Cui, J. König, I. Leier, U. Buchholz, and D. Keppler, “Hepatic Uptake of Bilirubin and Its Conjugates by the Human Organic Anion Transporter SLC21A6,” Journal of Biological Chemistry 276, no. 13 (2001): 9626–9630.

28. D. G. Levitt and M. D. Levitt, “Quantitative Assessment of the Multiple Processes Responsible for Bilirubin Homeostasis in Health and Disease,” Clinical and Experimental Gastroenterology 7 (2014): 307–328.

29. B. T. Doumas and T. W. Wu, “The Measurement of Bilirubin Fractions in Serum,” Critical Reviews in Clinical Laboratory Sciences 28, no. 5–6 (1991): 415–445.

30. M. Muraca, J. Fevery, and N. Blanckaert, “Relationships Between Serum Bilirubins and Production and Conjugation of Bilirubin: Studies in Gilbert's Syndrome, Crigler-Najjar Disease, Hemolytic Disorders, and Rat Models,” Gastroenterology 92, no. 2 (1987): 309–317.

31. C. J. Watson, “Proceedings of the Ninth Congress of the European Society of Haematology,” American Journal of Clinical Pathology 43 (1963): 817.

32. C. Ha and N. V. Bhagavan, “Hemoglobin and Metabolism of Iron and Heme,” in Essentials of Medical Biochemistry (Academic Press, 2023), 573–611.

33. T. Namihisa and K. Yamaguchi, “The Constitutional Hyperbilirubinemia in Japan Studies on the 139 Cases Reported During the Period From 1963 to 1969,” Gastroenterologia Japonica 8, no. 4 (1973): 311–321.

34. E. van de Steeg, V. Stránecký, H. Hartmannová, et  al., “Complete OATP1B1 and OATP1B3 Deficiency Causes Human Rotor Syndrome by Interrupting Conjugated Bilirubin Reuptake Into the Liver,” Journal of Clinical Investigation 122, no. 2 (2012): 519–528.

35. N. F. Maclagan, “Faecal Urobilinogen; Clinical Evaluation of a Simplified Method of Estimation,” British Journal of Experimental Pathology 27, no. 3 (1946): 190–200.

36. C. J. Watson, “Studies of Urobilinogen: II. Urobilinogen in the Urine and Feces of Subjects Without Evidence of Disease of the Liver or Biliary Tract,” Archives of Internal Medicine 59, no. 2 (1937): 196–205.

37. M. Shani, U. Seligsohn, E. Gilon, C. Sheba, and A. Adam, “Dubin-Johnson Syndrome in Israel: I. Clinical, Laboratory, and Genetic Aspects of 101 Cases,” QJM: An International Journal of Medicine 39, no. 4 (1970): 549–567.

38. P. J. Bosma, J. R. Chowdhury, C. Bakker, et al., “The Genetic Basis of the Reduced Expression of Bilirubin UDP-Glucuronosyltransferase 1 in Gilbert's Syndrome,” New England Journal of Medicine 333, no. 18 (1995): 1171–1175.

39. N. Memon, B. I. Weinberger, T. Hegyi, and L. M. Aleksunes, “Inherited Disorders of Bilirubin Clearance,” Pediatric Research 79, no. 3 (2016): 378–386.

40. D. S. Wishart, Y. D. Feunang, A. C. Guo, et al., “DrugBank 5.0: A Major Update to the DrugBank Database for 2018,” Nucleic Acids Research 46, no. D1 (2018): D1074–D1082.

41. T. O. Lankisch, U. Moebius, M. Wehmeier, et al., “Gilbert's Disease and Atazanavir: From Phenotype to UDP-Glucuronosyltransferase Haplotype,” Hepatology 44, no. 5 (2006): 1324–1332.

42. C. P. Strassburg, “Hyperbilirubinemia Syndromes (Gilbert-Meulengracht, Crigler-Najjar, Dubin-Johnson, and Rotor Syndrome),” Best Practice & Research Clinical Gastroenterology 24, no. 5 (2010): 555–571.

43. S. D. Zucker, W. Goessling, and A. G. Hoppin, “Unconjugated Bilirubin Exhibits Spontaneous Diffusion Through Model Lipid Bilayers and Native Hepatocyte Membranes,” Journal of Biological Chemistry 274, no. 16 (1999): 10852–10862.

44. A. F. McDonagh, “Movement of Bilirubin and Bilirubin Conjugates Across the Placenta,” Pediatrics 119, no. 5 (2007): 1032–1033, author reply 1033.

45. J. Roy-Chowdhury and N. Roy-Chowdhury, “Bilirubin Metabolism and Its Disorders,” in Zakim and Boyer's Hepatology, 7th ed., ed. A. J. Sanyal, T. D. Boyer, K. D. Lindor, and N. A. Terrault (Elsevier, 2018), 898–925.e8.

## Supporting Information

Additional supporting information can be found online in the Supporting Information section. Data S1: psp470183-sup-0001-DataS1. zip.