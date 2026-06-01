Article

# Reversal Effects of 20(R)- and 20(S)-Ginsenoside-Rg3 on Daunorubicin Uptake in Multidrug-Resistant Leukemia Cells Studied in the Single-Cell Biochip

Yuchun Chen 1, Nandini Joshi 1, Megan Chiem 1, Iryna Kolesnyk 1, Paul C. H. Li 1,\* , Patrick Y. K. Yue 2   
and Ricky N. S. Wong 2

1 Department of Chemistry, Simon Fraser University, Burnaby, BC V5A 1S6, Canada

2 Department of Biology, Hong Kong Baptist University, Hong Kong, China

\* Correspondence: paulli@sfu.ca

## Abstract

Multidrug resistance (MDR), frequently mediated by overexpression of the P-glycoprotein (P-gp) efflux transporter, remains a major challenge in the treatment of leukemia by limiting intracellular accumulation of chemotherapeutic agents such as daunorubicin (DNR). This study evaluates the applicability of a microfluidic-based single-cell biochip to investigate the reversal effects of microgram-level ginsenosides on daunorubicin uptake in multidrugresistant leukemia cells. Pure ginsenosides are difficult to obtain in bulk and are typically available only in milligram quantities, which restricts their evaluation using conventional MDR assays such as flow cytometry that require large cell populations and substantial amounts of compounds. To address this limitation, a microfluidic single-cell biochip (SCB) requiring microgram quantities of ginsenosides (<100 µg) and fewer than ten cells was employed. Intracellular DNR accumulation was measured in the CEM/VLB1000 leukemia cell line following treatment with DNR alone or in combination with ginsenoside Rg3-R, ginsenoside Rg3-S, 20(S)-protopanaxatriol (PPT), and 20(S)-protopanaxadiol (PPD), in order to compare their relative efficacy in enhancing drug accumulation. Although Rg3-R and Rg3-S share highly similar chemical structures and are glycosylated derivatives of the PPD aglycone, Rg3-S exhibited greater potency in increasing intracellular daunorubicin accumulation than Rg3-R, and both were more effective than PPD. These findings underscore the importance of ginsenoside stereochemistry modulating P-gp-associated drug resistance and demonstrate the utility of the SCB platform for quantifying daunorubicin accumulation in multidrug-resistant leukemia cells at single-cell resolution.

Keywords: microfluidic biochip; single cell fluorescence; leukemia drug uptake; multidrug resistance; daunorubicin efflux reversal; ginsenosides

## Check for updates

Academic Editors: Cheorl-Ho Kim and Yongjian Ai

Received: 23 December 2025   
Revised: 13 February 2026   
Accepted: 12 March 2026   
Published: 14 March 2026

Copyright: © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license.

## 1. Introduction

Multidrug resistance (MDR) remains a major obstacle to effective cancer chemotherapy, posing a substantial challenge to disease modulation and long-term treatment success. One of the most extensively studied mechanisms underlying MDR is the overexpression of the ATP-binding cassette (ABC) transporter called P-glycoprotein (P-gp/ABCB1), which actively effluxes a wide range of chemotherapeutic agents from cancer cells, thereby reducing intracellular drug accumulation and therapeutic efficacy [1–4]. In leukemia, elevated P-gp expression has been strongly associated with the resistance to anthracycline drugs such as daunorubicin (DNR), often leading to treatment failure and disease relapse [5].

We have previously reported a same-single-cell approach for studying the modulation of drug efflux in multidrug-resistant cancer cells using a microfluidic platform [6]. This approach was later extended to evaluate drug modulation by directly measuring intracellular drug accumulation rather than efflux [7]. Compared with the earlier efflux-based method, the accumulation-based approach is both faster and simpler while maintaining single-cell resolution. This methodology has since been adopted as the microfluidic single-cell biochip (SCB) platform for subsequent MDR studies [8].

In parallel with advances in microfluidic technologies, increasing attention has been directed toward traditional medicinal compounds due to their reported anticancer properties and potential to enhance chemotherapy outcomes, including improved therapeutic response and enhanced quality of life [9]. Among these compounds, ginsenosides, bioactive saponins derived from Panax ginseng, have attracted significant interest. Several studies have suggested that MDR in cancer cells can be reversed by ginsenosides, potentially through interactions with the P-gp transporter that reduce drug efflux [10–12]. As a result, intracellular accumulation of chemotherapeutic agents such as DNR may be enhanced in MDR cells.

Despite their therapeutic potential, purified ginsenosides are not easy to test because they are difficult to obtain in bulk and are typically available only in low amounts at the milligram level. This limitation presents a great challenge for conventional MDR assays, such as flow cytometry, which require large numbers of cells and milligram quantities of compounds in each experiment [13,14]. To overcome this constraint, the microfluidic singlecell biochip (SCB) method was developed to enable MDR evaluation using microgram quantities of compounds like ginsenosides and fewer than ten cells per experiment. In this study, the SCB platform was applied to measure intracellular DNR accumulation in single MDR leukemia cells using microgram quantities of ginsenosides (<100 µg), including Rg3.

Ginsenoside Rg3 has been reported to possess anticancer activity [15] and is present at low levels in white (air-dried) ginseng but at higher concentrations in steamed (red) ginseng [16–18]. Elevated levels of Rg3 have also been identified in certain commercial ginseng products [19]. There were four ginsenosides studied in this paper: 20(S)- ginsenoside Rg3 (Rg3-S), 20(R)-ginsenoside Rg3 (Rg3-R), 20(S)-protopanaxadiol (PPD) and 20(S)-protopanaxatriol (PPT). Rg3-S and Rg3-R are structurally similar as they are the two stereoisomers at the C-20 position of Rg3. In addition, PPD and PPT share similar core frameworks, with PPD serving as the aglycone of both Rg3 stereoisomers. While these compounds are all structurally similar, they exhibit distinct biological activities [20].

Moreover, only Rg3 and PPD have been reported to have the MDR-reversal effect [16,21,22]. However, differences in MDR-reversal activity between the Rg3 stereoisomers, Rg3-R and Rg3-S, have not been systematically investigated, particularly at the single-cell level. In this work, we employed the SCB platform to evaluate how four structurally related ginsenosides, Rg3-S, Rg3-R, PPD, and PPT, affect intracellular DNR accumulation in individual multidrug-resistant leukemia cells. This study aims to clarify the influence of ginsenoside stereochemistry on MDR modulation while further demonstrating the applicability of microfluidic single-cell analysis for drug resistance studies using scarce natural products.

## 2. Results and Discussion

## 2.1. MDR-Reversal Effect on DNR Accumulation in the MDR Cancer Cells

We first evaluated the effect of PPD on intracellular DNR accumulation in MDR cancer cells. As shown in Figure 1A, when only DNR solution was given to the cell, cell fluorescence increased, indicating continuous DNR accumulation. After \~700 s, fluorescence reached a steady state, reflecting equilibrium between DNR influx and efflux, with the latter process via P-gp transporters. Upon addition of DNR solution containing Rg3-R, intracellular DNR accumulation increased, indicating MDR reversal. The DNR accumulation increased 1.6-fold in the presence of PPD, demonstrating MDR reversal (Figure 1B).

<!-- image-->

<!-- image-->  
Figure 1. Uptake enhancement of DNR due to PPD (50 µM) on a single-cell. (A) Raw time-resolved intracellular DNR fluorescence. (B) Corrected DNR accumulation trace showing enhanced intracellular DNR uptake after PPD addition.

We next applied the same uptake procedure to Rg3-R, Rg3-S, and PPT. The results of the uptakes are summarized. As shown in Table 1, the ginsenosides have a dosedependent effect on CEM/VLB1000 cells. Intracellular DNR accumulation doubled with rising ginsenoside concentrations, indicating a dose-dependent effect. This result is superior to a previous study where the effective Rg3 concentration for MDR reversal as measured by the rhodamine 123 accumulation assay was observed not at 100 µM, but at a 320 µM level, though that was measured by the cytotoxicity assay as observed at a 5–40 µM level [16].

Table 1. Drug accumulation fold increases in the CEM/VLB cell also treated with ginsenosides.
<table><tr><td rowspan="2"></td><td colspan="6">DNR (35 μM) Only or with Added Compound</td></tr><tr><td>DNR 35 μM Only</td><td></td><td>DNR 35 μM + PPT</td><td>DNR 35 μM + PPD</td><td>DNR 35 μM + Rg3-S</td><td>DNR 35 μM + Rg3-R</td></tr><tr><td>35 μM (A)</td><td>1.35 ± 0.06 (n = 4)</td><td>(B) 50 μM</td><td>2.14 ± 0.67 (n =5)</td><td>1.68 ± 0.15 (n = 4)</td><td> $2 . 1 5 \pm 0 . 4 7$  (n = 4)</td><td>2.05 ± 0.24 (n = 4)</td></tr><tr><td>p1</td><td></td><td></td><td>0.06</td><td>0.02</td><td>0.04</td><td>0.01</td></tr><tr><td>35 μM (2)</td><td> $1 . 3 8 \pm 0 . 2 2$  (n = 4)</td><td>(C) 100 μM</td><td>3.52 ± 1.06 (n = 5)</td><td> $2 . 3 0 \pm 0 . 3 6$  (n = 4)</td><td> $5 . 9 0 \pm 1 . 8 9$  (n = 4)</td><td> $3 . 5 2 \pm 0 . 9 8$  (n = 5)</td></tr><tr><td>p2</td><td></td><td></td><td>0.04</td><td>0.03</td><td>0.03</td><td>0.05</td></tr><tr><td>P</td><td></td><td></td><td>0.004</td><td>0.0007</td><td>0.0006</td><td>0.001</td></tr></table>

p is the probability value of one-way ANOVA test for (A) DNR control, (B) DNR + reagent (50 µM) and (C) DNR + reagent (100 µM). p1 and p2 are the values of Student’s t tests; p1 is for the comparison of A with B, whereas p2 is for that of B with C. All differences are statistically significant as p < 0.05, except for 50 µM PPT.

Although Rg3-R and Rg3-S share similar chemical structures, Rg3-S was more potent at modulating MDR. The more potent effect of Rg3-S was also observed in its effect on insulin secretion [23] and anti-apoptotic effect [20].

## 2.2. DNR Accumulation Control Experiments

To confirm that the increased DNR accumulation was not caused by fluctuations from solution switching, we used DNR-only solution to replace the DNR/Rg3 solution. Specifically, DNR solution was added sequentially three times to the same cell, and accumulation was measured after each addition. The rate of accumulation curve of daunorubicin 35 µM in CEM/VLB1000 subline is shown in Figure 2. DNR was added into reservoir 2 at 100 s of the drug into the cell. Subsequent to addition, internal DNR accumulation increased until 500 s, after which the accumulation reached a plateau of 940.04 and the efflux of the drug out of the cell equated to the intracellular accumulation. Furthermore, switching drugs (DNR 35 µM) at 1100 s and at 2100 s did not increase intracellular accumulation of the drug significantly.

<!-- image-->  
Figure 2. Negative control conducted in the single-cell chip.

We have repeated the same experiments on three different cells, and the results are shown in Table 2. The results clearly show that the DNR accumulation will not increase dramatically after it reaches the steady state simply by repeatedly adding DNR to the cell, thus confirming that the enhanced DNR accumulations are caused by the MDR-reversal effects of Rg3-R and Rg3-S as described in Section 2.1.

Table 2. DNR accumulation in the MDR cancer cells untreated with any other reagents.
<table><tr><td rowspan="2"></td><td colspan="3">DNR Accumulation</td></tr><tr><td>Cell 1</td><td>Cell 2</td><td>Cell 3</td></tr><tr><td>DNR 35 μM 1</td><td>1.4</td><td>1.3</td><td>1.3</td></tr><tr><td>DNR 35 μM 2</td><td>1.3</td><td>1.2</td><td>1.3</td></tr><tr><td>Cell image</td><td><img src="images/8ac4d6279ceaad6784be5ef60224d80699fd4e6263a51bc6b3483f5f8b90749a.jpg"/></td><td><img src="images/ff1ba87d481f16f031a3dfd678b040432782ece86c8866d2cbf059536ff8c3a7.jpg"/></td><td><img src="images/7d0d76056fe763a230f43c649f0f09900239c3a59fd9800e6962ae1199aa956d.jpg"/></td></tr></table>

When we compared the effects of ginsenosides between two cell lines, CEM/VLB1000 and CEM/WT, it was evident that the fold increase is low in the CEM/WT, i.e., 1.70 ± 0.14 (n = 2) for $5 0 \mu \mathrm { M }$ and $2 . 3 5 \pm 0 . 5 0$ (n = 2) for $1 0 0 \mu \mathrm { M } .$ . This may be due to the evidence that CEM/wt does not possess as many P-gp pumps as the CEM/VLB1000 subline.

## 3. Materials and Methods

Cell cultures: The drug-sensitive human leukemia CCRF-CEM cell line (CEM/WT) and the multidrug-resistant Vinblastine (VLB) subline (CEM/VLB 1000) were obtained from BC Cancer Agency. Both CEM/WT and the resistant subline, CEM/VLB 1000, were cultured in α-MEM supplemented with 10% fetal bovine serum (FBS) and penicillin (5%). The cell lines were maintained at $3 7 ^ { \circ } \mathrm { C }$ in a humidified atmosphere containing 5% CO2 and were passaged once a week. In addition, the drug-resistant subline, CEM/VLB1000, was sub-cultured with 100 µg/mL vinblastine solution to maintain resistance of 1000 µg/mL (CEM/VLB). More information is provided in the Supplementary Information.

Microchip fabrication: Figure 3 depicts the design of the microfluidic single-cell chip, with the chip specification given in the caption. The microfluidic chip was fabricated using the standard micromachining procedures on glass by CMC Microsystems (Kingston, ON, Canada). These procedures, which include standard chip cleaning, thin metal film deposition, photolithography, photoresist development, glass etching by hydrofluoric acid, reservoir forming on cover plate, and chip bonding, have been described previously [24]. As shown in Figure 3A, the microfluidic chip consists of four reservoirs connected by four microchannels to a central cell-retention chamber. In the chamber, there is a V-shaped structure, which can retain a single cell. Reservoir 1 is the α-MEM solution inlet, reservoir 2 is the reagent inlet, reservoir 3 is the cell inlet, and reservoir 4 is the waste outlet. A microfluidic chip was prepared and cleaned with NOX soap, purified water and 90% ethanol, consecutively.

Drug accumulation: Prior to the experiment, an aliquot (\~100 µL) of CEM/VLB1000 cell culture suspension was taken for each of the experiments. The microfluidic chip was mounted on the stage of an inverted fluorescence microscope, and the equipment was connected to a CCD camera interfaced with a computer. Before introducing the vial with the cells, the chip was sterilized by introducing 70% ethanol through reservoir 4 and allowing it to flow through the microchannels. After 70% ethanol was pipetted out of reservoir 4, α-MEM was added to the remaining chip reservoirs. Next, about 10 µL of the cell sample was drawn by a micropipette and added into reservoir 3 of the microfluidic chip. By manually adjusting the pressure inside the microfluidic chip, one cell was selected and retained within the central chamber for the experiment. A measurement window was set up, and the drug accumulation was monitored by repeatedly positioning the cell within a defined measurement window over a total period of 3100 s (the first 100 s were used for background measurement, after which the reagent solutions were introduced at 1000 s intervals). The accumulation curves were processed and background-corrected [5,8,25]. The fold increases were calculated by normalizing the DNR accumulation in the presence of inhibitors to the baseline DNR accumulation measured in the same single cells.

<!-- image-->  
Figure 3. Design of the microfluidic single-cell chip. (A) A photograph image of the microchip colored with blue food dye. The microchip consists of 4 solution reservoirs and 1 cell-retention chamber. The dimensions of the microchip are 1.10 cm × 2.20 cm. (B) An image of the retained CEM/VLB1000 cell (as pointed by the red arrow) under 20× magnification, with chamber and channel dimensions shown in µm. The channel depth is 40 µm.

## 4. Conclusions

We evaluated the intracellular DNR accumulation in the presence of four ginsenosides: Rg3-S, Rg3-R, PPD, and PPT. Using the CEM/VLB1000 leukemia cell line, we compared the intracellular DNR accumulation in the presence of each ginsenoside to evaluate their relative efficacy at reversing MDR-mediated drug efflux. It was found that although Rg3-R and Rg3-S share similar chemical structures and are aglycones of PPD, Rg3-S exhibited greater potency in enhancing the intracellular DNR accumulation, and both Rg3 stereoisomers were more effective than PPD.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/ijms27062661/s1.

Author Contributions: Conceptualization, P.C.H.L. and R.N.S.W.; methodology, N.J., M.C., Y.C. and I.K.; formal analysis, N.J., M.C., Y.C. and I.K.; investigation, N.J., M.C., Y.C. and I.K.; resources, P.C.H.L. and R.N.S.W.; writing—original, N.J., M.C., Y.C. and I.K., writing—review, N.J., M.C., Y.C., I.K., P.Y.K.Y. and R.N.S.W.; supervision, P.C.H.L.; project admin, P.C.H.L.; funding acquisition, P.C.H.L. All authors have read and agreed to the published version of the manuscript.

Funding: Funding by NSERC of Canada as said in the paper, grant number is RGPIN-2022-03320.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The original contributions presented in this study are included in the article/Supplementary Material. Further inquiries can be directed to the corresponding author.

Acknowledgments: We thank the funding from Natural Sciences and Engineering Research Council (NSERC) of Canada.

Conflicts of Interest: The authors declare no conflicts of interest.

## References

1. Hu, X.F.; Martin, T.J.; Bell, D.R.; De Luise, M.; Zalcberg, J.R. Combined use of cyclosporine-A and verapamil in modulating multidrug resistance in human leukemia cell lines. Cancer Res. 1990, 50, 2953–2957.

2. Khamenehfar, A.; Wan, C.P.L.; Li, P.C.H.; Letchford, K.; Burt, H.M. Same-single-cell analysis using the microfluidic biochip to reveal drug accumulation enhancement by an amphiphilic diblock copolymer drug formulation. Anal. Bioanal. Chem. 2014, 406, 7071–7083. [CrossRef]

3. Rathod, S.; Desai, H.; Patil, R.; Sarolia, J. Non-ionic Surfactants as a P-Glycoprotein(P-gp) Efflux Inhibitor for Optimal Drug Delivery—A Concise Outlook. AAPS PharmSciTech 2022, 23, 55. [CrossRef]

4. Bruckmueller, H.; Cascorbi, I. ABCB1, ABCG2, ABCC1, ABCC2, and ABCC3 drug transporter polymorphisms and their impact on drug bioavailability: What is our current understanding? Expert Opin. Drug Metab. Toxicol. 2021, 17, 369–396. [CrossRef] [PubMed]

5. Khamenehfar, A.; Gandhi, M.K.; Chen, Y.; Hogge, D.E.; Li, P.C.H. Dielectrophoretic Microfluidic Chip Enables Single-Cell Measurements for Multidrug Resistance in Heterogeneous Acute Myeloid Leukemia Patient Samples. Anal. Chem. 2016, 88, 5680–5688. [CrossRef] [PubMed]

6. Li, X.; Ling, V.; Li, P.C.H. Same-single-cell analysis for the study of drug efflux modulation of multidrug resistant cells using a microfluidic chip. Anal. Chem. 2008, 80, 4095–4102. [CrossRef]

7. Li, X.; Chen, Y.; Li, P.C.H. A simple and fast microfluidic approach of same-single-cell analysis (SASCA) for the study of multidrug resistance modulation in cancer cells. Lab Chip 2011, 11, 1378–1384. [CrossRef] [PubMed]

8. Khamenehfar, A.; Beischlag, T.V.; Russell, P.J.; Ling, M.T.P.; Nelson, C.; Li, P.C.H. Label-free Isolation of a Prostate Cancer Cell among Blood Cells and the Single-Cell Measurement of Drug Accumulation Using an Integrated Microfluidic Chip. Biomicrofluidics 2015, 9, 064104. [CrossRef]

9. Ruan, W.; Lai, M.; Zhou, J. Anticancer effects of Chinese herbal medicine, science or myth? J. Zhejiang Univ. Sci. B 2006, 7, 1006–1018. [CrossRef]

10. Chai, S.; To, K.K.; Lin, G. Circumvention of multi-drug resistance of cancer cells by Chinese herbal medicines. Chin. Med. 2010, 5, 26. [CrossRef]

11. Chang, Y.; Fu, Q.; Lu, Z.; Jin, Q.; Jin, T.; Zhang, M. Ginsenoside Rg3 combined with near-infrared photothermal reversal of multidrug resistance in breast cancer MCF-7/ADR cells. Food Sci. Nutr. 2024, 12, 5750–5761. [CrossRef]

12. Peng, S.; Wang, J.; Lu, C.; Xu, Z.; Chai, J.; Ke, Q.; Deng, X. Emodin enhances cisplatin sensitivity in non-small cell lung cancer through Pgp downregulation. Oncol. Lett. 2021, 21, 230. [CrossRef] [PubMed]

13. Chang, Y.S.; Seo, E.K.; Gyllenhaal, C.; Block, K.I. Panax ginseng: A role in cancer therapy? Integr. Cancer Ther. 2003, 2, 13–33. [CrossRef]

14. Kim, W.Y.; Kim, J.M.; Han, S.B.; Lee, S.K.; Kim, N.D.; Park, M.K.; Kim, C.K.; Park, J.H. Steaming of ginseng at high temperature enhances biological activity. J. Nat. Prod. 2000, 63, 1702–1704. [CrossRef] [PubMed]

15. Mochizuki, M.; YOO, Y.; Matsuzawa, K.; Sato, K.; Saiki, I.; Tonooka, S.; Samukawa, K.; Azuma, I. Inhibitory effect of tumor metastasis in mice by saponins, ginsenoside-Rb2, 20(R)- and 20(S)-ginsenoside-Rg3, of red ginseng. Biol. Pharm. Bull. 1995, 18, 1197–1202. [CrossRef]

16. Kim, S.-W.; Kwon, H.-Y.; Chi, D.-W.; Shim, J.-H.; Park, J.-D.; Lee, Y.-H.; Pyo, S.; Rhee, D.-K. Reversal of P-glycoprotein-mediated multidrug resistance by ginsenoside Rg3. Biochem. Pharmacol. 2003, 65, 75–82. [CrossRef]

17. Yun, T.K.; Lee, Y.S.; Lee, Y.H.; Kim, S.I.; Yun, H.Y. Anticarcinogenic effect of Panax ginseng C.A. Meyer and identification of active compounds. J. Korean Med. Sci. 2001, 16, S6-18. [CrossRef]

18. Feng, S.-L.; Luo, H.-B.; Cai, L.; Zhang, J.; Wang, D.; Chen, Y.-J.; Zhan, H.-X.; Jiang, Z.-H.; Xie, Y. Ginsenoside Rg5 overcomes chemotherapeutic multidrug resistance mediated by ABCB1 transporter: In vitro and in vivo study. J. Ginseng Res. 2020, 44, 247–257. [CrossRef]

19. Uhr, L.; Chen, Y.; Sit, D.; Li, P.C.H. Ginsenosides in commercial ginseng products analyzed by liquid chromatography-tandem mass spectrometry. Int. Sch. Res. Not. 2014, 2014, 486842. [CrossRef]

20. Yue, P.Y.; Wong, D.Y.; Wu, P.; Leung, P.; Mak, N.; Yeung, H.; Liu, L.; Cai, Z.; Jiang, Z.-H.; Fan, T.; et al. The angiosuppressive effects of 20(R)-ginsenoside Rg3. Biochem. Pharmacol. 2006, 72, 437–445. [CrossRef] [PubMed]

21. Park, J.-D.; Kim, D.-S.; Kwon, H.-Y.; Son, S.-K.; Lee, Y.-H.; Baek, N.-I.; Kim, S.-I.; Rhee, D.-K. Effects of ginseng saponin on modulation of multidrug resistance. Arch. Pharmacal Res. 1996, 19, 213–218. [CrossRef]

22. Zhao, Y.; Bu, L.; Yan, H.; Jia, W. 20S-Protopanaxadiol inhibits P-glycoprotein in multidrug resistant cancer cells. Planta Med. 2009, 75, 1124–1128. [CrossRef] [PubMed]

23. Park, M.W.; Ha, J.; Chung, S.H. 20(S)-ginsenoside Rg3 enhances glucose-stimulated insulin secretion and activates AMPK. Biol. Pharm. Bull. 2008, 31, 748–751. [CrossRef]

24. Rahimi, A.; Sharifi, H.; Li, P.C. Cytosolic Calcium Measurement Utilizing a Single-Cell Biochip to Study the Effect of Curcumin and Resveratrol on a Single Glioma Cell. In Single-Cell Assays: Genomics, Microfluidics and Drug Discovery; Li, P.C.H., Wu, A.R., Eds.; Springer Nature: New York, NY, USA, 2023; pp. 13–25. [CrossRef]

25. Chen, Y.; Chiem, M.; Joshi, N.; Li, P.C. Real-Time Single-Cell Measurement and Kinetic Modeling of Daunorubicin Uptake in Multidrug Resistant Leukemia Cells Using a Microfluidic Biochip. Preprints 2026, 2026020925.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.