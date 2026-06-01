https://doi.org/10.1038/s44259-026-00197-5

# Mechanistic insights into plasmid transfer inhibition in Enterobacterales by nucleoside analogues

Check for updates

Ilyas Alav1,2, Ayesha Ashraf1 , Parisa Pordelkhaki1 & Michelle M. C. Buckner1

Antimicrobial resistance (AMR) poses a major global health threat, with carbapenem-resistant and extended-spectrum β-lactamase (ESBL)-producing Enterobacterales causing widespread infections and deaths. Much of this resistance spreads through conjugative plasmids, autonomously replicating mobile genetic elements that transfer between bacteria and carry multiple AMR genes. Targeting plasmid conjugation could therefore help curb the spread of AMR. In this study, we tested whether clinically approved nucleoside analogues (NAs) inhibited the transfer of the GFP-tagged ESBLencoding IncK plasmid pCTgfp in Escherichia coli and the carbapenemase-encoding IncF plasmid pKpQILgfp in Klebsiella pneumoniae using flow cytometry. Alongside the known inhibitor azidothymidine (AZT), didanosine, stavudine, and trifluridine reduced plasmid conjugation in both species without affecting growth. Conversely, famciclovir and zalcitabine promoted pCTgfp conjugation in E. coli, while aciclovir and valaciclovir enhanced pKpQILgfp conjugation in K. pneumoniae. Mechanistic studies showed that plasmid conjugation-promoting NAs altered intracellular ATP levels. RNA sequencing revealed that AZT downregulated the expression of genes linked to motility in E. coli. Genetic inactivation of motility in E. coli mirrored the decrease in pCTgfp conjugation, like AZT. In K. pneumoniae, AZT upregulated genes linked to DNA damage and the SOS response, but downregulated methionine biosynthesis and metabolism genes. The exogenous addition of zinc acetate to inhibit RecA or the end product of methionine metabolism, S-adenosylmethionine, restored pKpQILgfp conjugation in K. pneumoniae. Overall, our results indicated that existing NAs, including AZT, represent structural scaffolds for the development of potent conjugation inhibitors and highlight motility, DNA repair, and methionine metabolism as potential key factors in plasmid conjugation.

Antimicrobial resistance (AMR) in bacterial pathogens is a major global public health issue. Specifically, carbapenem-resistant and extendedspectrum β-lactamase (ESBL)-producing Enterobacterales are classified as critical priority pathogens by the World Health Organisation for research, development, and public health initiatives1 . Within Enterobacterales, Escherichia coli and Klebsiella pneumoniae strains were estimated to be responsible for most human mortality attributed to antibiotic resistance in 20192 . Most AMR genes (ARGs) in K. pneumoniae and E. coli are found on mobile genetic elements, including conjugative plasmids that often carry multiple ARGs, resulting in multidrug resistance3–5 . Conjugative plasmids can replicate and transfer autonomously, thereby facilitating the dissemination of AMR genes throughout bacterial populations6,7 .

Several characteristics of conjugative plasmids enable their dissemination and persistence in bacterial populations. For example, the CTX-M-14 ESBL-encoding IncK plasmid pCT has a low fitness cost on its host, can persist in the presence or absence of antibiotic selective pressure, and is readily transmitted between bacteria8,9 . This is also the case for carbapenemase-encoding IncF plasmids, such as pKpQIL and pCPE16_3, that transfer at high frequencies in K. pneumoniae strains 10,11 . Plasmidmediated transmission of ARGs occurs in clinical environments, often resulting in hospital outbreaks of carbapenemase-producing

Enterobacterales (CPE). For example, in a retrospective study of public Singaporean hospitals involving 779 patients and 1215 CPE isolates, 50% of CPE dissemination was due to plasmid-mediated transmission of ARGs12. Similar findings have been reported across the world, such as in Thailand, the US, and the UK13–15, highlighting the global problem of plasmidmediated spread of ARGs. Notably, the otherwise promising β-lactam/ β-lactamase inhibitor combinations, such as ceftazidime/avibactam and piperacillin/tazobactam, have been shown to be ineffective against K. pneumoniae strains carrying variants of pKpQIL plasmids16,17. Therefore, there is an urgent unmet need for alternative strategies to tackle AMR, such as targeting AMR plasmids.

One approach to target AMR plasmids is the development and use of anti-plasmid compounds18. These may alter the stability of AMR plasmids, entirely remove the plasmid (plasmid curing), or impair the dissemination of AMR genes by inhibiting horizontal gene transfer, such as bacterial conjugation19. A range of compounds exhibiting variable anti-plasmid activity have been identified, such as unsaturated fatty acids, natural products, and clinically approved drugs20–22. To date, the use of anti-plasmid compounds is in early stages with none having been approved for clinical use. Previous work by our group identified two nucleoside analogues (NAs) as novel anti-plasmid agents: abacavir and azidothymidine (AZT). In particular, AZT significantly reduced the transmission of pCTgfp in E. coli and pKpQILgfp in K. pneumoniae at below peak serum concentrations, without affecting bacterial growth21.

In this study, we explored whether a range of clinically approved nucleoside analogues modulated plasmid transmission in E. coli and K. pneumoniae. We found that famciclovir and zalcitabine promoted the conjugation frequency of the ESBL-encoding IncK plasmid pCT in Escherichia coli, and aciclovir and valaciclovir promoted the conjugation frequency of the carbapenemase-encoding IncF plasmid pKpQIL in Klebsiella pneumoniae. We identified three additional nucleoside analogues, didanosine, stavudine, and trifluridine, that reduced the conjugation frequencies of pCT in E. coli and pKpQIL in K. pneumoniae. As AZT showed the most potent activity, we explored the mechanism by which AZT reduced plasmid conjugation in E. coli and K. pneumoniae. RNA sequencing revealed that AZT significantly reduced the expression of motility genes in E. coli, and DNA repair pathway genes and methionine metabolism genes in K. pneumoniae. In phenotypic testing, this translated to a reduction in pCTgfp conjugation frequency in E. coli through inhibition of motility. In K. pneumoniae, addition of zinc acetate, which reversed recA expression, or Sadenosyl-methionine, which restored depleted levels, reversed AZTmediated reduction in pKpQILgfp conjugation frequency. Our work highlights the potential use of clinically approved NAs as structural scaffolds for the development of novel plasmid transmission inhibitors and sheds light onto the complex mechanism by which AZT reduces plasmid conjugation.

## Results

## Screening of clinically approved nucleoside analogues for plasmid transmission inhibitors

To identify additional nucleoside analogues (NAs) as potential plasmid transmission inhibitors, 14 clinically approved NAs were screened using flow cytometry. Firstly, the minimum inhibitory concentration (MIC) of all NAs for the E. coli EC958 and K. pneumoniae Ecl8 strains was determined. The MICs of almost all NAs were greater than 256 µg/mL, except for azidothymidine (AZT) and didanosine, which had MICs of 2 and 128 µg/mL, respectively (Supplementary Table 1). Accordingly, all NAs, except AZT, were tested at 1, 10 and 100 µg/mL for the initial flow cytometry screening of plasmid inhibition activity. Previously, we found AZT to be effective at reducing plasmid transmission at concentrations as low as 0.008 µg/mL21, therefore, this concentration was used throughout. As expected, 0.008 µg/mL AZT significantly reduced transmission of pCTgfp in E. coli and pKpQILgfp in K. pneumoniae. Most of the NAs at the tested concentrations did not significantly affect pCTgfp and pKpQILgfp transmission (Supplementary Fig. 1). Notably, didanosine reduced the transmission of both pCTgfp in E. coli and pKpQILgfp in K. pneumoniae at 10 and 100 µg/mL, and stavudine and trifluridine reduced plasmid transmission at 100 µg/mL (Supplementary Fig. 1). Conversely, 10 and 100 µg/mL aciclovir and 1, 10 and 100 µg/mL valaciclovir significantly increased pKpQILgfp transmission in K. pneumoniae (Supplementary Fig. 1). In E. coli, 1, 10 or 100 µg/mL famciclovir or zalcitabine significantly increased pCTgfp transmission (Supplementary Fig. 1). Therefore, from the initial screen, didanosine, stavudine, and trifluridine were selected for further investigation to narrow down the lowest concentration at which plasmid transmission was inhibited. Aciclovir, famciclovir, valaciclovir, and zalcitabine were also selected for further investigation as they significantly increased plasmid transmission. The chemical structures of the nucleoside analogues that reduced and promoted plasmid transfer are illustrated in Supplementary Fig. 2.

## Didanosine, stavudine, and trifluridine reduced the conjugation of pCT and pKpQIL

gfp gfpTo determine the lowest concentration of didanosine, stavudine, and trifluridine that reduced plasmid conjugation, a range of concentrations between 10 and 100 µg/mL was tested (10, 25, 40, 55, 70, 85, and 100 µg/ mL). In E. coli, didanosine significantly reduced the conjugation frequency (CF) of pCTgfp starting at 10 µg/mL, with slightly further reductions at 25 µg/mL and above compared to DMSO control (Fig. 1). For stavudine and trifluridine, 10 µg/mL was also the lowest concentration that significantly reduced the CF of pCTgfp in E. coli (Fig. 1). For famciclovir, 100 µg/mL significantly increased the CF of pCTgfp, whilst 1, 10 and 100 µg/mL zalcitabine significantly increased the CF of pCTgfp (Fig. 1). The growth and mean generation times of the E. coli strains EC24 and EC25 grown in LB broth supplemented with 0.008 µg/mL azidothymidine, 10 µg/mL didanosine, 25 µg/mL stavudine, 25 µg/mL trifluridine, 100 µg/mL zalcitabine or 100 µg/mL famciclovir were not significantly different to the DMSO vehicle control (Supplementary Figs. 3 and 5). Therefore, these concentrations, which impacted CF without affecting growth, were selected for E. coli mechanism of action investigations.

In K. pneumoniae, 10 µg/mL didanosine, stavudine, and trifluridine significantly reduced the CF of pKpQILgfp compared to DMSO control (Fig. 2). However, since 10 µg/mL stavudine had no effect on pKpQILgfp transmission in the preliminary screen (Supplementary Fig. 1), 25 µg/mL was selected for downstream experiments. At 1, 10 and 100 µg/mL, both aciclovir or valaciclovir significantly increased the CF of pKpQILgfp compared to the DMSO control (Fig. 2). The growth and mean generation times of the K. pneumoniae strains KP18 and KP19 grown in LB broth supplemented with 0.008 µg/mL azidothymidine, 10 µg/mL didanosine, 25 µg/mL stavudine, 25 µg/mL trifluridine, 100 µg/mL valaciclovir or 100 µg/mL aciclovir, were not significantly different to DMSO vehicle control (Supplementary Figs. 3 and 5), indicating no impact on growth. Therefore, these concentrations were selected to be used in the mechanism of action investigations for K. pneumoniae.

## Impact of nucleoside analogues on bacterial physiology

Compounds that affect plasmid conjugation have been reported to influence various aspects of bacterial physiology, including membrane permeability and potential, reactive oxygen species (ROS) generation, and ATP synthesis23. To that end, we investigated the impact of NAs on some of these processes. Since the donor strains in our assays carried conjugative AMR plasmids tagged with GFP, luminescence-based assays were used to measure ROS levels and ATP content, as commercially available dyes for ROS or ATP detection have overlapping wavelengths with GFP. The bacterial strains were treated with the NAs for the same timeframe and conditions as per the conjugation assays. The treatment of the donor E. coli strain EC24 and the donor K. pneumoniae strain KP19 with the NAs for 4 h did not significantly affect ROS levels, whilst the positive control of 50 µM menadione significantly increased ROS levels, compared to DMSO control (Fig. 3A, B). Conjugative plasmid transmission is mediated by type IV secretion systems, which require ATP to function24. Therefore, we

Fig. 1 | The effect of selected nucleoside analogues (NAs) from the initial screen on pCT congfpjugation in   EC958. The conjugation frequency (CF) of pCTgfp from EC24 (E. coli EC958/pCTgfp) to EC25 (E. coli EC958 mCherry ) in the presence of A didanosine, B stavudine, C trifluridine, D zalcitabine, and E famciclovir. The CF of $\mathsf { p C T } g f \bar { p }$ was determined as the number of transconjugants divided by the number of recipient cells. Data presented are the mean ± standard deviation of three independent experiments, each consisting of four biological replicates. The CF of pCTgfp treated with DMSO was compared to those treated with the NAs using one-way ANOVA, followed by the Dunnett ’s test to correct for multiple comparisons. Signi ficantly different results are indicated with $^ { * } \left( P \leq 0 . 0 5 \right) ^ { * * } \left( P \leq 0 . 0 1 \right)$ $\mathrm { o r } ^ { * * * } \left( P < 0 . 0 0 1 \right)$ . ns not signi ficant.

Fig. 2 | The effect of selected nucleoside analogues (NAs) from the initial screen on pKpQIL congfpjugation in  Ecl8. The con-Klebsiella pneumoniaejugation frequency (CF) of pKpQILgfp from KP19 (K. pneumoniae Ecl8/pKpQILgfp) to KP18 (K. pneumoniae Ecl8 mCherry) in the presence of A didanosine, B stavudine, C trifluridine, D valaciclovir, and E aciclovir. The CF of pKpQILgfp was determined as the number of transconjugants divided by the number of recipient cells. Data presented are the mean ± standard deviation of three independent experiments, each consisting of four biological replicates. The CF of pKpQILgfp treated with DMSO was compared to those treated with the NAs using one-way ANOVA, followed by Dunnett’s test to correct for multiple comparisons. Signi ficantly different results are indicated with $^ { * } _ { } \left( { P } _ { } \leq 0 . 0 5 \right) ^ { * * } ( { P } _ { } \leq 0 . 0 1 ) , \mathrm { o r } ^ { * * * } \left( { P } _ { } < 0 . 0 0 1 \right)$ . ns, not signi ficant.

A  
<!-- image-->

B  
<!-- image-->

C  
<!-- image-->

D  
<!-- image-->

E  
<!-- image-->

A  
<!-- image-->

B  
<!-- image-->

C  
<!-- image-->  
D

<!-- image-->  
E

<!-- image-->

Fig. 3 | The effect of nucleoside analogues (NAs) on reactive oxygen species levels and ATP content in  EC958/pCT and Ecl8/pKpQIL The level of reactive oxygen species was measured by ROS-Glo H2O2 Assay Kit in A K. pneumoniae Ecl8/pKpQILgfp and B E. coli EC958/pCTgfp, following treatment with the indicated concentrations of NAs or 50 µM menadione as positive control for 4 h. Bacterial cells treated with vehicle control (1% DMSO) were used as negative control. The total intracellular ATP content was measured by BacTiter-Glo Microbial Cell Viability Assay Kit in C E. coli EC958/pCTgfp and D K. pneumoniae Ecl8/pKpQILgfp, following treatment with the indicated concentrations of NAs or 2 µg/mL doripenem as a positive control for 4 h. Bacterial cells treated with vehicle control (1% DMSO) were used as a negative control. For both assays, the data presented are the mean ± standard deviation of ROS levels or ATP content in treated bacteria relative to the DMSO control, tested in three independent experiments, each comprising a biological replicate tested in triplicate. Statistical significance was determined by comparing relative ROS levels or ATP content in treated bacteria to the DMSO control by one-way ANOVA, followed by Dunnett’s test to correct for multiple comparisons. Significantly different results are indicated with \* (P ≤ 0.05), \*\* (P < 0.01), or \*\*\* (P < 0.001). ns, not significant.  
A  
<!-- image-->

C  
B  
<!-- image-->

<!-- image-->

D  
<!-- image-->

investigated whether any of the NAs affected ATP generation in the donor strains. As a positive control, 2 µg/mL doripenem was used as it is bactericidal and caused a severe reduction in ATP content due to cell death (Fig. 3B, D). In K. pneumoniae Ecl8/pKpQILgfp, most of the NAs did not significantly impact ATP content following treatment for 4 h. However, 100 µg/mL valaciclovir caused a modest yet significant reduction in ATP content (Fig. 3C). In E. coli EC958/pCTgfp, 100 µg/mL famciclovir, 25 µg/ mL trifluridine, and 100 µg/mL zalcitabine significantly reduced ATP content after 4 h (Fig. 3D).

Next, we explored the impact of the NAs on membrane permeability and potential. To measure outer membrane permeability, we used the dye NPN (N-phenyl-1-naphthylamine), a hydrophobic fluorescent dye that is normally excluded by the intact outer membrane but displays increased fluorescence upon partitioning into compromised membranes. The detergent sodium dodecyl sulphate (SDS) was used as a positive control, as it is a well-known membrane permeabilizing agent. As expected, 0.125% SDS significantly increased outer membrane permeability in both E. coli/pCTgfp and K. pneumoniae/pKpQILgfp (Fig. 4A, B). However, none of the NAs significantly affected NPN fluorescence in both species, indicating a lack of outer membrane permeabilising effects by the NAs (Fig. 4A, B). To measure inner membrane permeability, we used propidium iodide (PI), a fluorescent dye that cannot penetrate intact inner membranes but fluoresces highly once it intercalates with DNA. As expected, 0.125% SDS significantly increased PI fluorescence (Fig. 4C, D). Similarly to the NPN uptake assay, none of the NAs significantly affected PI fluorescence, indicating a lack of membrane-permeabilising effects in both E. coli and K. pneumoniae. Lastly, we assessed the effect of NAs on bacterial membrane potential using the voltage-sensitive dye DiSC3(5) (3,3’-dipropylthiadicarbocyanine iodide), which accumulates on hyperpolarised membranes and is translocated into lipid bilayers. As a positive control, we used polymyxin B, which disrupts the outer membrane and causes rapid depolarisation, indicated by a transient reduction in DiSC3(5) fluorescence in both E. coli and K. pneumoniae (Fig. 4E, F). At the tested concentrations, none of the NAs had an observable effect on the membrane potential of E. coli and K. pneumoniae (Fig. 4E, F). Together, these results highlighted that the NAs did not affect the membrane physiology of E. coli and K. pneumoniae.

## Exploring the effects of azidothymidine (AZT) on bacterial gene expression

In order to provide more in-depth insight into the mechanism of action, we used RNA sequencing to assess how the most promising NA, AZT, affected the transcription of E. coli EC958/pCTgfp and K. pneumoniae Ecl8/ pKpQILgfp. RNA sequencing was carried out for both strains (n = 4) grown in LB broth supplemented with 0.008 µg/mL AZT or an equal volume of DMSO as a vehicle control. Differentially expressed genes were determined by comparing DMSO-treated samples to the AZT-treated samples for both strains. In both species, most of the significantly upregulated genes were associated with DNA damage repair pathways and the SOS response. However, there were major differences in the type of downregulated genes between the two species.

Fig. 4 | The effect of nucleoside analogues on membrane permeability and potential in Escher-  EC958/pCT and Ecl8/pKpQIL The effect of nucleoside analogues on outer membrane permeability was determined by measuring the uptake of the hydrophobic dye N-phenyl-1-naphthylamine (NPN) in A K. pneumoniae Ecl8/pKpQILgfp and B E. coli EC958/pCTgfp, following treatment with the indicated concentrations of NAs or 0.125% sodium dodecyl sulphate (SDS) as a positive control for 4 h. The effect of nucleoside analogues on inner membrane permeability was determined by measuring uptake of the intercalating dye propidium iodide in C K. pneumoniae Ecl8/pKpQILgfp and D E. coli EC958/pCTgfp, following treatment with the indicated concentrations of NAs or 0.125% sodium dodecyl sulphate (SDS) as a positive control for 4 h. The effect of nucleoside analogues on membrane potential was determined using the voltage-sensitive dye DiSC3(5) (3,3’-dipropylthiadicarbocyanine iodide) in E K. pneumoniae Ecl8/pKpQILgfp and F E. coli EC958/pCTgfp. DiSC3(5) was added to bacterial cells and allowed to quench, followed by the addition of indicated concentrations of NAs or 20 µg/mL polymyxin B as a positive control. For all assays, bacterial cells treated with vehicle control (1% DMSO) were used as a negative control. Data presented are the mean ± standard deviation of three biological replicates, each tested in triplicate, on independent occasions. Statistical significance for the NPN and propidium iodide uptake assays was determined by comparing the mean of the DMSO control to the treatment groups using oneway ANOVA, followed by Dunnett’s test to correct for multiple comparisons. Significantly different results are indicated with $* * * \mathrm { ~ } ( P < 0 . 0 0 1 )$ . ns, not significant.

A  
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

## Azidothymidine reduces pCT conjugation in EC958 by impairing motility

In E. coli EC958/pCTgfp, the most downregulated genes were zraP and dosP, encoding the zinc resistance-associated protein ZraP and the oxygen-sensor protein DosP, respectively. Other downregulated genes included dgcE (encodes diguanylate cyclase), digH (encodes glycosyl hydrolase), and yebV (encodes DUF1480 family protein) (Supplementary Data 1). Of the genes on pCTgfp, the most upregulated gene, was HXG14_RS00170, encoding for the post-segregation killing protein PndC, and the most downregulated gene was HXG14_RS00465, encoding for the type IV pilus major pilin (Supplementary Data 1). Notably, 27 genes within flagellar operons, including genes encoding the flagellar basal body, hook, and filament, were significantly downregulated. Genes encoding the master flagella transcriptional regulator FlhC and the downstream flagella-specific sigma factor FliA were also significantly downregulated. The anti-sigma factor for FliA, FlgM, was significantly upregulated (Fig. 5B). These data strongly suggested that AZT inhibited flagella biosynthesis and motility in E. coli EC958. Therefore, we tested the effect of AZT on swimming motility in both the donor EC958 carrying pCTgfp and the recipient EC958 mCherry strains. Supplementing swimming agar with 0.008 µg/mL AZT significantly impaired swimming motility compared to DMSO. The swimming area decreased from approximately 2000–3000 mm2 to near negligible across both donor and recipient E. coli EC958 strains (Fig. 5C). The reduction in swimming motility was not due to growth inhibition as 0.008 µg/mL azidothymidine had no effect on the growth of E. coli EC958/pCTgfp or E. coli EC958 mCherry (Supplementary Fig. 3). This indicated that the altered expression of motility genes observed from the RNA sequencing results translated to impaired motility.

A  
<!-- image-->  
C

B  
<!-- image-->

<!-- image-->

We hypothesised that the loss of motility mediated by AZT could reduce the likelihood of donor and recipient cells encountering and interacting to facilitate plasmid transfer. To test this hypothesis, we inactivated one of the significantly downregulated flagella genes, fliE, encoding the flagellar hook-basal body complex protein FliE, in both the donor EC958/ pCTgfp and the recipient EC958 mCherry strains. This inactivation of fliE in both the donor and recipient strains completely abrogated swimming motility in both the donor and recipient EC958 strains, as expected (Supplementary Fig. 5). Firstly, we wanted to ascertain whether loss of motility in the donor or recipient had a greater impact on pCTgfp conjugation compared to 0.008 μg/mL AZT. Secondly, we wanted to find out if AZT exerted any further influence on pCTgfp conjugation when motility was already

<!-- image-->

<!-- image-->

Fig. 5 | Investigating the mechanism of action of azidothymidine on pCT gfpconjugation in  EC958. A Volcano plot of differentially expressed Escherichia coligenes in E. coli EC958/pCTgfp treated with 0.008 µg/mL azidothymidine (AZT) compared to DMSO control (n = 4). Dots in blue and red indicate significantly downregulated and upregulated genes, respectively. The log2 fold-change cut-off and adjusted p-value cut-off were 0.5 and 0.05, respectively. B Schematic diagram of the flagellum labelled with the structural proteins and the transcriptional regulation of the flagella operon (in dashed box), coloured according to whether the corresponding genes are significantly downregulated or upregulated. C Swimming motility of E. coli EC958/pCTgfp and EC958 mCherry on 0.3% agar supplemented with 0.008 µg/mL AZT or an equal volume of DMSO as a control. Plates were incubated at 37 °C for 18 h. Swimming motility was determined by measuring the diameter and calculating the area of the swimming zone. Representative images of swimming motility by EC958/pCTgfp and EC958 mCherry treated with AZT or DMSO (top). Swimming area of EC958/pCTgfp and EC958 mCherry treated with

impaired. Compared with the fully motile strains, the CF of pCTgfp was significantly reduced when motility was impaired in the E. coli EC958 donor, recipient or both (Fig. 5D). A similar reduction in CF was observed in the fully motile strains treated with AZT compared with the DMSO control (Fig. 5D). Treatment of strain pairs where one or both strains were nonmotile with AZT did not significantly further reduce the CF pCTgfp, supporting the hypothesis that AZT reduces conjugation in E. coli by limiting bacterial motility.

## Azidothymidine reduces pKpQIL conjugation in gfp Klebsiella Ecl8 partly by altering the expression of the DNA pneumoniaerepair pathway and methionine metabolism genes

In K. pneumoniae Ecl8/pKpQILgfp, the RNA sequencing data showed significant upregulation of several genes involved in DNA damage response (Fig. 6A, B), such as recN, dinI, and recA, the latter encoding RecA, a key sensor of DNA damage and a regulator of the SOS response. Conjugation involves the transfer of a conjugative plasmid to a recipient cell in the form of a single-stranded DNA molecule. Under typical circumstances, the presence of such single-stranded DNA would activate RecA to trigger the SOS response, a cellular stress mechanism that can be detrimental to the cell25. Hence, RecA is inhibited by the product of the plasmid-encoded psiB gene to ensure a stable and controlled genetic exchange26. However, we did not find psiB to be differentially expressed. Therefore, we hypothesised that upregulation of recA expression induced by AZT was impeding efficient plasmid transmission in K. pneumoniae. A previous study showed that RecA expression in E. coli increased upon AZT exposure, which was reversed with the addition of zinc acetate27. We tested whether the AZT-mediated reduction in pKpQILgfp CF was due to upregulation of recA expression, which could be reversed by the addition of zinc acetate. Therefore, we tested the effects of 0.008 µg/mL AZT combined with 25, 50, or 75 µg/mL of zinc acetate on the CF of pKpQILgfp using flow cytometry. The combination of AZT with 25, 50 or 75 µg/mL zinc acetate significantly restored the CF of pKpQILgfp compared to AZT treatment (Fig. 6C). To ascertain whether the effect of zinc acetate was mediated through downregulation of recA expression, RT-qPCR was carried out for both the donor K. pneumoniae Ecl8/pKpQILgfp and the recipient K. pneumoniae Ecl8 mCherry strains. In agreement with the RNA sequencing data (Fig. 6B), exposure to 0.008 µg/ mL AZT significantly increased recA expression by 4-fold in both the donor and recipient strains (Fig. 6D). Treatment with 75 µg/mL zinc acetate had no effect on recA expression, whereas the combined treatment with AZT and zinc acetate significantly reduced recA expression to levels comparable with the DMSO vehicle control treatment (Fig. 6D). These data suggested that AZT interfered with pKpQILgfp conjugation in K. pneumoniae, partly by upregulating recA expression.

In K. pneumoniae Ecl8/pKpQILgfp, some of the most significantly downregulated genes were also associated with the methionine biosynthesis pathway (Fig. 6E). The main end product of methionine biosynthesis is Sadenosylmethionine (SAM) (Fig. 6E), a key methyl donor for methylation reactions, which are essential for ribosome biogenesis, DNA/RNA

0.008 µg/mL AZT or DMSO (bottom). Data presented are the mean ± standard deviation of three independent experiments, each consisting of three biological replicates. The mean swimming area of EC958/pCTgfp and EC958 mCherry treated with 0.008 µg/mL AZT was compared to that of DMSO treatment using an unpaired two-tailed t-test. Significantly different results are indicated with \*\*\* (P < 0.001). D Flow cytometry-based measurement of pCTgfp conjugation frequency (CF) from the motile donor EC24 (WT EC958/pCTgfp) or the non-motile donor EC83 (fliE::aph EC958/pCTgfp) to the motile recipient EC25 (EC958 mCherry) or the nonmotile recipient EC85 (fliE::aph EC958 mCherry) treated with 0.008 µg/mL AZT or an equal volume of DMSO. The CF of pCTgfp was determined as the number of transconjugant cells divided by the number of recipient cells. Data presented are the mean ± standard deviation of three independent experiments, each consisting of four biological replicates. The indicated comparisons were carried out using oneway ANOVA, followed by the Holm-Šídák test to correct for multiple comparisons. Significantly different results are indicated with \*\*\* (P < 0.001). ns, not significant.

modifications, and many other processes28. We hypothesised that since AZT downregulated all the methionine biosynthesis pathway genes, SAM levels would be significantly reduced. Therefore, we tested to see whether the addition of SAM could reverse the AZT-mediated reduction in the CF of pKpQILgfp. The addition of 50, 100 or 125 µg/mL SAM with 0.008 µg/mL AZT significantly increased the CF of pKpQILgfp compared to AZT treatment alone, indicating reversal of the AZT-induced reduction in pKpQILgfp CF (Fig. 6F).

## Discussion

Plasmid-mediated spread of ARGs represents a major threat to global public health. Therefore, targeting plasmid conjugation between bacteria signifies a novel strategy to reduce the dissemination of ARGs. Building on our previous findings of AZT as a plasmid conjugation inhibitor21, we screened clinically approved NAs for potential plasmid conjugation-reducing activity in E. coli and K. pneumoniae using flow cytometry. Through our screening, we identified didanosine, stavudine, and trifluridine as further plasmid conjugation reducing agents. We also found that famciclovir and zalcitabine increased plasmid conjugation in E. coli, and aciclovir and valaciclovir increased plasmid transmission in K. pneumoniae. As the most promising NA, we explored the mechanisms by which AZT reduced plasmid conjugation in E. coli and K. pneumoniae using a combination of RNAseq and phenotypic testing.

Our data suggests that aciclovir, famciclovir, valaciclovir, and zalcitabine, commonly used as antiviral agents, could have an unexpected impact on the spread of AMR genes in bacteria. The antibacterial activity of famciclovir has not been explored before, and aciclovir and zalcitabine lack antibacterial activity in E. coli and Salmonella29,30. Based on their reported peak serum concentrations and bioavailability, these NAs may affect the spread of AMR genes in the gut, which is known to be a highly permissive environment for horizontal gene transfer31. The mean peak serum concentration of the highest dose of famciclovir (500 mg) is 3.3 µg/ mL32,33, and we observed an impact at 1 µg/mL, which is lower than the peak serum concentration. For the highest oral dose of zalcitabine (1.5 mg), the peak serum concentration is 0.0252 µg/mL, indicating our results are at concentrations above the peak serum concentration. Furthermore, the bioavailability of both drugs is very high, 77% and greater than 80% for famciclovir and zalcitabine, respectively33,34. A 1 g dose of valaciclovir (a pro-drug giving rise to aciclovir) administered orally gives a peak serum concentration of 5–6 µg/mL aciclovir35, which is between the 1 and 10 µg/mL concentrations tested in this study. While aciclovir has poor bioavailability (10-20%), valaciclovir has improved bioavailability of 54%36. Importantly, these NAs could reach higher concentrations in the gut, where they may affect the gut microbiota and potentiate the spread of AMR genes. A previous study found that a 1.25 mg dose of aciclovir in mice caused gut dysbiosis by reducing the abundance of Bacteroidetes and Akkermansia muciniphila37. However, further work is necessary to investigate the influence of these NAs on the gut resistome at a population level.

A  
<!-- image-->

<!-- image-->

D  
<!-- image-->  
B

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 6 | Investigating the mechanism of action of azidothymidine on pKpQILgfp conjugation frequency in Klebsiella pneumoniae Ecl8. A Volcano plot of differentially expressed genes in K. pneumoniae Ecl8/pKpQILgfp treated with 0.008 µg/mL azidothymidine (AZT) compared to DMSO control (n = 4). Dots in blue and red indicate significantly downregulated and upregulated genes, respectively. The log2 fold-change cut-off and adjusted p-value cut-off was 0.5 and 0.05, respectively. B Selected differentially expressed genes involved in DNA repair and SOS response pathways, methionine biosynthesis, salvage, and transport, and cysteine metabolism. C Flow cytometry-based measurement of pKpQILgfp conjugation frequency (CF) from KP19 (K. pneumoniae Ecl8/ pKpQILgfp) to KP18 (K. pneumoniae Ecl8 mCherry) treated with 0.008 µg/mL azidothymidine (AZT), zinc acetate (Zn (OAC)2), combination of both, or an equal volume of DMSO as control. The CF of pKpQILgfp calculated as the number of transconjugant cells divided by the number of recipient cells. Data presented are the mean ± standard deviation of three independent experiments, each consisting of four biological replicates. The indicated comparisons were carried out using one-way ANOVA, followed by the Holm-Šídák test to correct for multiple comparisons. Significantly different results are indicated with $^ { * } _ { \mathit { \Phi } } ( P \leq 0 . 0 5 ) ,$ \*\* $( P < 0 . 0 1 ) \mathrm { o r } ^ { * * * } ( P < 0 . 0 0 1 )$ . ns, not significant. D Fold-change in recA expression relative to rpoD in K. pneumoniae Ecl8 mCherry and K. pneumoniae Ecl8/  
pKpQILgfp following treatment with 0.008 µg/mL AZT, 75 µg/mL Zn $( \mathrm { O A C } ) _ { 2 } ,$ o r 0.008 µg/mL AZT and 75 µg/mL $Z \mathrm { n } \left( \mathrm { O A C } \right) _ { 2 } ,$ compared to DMSO vehicle control. The data presented are the mean ± standard deviations from three biological replicates tested in triplicate. Statistical significance was determined using oneway ANOVA, followed by the Holm-Šídák test to correct for multiple comparisons. Significantly different results are indicated with $^ { * * * } \left( P \leq 0 . 0 0 1 \right)$ . ns, not significant. E A simplified methionine biosynthesis and transport pathway of K. pneumoniae annotated with the major downregulated genes induced by AZT treatment. metR encodes MetR, the positive activator of metA and metE genes. metI and metN encode components of the methionine import system. F Flow cytometry-based measurement of pKpQILgfp CF from KP19 (K. pneumoniae Ecl8/pKpQILgfp) to KP18 (K. pneumoniae Ecl8 mCherry) treated with 0.008 µg/ mL AZT, S-adenosylmethionine (SAM), a combination of both, or an equal volume of DMSO as a control. Data presented are the mean ± standard deviation of three independent experiments, each consisting of four biological replicates. The indicated comparisons were carried out using one-way ANOVA, followed by the Holm-Šídák test to correct for multiple comparisons. Significantly different results are indicated with \* (P ≤ 0.05), \*\* (P < 0.01), or \*\*\* (P < 0.001). ns, not significant.

In the mechanistic investigations performed here, aciclovir, famciclovir, valaciclovir, and zalcitabine had no effect on membrane permeability and potential, and ROS generation. However, famciclovir and zalcitabine reduced intracellular ATP content in E. coli, and valaciclovir reduced intracellular ATP content in K. pneumoniae, following exposure after 4 h. This surprising reduction in intracellular ATP concentrations after exposure to famciclovir, valaciclovir, or zalcitabine raises important mechanistic questions. As these NAs did not affect bacterial growth under the tested concentrations, the decrease in intracellular ATP was unlikely because of generalised metabolic dysfunction or bacterial cell death. A possible explanation is that NAs, after intracellular phosphorylation, could potentially disrupt the balance of the nucleotide pools and replication processes, indirectly affecting central metabolic flux and energy homoeostasis38,39. Alternatively, an increased utilisation of the conjugation apparatus may itself cause an energetic burden on the donor cells. Conjugative plasmid transfer is known to require ATP for the assembly and functioning of the type IV secretion system and plasmid DNA processing and translocation40. Therefore, increased plasmid conjugation may cause a transient decrease in intracellular ATP concentrations without affecting overall growth kinetics. It is also possible that species-specific differences in nucleotide metabolism or energy regulation41 may explain the noted differences in responses between E. coli and K. pneumoniae. Although our current study does not provide evidence for direct causality between ATP modulation and changes in plasmid conjugation frequency, plasmid acquisition is associated with metabolic burden in bacterial cells42. Hence, our results suggest that intracellular energy homoeostasis may provide an additional regulatory mechanism for plasmid transfer.

Several antibiotics have been reported to increase plasmid transfer, typically through induction of cellular stress responses such as the SOS response pathway43. The NAs investigated in this study likely differ mechanistically from classical antibiotics. Rather than disrupting cell wall synthesis, translation, or DNA gyrase activity, the NAs presumably interfere with other cellular processes, including DNA replication, motility and cellular metabolism. However, there is evidence that antibiotic-induced plasmid conjugation and SOS response induction can occur through different mechanisms, indicating a lack of correlation between SOS response induction and plasmid transfer44. Furthermore, Lopatkin et al.45 found that sub-inhibitory concentrations of widely used classes of antibiotics, including aminoglycosides, β-lactams, cephalosporins, macrolides, amphenicols and quinolones did not increase plasmid conjugation frequency, but instead modulate antibiotic-mediated selection, thus promoting and suppressing conjugation frequency. Therefore, while bacterial stress-related pathways may contribute to the increase in plasmid conjugation, our findings suggest that alterations in other cellular mechanisms may represent an additional layer of regulation influencing plasmid transmission.

Through our screening, we found that the NAs didanosine, stavudine, and trifluridine, reduced the conjugation of pCTgfp in E. coli and pKpQILgfp in K. pneumoniae at concentrations that did not impact growth. In agreement with our findings, a previous study reported that 10 µg/mL didanosine did not significantly impact E. coli growth across 24 h46. A different study found that 20 µM didanosine (\~4.7 µg/mL) reduced K. pneumoniae growth after 24 h47, however, we did not find that 10 µg/mL didanosine affected the generation time or growth kinetics of K. pneumoniae Ecl8, which is a different strain than was used by Hind et al.47. Stavudine is not antibacterial up to 50 µg/mL after 4 hours46, which was within the time-frame of our experiments. There is no reported antibacterial activity of trifluridine in E. coli or K. pneumoniae, and we did not find that 25 µg/mL trifluridine affected the growth or generation times in either species. Therefore, the effect of didanosine, stavudine, and trifluridine on plasmid conjugation was not due to their antibacterial activity. In both E. coli and K. pneumoniae, AZT, didanosine, and stavudine had no effect on ROS generation or ATP content. Trifluridine only reduced ATP content in E. coli. These four drugs had no impact on membrane permeability or potential, indicating that they reduced plasmid transfer without interfering with membrane physiology. In agreement with our findings, Liu et al. 48, found that AZT also had no impact on membrane permeability, potential and ROS generation in E. coli. Unlike the NAs that increased plasmid conjugation, trifluridine may reduce pCTgfp conjugation by disrupting the availability of ATP needed for the type IV secretion system apparatus. For example, certain fatty acids have been reported to target the ATPase component of type IV secretion systems to inhibit plasmid conjugation49, whereas, other compounds have been reported to interfere with energy metabolism to deplete intracellular ATP needed for plasmid conjugation50,51. However, trifluridine had no effect on ATP content in K. pneumoniae, suggesting that it reduced pKpQILgfp through a different mechanism that remains to be identified.

In E. coli, AZT caused downregulation of motility and flagellaassociated genes, which was corroborated by the complete inhibition of swimming motility by AZT. When the motility-associated gene fliE was inactivated in donor or recipient E. coli strains, the result was a reduction of pCTgfp conjugation, similar to AZT treatment. Together, these suggested that AZT reduced plasmid conjugation in E. coli by inhibiting motility. The link between plasmid transfer and motility has been reported in several studies52. In agreement with our findings, Wonterghem et al. 53., found that inactivation of the flagella genes fliF or fliK in donor E. coli strains significantly reduced the conjugation of the broad host-range plasmid pKJK10 in liquid broth. As our experiments were also carried out in liquid broth, motility likely plays an important role in facilitating contact between donor and recipient cells. Whether this holds true for plasmid conjugation on solid surfaces remains to be fully established, but a previous study reported that the absence of motility resulted in Xanthomonas retroflexus and Pseudomonas putida enhanced plasmid uptake in biofilms54. In addition to chromosomal genes, type IV pilus (HXG14_RS00465, pilP, and pilV) genes in pCTgfp were also significantly downregulated in pKpQILgfp (Supplementary Data 1). The type IV pilus is critical for facilitating mating pair stabilization between donor and recipient cells55. Previously, loss of pilV was shown to impair plasmid conjugation in liquid broth56. Therefore, AZTinduced reduction in motility coupled with decreased pili production likely reduces donor and recipient contact and prevents mating pair stabilisation in liquid broth, thereby reducing plasmid transfer. Another layer of complexity is the interplay between the loss of motility, reduced plasmid conjugation, and intracellular energy availability, which remains to be established. Whilst plasmid conjugation requires ATP for the assembly of the type IV secretion system and translocation of plasmid DNA, flagellar rotation is driven by the proton motive force. Hence, future studies aimed at elucidating the relationship between the energy costs of flagellar rotation and plasmid conjugation apparatus will be needed to clarify the relationship between energy balance, motility, and plasmid conjugation.

In K. pneumoniae, AZT caused upregulation of DNA damage and SOS response genes. The addition of zinc acetate restored the transfer of pKpQILgfp in the presence of AZT, which was attributed to a reduction in recA expression. This is in agreement with previous studies, which have demonstrated the ability of zinc acetate to inhibit RecA activity57,58. The ability of zinc acetate to restore pKpQILgfp transfer in AZT-treated K. pneumoniae may also be attributed to its ability to disrupt interactions between single-stranded DNA and RecA, as previously observed58. Therefore, increased recA expression caused by AZT may encourage such interactions and, as a result, SOS-mediated degradation of the plasmid transferred to the recipient cells. We also found that AZT downregulated methionine biosynthesis pathway genes in K. pneumoniae, and likely SAM biosynthesis as the endpoint product. In line with this hypothesis, exogenous addition of SAM restored the conjugation of pKpQILgfp in the presence of AZT. A previous study hypothesised that plasmid methylation by SAM may protect against restriction activity in recipient K. pneumoniae. Oo et al.59 identified a link between spermidine synthesis and plasmid conjugation, with K. pneumoniae mutants of the spermidine synthesis pathways displaying lower conjugation frequencies. The overexpression of metK in the spermidine synthesis mutant strains caused a significant increase in plasmid conjugation59. Therefore, AZT treatment may reduce the protective effect of methylation by SAM, leading to the observed reduction in pKpQILgfp conjugation. Such protective effects of SAM have been formerly described in the context where the donor and recipient possess similar restriction modification systems.

Table 1 | List of bacterial strains used in this study
<table><tr><td>Strain ID</td><td>Description</td><td>Reference</td></tr><tr><td>EC24</td><td>Escherichia coli EC958, cured of pEC958, carrying IncK plasmid pCTgfp (gfp-aph inserted into the  $b 1 a _ { C T \times M - 1 4 }$  gene)</td><td>21</td></tr><tr><td>EC25</td><td>hh</td><td>21</td></tr><tr><td>EC83</td><td>EC24 with the fl gene inactivated by insertion f the hygromycin resistance gene hph</td><td>This study</td></tr><tr><td>EC84</td><td>EC25 with the fliE gene inactivated by insertion of the hygromycin resistance gene hph</td><td>This study</td></tr><tr><td>KP18</td><td>K alheheryseee </td><td>21</td></tr><tr><td>KP19</td><td>Klebsiella pneumoniae Ecl8 carrying IncF plasmid pKpQILgfp (gfp-aph cassette inserted into the  $b \vert a _ { \mathsf { K P C } - 3 }$  gene on pKpQIL)</td><td>21</td></tr><tr><td>SA01</td><td>Staphylococcus aureus ATCC 29213</td><td>ATCC</td></tr><tr><td>PA02</td><td>Pseudomonas aeruginosa ATCC 27853</td><td>ATCC</td></tr></table>

Although our work provides an important mechanistic insight into how NAs may modulate plasmid transfer, a limitation was that all experiments were carried out in vitro. Whilst this allowed us to explore the mechanistic effects of NAs on plasmid conjugation in a controlled and reproducible manner, it does not capture the complexity of plasmid dynamics in natural environments. In particular, plasmid conjugation within the gastrointestinal tract is influenced by multiple factors, including host factors, microbial community interactions, and nutrient availability60. Therefore, future work is necessary to determine whether NAs affect plasmid transfer in the same manner in physiologically relevant systems, such as ex vivo faecal models or in vivo animal infection models61. Another limitation of our study was the use of two AMR plasmids in two bacterial hosts, which may limit the general applicability of NAs as plasmid conjugation reducing agents. Hence, the effect of NAs on plasmid transmission needs to be studied in other plasmid types and bacterial hosts. Nevertheless, defining these mechanisms under controlled conditions using two different clinically important AMR plasmids represents an important first step toward understanding how clinically approved compounds may influence horizontal gene transfer.

In summary, our results indicated that additional clinically approved NAs didanosine, stavudine, and trifluridine possess plasmid conjugation reducing activities in E. coli and K. pneumoniae. Additionally, certain NAs increased plasmid conjugation, suggesting their role as potential promoters of plasmid dissemination. Our mechanistic investigation revealed that AZT reduced plasmid conjugation in E. coli by interfering with motility gene expression, corroborating the reduced plasmid transfer observed upon genetic inactivation of motility. In K. pneumoniae, AZT reduced plasmid conjugation by inducing DNA damage and SOS response genes and suppressing methionine biosynthesis and metabolism. That this inhibition can be restored by targeting RecA with zinc acetate or by supplementing Sadenosyl-methionine underscores the important contribution of these pathways and provides a mechanistic understanding of how AZT reduces plasmid dissemination. Therefore, AZT could provide a structural scaffold for the development and optimisation of more potent conjugation inhibitors.

## Methods

## Bacterial strains and growth conditions

The bacterial strains used are listed in Table 1. Unless stated otherwise, all strains were grown in Luria–Bertani (LB) broth (Sigma-Aldrich, USA) and incubated at $3 7 ^ { \circ } \mathrm { C }$ with aeration.

## Generation of fl -inactivated   strains

iE Escherichia coliThe fliE gene, encoding the flagellar hook-basal body complex protein, was inactivated in strains EC24 and EC25 (Table 1) by inserting the hph gene, encoding for hygromycin B phosphotransferase, using the pACBSCE plasmid62. Firstly, the hph gene was amplified from the pSIM18 plasmid63 using primers (Supplementary Table 2) that have flanking 40 bp homology to the fliE gene in E. coli EC958. The arabinose-inducible recombineering plasmid pACBSCE was electroporated into EC24 and EC25 with subsequent electroporation of the PCR-amplified hygromycin resistance cassette. Successful recombinants were selected on LB agar supplemented with 150 µg/mL hygromycin (Sigma-Aldrich, USA). PCR and Sanger sequencing (Eurofins Genomics, UK) using primers (Supplementary Table 2) that bind upstream and downstream of fliE, were used to verify the successful insertion of the hph gene.

## Antimicrobial susceptibility testing

To determine suitable concentrations of nucleoside analogues and selected antibiotics, minimum inhibitory concentrations (MICs) were determined by the broth microdilution method64. Nucleoside analogues were purchased from Sigma-Aldrich (USA) or Cambridge Bioscience (UK). The MICs were recorded as the lowest concentration at which no visible growth was observed.

## Measuring plasmid transmission and conjugation using flow cytometry

The transmission of pCTgfp in E. coli EC958 and pKpQILgfp in K. pneumoniae Ecl8 in the presence of the nucleoside analogues was assessed by flow cytometry as described previously21. Briefly, 1 mL of overnight cultures of donor (E. coli EC958/pCTgfp or K. pneumoniae Ecl8/pKpQILgfp) and recipient (E. coli EC958 or K. pneumoniae Ecl8 with chromosomal mCherry) strains were pelleted, washed in sterile PBS, and adjusted to an OD600 of 0.5. Equal volumes were mixed (1:1 ratio), and 20 µL of the mix was added to 180 µL LB broth with either the test compound or DMSO (vehicle control) in a 96-well round-bottom plate (Corning, USA). Plates were incubated at $3 7 ^ { \circ } \mathrm { C }$ with gentle agitation (100 rpm) for 4 h. After incubation, 20 µL was serially diluted 1:1000 in filter-sterilised Dulbecco’s PBS (Sigma-Aldrich, USA) and analysed on an Attune NxT flow cytometer with an Autosampler (Thermo Scientific, USA). GFP and mCherry emissions were detected using BL1-H and YL2-H channels, respectively. For each sample, 10,000 bacterial events were recorded. Conjugation was assessed by quantifying GFP+ (donor), mCherry+ (recipient), and GFP + / mCherry+ (transconjugant) populations using previously described gating strategies21. In the initial screening of NAs, plasmid transmission as a percentage of control was calculated as the number of transconjugants in the treated sample divided by the number of transconjugants in the control sample, multiplied by 100. In all the follow-up experiments with selected NAs, plasmid conjugation frequency was calculated as the number of transconjugant cells divided by the number of recipient cells, unless otherwise specified.

## Bacterial motility assays

Bacterial motility was assessed by swimming assays. Plates were prepared with 0.3% Difco granulated agar (BD, USA, cat. no. 214530), as previously described65, and allowed to dry overnight at room temperature. These were then inoculated by stabbing with overnight cultures adjusted to an $\mathrm { O D } _ { 6 0 0 }$ of 0.5 and incubated at 37 °C for 18 h. Swimming motility was determined by measuring the diameter and calculating the area of the swimming zone. Data presented are the means ± standard deviation of three independent experiments, each consisting of three biological replicates.

## Measurement of bacterial membrane potential

The impact of nucleoside analogues on E. coli and K. pneumoniae membrane potential was measured as previously described66. All media, plates, and the plate reader were warmed to $3 7 ^ { \circ } \mathrm { C }$ prior to use. Briefly, overnight bacterial cultures were subcultured in 5 mL LB broth (1% inoculum), grown to the exponential phase, and adjusted to an $\mathrm { O D } _ { 6 0 0 }$ of 0.5 in LB broth supplemented with 0.5 mg/mL bovine serum albumin. The cells were then dispensed into black polystyrene 96-well plates (Greiner Bio-One, Austria) and the autofluorescence of bacterial cells was measured for 5 min. DiSC3(5) (3,3’-dipropylthiadicarbocyanine iodide) (Cayman Chemical, USA) was dissolved in DMSO and added to the cells at a final concentration of 1 µM. The fluorescence quenching of $\mathrm { D i S C } _ { 3 } ( 5 )$ was monitored for 15 min before the addition of test compounds. As positive control, 20 µg/mL polymyxin B was used as previously described66. Fluorometric measurements were recorded every minute using a BioTek Synergy H1 Multimode Reader (Agilent Technologies, USA), with vigorous shaking between measurements, at excitation and emission wavelengths of 610 nm (±10) and 660 nm (±10), respectively. To ensure that the nucleoside analogues did not interfere with DiSC3(5) fluorescence, the assay was also carried out without bacterial cells. Data presented are the means ± standard deviation of three biological replicates, each tested on independent occasions.

## Measurement of reactive oxygen species generation

The effect of nucleoside analogues on reactive oxygen species (ROS) production in E. coli and K. pneumoniae cells was determined using the ROS-Glo $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ Assay Kit (Promega, USA) as per the manufacturer’s instructions. Briefly, overnight cultures were diluted to an $\mathrm { O D } _ { 6 0 0 } { \bf o f } 0 . 0 5$ in LB broth, and 80 µL was dispensed into white, flat-bottom 96-well plates (Corning, USA). A 20 µL volume of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ substrate solution combined with the nucleoside analogues, DMSO vehicle control, or 50 µM menadione as positive control, was added to bacterial cells, and incubated for 4 h at $3 7 ^ { \circ } \mathrm { C }$ with shaking (100 rpm). Following incubation, 100 µL of ROS-Glo Detection Solution was added to each well, and the plate was incubated at room temperature for 20 min. Luminescence was then measured using a BioTek Synergy H1 Multimode Reader (Agilent Technologies, USA). Data presented are the mean ± of three biological replicates tested on three independent occasions and expressed as luminescence relative to DMSO vehicle control.

## Measurement of intracellular ATP content

The effect of nucleoside analogues on ATP production in E. coli and K. pneumoniae cells was determined using the BacTiter-Glo Kit (Promega, USA) as per the manufacturer’s instructions. Briefly, overnight bacterial cultures were diluted to an $\mathrm { O D } _ { 6 0 0 }$ of 0.5 in LB broth, and 10 µL of this solution was mixed with 90 µL of LB broth supplemented with nucleoside analogues, DMSO vehicle control, or 2 µg/mL doripenem as a positive control, in white, flat-bottom 96-well plates. Bacterial cells were incubated for 4 h at $3 7 ^ { \circ } \mathrm { C }$ with shaking (100 rpm), and then equilibrated to room temperature for 5 min. A 100 µL volume of BacTiter-Glo Reagent was added to each well, and the contents of the plate were mixed briefly on an orbital shaker for 5 min. Luminescence was then measured using a BioTek Synergy H1 Multimode Reader (Agilent Technologies, USA). Data presented are the mean ± standard deviation of three biological replicates tested on three independent occasions and expressed as luminescence relative to DMSO vehicle control.

## Measurement of inner-membrane and outer-membrane permeability

The effect of nucleoside analogues on inner- and outer-membrane permeability in E. coli and K. pneumoniae cells was determined using propidium iodide (PI) and N-phenyl-1-naphthylamine (NPN)

uptake, respectively. Stock solutions of NPN (Fisher Scientific, USA) and PI (Sigma-Aldrich, USA) were prepared in ethanol and sterile distilled water, respectively, and diluted to working stock solutions in 5 mM HEPES buffer. Overnight bacterial cultures were subcultured in 5 mL LB broth (1% inoculum), grown to the exponential phase, and then adjusted to an $\mathrm { O D } _ { 6 0 0 }$ of 0.5 in 5 mM HEPES buffer. A 198 µL volume of bacterial suspension was mixed with 1 µL of 100 µM NPN or PI $( 1 0 \mu \mathrm { M }$ final concentration) and 1 µL of nucleoside analogues, DMSO vehicle control, or sodium dodecyl sulphate as a positive control, in black, flat-bottom 96-well plates (Greiner Bio-One, Austria). The plates were incubated in darkness for 30 minutes at room temperature. Fluorescence was measured using a BioTek Synergy H1 Multimode Reader (Agilent Technologies, USA). For NPN, excitation and emission wavelengths were 350 nm and 420 nm, and for PI, the excitation and emission wavelengths were 540 nm and 640 nm. Data presented are the mean ± of three biological replicates tested on three independent occasions and expressed as NPN or PI fluorescence relative to DMSO vehicle control.

## RNA extractions

Four overnight cultures of EC24 (E. coli EC958/pCTgfp and KP19 (K. pneumoniae Ecl8/pKpQILgfp were subcultured in 10 mL LB broth (2% inoculum) supplemented with 0.008 µg/mL AZT or an equal volume of DMSO as a vehicle control. Bacterial cells were grown to the exponential phase $\mathrm { ( O D _ { 6 0 0 } }$ of 0.5) at $3 7 ^ { \circ } \mathrm { C }$ with aeration, and total RNA was extracted using the Monarch Total RNA Miniprep Kit (NEB, USA), with on-column DNase I treatment to eliminate genomic DNA contamination as per the manufacturer’s instructions. RNA quality and quantity were determined using a NanoDrop spectrophotometer (Thermo Scientific, USA) and the Qubit RNA Broad Range Assay Kit (Invitrogen, USA), respectively.

## RNA sequencing and data analysis

Library preparation, sequencing and bioinformatic data analysis were carried out by GeneWiz UK Ltd. rRNA depletion was performed using a NEBNext rRNA Depletion Kit (Bacteria). Library preparation was performed using a NEBNext Ultra II RNA Library Prep Kit (NEB, USA) for Illumina according to the manufacturer’s instructions. Briefly, enriched RNAs were fragmented according to the manufacturer’s instructions. Firststrand and second-strand cDNA were subsequently synthesised. cDNA fragments were end-repaired and adenylated at 3’ ends, and a universal adapter was ligated to cDNA fragments, followed by index addition and library enrichment with limited-cycle PCR. Sequencing libraries were validated using the NGS Kit on the Agilent 5300 Fragment Analyzer (Agilent Technologies, USA) and quantified by using a Qubit 4.0 Fluorometer (Invitrogen, USA). The sequencing libraries were multiplexed and loaded on the flow cell of an Illumina NovaSeq 6000 instrument according to the manufacturer’s instructions. The samples were sequenced using a 2 × 150 Pair-End (PE) configuration v1.5. Image analysis and base calling were conducted by the NovaSeq Control Software v1.7 on the NovaSeq instrument. Raw sequence data (.bcl files) generated from Illumina NovaSeq were converted into fastq files and de-multiplexed using the Illumina bcl2fastq program version 2.20. One mismatch was allowed for index sequence identification. After investigating the quality of the raw data, sequence reads were trimmed to remove possible adapter sequences and nucleotides with poor quality using Trimmomatic v.0.36. The trimmed reads were mapped to the reference genomes using the Bowtie2 aligner v.2.2.6 to generate BAM files. Unique gene hit counts were calculated using featureCounts from the Subread package v.1.5.2. Only unique reads that fell within gene regions were counted. After the extraction of gene hit counts, the gene hit counts table was used for downstream differential expression analysis. Using DESeq2, a comparison of gene expression between DMSO- and AZTtreated samples was performed. The Wald test was used to generate p-values and log2 fold-changes. Genes with an adjusted p value ≤ 0.05 and absolute log2 fold-change > 0.5 were called as differentially expressed genes for each comparison.

## Ethics

No ethical approval was required for this work.

## Data availability

The RNA sequencing data generated in this project have been deposited in ArrayExpress under accession code E-MTAB-15827.

Received: 7 January 2026; Accepted: 12 March 2026;

Published online: 14 April 2026

## References

1. Sati, H. et al. The WHO Bacterial Priority Pathogens List 2024: a prioritisation study to guide research, development, and public health strategies against antimicrobial resistance. Lancet Infect. Dis 25, 1033–1043 (2025).

2. Murray, C. J. L. et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet 399, 629–655 (2022).

3. Rozwandowicz, M. et al. Plasmids carrying antimicrobial resistance genes in Enterobacteriaceae. J. Antimicrob. Chemother. 73, 1121–1137 (2018).

4. Wyres, K. L. & Holt, K. E. Klebsiella pneumoniae as a key trafficker of drug resistance genes from environmental to clinically important bacteria. Curr. Opin. Microbiol. 45, 131–139 (2018).

5. Rana, C. et al. Antimicrobial resistance genes and associated mobile genetic elements in Escherichia coli from human, animal and environment. Chemosphere 369, 143808 (2024).

6. León-Sampedro, R. et al. Pervasive transmission of a carbapenem resistance plasmid in the gut microbiota of hospitalized patients. Nat. Microbiol. 6, 606–616 (2021).

7. Castañeda-Barba, S., Top, E. M. & Stalder, T. Plasmids, a molecular cornerstone of antimicrobial resistance in the One Health era. Nat. Rev. Microbiol. 22, 18–32 (2024).

8. Cottell, J. L., Webber, M. A. & Piddock, L. J. V. Persistence of Transferable Extended-Spectrum-β-Lactamase resistance in the absence of antibiotic pressure. Antimicrob. Agents Chemother. 56, 4703–4706 (2012).

9. Cottell, J. L., Saw, H. T., Webber, M. A. & Piddock, L. J. Functional genomics to identify the factors contributing to successful persistence and global spread of an antibiotic resistance plasmid. BMC Microbiol. 14, 168 (2014).

10. Buckner, M. M. C. et al. Clinically Relevant Plasmid-Host Interactions Indicate that Transcriptional and Not Genomic Modifications Ameliorate Fitness Costs of Klebsiella pneumoniae Carbapenemase-Carrying Plasmids. mBio 9, e02303-17 (2018).

11. Element, S. J. et al. Growth in a biofilm promotes conjugation of a blaNDM-1 -bearing plasmid between Klebsiella pneumoniae strains. mSphere 8, e00170–23 (2023).

12. Marimuthu, K. et al. Whole genome sequencing reveals hidden transmission of carbapenemase-producing Enterobacterales. Nat. Commun. 13, 3052 (2022).

13. Takeuchi, D. et al. Nationwide surveillance in Thailand revealed genotype-dependent dissemination of carbapenem-resistant Enterobacterales. Microb. Genomics 8, 000797 (2022).

14. Roberts, L. W. et al. Long-read sequencing reveals genomic diversity and associated plasmid movement of carbapenemase-producing bacteria in a UK hospital over 6 years. Microb. Genomics 9, 001048 (2023).

15. Gomez-Simmonds, A. et al. Genomic epidemiology of carbapenemresistant Enterobacterales at a New York City hospital over a 10-year period reveals complex plasmid-clone dynamics and evidence for frequent horizontal transfer of blaKPC. Genome Res. 34, 1895–1907 (2024).

16. Chen, L. et al. Comparative Genomic Analysis of KPC-Encoding pKpQIL-Like Plasmids and Their Distribution in New Jersey and New York Hospitals. Antimicrob. Agents Chemother. 58, 2871–2877 (2014).

17. Piazza, A. et al. A novel KPC-166 in ceftazidime/avibactam resistant ST307 Klebsiella pneumoniae causing an outbreak in intensive care COVID Unit, Italy. J. Microbiol. Immunol. Infect. 57, 457–469 (2024).

18. Buckner, M. M. C., Ciusa, M. L. & Piddock, L. J. V. Strategies to combat antimicrobial resistance: anti-plasmid and plasmid curing. FEMS Microbiol. Rev. 42, 781–804 (2018).

19. Getino, M. & De La Cruz, F. Natural and artificial strategies to control the conjugative transmission of plasmids. Microbiol. Spectr. 6, https://doi. org/10.1128/microbiolspec.mtbp-0015-2016 (2018).

20. Fernandez-Lopez, R. et al. Unsaturated fatty acids are inhibitors of bacterial conjugation. Microbiology 151, 3517–3526 (2005).

21. Buckner, M. M. C. et al. HIV drugs inhibit transfer of plasmids carrying extended-Spectrum β-Lactamase and Carbapenemase Genes. mBio 11, e03355–19 (2020).

22. Alav, I. et al. Natural products from food sources can alter the spread of antimicrobial resistance plasmids in Enterobacterales. Microbiology 170, 001496 (2024).

23. Alav, I. & Buckner, M. M. C. Non-antibiotic compounds associated with humans and the environment can promote horizontal transfer of antimicrobial resistance genes. Crit. Rev. Microbiol. 1–18 https://doi. org/10.1080/1040841X.2023.2233603 (2023).

24. Moncalián, G. et al. Characterization of ATP and DNA binding activities of TrwB, the coupling protein essential in Plasmid R388 conjugation. J. Biol. Chem. 274, 36117–36124 (1999).

25. Baharoglu, Z., Bikard, D. & Mazel, D. Conjugative DNA transfer induces the bacterial SOS response and promotes antibiotic resistance development through integron activation. PLoS Genet 6, e1001165 (2010).

26. Petrova, V., Chitteni-Pattu, S., Drees, J. C., Inman, R. B. & Cox, M. M. An SOS inhibitor that binds to free RecA protein: the PsiB protein. Mol. Cell 36, 121–130 (2009).

27. Crane, J. K., Alvarado, C. L. & Sutton, M. D. Role of the SOS response in the generation of antibiotic resistance in vivo. Antimicrob. Agents Chemother. 65, e0001321 (2021).

28. Fontecave, M., Atta, M. & Mulliez, E. S-adenosylmethionine: nothing goes to waste. Trends Biochem. Sci. 29, 243–249 (2004).

29. Sperber, S. J., Feibusch, E. L., Damiani, A. & Weinstein, M. P. In vitro activities of nucleoside analog antiviral agents against salmonellae. Antimicrob. Agents Chemother. 37, 106–110 (1993).

30. Shilaih, M. et al. Antibacterial effects of antiretrovirals, potential implications for microbiome studies in HIV. Antivir. Ther. 23, 91–94 (2018).

31. McInnes, R. S., McCallum, G. E., Lamberte, L. E. & Van Schaik, W. Horizontal transfer of antibiotic resistance genes in the human gut microbiome. Curr. Opin. Microbiol. 53, 35–43 (2020).

32. Pue, M. A. et al. Linear pharmacokinetics of penciclovir following administration of single oral doses of famciclovir 125, 250, 500 and 750 mg to healthy volunteers. J. Antimicrob. Chemother. 33, 119–127 (1994).

33. Devineni, D. & Gallo, J. M. Zalcitabine: clinical pharmacokinetics and efficacy. Clin. Pharmacokinet. 28, 351–360 (1995).

34. Gill, K. S. & Wood, M. J. The Clinical Pharmacokinetics of Famciclovir. Clin. Pharmacokinet. 31, 1–8 (1996).

35. Jacobson, M. A. Valaciclovir (BW256U87): The L-valyl ester of acyclovir. J. Med. Virol. 41, 150–153 (1993).

36. Soul-Lawton, J. et al. Absolute bioavailability and metabolic disposition of valaciclovir, the L-valyl ester of acyclovir, following oral administration to humans. Antimicrob. Agents Chemother. 39, 2759–2764 (1995).

37. Ramakrishna, C. et al. Herpes simplex virus infection, Acyclovir and IVIG treatment all independently cause gut dysbiosis. PLOS ONE 15, e0237189 (2020).

38. Yssel, A. E. J., Vanderleyden, J. & Steenackers, H. P. Repurposing of nucleoside- and nucleobase-derivative drugs as antibiotics and biofilm inhibitors. J. Antimicrob. Chemother. 72, 2156–2170 (2017).

39. Thomson, J. M. & Lamont, I. L. Nucleoside analogues as antibacterial agents. Front. Microbiol. 10, 952 (2019).

40. San Millan, A. & MacLean, R. C. Fitness costs of plasmids: a limit to plasmid transmission. Microbiol. Spectr 5, 5.5.02 (2017).

41. Leiva, L. E., Zegarra, V., Bange, G. & Ibba, M. At the crossroad of nucleotide dynamics and protein synthesis in bacteria. Microbiol. Mol. Biol. Rev. 87, e00044–22 (2023).

42. Curtsinger, H. D., Martínez-Absalón, S., Liu, Y. & Lopatkin, A. J. The metabolic burden associated with plasmid acquisition: An assessment of the unrecognized benefits to host cells. BioEssays 47, 2400164 (2025).

43. Hallal Ferreira Raro, O., Poirel, L., Tocco, M. & Nordmann, P. Impact of veterinary antibiotics on plasmid-encoded antibiotic resistance transfer. J. Antimicrob. Chemother. 78, 2209–2216 (2023).

44. Zhao, R. et al. Mechanistic divergence between SOS response activation and antibiotic-induced plasmid conjugation in Escherichia coli. Microbiol. Spectr. 13, e00090–25 (2025).

45. Lopatkin, A. J. et al. Antibiotics as a selective driver for conjugation dynamics. Nat. Microbiol. 1, 16044 (2016).

46. Wallace, V. J., Sakowski, E. G., Preheim, S. P. & Prasse, C. Bacteria exposed to antiviral drugs develop antibiotic cross-resistance and unique resistance profiles. Commun. Biol. 6, 837 (2023).

47. Hind, C. K. et al. Evaluation of a Library of FDA-approved drugs for their ability to potentiate antibiotics against multidrug-resistant gramnegative pathogens. Antimicrob. Agents Chemother. 63, e00769-19 (2019).

48. Liu, Y. et al. Anti-HIV agent azidothymidine decreases Tet(X)- mediated bacterial resistance to tigecycline in Escherichia coli. Commun. Biol. 3, 162 (2020).

49. Ripoll-Rozada, J. et al. Type IV traffic ATPase TrwD as molecular target to inhibit bacterial conjugation. Mol. Microbiol. 100, 912–921 (2016).

50. Wang, X.-Y. et al. Dihydroartemisinin inhibits plasmid transfer in drugresistant Escherichia coli via limiting energy supply. Zool. Res. 44, 894–904 (2023).

51. Li, G. et al. Targeting Plasmid conjugation with cinnamic acid: a novel approach to combat antibiotic resistance. Engineering S2095809925004163, https://doi.org/10.1016/j.eng.2025.06.040 (2025).

52. Bhattacharya, S. et al. Flagellar rotation facilitates the transfer of a bacterial conjugative plasmid. EMBO J. 44, 587–611 (2024).

53. Van Wonterghem, L. et al. Genome-wide association study reveals host factors affecting conjugation in Escherichia coli. Microorganisms 10, 608 (2022).

54. Røder, H. L. et al. Flagellar interference with plasmid uptake in biofilms: a joint experimental and modeling study. Appl. Environ. Microbiol. 90, e01510–e01523 (2024).

55. Ou, J. T. & Anderson, T. F. Role of pili in bacterial conjugation. J. Bacteriol. 102, 648–654 (1970).

56. Allard, N., Neil, K., Grenier, F. & Rodrigue, S. The Type IV Pilus of Plasmid TP114 displays adhesins conferring conjugation specificity and is important for DNA transfer in the mouse gut microbiota. Microbiol. Spectr. 10, e02303–e02321 (2022).

57. Bunnell, B. E., Escobar, J. F., Bair, K. L., Sutton, M. D. & Crane, J. K. Zinc blocks SOS-induced antibiotic resistance via inhibition of RecA in Escherichia coli. PLOS ONE 12, e0178303 (2017).

58. Crane, J. K., Cheema, M. B., Olyer, M. A. & Sutton, M. D. Zinc blockade of SOS response inhibits horizontal transfer of antibiotic resistance genes in enteric bacteria. Front. Cell. Infect. Microbiol. 8, 410 (2018).

59. Oo, G. et al. Anti-plasmid defense in hypervirulent Klebsiella pneumoniae involves Type I-like and Type IV restriction modification systems. Emerg. Microbes Infect. 14, 2558877 (2025).

60. Liu, W. et al. Factors and mechanisms influencing conjugation in vivo in the gastrointestinal tract environment: a review. Int. J. Mol. Sci. 24, 5919 (2023).

61. Kessler, C., Hou, J., Neo, O. & Buckner, M. M. C. In situ, in vivo, and in vitro approaches for studying AMR plasmid conjugation in the gut microbiome. FEMS Microbiol. Rev. 47, fuac044 (2023).

62. Lee,D. J. et al. Gene doctoring: amethodfor recombineering in laboratory and pathogenic Escherichia coli strains. BMC Microbiol 9, 252 (2009).

63. Chan, W. et al. A recombineering based approach for high-throughput conditional knockout targeting vector construction. Nucleic Acids Res. 35, e64 (2007).

64. CLSI. Performance Standards for Antimicrobial Susceptibility Testing. (Clinical and Laboratory Standards Institute, 2025).

65. Clemmer, K. M., Bonomo, R. A. & Rather, P. N. Genetic analysis of surface motility in Acinetobacter baumannii. Microbiology 157, 2534–2544 (2011).

66. Buttress, J. A. et al. A guide for membrane potential measurements in Gram-negative bacteria using voltage-sensitive dyes. Microbiology 168, 001227 (2022).

## Acknowledgements

I.A., A.A., P.P., and M.M.C.B. were funded by the MRC grant MR/V009885/1 (New Investigator Research Grant to M.M.C.B.).

## Author contributions

I.A. and M.B conceived the experiments. I.A., P.P., and A.A. performed the experiments. All authors contributed to writing and reviewing the manuscript.

## Competing interests

M.M.C.B. is an Editorial Board Member of npj Antimicrobials and Resistance but was not involved in the journal’s review of, or decisions related to, the manuscript. The other authors declare no competing interests.

## Consent to participate

No human participants were involved in this work.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s44259-026-00197-5.

Correspondence and requests for materials should be addressed to Michelle M. C. Buckner.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2026