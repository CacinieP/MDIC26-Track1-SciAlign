RESEARCH ARTICLE OPEN ACCESS

# Optimized Bioconversion of Naringenin to Hesperetin in With Halide Methyltransferase-Mediated Escherichia coli-Adenosylmethionine Regeneration

Maik Wildhagen1 Nina Malke1 Qimin Wang2 Xiaoying Zhuang2 Sascha Beutel1

1 Institute of Technical Chemistry, Leibniz University Hannover, Hannover, Germany 2Institute of Photonics, Leibniz University Hannover, Hannover, Germany

Correspondence: Sascha Beutel (beutel@iftc.uni-hannover.de)

Received: 9 August 2025 Revised: 5 December 2025 Accepted: 21 January 2026

Keywords: halide methyltransferase hesperetin | HpaBC | O-methyltransferase | whole-cell biocatalysis

## ABSTRACT

Hesperetin is a bioactive flavonoid with potential applications in pharmaceuticals and nutraceuticals, yet its low natural abundance limits commercial use. In this study, a two-step whole-cell bioconversion process was developed for the microbial production of hesperetin from naringenin in Escherichia coli. The 4-hydroxyphenylacetate-3-hydroxylase enzyme complex (HpaBC) enabled cytochrome P450-independent conversion of naringenin to eriodictyol. Subsequent 4′-O-methylation was achieved using a plant-derived flavonoid 4’-O-methyltransferase (FOMT) coupled with a halide methyltransferase (HMT) for in situ S-adenosylmethionine (SAM) regeneration. Enzyme activity was first confirmed individually in vitro and in vivo, followed by integration into recombinant whole-cell systems, co-expressing all desired enzymes. Process optimization through delayed co-substrate addition, improving induction conditions, and machine learning-guided parameter selection increased hesperetin yields up to 70.6% with minimal byproduct formation. This work demonstrates the feasibility of combining process development and digital optimization strategies for the sustainable production of methylated flavonoids in microbial systems. The resulting E. coli platform provides a scalable blueprint for future biotechnological applications involving cofactor-dependent plant secondary metabolism.

## 1 Introduction

Flavonoids constitute one of the largest groups of plant-derived secondary metabolites, best known for the yellow-to-reddish hues they impart to flowers and fruits as well as for a broad spectrum of bioactivities beneficial to human health [1–3]. Their antioxidant, anti-inflammatory, anti-microbial, anti-viral, anti-carcinogenic, and cardioprotective properties, together with their ability to modulate key metabolic and signaling pathways, have sparked great interest in their application as pharmaceuticals, nutraceuticals, and cosmetic ingredients [4–6]. Among the more than 8000 flavonoids identified so far, hesperetin, a 4′-O-methylated flavanone that naturally occurs only in trace amounts in citrus peels, has attracted particular attention [7]. Beyond the general advantages related to the flavanone scaffold, hesperetin acts as a positive allosteric modulator of sweet taste receptors, enhancing the perceived sweetness of sucrose solutions by up to 41% at concentrations as low as 100 ppm, without binding to the active site itself [8]. This receptor conformational change facilitates sweeter taste perception and may significantly reduce the amount of sugar

## Practical application

Hesperetin is a bioactive flavonoid with antioxidant, antiinflammatory, and sweet taste–modulating properties, making it highly attractive for applications in functional foods, beverages, and nutraceuticals. However, its low natural abundance and poor extractability from plant material limit its commercial use. This study presents a scalable microbial production route for hesperetin based on a recombinant Escherichia coli strain capable of converting the inexpensive precursor naringenin into hesperetin through a two-step enzymatic cascade. The integration of a P450-independent hydroxylase, a plant-derived methyltransferase, and a onestep SAM regeneration module enables a cofactor-efficient, solvent-free bioprocess under mild conditions. Systematic optimization and machine learning-guided process development led to high product yields and minimal byproduct formation. The presented platform provides a sustainable alternative to chemical synthesis or plant extraction and offers a blueprint for the microbial production of other methylated flavonoids. This makes the process particularly relevant for companies seeking natural ingredients for health-promoting products or sugar-reduced formulations.

needed in food and beverage formulations [8, 9]. Furthermore, hesperetin has demonstrated neuroprotective properties [10, 11] and an inhibitory effect on cholesterol biosynthesis, which results in a reduction of cholesterol levels [12]. Unfortunately, low natural abundance, agricultural seasonality, and the environmental footprint of conventional solvent-based extraction hamper the sustainable supply of hesperetin at high purity and competitive cost [13, 14].

Biotechnological production of natural compounds has become increasingly important in recent decades and offers a compelling alternative to conventional extraction methods from natural sources [15]. In vivo whole-cell biocatalysis can circumvent the use of toxic organic solvents, unlock otherwise inaccessible reaction routes, and streamline cofactor regeneration, thereby lowering resource consumption and waste generation relative to traditional chemical processing [16–19]. Escherichia coli, in particular, has emerged as a versatile microbial factory owing to its fast growth, well-characterized genetics, and the availability of a rich toolbox for recombinant protein expression and metabolic engineering [20, 21]. Moreover, the flavonoid pathway is modular: once the key hydroxylases, reductases, and transferases are functionally expressed, E. coli can be modified to convert inexpensive precursors into high-value flavonoids under mild process conditions [22].

Hesperetin can, in principle, be obtained from readily available naringenin by sequential hydroxylation at the 3′-position followed by regioselective 4′-O-methylation (Figure 1) [13, 23]. In plants, these steps are catalyzed by cytochrome-P450- dependent flavonoid-3‘-hydroxylases (F3’H) [24, 25] and Sadenosylmethionine (SAM)-dependent flavonoid 4’-O-methyltransferases (FOMTs) [26–28], respectively. Translating such a pathway into a bacterial host poses several challenges: P450 mono-oxygenase’s often display low activity in prokaryotes [29], and the dependency on SAM requires an efficient regeneration strategy to sustain enzyme function throughout the bioconversion and ensure economic viability [30].

Even though the P450 mono-oxygenase flavonoid 3’-hydroxylase (F3’H) has already been successfully expressed in E. coli [13], there are alternative enzymes that are better suited for biotechnological applications in this host. Studies have demonstrated that the native E. coli 4-hydroxyphenylacetate-3-hydroxylase enzyme complex (HpaBC) can act as a robust, soluble alternative to plant-derived P450s, converting naringenin to eriodictyol with high specificity [31, 32]. In addition, Wang et al. [32] showed that HpaB from Rhodococcus opacus B-4 exhibits substantially higher activity toward naringenin than the E. coli HpaB, which highlights the potential of using non-native HpaB homologs to further enhance conversion efficiency.

Likewise, plant FOMTs can be functionally expressed in E. coli to convert eriodictyol to hesperetin, but their activity depends on sufficient SAM supply [33]. Although E. coli possesses a native SAM regeneration cycle, its capacity may become limiting under the high cofactor demand imposed by heterologous bioconversion pathways [13]. Regeneration strategies based on halide methyl-transferases (HMTs), while so far demonstrated only in vitro, offer a promising route to enhance cofactor availability via a direct, single-enzyme regeneration mechanism [30, 34].

In addition to such enzyme-based exogenous regeneration approaches, recent studies have shown that enhancing endogenous SAM recycling through overexpression of metK, mtn, and luxS can significantly increase intracellular SAM availability [13, 35, 36]. MetK encodes SAM synthase, which catalyzes SAM formation, while mtn and luxS encode S-adenosylhomocysteine (SAH) nucleosidase and S-ribosylhomocysteine lyase, respectively. Together, these two enzymes degrade SAH, a potent inhibitor of FOMTs, thereby sustaining SAM-dependent methylation activity.

In the present study, however, we focused on implementing the one-step halide-methyltransferase-based regeneration system provided by Bornscheuer and co-workers [34], as it was readily available and directly compatible with the E. coli Δmtn strain used in this study. Nevertheless, evaluating endogenous SAM regeneration pathways is a promising alternative approach that is currently being explored in ongoing follow-up studies but was beyond the scope of the present work. Apart from the challenge of implementing a sufficient cofactor regeneration system, the formation of undesired byproducts due to enzyme promiscuity plays a major role in the development of in vivo whole-cell biocatalytic processes. In the context of microbial hesperetin production, the limited substrate specificity of certain FOMTs can lead to the formation of isosakuranetin, a 4′-Omethylated derivative of naringenin [23]. This byproduct is not accepted by the hydroxylase HpaBC and therefore accumulates as a metabolic dead end, ultimately reducing the yield of the desired product, hesperetin. Previous studies have addressed this issue by engineering FOMT variants with improved specificity. For instance, Liu et al. [23] developed a mutated version of the Mentha x piperita FOMT that displayed enhanced activity toward eriodictyol and reduced conversion of naringenin. While such approaches highlight the potential for enzyme optimization, the issue of byproduct formation remains a relevant challenge, particularly in complex intracellular environments. In this study, we additionally explored process-based strategies to mitigate isosakuranetin formation, focusing on the temporal coordination of co-substrate availability to favor the desired reaction pathway.

<!-- image-->  
FIGURE 1 Reaction scheme of two-step flavonoid bioconversion using HpaBC and FOMT with HMT-mediated SAM regeneration. Dead end byproduct formation of isosakuranetin, due to methylation of the substrate naringenin.

In light of the aforementioned findings, the objective of this study is to establish an integrated whole-cell approach for the efficient conversion of naringenin to hesperetin in E. coli. Initially, the catalytic performance of the HpaBC hydroxylase for conversion of naringenin to eriodictyol was evaluated in the host organism. Concurrently, the activity of a plant-derived 4′-O-methyltransferase coupled with the HMT-based SAM regeneration system was assessed both in vitro and in vivo, to evaluate the conversion of eriodictyol to hesperetin. These components were subsequently combined into single recombinant strains, thereby enabling the one-pot bioconversion of naringenin to hesperetin. In order to further enhance product yield and reduce undesired byproduct formation, key process parameters, including timing and concentration of (co-)substrate addition, induction conditions, and cultivation temperature, were systematically optimized by using conventional one-factor-at-a-time (OFAT) experiments, design of experiments (DoE) and machine learning (ML) approaches.

## 2 Methods

## 2.1 Strain and Plasmids

An overview of all strains and plasmids used and generated in this work is listed in Table 1. The plasmid pHpaBC harbors the genetic information of 4-hydroxyphenylacetate 3- monooxygenase (HpaB) and the corresponding flavin oxidoreductase (HpaC). Based on the results of Wang et al., a variant of the enzyme HpaB from Rhodococcus opacus B-4 is used, which has an amino acid exchange from tyrosine to alanine at position 215 [32]. Genetic information for HpaC originated from Pseudomonas aeruginosa [37]. The 4’-flavonoid O-methyltransferase located on pFOMTS142V was designed according to Liu et al. and has an additional amino acid exchange from serine to valine [13, 23]. The plasmids pFOMT, pFOMTS142V, and pHpaBC were synthesized and cloned by BioCat GmbH (Heidelberg, Germany). The plasmid pET28a(+)-HMT (pHMT) present in the strain E. coli BL21(DE3) Δmtn was kindly provided by the Bornscheuer group from Uni Greifswald [34]. This strain carries a deletion of the mtn gene encoding SAH nucleosidase, thereby preventing the degradation of SAH. SAH serves as the substrate for HMT in the one-step regeneration of SAM. The plasmids were isolated from overnight cultures of the corresponding strains using the QIAprep Spin Miniprep Kit (Qiagen, Netherlands). The identity of the plasmids was verified by analytical restriction digestion (Figures S1– S3). The resulting plasmid DNA was stored at −20◦C until use.

## 2.2 Strain Construction

Plasmid HpaBC was transformed into chemical-competent E. coli BL21(DE3) cells from Novagen (Merck, Germany) via heat shock to obtain the strain E. coli_HpaBC. To generate the strains E. coli_FOMT, E. coli_FOMT-HMT, E. coli_WCB1 and E. coli_WCB2, the strain E. coli Bl21(DE3) Δmtn was made chemically competent according to the method of Green and Rogers and subsequently (co)-transformed via heat shock with the corresponding plasmids [38] (Table 2).

## 2.3 Cultivation and Flavonoid Conversion

Small-scale cultivations for enzyme production and flavonoid bioconversion were conducted in baffled shake flasks. Therefore 100 mL of terrific broth (TB) medium (12 $\mathrm { g } \mathrm { L } ^ { - 1 }$ tryptone, 24 $\mathrm { g } \mathrm { L } ^ { - 1 }$ yeast extract, $5 \ { \tt g } \ { \tt L } ^ { - 1 }$ glycerol, 100 mL $\mathrm { L } ^ { - 1 }$ potassium phosphate buffer) or AM-medium (according to Jones et al. [39]) supplemented with appropriate antibiotics (kanamycin 50 mg $\mathrm { L } ^ { - 1 }$ and or streptomycin $5 0 \mathrm { m g L ^ { - 1 } }$ and or chloramphenicol $3 4 \mathrm { g } \mathrm { L } ^ { - 1 } )$ were used in 500 mL baffled shake flasks. Precultures were performed in 20 mL of lysogeny broth (LB) medium supplemented with the appropriate antibiotics in 100 mL baffled shake flasks. Precultures were inoculated with glycerol stocks of cells and incubated overnight at $3 7 ^ { \circ } \mathrm { C }$ and 150 rpm in an orbital shaker. The main culture was inoculated with preculture to give an initial $\mathrm { O D } _ { 6 0 0 }$ of 0.1 rel. AU and incubated at $3 7 ^ { \circ } \mathrm { C }$ and 150 rpm in an orbital shaker. Gene expression was induced by the addition of 0.5 mM isopropyl-ß-thiogalactopyranoside (IPTG) and the temperature was lowered to 16◦C, 18◦C, 24.2◦C, or $3 0 ^ { \circ } \mathrm { C }$ to prevent inclusion body formation.

TABLE 1 Overview of the plasmids used in this work.
<table><tr><td colspan="2"></td><td colspan="2">Description (origin of replication, compatibility group, promoter, antibiotic resistance, and genes)</td></tr><tr><td>Name pHpaBC</td><td>Plasmid pCDFDuet-1-HpaB-HpaC</td><td>CloDF13, C, T7, Streptomycin, containing the gens for the 4-hydroxy</td><td>Reference [32, 37]</td></tr><tr><td>pFOMT</td><td>pACYCDuet-1-4&#x27;FOMT</td><td>phenylacetate 3-monooxygenase enzyme complex P15A, B, T7, Kanamycin, containing the gene for 4&#x27;-flavonoid</td><td>[13]</td></tr><tr><td></td><td></td><td>O-methyltransferase pFOMTS142V pACYCDuet-1-4&#x27;FOMTS142V P15A, B, T7, Kanamycin, containing the gene for mutate 4flavood</td><td>[23]</td></tr><tr><td></td><td></td><td>O-methyltransferase</td><td></td></tr><tr><td>pHMT</td><td>pET28a(+)-HMT</td><td>PBR322, A, T7, Chloramphenicol, containing the gene for the halide methyltransferase</td><td>[33]</td></tr></table>

TABLE 2 Overview of the strains used in this work.
<table><tr><td>Name</td><td>Strain</td><td>Plasmids</td><td>Reference</td></tr><tr><td>E. coli_HpaBC</td><td>E. coli Bl21(DE3)</td><td>pHpaBC</td><td>[*]</td></tr><tr><td>E. coli_FOMT</td><td>E. coli Bl21(DE3) Δmtn</td><td>pFOMT</td><td>[*]</td></tr><tr><td>E. coli_HMT</td><td>E. coli Bl21(DE3) Δmtn</td><td>pHMT</td><td>[33]</td></tr><tr><td>E. coli_FOMT-HMT</td><td>E. coli Bl21(DE3) Δmtn</td><td>pFOMT, pHMT</td><td>[*]</td></tr><tr><td>E. coli_WCB1</td><td>E. coli Bl21(DE3) ∆mtn</td><td>pHpaBC, pFOMT, pHMT</td><td>[*]</td></tr><tr><td>E. coli_WCB2</td><td>E. coli Bl21(DE3) Δmtn</td><td>pHpaBC, pFOMTS142V, pHMT</td><td>[*]</td></tr></table>

\*Strain constructed in this work.

Larger-scale cultivations were carried out in a 2 L stirred tank bioreactor (Biostat A+, Sartorius, Germany) with a working volume of 1.5 L TB medium supplemented with the appropriate antibiotics. The bioreactor was equipped with two Rushton impellers and was gassed with compressed air with an aeration rate of 1 vvm. The stirrer speed is cascaded (400–700 rpm) so that the oxygen partial pressure $\left( \mathsf { p O } _ { 2 } \right)$ in the culture does not decrease below 30% (v/v). Foam production was controlled by the addition of antifoam. The pH value was set to 7.5 and was controlled by titration with 1 M HCl and 1 M NaOH. Precultures for the bioreactor were carried out in 100 mL LB medium in 500 mL baffled shake flasks.

No flavonoid substrate was added for recombinant enzyme production of FOMT and HMT, while 0.367 mM (100 mg L−1 ) naringenin or 0.346 mM (100 mg L−1 ) eriodictyol together with

1 mM MeI were added at various time points after induction of the enzyme expression for bioconversion.

## 2.4 In Vitro Enzymatic Conversion of Eriodictyol to Hesperetin Using FOMT and HMT

To test the enzymatic conversion of eriodictyol to hesperetin with one-step cofactor regeneration in vitro, isolated enzymes of FOMT and HMT were used. Since the enzymes possess an Nterminal histidine tag, purification by affinity chromatography using a nickel-nitrilotriacetic acid column (Ni-NTA) was possible. Therefore, the enzymes were overexpressed as described in Section 2.2, and cells were harvested by centrifugation (5000 rpm, 30 min, and $4 ^ { \circ } \mathrm { C } ) .$ . Cell pellet was suspended in TRIS buffer (40 mM TRIS-HCl, 100 mM NaCl) containing 25 mM imidazole. The cells were disrupted by high-pressure homogenization (15,000 psi, 5 cycles), and cell debris was removed by centrifugation (5000 rpm, 50 min, and $4 ^ { \circ } \mathrm { C } )$ . The supernatant was filtered using a bottle top filter with 0.22 µm pore size. The FOMT and HMT enzymes were purified by $\mathrm { N i } ^ { 2 + }$ -decorated IMAC using the ÄKTAstart (Cytiva) system. The Ni-NTA column (HisTrap Fast Flow Crude, Cytiva) was loaded with the filtered supernatant. FOMT or HMT was eluted with imidazole using a gradient with a maximum concentration of 500 mM. Proteins were detected by absorption at 280 nm, and the peak fraction of the elution was collected. Imidazole was removed by buffer exchange using size exclusion chromatography (SEC) (HiTrap, Desalting Columns, Cytiva) and ultrafiltration (UF) with a centrifugal concentrator with a cutoff of 30 kDa. FOMT and HMT enzymes were preserved in a preservation buffer (20 mM TRIS-HCl, 1 mM DTT, 100 mM NaCl, 20% (v/v) glycerol) and stored at −80◦C.

For the in vitro enzymatic reaction procedure, the purified enzymes, FOMT and HMT, were combined with the substrate eriodictyol, the alkyl donor methyl iodide (MeI), and the cofactors SAH and SAM. The reaction was carried out in 2 mL reaction vessels at $2 7 ^ { \circ } \mathrm { C }$ and 1200 rpm and incubated for 24 h.

## 2.5 Extraction of Flavonoids From Aqueous Solution

Flavonoids were extracted from the entire culture broth containing cells via liquid-liquid extraction. Therefore, 1 mL of the sample was vigorously mixed with three times 0.5 mL of ethyl acetate. The organic phase was collected and evaporated using a rotational vacuum concentrator. The remaining pellet was dissolved in 1 mL of MeOH and transferred into HPLC vials.

## 2.6 Analytical Procedures

## 2.6.1 Sodium Dodecyl Sulfate Polyacrylamide Gel Electrophoresis (SDS-PAGE)

The SDS-PAGE sample volume was normalized to an $\mathrm { O D } _ { 6 0 0 }$ of 2.0 rel. AU. Cells were pelleted by centrifugation (10 min, $1 0 , 0 0 0 \times g ,$ and $4 ^ { \circ } \mathrm { C } )$ , and the supernatant was discarded. Cell lysis was performed enzymatically using the BugBuster Protein Extraction Reagent (Merck, Germany) according to the manufacturer’s instructions. Soluble and insoluble protein fractions were separated by centrifugation (20 min, $1 0 , 0 0 0 \times g ,$ and $4 ^ { \circ } \mathrm { C } )$ The supernatant contains the soluble fraction (SF), and the pellet represents the insoluble fraction (IF). The supernatant was removed, and the pellet was suspended with the same volume of ${ \mathrm { d } } { \mathrm { d } } \mathrm { H } _ { 2 } \mathrm { O } .$ Both protein fractions were mixed with 4× Laemmli loading buffer and heated at 95◦C for 5 min. All analyses were performed in 10% SDS-polyacrylamide gels. Protein separation was performed at constant voltage and varying current. Gels were stained with colloidal Coomassie.

## 2.6.2 HPLC

The flavonoids extracted from the samples were chromatographically separated using a Zorbax SB-C18 reversed-phase column with a particle size of 1.8 µm on an HPLC system (Chromaster, VWR International, Germany). The eluents 0.1% (v/v) acetic acid solution and pure acetonitrile were used in a gradient program. Detection was performed with a diode array detector at a wavelength of 280 nm. Quantification of the flavonoids was performed with a mixture of commercially available standards of naringenin, eriodictyol, hesperetin, and isosakuranetin in concentrations between 0.003 and 3.769 mM (equal to 0.001– $1 . 0 0 0 \ \mathrm { g } \ \mathrm { L } ^ { - 1 } )$ . Calibration curves were calculated from the peak area (Table S1, Figure S4).

For qualitative identification of the flavonoids, retention times obtained from HPLC-DAD chromatograms were compared with those of the corresponding analytical standards (Figure S5). In addition, selected samples were analyzed by nano-LC-MS to confirm the identity of naringenin, eriodictyol, hesperetin, and isosakuranetin based on their exact mass-to-charge ratios (Tables S2 and S3; Figures S6 and S7).

## 2.7 Use of AI Tools

Minor language editing was assisted by ChatGPT (OpenAI, GPT-4, 2024 version) to improve grammar and clarity. All research content, data analysis, and interpretations were solely generated by the authors.

## 3 Results and Discussion

## 3.1 Hydroxylation of Naringenin to Eriodictyol Using HpaBC

The first of the two successive reactions, the hydroxylation of naringenin to eriodictyol, was tested using an in vivo bioconversion approach. As mentioned in the introduction, hydroxylation of flavonoids is usually performed by cytochrome P450s in the natural biosynthetic pathway. However, expressing P450s in E. coli is challenging due to the unique characteristics of these enzymes and the differences between their native environments and the bacterial host. These differences include membrane association and folding mechanisms. Therefore, the non-cytochrome P450-dependent monooxygenase HpaB was used, and the engineered strain E. coli BL21(DE3) harboring the plasmid pHpaBC (E. coli_HpaBC) was constructed for this purpose. This plasmid carries a codon-optimized gene for a Y215A variant of HpaB derived from Rhodococcus opacus B-4, which exhibits enhanced affinity for naringenin [32], and a gene for HpaC from P. aeruginosa, which acts as the corresponding HpaC [37]. These genes are placed under the control of T7 promoters and co-expressed to facilitate efficient hydroxylation of naringenin.

For initial assessment of in vivo activity, shake flask cultures of E. coli_HpaBC were cultivated in AM-medium, a semi-defined formulation supplemented with glycerol as the carbon source. This medium was chosen based on literature results [31]. Cultures were induced with IPTG at an $\mathrm { O D } _ { 6 0 0 }$ of approximately 0.7 rel. AU, followed by a temperature downshift to $3 0 ^ { \circ } \mathrm { C }$ to reduce the formation of inclusion bodies. One hour post induction, naringenin was added to a final concentration of 0.367 mM (100 mg L−1 ) to initiate the bioconversion reaction.

Growth behavior of E. coli_HpaBC remained largely unaffected by the presence of naringenin. After an initial lag phase, the strain exhibited linear growth, consistent with previously reported cold-shift induction protocols [40–42]. Final $\mathrm { O D } _ { 6 0 0 }$ values were comparable to control cultures and reached approximately 9– 11 rel. AU, indicating no major cytotoxic effects from either the substrate or the product (data not shown). Protein expression analysis using SDS-PAGE confirmed high-level expression of HpaC, detectable as a distinct band at the expected molecular weight of 20.4 kDa. Despite the detection of a larger protein band in the IF, HpaC was also identified in the SF, suggesting that it is expressed in active conformation. In contrast, the HpaB protein (59.3 kDa) could not be conclusively visualized, likely due to overlapping native proteins in that size range and an intrinsic expression imbalance between the two components (Figure 2A) [43]. Nevertheless, a successful bioconversion of naringenin could provide indirect evidence for the functional expression and activity of both enzymes. Quantitative HPLC analysis of samples taken at regular intervals over the cultivation course revealed a complete conversion of naringenin to eriodictyol within the first 3.25 h following substrate addition (Figure 2B). The concentration profiles of both compounds displayed a mirrored pattern, with the decrease in naringenin concentration precisely matching the increase in eriodictyol levels, confirming stoichiometric conversion without the accumulation of side products. The maximum eriodictyol concentration observed was 0.318 mM, equal to the initial amount of naringenin measured, indicating 100% molar conversion efficiency at the reaction peak. However, extended cultivation beyond this time point resulted in a noticeable decline in eriodictyol concentration, suggesting product instability under the applied conditions. This degradation is attributed to either microbial catabolism or spontaneous chemical decomposition, possibly via catechol-mediated autoxidation. Eriodictyol contains a vicinal dihydroxy group (catechol moiety) on the B-ring, rendering it particularly susceptible to oxidative degradation, especially in the presence of reactive oxygen species or trace metal ions commonly found in media components [44–46]. Notably, no intermediate compounds or byproducts were observed in the HPLC chromatograms, underlining the high regioselectivity and substrate specificity of the HpaBC complex under these conditions (Figure S8).

<!-- image-->

B  
<!-- image-->  
FIGURE 2 Bioconversion of naringenin to eriodictyol using HpaBC from R. opacus and P. aeruginosa in E. coli. (A) Analysis of the overexpression of the insoluble (IF) and soluble (SF) protein fractions from E. coli_HpaBC fermentation using 10% SDS-PAGE. Samples from fermentation at 0, 3, and 24 h after induction are shown. (M) Protein molecular weight marker. (B) Growth behavior $\mathrm { ( O D _ { 6 0 0 } ) }$ and flavonoid concentration profiles during the bioconversion of naringenin to eriodictyol using E. coli_HpaBC. Sampling gaps resulted from the mandatory overnight pause.

In summary, the use of the heterologous HpaBC complex from R. opacus and P. aeruginosa expressed from the pCDFDuet1 vector in E. coli enabled efficient, high-yield conversion of naringenin to eriodictyol in AM-medium. Despite partial degradation of the product over time, the system achieved full substrate turnover without detectable byproduct formation, laying a solid foundation for further downstream modification toward hesperetin. Future optimization strategies may include stabilizing eriodictyol in situ or shortening the total cultivation time to minimize product loss.

## 3.2 Methylation of Eriodictyol to Hesperetin Using FOMT and HMT

The enzymatic methylation of eriodictyol to hesperetin represents the second and final step in the proposed biocatalytic cascade.

This transformation is catalyzed by a 4′-O-methyltransferase (FOMT), which specifically transfers a methyl group to the hydroxyl group at the 4′-position of the B-ring of eriodictyol [13]. The reaction requires the cofactor SAM as a methyl donor, the regeneration of which is critical for economic and practical feasibility. For this purpose, a HMT was employed to enable a onestep regeneration of SAM from SAH, using MeI as a methyl group donor [30, 47].

To evaluate the performance of these enzymes, both in vitro and in vivo methylation strategies were tested. Three recombinant E. coli strains were constructed: one expressing only FOMT, one expressing only HMT, and a co-expressing strain harboring both enzymes. The genes encoding the FOMT from M. x piperita and the HMT from Arabidopsis thaliana were codon-optimized for E. coli and carried N-terminal His -tags for purification purposes. The HMT gene was introduced into a Δmtn variant of E. coli BL21 (DE3), which lacks the mtn gene encoding SAH nucleosidase, thus preventing the degradation of SAH, a prerequisite for efficient SAM regeneration [30]. All expression vectors used were compatible and carried different antibiotic resistance markers to allow for co-transformation and stable expression of both enzymes.

While the strains expressing individual enzymes showed comparable growth profiles, the co-expressing strain exhibited slightly slower growth in the early cultivation phase, likely due to the increased metabolic burden of carrying two plasmids (Figure 3A) [48]. However, this difference diminished over time, and all strains reached similar final cell densities. SDS-PAGE analysis confirmed successful expression of both FOMT and HMT, with HMT being produced primarily in soluble form and FOMT showing partially insoluble expression. Despite this, sufficient quantities of soluble enzyme were produced and purified for subsequent bioconversion experiments (Figure 3B).

To assess the catalytic function of the enzymes independently from cellular metabolism, in vitro methylation assays were performed using the purified enzymes. Both FOMT and HMT were produced and purified by immobilized metal affinity chromatography (IMAC) followed by SEC for desalting (DS) and UF to increase protein concentration. The quality of the purified proteins was confirmed by SDS-PAGE (Figure 3B). In the first methylation assay (1), eriodictyol (1.0 mM) was incubated with FOMT and a limiting amount of SAM (0.1 mM), equivalent to a 10:1 substrate-to-cofactor ratio. In the second assay (2), SAM was replaced with its product SAH (0.1 mM), and HMT together with MeI (8.0 mM) was added to allow regeneration of SAM. Quantitative HPLC analysis confirmed that hesperetin formation occurred in both reaction setups. The corresponding chromatograms for these in vitro assays are provided in the Supporting Information (Figure S9). The negative control (NC) reactions without enzymes yielded no product, indicating no chemical methylation of eriodictyol by MeI (Figure 3C). However, product formation was significantly higher in the reaction that included the regeneration system. In the absence of SAM recycling, only 0.11 mM hesperetin was detected, consistent with the initial SAM concentration, highlighting the cofactor as the limiting factor. In contrast, the reaction with HMT and MeI produced 0.67 mM hesperetin, corresponding to approximately 93% of the total flavonoid concentration detected in the reaction mixture. This implies that the SAM pool was successfully regenerated in multiple cycles, confirming the functionality of the regeneration module.

A  
<!-- image-->

<!-- image-->

C  
<!-- image-->

D  
<!-- image-->  
FIGURE 3 Bioconversion of eriodictyol to hesperetin using FOMT from Mentha x piperita and HMT from A. thaliana produced by E. coli. (A) Growth behavior of the HMT- and FOMT-producing strains E. coli_HMT, E. coli_FOMT and E. coli_FOMT-HMT. (B) Analysis of the overexpression of the insoluble (IF) and soluble (SF) protein fractions from E. coli_FOMT, E. coli_HMT and E. coli_FOMT-HMT fermentation using 10% SDS-PAGE. Samples from fermentation at different times after induction are shown. (M) Protein molecular weight marker. (C) Flavonoid concentration of the in vitro methylation of eriodictyol to hesperetin with isolated enzymes without (1) and with (2) cofactor regeneration. (NC) Negative control without enzymes. (D) Growth behavior $\left( \mathrm { O D } _ { 6 0 0 } \right)$ and flavonoid concentration profiles during the methylation of eriodictyol to hesperetin using E. coli_FOMT-HMT. Sampling gaps resulted from the mandatory overnight pause.

Encouraged by these in vitro results, in vivo methylation was investigated using the co-expressing E. coli_FOMT-HMT strain. Eriodictyol was added during exponential growth, 1 h after IPTG induction of enzyme expression. Compared to the hydroxylation process, the methylation reaction exhibited a delayed onset, with product formation only detectable toward the end of the cultivation (24 h) (Figure 3D). A final hesperetin concentration of 0.062 mM was achieved, corresponding to a yield of 17.8%. No major accumulation of flavonoids in the cells was observed, and HPLC data suggested the presence of an additional peak, possibly representing a degradation product (Figure S10).

Overall, both enzymes proved functional in vitro and in vivo. While the in vitro system demonstrated high conversion efficiency, the in vivo methylation approach was chosen for integration into the complete whole-cell cascade due to its simplicity and practical advantages for process development.

## 3.3 Establishing the Whole-Cell Bioconversion From Naringenin to Hesperetin Using HpaBC, FOMT, and HMT

To establish the complete whole-cell bioconversion route from naringenin to hesperetin, the previously separated hydroxylation and methylation reactions were combined in single E. coli strains. Two recombinant hosts, E. coli_WCB1 expressing HpaBC, FOMT, and HMT, and E. coli_WCB2, carrying the same modules but with a modified methyltransferase variant (FOMTS142V) according to Liu et al. [23], were evaluated for their ability to convert naringenin to hesperetin in vivo.

Initial bioconversion experiments were performed in shake flasks using TB medium. 1 h upon IPTG induction, the cultures were supplemented with 0.367 mM (100 mg L−1 ) naringenin and 1 mM MeI. Quantitative HPLC analysis of culture supernatants revealed that E. coli_WCB1 exhibited efficient hydroxylation, reaching 0.281 mM eriodictyol within 3 h (86% conversion of initial naringenin), with minimal byproduct formation in shake flasks (isosakuranetin < 0.003 mM) (Figure 4A). However, only 0.017 mM hesperetin was detected by the end of cultivation, likely due to limited methylation efficiency and oxidative degradation of eriodictyol [44–46]. In contrast, E. coli_WCB2 accumulated significantly more isosakuranetin (0.135 mM), indicating notable promiscuity of FOMTS142V toward naringenin despite prior reports of increased substrate specificity [23] (Figure 4B). Nevertheless, E. coli_WCB2 produced 0.076 mM hesperetin, corresponding to a 23% yield based on the starting naringenin concentration, substantially higher than that of E. coli_WCB1. This suggests that the FOMTS142V variant provides improved methylation of eriodictyol, albeit at the cost of elevated byproduct formation.

To investigate the effect of controlled cultivation conditions, both strains were cultivated in a 2 L stirred-tank bioreactor under regulated pH 7.5 and dissolved oxygen (30% pO ). Both strains reached similar growth profiles. While E. coli_WCB1 produced only 0.02 mM hesperetin (6% yield) (Figure 4C), E. coli_WCB2 reached a final concentration of 0.051 mM (19.2% yield) (Figure 4D). The relative proportion of hesperetin to isosakuranetin remained comparable to flask experiments, confirming the stability of the product profile across scales. In contrast to the shake flask experiments, the bioreactor cultivations resulted in lower overall conversion of naringenin to hesperetin. This difference can be explained by two factors. First, the substantially higher oxygen transfer rate in the bioreactor likely promoted the non-enzymatic oxidation of eriodictyol, whose catechol moiety is known to be highly sensitive to oxidative degradation [46, 49]. Consistent with this, we observed a progressive brown coloration of the culture broth during bioreactor cultivation, which is characteristic of the formation of oxidized polyphenol species [31, 50]. Such oxidation reduces the measurable total flavonoid concentration and decreases the amount of eriodictyol available for methylation. Second, the controlled pH of 7.5 in the bioreactor differs from the pH conditions in the shake flasks (approximately pH 7.0, uncontrolled) and may have reduced the activity of the SAM-dependent O-methyltransferase, resulting in lower product formation. Together, these effects explain why higher conversion was achieved in shake flasks compared to bioreactor cultivations.

Overall, both strains demonstrated successful whole-cell bioconversion of naringenin to hesperetin. While E. coli_WCB1 showed efficient hydroxylation with minimal byproduct formation, E. coli_WCB2 outperformed in total hesperetin yield, although more side product was formed. These results provide a foundation for further optimization toward a robust microbial production process.

## 3.4 Optimization of the Whole-Cell Bioconversion From Naringenin to Hesperetin

The next step in the process development was to optimize the whole-cell bioconversion process in order to increase hesperetin yield and reduce side product formation. Initially, conventional optimization strategies, such as OFAT experiments or DoE, were applied. Then the resulting process data formed the basis for developing ML algorithms for process optimization and digitalization. We selected the strain E. coli_WBC2 for optimization due to its higher product yield.

## 3.5 Effect of Delayed MeI Addition

To mitigate the formation of the undesired byproduct isosakuranetin during the bioconversion of naringenin to hesperetin, the influence of delayed MeI addition was systematically evaluated. The hypothesis was that postponing the supply of MeI, the methyl group donor required for SAM regeneration, could temporally decouple hydroxylation and methylation, thus reducing methylation of the substrate naringenin. Thus, E. coli_WCB2 was cultivated under identical conditions, with MeI added at 3, 6, 12, and 20 h after naringenin supplementation.

In addition to its effect on product selectivity, the impact of delayed MeI supplementation on the E. coli growth behavior was examined. Cultures in which MeI was added early (e.g., 3 h after naringenin supplementation) reached the highest optical densities, while those with later addition (e.g., +20 h) exhibited markedly reduced growth (Figure 5A). This is likely due to the strain’s dependency on MeI-driven SAM regeneration via HMT, as the native SAH-hydrolyzing pathway is disrupted in the Δmtn deletion strain [30]. In the absence of sufficient SAM, cellular metabolism and proliferation are negatively affected [51, 52]. These observations highlight the dual role of MeI, both enabling methylation activity and supporting overall cell viability in this engineered system.

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
FIGURE 4 Whole-cell bioconversion from naringenin to hesperetin using HpaBC from R. opacus and P. aeruginosa, FOMT (FOMTS142V) from Mentha x piperita and HMT from A. thaliana in E. coli. Growth behavior $\mathrm { ( O D _ { 6 0 0 } ) }$ and flavonoid concentration profiles during the bioconversion of naringenin to hesperetin by: (A) E. coli_WCB1 in shake flasks, (B) E. coli_WCB2 in shake flasks, (C) E. coli_WCB1 in controlled stirred tank bioreactor, and (D) E. coli_WCB2 in controlled stirred tank bioreactor. Sampling gaps resulted from the mandatory overnight pause.

Delayed addition led to significant differences in flavonoid conversion profiles. Figure 5B shows flavonoid concentration at the end of the respective bioconversion experiments, while the full time-resolved flavonoid concentration profiles are provided in Figure S11. A 12 h delay resulted in the highest product titer of 0.19 mM hesperetin, corresponding to a 55.7% yield, while simultaneously limiting the formation of the undesired side product isosakuranetin to just 0.07 mM, equivalent to 23% of the initially supplied naringenin (Figure 5B). In contrast, early MeI addition after 3 h led to substantially higher isosakuranetin levels (0.16 mM or 57.8%) and a reduced hesperetin yield of only 32.7% (0.103 mM), likely due to premature methylation of residual naringenin before its hydroxylation to eriodictyol. A 6 h delay yielded a comparable hesperetin concentration of 0.187 mM (55.3%) but slightly higher isosakuranetin levels (0.089 mM or 26.4%), suggesting partial improvement in selectivity. Notably, even a 20 h delay led to a relatively high hesperetin yield (46.7%), but isosakuranetin formation remained at 21.2%, and product titers were overall lower, possibly due to flavonoid degradation at late cultivation stages. These findings indicate that delaying MeI addition allows eriodictyol to accumulate prior to activation of the methylation pathway, thereby increasing conversion efficiency and improving product selectivity. Among the tested conditions, the 12 h delay was most effective, though a 6 h delay was selected for further process development due to its favorable balance of yield, selectivity, and operational practicality.

## 3.6 Optimization of Induction Parameters Using DoE

To improve recombinant enzyme production and maximize hesperetin yield, key induction parameters—temperature, optical density at induction $\mathrm { ( O D _ { 6 0 0 } ) }$ , and IPTG concentration—were optimized using DoE. A full-factorial design predicted that hesperetin formation would be highest (53.1%) when induction occurred at an $\mathrm { O D } _ { 6 0 0 }$ of 3.6 rel. AU and a temperature of 24.2◦C (Figure 5C,D). Conversely, lower induction densities and temperatures were associated with reduced product formation and increased isosakuranetin levels. However, model predictions diverged from experimental results: the highest measured hesperetin yield (55.7%) was achieved at parameters where the model had only forecasted 35%–40%, highlighting limitations of the initial model.

To validate the predictions, three cultivation experiments were performed under varying $\mathrm { O D } _ { 6 0 0 }$ conditions (1.6, 3.6, and

<!-- image-->

B  
<!-- image-->

<!-- image-->

<!-- image-->

E  
<!-- image-->  
FIGURE 5 Optimization of whole-cell bioconversion from naringenin to hesperetin using E. coli_WCB2. (A) Impact of delayed MeI supplementation on E. coli_WCB2 growth behavior $\scriptstyle ( \mathrm { O D } _ { 6 0 0 } ) .$ (B) Impact of delayed MeI supplementation on flavonoid concentration. (C) “Response Contour Plots” with final yield at the end of bioconversion of hesperetin and (D) isosakuranetin as target values; the x-axis shows $\mathrm { O D } _ { 6 0 0 }$ and the y-axis the temperature; red areas represent a high product yield and blue areas a low product yield; asterisks (\*) mark the parameters of the experiments carried out for verification. (E) Flavonoid yields achieved after 12 h of the whole-cell bioconversion of naringenin to hesperetin with E. coli_WCB2 with additional eriodictyol supplementation (yields refer to the substrate concentration of naringenin and eriodictyol used).

4.9 rel. AU). Surprisingly, the highest hesperetin concentration and yield (0.184 mM, 61.7%) was achieved with induction at an $\mathrm { O D } _ { 6 0 0 }$ of 1.6 rel. AU, not at higher densities as predicted (Figure S12). In parallel, isosakuranetin formation was minimized to 18.8%. These findings suggest that earlier induction reduces metabolic stress and favors selective methylation of eriodictyol. While the DoE successfully identified an improved induction temperature (24.2◦C), its growth-dependent predictions were less accurate, emphasizing the need for iterative validation when optimizing multienzyme biocatalytic systems.

## 3.7 Additional Eriodictyol Supplementation

To further reduce the formation of the undesired byproduct isosakuranetin, the impact of supplementing the intermediate eriodictyol at the start of the bioconversion process was evaluated. The hypothesis was that FOMTS142V would preferentially methylate eriodictyol over naringenin, thereby improving product selectivity. Eriodictyol was added at six different concentrations, ranging from 0 to 0.173 mM (0–50 mg L−1 ), alongside naringenin under previously optimized conditions.

TABLE 3 Real experimental results versus target values predicted using ML for the verification of different ML-models.
<table><tr><td rowspan="2">Experiment- No.</td><td rowspan="2">Selection criteria for data set (description)</td><td rowspan="2">Real experimental results</td><td colspan="3">Prediction</td></tr><tr><td>RF</td><td>MLP</td><td>MIX</td></tr><tr><td>1</td><td>Highest hesperetin conc. [mM]</td><td>0.186</td><td>0.180</td><td>0.188</td><td>0.184</td></tr><tr><td>2</td><td>Highest hesperetin yield [%]</td><td>70.2</td><td>65.2</td><td>59.9</td><td>55.8</td></tr><tr><td>3</td><td>Lowest isosakuranetin conc. [mM]</td><td>0.009</td><td>0.012</td><td>0.011</td><td>0.006</td></tr><tr><td>4</td><td>Best product-to-byproduct ratios</td><td>0.05</td><td>0.05</td><td>0.07</td><td>0.05</td></tr><tr><td>5</td><td>Highest hesperetin yield with lowest induction  $\mathrm { O D } _ { 6 0 0 }$  [%]</td><td>59.4</td><td>55.6</td><td>56.1</td><td>53.0</td></tr><tr><td>6</td><td>Highest hesperetin yield at  $2 8 . 0 ^ { \circ } \mathrm { C }$  [%]</td><td>46.9</td><td>46.6</td><td>44.7</td><td>38.7</td></tr><tr><td>7</td><td>Highest hesperetin yield at  $2 0 . 5 ^ { \circ } \mathrm { C }$  [%]</td><td>58.9</td><td>58.2</td><td>52.5</td><td>33.5</td></tr><tr><td>8</td><td>Highest hesperetin yield at 23.0°C [%]</td><td>58.3</td><td>57.5</td><td>51.6</td><td>30.6</td></tr></table>

Although the additional eriodictyol did not significantly influence cell growth or the overall bioconversion profiles (Figure S13), the experiment yielded the highest hesperetin titer observed in this study. A supplementation of 0.017 mM (5 mg L−1 ) eriodictyol alongside naringenin resulted in a hesperetin yield of 70.6%, withisosakuranetin formation reduced to 10.6% (Figure 5E). Surprisingly, neither higher nor lower eriodictyol concentrations improved this product-to-byproduct ratio further. The effect appears to be influenced more by biological variability, such as cryo-culture performance or pre-culture dynamic, than by the eriodictyol itself. While the results confirm that eriodictyol supplementation is not required for high selectivity, this experiment demonstrates that, under favorable conditions, exceptionally high hesperetin yields with minimal byproduct formation can be achieved.

## 3.8 Further Optimization Attempts Using ML

Supervised ML models were applied to predict optimal parameter combinations for improving hesperetin yield. In addition, this approach was used to evaluate whether data-driven methods can reliably describe the bioconversion and thereby support the design of future optimization experiments. The ML analysis was based on a dataset comprising approximately 100 shakeflask bioconversion experiments, with four to five sampling points for biomass and flavonoid concentrations provided by each experiment. These experiments differed in terms of the induction $\mathrm { O D } _ { 6 0 0 } ,$ the cultivation temperature, the IPTG level, and the timing of the addition of naringenin or MeI, thereby covering the range of conditions used during process development. The experimentally controlled parameters, together with the sampling time, were used as model inputs, while the measured hesperetin and isosakuranetin levels over time served as the prediction targets. Although the dataset was initially small, it became sufficiently heterogeneous for supervised learning once validation experiments had been conducted, as indicated by stabilizing cross-validation loss. The models aimed to identify parameter combinations that would improve hesperetin yield while limiting byproduct formation.

A random forest (RF) model was first implemented due to its robustness on small, noisy datasets and its ability to handle nonlinear feature interactions [53, 54]. In parallel, a multilayer perceptron (MLP) neural network with five hidden layers and ReLU activation was constructed and trained using the Adam optimizer with L2 regularization. A hybrid ensemble combining RF and MLP predictions was also evaluated to balance interpretability and performance [55].

A total of 192,000 virtual process conditions were screened through model-based simulation, and eight candidate parameter sets were selected for experimental validation. Selection criteria included predicted high hesperetin concentration, minimal isosakuranetin formation, and an optimized product-tobyproduct ratio. Shake flask fermentations were performed under these ML-recommended settings. Although slight deviations occurred between target and actual induction $\mathrm { O D } _ { 6 0 0 }$ (due to operational constraints in real-time control), most experimental outcomes closely matched the predicted values. Among the tested models, RF provided the most consistent predictions. These results highlight the model’s utility in narrowing down the experimental design space and accelerating data-driven process optimization.

The RF model proved to be the most accurate, with an average root mean squared error (RMSE) of 0.075 for flavonoid concentrations, significantly outperforming the MLP (0.147) and hybrid model (0.134). Although minor deviations between predicted and actual values were observed, the ML models generally captured the experimental trends well, with growth and product formation aligning closely across most conditions. An exception was the second validation experiment, where the model predicted a hesperetin yield of approximately 65%, yet the actual yield reached 70.2% (Table 3). Despite this discrepancy, the result represents one of the highest yields achieved in this study, underlining the practical benefit of ML-guided optimization even when predictions are not perfectly accurate. Although the MLguided process conditions did not surpass the maximum yield previously obtained under optimized supplementation (70.6%), the models successfully captured the underlying process dynamics and proved highly effective in narrowing the experimental design space. Given the complexity of the multivariate parameter set and the strong interdependencies between induction behavior, SAM availability, and metabolic burden, true yield improvements cannot always be expected from purely datadriven predictions. Instead, the ML approach demonstrated substantial value as a complementary tool, confirming its suitability for describing the system and identifying conditions that, for example, minimize byproduct formation. This highlights the utility of ML for guiding future process optimization rather than functioning solely as a means to exceed established yield benchmarks.

Besides, some prediction errors were observed, mainly due to discrepancies in actual versus assumed initial substrate concentrations. ML-assisted process development demonstrated considerable potential. In particular, RF-based predictions proved robust against experimental variability and noise. To further enhance model accuracy, especially for input-dependent constraints, integration of domain-specific rules (e.g., maximum theoretical substrate concentrations) and expansion of the dataset, especially under suboptimal conditions, will be crucial. These findings highlight the added value of ML as a complementary strategy in the design and refinement of whole-cell bioconversion processes.

## 3.9 Concluding Remarks

In this study, a two-step whole-cell bioconversion process was developed for the microbial production of hesperetin from naringenin in E. coli. The approach combined HpaBC with a plant-derived flavonoid 4′-O-methyltransferase (FOMT) and an HMT for SAM regeneration. To build a functional cascade, both enzymatic steps were first investigated individually: HpaBC was shown to efficiently hydroxylate naringenin to eriodictyol in vivo, while the combination of FOMT and HMT enabled methylation of eriodictyol to hesperetin in vitro and in vivo, with the in vitro system yielding up to 67% conversion. Subsequently, both reactions were integrated into recombinant E. coli strains. While E. coli_WCB1 showed high regioselectivity, E. coli_WCB2 (carrying the FOMTS142V mutant) achieved a higher final hesperetin yield (up to 23%) despite elevated isosakuranetin formation. Process optimization efforts focused on improving product selectivity and yield. Delayed addition of MeI enabled temporal separation of hydroxylation and methylation, increasing hesperetin yield to 55.7% and reducing byproduct formation. Further optimization of induction conditions using DoE increased yields to 61.7%. The highest hesperetin yield was achieved during the investigation of additional eriodictyol supplementation. It was determined that a yield of 70.6% was achieved, corresponding to a hesperetin concentration of 0.233 mM (71 mg L−1 ). This is, to the best of our knowledge, the highest published yield using E. coli. Finally, ML models were trained on experimental data and used to propose process parameters combinations for further process optimization. While the ML-guided settings did not surpass the highest experimentally achieved hesperetin yield, they demonstrated applicability of data-driven tools in process development by identifying parameters that improved selectivity and byproduct formation. This illustrates the potential of ML as a complementary tool for describing process dynamics and guiding optimization strategies.

Future work will focus on further improving pathway performance through targeted molecular engineering. Strategies include balancing and optimizing gene expression as well as protein engineering of key enzymes. Recent studies on Omethyltransferase variants indicate that active-site mutation can substantially enhance catalytic efficiency, providing a promising route for improving the FOMT/HMT module [56].

In conclusion, this work demonstrates how process development and data-driven tools can be integrated to enable the efficient microbial synthesis of hesperetin. Moreover, the process understanding gained in this study, together with the ML framework developed, will be directly applied to ongoing efforts toward the recombinant microbial production of other flavonoid products such as homoeriodictyol. Future research may also explore the application of predictive models in bioreactor systems, the use of real-time control strategies, and the integration of kinetic knowledge into ML models, for example through physics-informed neural networks (PINNs), to improve extrapolation under new process conditions. These strategies may facilitate the development of robust, scalable whole-cell bioconversion processes for hesperetin, homoeriodictyol, and other O-methylated flavonoids.

## Acknowledgments

The authors would like to thank Martina Weiß and Martin Pähler for their technical assistance, and Ulrich Krings from the Institute of Food Chemistry for his support with LC-MS analysis. Financial support from the Ministry of Science and Culture of Lower Saxony within the ABA project (grant number ZN3822) funded by the Lower Saxony “Volkswagen Stiftung Vorab” program is gratefully acknowledged.

Open access funding enabled and organized by Projekt DEAL.

## Ethics Statement

No experiments involving animals or humans were performed in the context of this work.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## References

1. K. Slámová, J. Kapešová, and K. Valentová, “‘Sweet Flavonoids’: Glycosidase-Catalyzed Modifications,” International Journal of Molecular Sciences 19, no. 7 (2018): 2126, https://doi.org/10.3390/ijms19072126.

2. A. N. Panche, A. D. Diwan, and S. R. Chandra, “Flavonoids: An Overview,” Journal of Nutritional Science 5 (2016): e47, https://doi.org/10. 1017/jns.2016.41.

3. M. M. Giusti and T. C. Wallace, “Flavonoids as Natural Pigments,” in Handbook of Natural Colorants, ed. T. Bechtold and R. Mussak (Wiley, 2010), 255–275.

4. N. F. Shamsudin, Q. U. Ahmed, S. Mahmood, et al., “Antibacterial Effects of Flavonoids and Their Structure-Activity Relationship Study: A Comparative Interpretation,” Molecules 27, no. 4 (2022): 1149, https://doi. org/10.3390/molecules27041149.

5. J. Mierziak, K. Kostyn, and A. Kulma, “Flavonoids as Important Molecules of Plant Interactions With the Environment,” Molecules 19, no. 10 (2014): 16240–16265, https://doi.org/10.3390/molecules191016240.

6. W. S. U. Roland, L. van Buren, H. Gruppen, et al., “Bitter Taste Receptor Activation by Flavonoids and Isoflavonoids: Modeled Structural Requirements for Activation of hTAS2R14 and hTAS2R39,” Journal of

Agricultural and Food Chemistry 61, no. 44 (2013): 10454–10466, https:// doi.org/10.1021/jf403387p.

7. R. E. Mutha, A. U. Tatiya, and S. J. Surana, “Flavonoids as Natural Phenolic Compounds and Their Role in Therapeutics: An Overview,” Future Journal of Pharmaceutical Science 7 (2021): 25, https://doi.org/10. 1186/s43094-020-00161-8.

8. J. Ley, G. Kindel, S. Paetz, et al. (2014)., Use of Hesperetin for Enhancing the Sweet Taste. US Patent 8679461B2.

9. Z. Wang, F. G. Gmitter, J. W. Grosser, and Y. Wang, “Natural Sweeteners and Sweetness-Enhancing Compounds Identified in Citrus Using an Efficient Metabolomics-Based Screening Strategy,” Journal of Agricultural and Food Chemistry 70, no. 34 (2022): 10593–10603, https://doi.org/10. 1021/acs.jafc.2c03515.

10. A. Khan, M. Ikram, J. R. Hahm, and M. O. Kim, “Antioxidant and Anti-Inflammatory Effects of Citrus Flavonoid Hesperetin: Special Focus on Neurological Disorders,” Antioxidants 9, no. 7 (2020): 609, https://doi.org/ 10.3390/antiox9070609.

11. E. Kheradmand, A. Hajizadeh Moghaddam, and M. Zare, “Neuroprotective Effect of Hesperetin and Nano-Hesperetin on Recognition Memory Impairment and the Elevated Oxygen Stress in Rat Model of Alzheimer’s Disease,” Biomedicine & Pharmacotherapy 97 (2018): 1096–1101, https:// doi.org/10.1016/j.biopha.2017.11.047.

12. H. K. Kim, T.-S. Jeong, M.-K. Lee, et al., “Lipid-Lowering Efficacy of Hesperetin Metabolites in High-Cholesterol Fed Rats,” Clinica Chimica Acta 327 (2003): 129–137, https://doi.org/10.1016/S0009-8981(02)00344-3.

13. J. Liu, M. Tian, Z. Wang, et al., “Production of Hesperetin From Naringenin in an Engineered Escherichia coli Consortium,” Journal of Biotechnology 347 (2022): 67–76, https://doi.org/10.1016/j.jbiotec.2022.02. 008.

14. A. Garg, S. Garg, L. J. Zaneveld, and A. K. Singla, “Chemistry and Pharmacology of the Citrus Bioflavonoid Hesperidin,” Phytotherapy Research 15 (2001): 655–669, https://doi.org/10.1002/ptr.1074.

15. I. Süntar, S. Çetinkaya, Ü. S. Haydaroğlu, and S. Habtemariam, “Bioproduction Process of Natural Products and Biopharmaceuticals: Biotechnological Aspects,” Biotechnology Advances 50 (2021): 107768.

16. B. Lin and Y. Tao, “Whole-Cell Biocatalysts by Design.” Microbial Cell Factories 16, no. 1 (2017): 106, https://doi.org/10.1186/s12934-017-0724-7.

17. M. Kadisch, C. Willrodt, M. Hillen, et al., “Maximizing the Stability of Metabolic Engineering-Derived Whole-Cell Biocatalysts,” Biotechnology Journal 12, no. 8 (2017): 1600170, https://doi.org/10.1002/biot.201600170.

18. C. C. De Carvalho, “Enzymatic and Whole Cell Catalysis: Finding New Strategies for Old Processes,” Biotechnology Advances 29, no. 1 (2011): 75– 83, https://doi.org/10.1016/j.biotechadv.2010.09.001.

19. M. Wildhagen, T. Pudenz, T. Nguyen, et al., “Biokatalytische Ganzzellproduktion des Sesquiterpens Presilphiperfolan-8β-ol in Stoffwechseloptimierten Escherichia coli,” Chemie Ingenieur Technik 95, no. 4 (2023): 576–586, https://doi.org/10.1002/cite.202200115.

20. E. Russo, “The Birth of Biotechnology,” Nature 421 (2003): 456–457, https://doi.org/10.1038/nj6921-456a.

21. P. Tucci, V. Veroli, M. Señorale, and M. Marín, “Escherichia coli: The Leading Model for the Production of Recombinant Proteins,” in Microbial Models: From Environmental to Industrial Sustainability. Microorganisms for Sustainability, ed. S. Castro-Sowinski (Springer, 2016), 119–147, https:// doi.org/10.1007/978-981-10-2555-6.

22. S. Huerta-Ochoa, C. O. Castillo-Araiza, A. R. Guerrero, and A. Prado-Barragán, “Whole-Cell Bioconversion of Citrus Flavonoids to Enhance Their Biological Properties,” in Studies in Natural Products Chemistry (Elsevier, 2019), 335–367.

23. J. Liu, Z. Xiao, S. Zhang, et al., “Restricting Promiscuity of Plant Flavonoid 3′-Hydroxylase and 4′-O-Methyltransferase Improves the Biosynthesis of (2S)-Hesperetin in E. coli,” Journal of Agricultural and Food Chemistry 71 (2023): 9826–9835, https://doi.org/10.1021/acs.jafc. 3c02071.

24. I. L.-B. Amor, A. Hehn, E. Guedon, et al., “Biotransformation of Naringenin to Eriodictyol by Saccharomyces cerevisiea Functionally Expressing Flavonoid 3′ Hydroxylase,” Natural Products Communications 5, no. 12 (2010): 1934578×1000501.

25. H. Halbwirth, “The Creation and Physiological Relevance of Divergent Hydroxylation Patterns in the Flavonoid Pathway,” International Journal of Molecular Sciences 11, no. 2 (2010): 595–621, https://doi.org/10.3390/ ijms11020595.

26. G. Schröder, E. Wehinger, R. Lukacin, et al., “Flavonoid Methylation: A Novel 4′-O-Methyltransferase From Catharanthus roseus, and Evidence That Partially Methylated Flavanones Are Substrates of Four Different Flavonoid Dioxygenases,” Phytochemistry 65, no. 8 (2004): 1085–1094, https://doi.org/10.1016/j.phytochem.2004.02.010.

27. X. Liu, Y. Wang, Y. Chen, et al., “Characterization of a Flavonoid 3′/5′/7-O-Methyltransferase From Citrus Reticulata and Evaluation of the In Vitro Cytotoxicity of Its Methylated Products,” Molecules 25, no. 4 (2020): 858, https://doi.org/10.3390/molecules25040858.

28. B.-G. Kim, S. H. Sung, Y. Chong, et al., “Plant Flavonoid O-Methyltransferases: Substrate Specificity and Application,” Journal of Plant Biology 53 (2010): 321–329, https://doi.org/10.1007/s12374-010-9126- 7.

29. J. Hausjell, H. Halbwirth, and O. Spadiut, “Recombinant Production of Eukaryotic Cytochrome P450s in Microbial Cell Factories,” Bioscience Reports 38, no. 2 (2018): BSR20171290, https://doi.org/10.1042/ BSR20171290.

30. C. Liao and F. P. Seebeck, “S-Adenosylhomocysteine as a Methyl Transfer Catalyst in Biocatalytic Methylation Reactions,” Nature Catalysis 2 (2019): 696–701, https://doi.org/10.1038/s41929-019-0300-0.

31. J. A. Jones, S. M. Collins, V. R. Vernacchio, et al., “Optimization of Naringenin and p-Coumaric Acid Hydroxylation Using the Native E. coli Hydroxylase Complex, HpaBC,” Biotechnology Progress 32, no. 1 (2016): 21–25, https://doi.org/10.1002/btpr.2185.

32. H. Wang, S. Wang, J. Wang, et al., “Engineering a Prokaryotic Non-P450 Hydroxylase for 3′-Hydroxylation of Flavonoids,” ACS Synthetic Biology 11, no. 11 (2022): 3865–3873, https://doi.org/10.1021/acssynbio. 2c00430.

33. A. Kunzendorf, B. Zirpel, L. Milke, et al., “Engineering an O-Methyltransferase for the Regioselective Biosynthesis of Hesperetin Dihydrochalcone,” ChemCatChem 15, no. 22 (2023): e202300951.

34. Q. Tang, I. V. Pavlidis, C. P. S. Badenhorst, and U. T. Bornscheuer, “From Natural Methylation to Versatile Alkylations Using Halide Methyltransferases,” ChemBioChem 22, no. 16 (2021): 2584–2590, https://doi.org/ 10.1002/cbic.202100153.

35. R. Chen, J. Gao, W. Yu, et al., “Engineering Cofactor Supply and Recycling to Drive Phenolic Acid Biosynthesis in Yeast,” Nature Chemical Biology 18 (2022): 520–529 , https://doi.org/10.1038/s41589-022-01014-6.

36. Y. Lv, J. Chang, W. Zhang, and H. Dong, “Improving Microbial Cell Factory Performance by Engineering SAM Availability,” Journal of Agricultural and Food Chemistry 72, no. 8 (2024): 3846–3871 , https://doi. org/10.1021/acs.jafc.3c09561.

37. T. Hashimoto, D. Nozawa, K. Mukai, et al., “Monooxygenase-Catalyzed Regioselective Hydroxylation for the Synthesis of Hydroxyequols,” RSC Advances 9 (2019): 21826–21830, https://doi.org/10.1039/ C9RA03913A.

38. R. Green and E. J. Rogers, “Transformation of Chemically Competent E. coli,” Methods in Enzymology 529 (2013): 329–336.

39. J. A. Jones, V. R. Vernacchio, D. M. Lachance, et al., “ePathOptimize: A Combinatorial Approach for Transcriptional Balancing of Metabolic Pathways,” Scientific Reports 5 (2015): 11301, https://doi.org/10.1038/ srep11301.

40. A. R. Tuttle, N. D. Trahan, and M. S. Son, “Growth and Maintenance of Escherichia coli Laboratory Strains,” Current Protocols 1 (2021): e20, https://doi.org/10.1002/cpz1.20.

41. C.-Y. Yang, M. Erickstad, L. Tadrist, et al., “Aggregation Temperature of Escherichia coli Depends on Steepness of the Thermal Gradient,” Biophysical Journal 118 (2020): 2816–2828, https://doi.org/10.1016/j.bpj. 2020.02.033.

42. A. L. Larentis, J. F. M. Q. Nicolau, G. D. S. Esteves, et al., “Evaluation of Pre-induction Temperature, Cell Growth at Induction and IPTG Concentration on the Expression of a Leptospiral Protein in E. coli Using Shaking Flasks and Microbioreactor,” BMC Research Notes 7 (2014): 671, https://doi.org/10.1186/1756-0500-7-671.

43. B. E. Chong, D. B. Wall, D. M. Lubman, and S. J. Flynn, “Rapid Profiling of E. coli Proteins up to 500 kDa From Whole Cell Lysates Using Matrix-Assisted Laser Desorption/Ionization Time-of-Flight Mass Spectrometry,” Rapid Communications in Mass Spectrometry 11, no. 17 (1997): 1900–1908, https://doi.org/10.1002/(SICI)1097-0231(199711)11:17% 3c1900::AID-RCM95%3e3.0.CO;2-K.

44. A. Sadžak, M. Eraković, and S. Šegota, “Kinetics of Flavonoid Degradation and Controlled Release From Functionalized Magnetic Nanoparticles,” Molecular Pharmaceutics 20 (2023): 5148–5159.

45. S. Ramešová, R. Sokolová, I. Degano, et al., “On the Stability of the Bioactive Flavonoids Quercetin and Luteolin Under Oxygen-Free Conditions,” Annals of Bioanalytical Chemistry 402 (2012): 975–982.

46. M. Bayati and M. M. Poojary, “Polyphenol Autoxidation and Prooxidative Activity Induce Protein Oxidation and Protein-Polyphenol Adduct Formation in Model Systems,” Food Chemistry 466 (2025): 142208, https:// doi.org/10.1016/j.foodchem.2024.142208.

47. Q. Tang, C. W. Grathwol, A. S. Aslan-Üzel, et al., “Directed Evolution of a Halide Methyltransferase Enables Biocatalytic Synthesis of Diverse SAM Analogs,” Angewandte Chemie 60, no. 3 (2021): 1524–1527, https:// doi.org/10.1002/anie.202013871.

48. T. Schweder, H. Y. Lin, B. Jürgen, et al., “Role of the General Stress Response During Strong Overexpression of a Heterologous Gene in Escherichia coli,” Applied Microbiology and Biotechnology 58 (2002): 330–337, https://doi.org/10.1007/s00253-001-0904-5.

49. F. Garcia-Ochoa and E. Gomez, “Bioreactor Scale-Up and Oxygen Transfer Rate in Microbial Processes: An Overview,” Biotechnology Advances 27, no. 2 (2009): 153–176, https://doi.org/10.1016/j.biotechadv. 2008.10.006.

50. A. Meyer, A. Schmid, M. Held, et al., “Changing the Substrate Reactivity of 2-Hydroxybiphenyl 3-Monooxygenase From Pseudomonas azelaica HBP1 by Directed Evolution,” Journal of Biological Chemistry 277, no. 7 (2002): 5575–5582, https://doi.org/10.1074/jbc.M110018200.

51. N. Parveen and K. A. Cornell, “Methylthioadenosine/S-Adenosylhomocysteine Nucleosidase, a Critical Enzyme for Bacterial Metabolism,” Molecular Microbiology 79, no. 1 (2011): 7–20, https://doi.org/10.1111/j.1365-2958.2010.07455.x.

52. E. B. Newman, L. I. Budman, E. C. Chan, et al., “Lack of S-Adenosylmethionine Results in a Cell Division Defect in Escherichia coli,” Journal of Bacteriology 180 (1998): 3614–3619, https://doi.org/10.1128/JB. 180.14.3614-3619.1998.

53. M. Mowbray, T. Savage, C. Wu, et al., “Machine Learning for Biochemical Engineering: A Review,” Biochemical Engineering Journal 172 (2021): 108054, https://doi.org/10.1016/j.bej.2021.108054.

54. Y. Qi, “Random Forest for Bioinformatics,” in Ensemble Machine Learning, ed. C. Zhang and Y. Ma (Springer, 2012), 307–323, https://doi. org/10.1007/978-1-4419-9326-7.

55. F. Murtagh, “Multilayer Perceptrons for Classification and Regression,” Neurocomputing 2 (1991): 183–197, https://doi.org/10.1016/0925- 2312(91)90023-5.

56. J.-P. Kanter, M. Ahlhorn, H. Zorn, et al., “Tailoring the Regioselectivity of Lentinula edodes O-Methyltransferases for Precise O-Methylation of Flavonoids,” Journal of Agricultural and Food Chemistry 73, no. 22 (2025): 13594–13604, https://doi.org/10.1021/acs.jafc.5c02429.

## Supporting Information

Additional supporting information can be found online in the Supporting Information section. Supporting File: elsc70069-sup-0001-SuppMat.pdf.