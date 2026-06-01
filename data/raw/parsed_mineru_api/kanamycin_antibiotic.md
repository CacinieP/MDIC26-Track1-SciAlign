RESEARCH

Open Access

# Bicuculline reversal of aminoglycoside O-nucleotidyltransferase EanT-1–mediated kanamycin resistance

<!-- image-->

Jiahui Wang1,2, Minghui Yu1,2, Mingzhen Zhang3 , Zhihui Meng1,2, Peitong Yang1,2, Xingyu Cui1,2, Ziqian Yu3 , Yongan Wang3\* and Gongli Zong1,2\*

## Abstract

Background Kanamycin, an aminoglycoside, is an effective broad-spectrum antimicrobial agent against bacterial infections. However, the clinical efficacy of aminoglycosides has been overshadowed by the emergence of resistance mechanisms involving enzyme-mediated covalent modifications. Aminoglycoside nucleotidyltransferases (ANTs) inactivate aminoglycosides via AMP group transfer. Elucidating their molecular mechanisms and identifying effective inhibitors are critical for combating antimicrobial resistance.

Methods Exiguobacterium sp. PL221A was isolated from hospital sewage under selection with 16 mg/L aminoglycosides. Following genomic sequencing using the Oxford Nanopore and BGISEQ-500 platforms, the eanT-1 gene encoding an ANT was identified, cloned, and expressed in Escherichia coli DH5α. Minimum inhibitory concentrations (MICs) against kanamycin were determined. Protein–ligand interactions between Eant-1 and kanamycin, virtual mutations of EanT-1, and inhibitor screening were assessed using the MaXFlow platform. To evaluate the catalytic mechanism, eant-1 mutants were expressed in vitro and their kinetic parameters were characterized. The impact of bicuculline on MICs and time-kill curves was also evaluated.

Results Strain PL221A exhibited notable resistance to neomycin, kanamycin, and gentamicin (all MICs > 128 mg/L). Heterologous expression indicated that EanT-1 confers kanamycin resistance. Mutation of residues D43A and D98A abrogated enzymatic activity, whereas alanine substitutions at R51 and T100 had no apparent effect. Bicuculline, an isoquinoline alkaloid compound, was identified as an effective EanT-1 inhibitor, showing stronger binding affinity (˗8.72 kcal/mol) for EanT-1 than kanamycin (˗7.51 kcal/mol) and an ability to occupy aspartate residues critical for electrophilic polarization. Its hydroxyl-free alkaloid scaffold may prevent adenylation, enabling competitive binding with kanamycin at the catalytic site and inactivating EanT-1. Additionally, the combination of kanamycin and bicuculline effectively inhibited the growth of eanT-1–expressing bacteria.

Conclusions The ANT encoded by eanT-1 in Exiguobacterium sp. PL221A mediates resistance to kanamycin, which can be counteracted by the alkaloid bicuculline through inhibition of its catalytic activity.

Keywords Exiguobacterium sp., Aminoglycoside nucleotidyltransferases, Kanamycin, ANT inhibitor, Bicuculline

## Introduction

Aminoglycosides are a powerful class of antibiotics composed of an aminocyclitol nucleus (typically streptamine, 2-deoxystreptamine, or streptidine) linked to amino sugars via glycosidic bonds. Aminoglycoside antibiotics disrupt bacterial protein synthesis by targeting the 30S ribosomal subunit, a mechanism that underscores their widespread clinical use [1]. However, the extensive application of these agents has contributed to rising bacterial resistance, posing a serious threat to public health [2].

The most common form of aminoglycoside resistance involves their inactivation by several diverse families of aminoglycoside-modifying enzymes (AMEs), which operate through molecular mechanisms that include phosphorylation, acetylation, and adenylation. AMEs catalyze the modification of hydroxyl or amino groups on the aminocyclitol nucleus or associated sugar moieties, functioning as acetyltransferases (AACs), nucleotidyltransferases (ANTs), or phosphotransferases (APHs) [2]. ANTs catalyze the metal-dependent nucleophilic attack of a deprotonated hydroxyl group on the antibiotic [3]. ANTs are classified into five functional groups by the antibiotic position they modify and are further subclassified by amino acid sequence, as follows: ANT(2′′)-Ia, ANT(3′′), ANT(4′)-Ia, -IIa, -IIb, ANT(6)-Ia, -Ib, -Ic, -Id, -Ie, -If, -Ig, ANT(9)-Ia, and -Ib [3]. Each ANT enzyme family recognizes its specific antibiotic substrate(s) via distinct mechanisms [3].

Inhibitors that prevent these enzymatic reactions by disrupting the initial ternary complex formation through ordered or random substrate binding have been proposed as potential tools to weaken the antibiotic resistance. Cationic antimicrobial peptides [4] and non-carbohydrate diamine derivatives [5] have been shown to inhibit AMEs, such as APH(3′)-IIIa, AAC(6′)-Ii, and ANT(2′′). Additionally, isoquinolinesulfonamide group compounds were found to inactivate APH(3′)-IIIa and the fusion protein AAC(6′)-APH(2′′) [2]. Apart from these advances, the discovery of inhibitors targeting ANT-type enzymes remains relatively scarce.

Gram-positive bacteria of Exiguobacterium genus were thought to be rarely associated with human infections [6, 7]. However, the potential pathogenicity of Exiguobacterium related to community-acquired pneumonia [7], bacteraemia (with myeloma) [8] and skin infection [9] in human has been revealed. In this study, we isolated an aminoglycoside-resistant strain of Exiguobacterium sp., designated as PL221A, and identified a novel aminoglycoside O-nucleotidyltransferase gene, eanT−1, in its genome. EanT-1 was demonstrated to contribute to resistance to kanamycin, and the isoquinoline alkaloid bicuculline was assessed as an EanT-1 inhibitor.

## Materials and methods

## Isolation and identification of aminoglycoside-resistant Exiguobacterium sp. PL221A

Hospital sewage samples collected in Shandong Province, China were spread onto Luria–Bertani (LB) agar (0.5% yeast extract, 1% tryptone, 1% sodium chloride, 2% agar) plates supplemented with a 16  mg/L mixture of aminoglycosides (streptomycin, neomycin, kanamycin, gentamicin, netilmicin, and amikacin) (Sigma Co., Shanghai, China) and incubated at 28  °C for 24  h. Colonies with different phenotypes were isolated and cultivated three consecutive times on LB agar plates containing individual aminoglycosides to obtain single colonies. A single kanamycin-resistant colony, designated PL221A, was further purified and verified by 16S rDNA PCR amplification and sequencing. Susceptibility testing was performed to determine the minimum inhibitory concentrations (MICs) of six aminoglycosides (streptomycin, neomycin, kanamycin, gentamicin, netilmicin, and amikacin) against strain PL221A. Data were analyzed based on breakpoints defined by the Clinical and Laboratory Standards Institute [10].

## Analysis of antibiotic resistance genes

The genome of Exiguobacterium sp. PL221A was sequenced using the Nanopore and BGISEQ-500 platforms at BGI Co., Ltd. (Wuhan, China). Genome annotation was performed using the Prokaryotic Genome Annotation Pipeline on NCBI (https://ncbi.nlm.nih.go v/genome/annotation_prok/). The antibiotic resistance genes were further analyzed using RAST and BLASTp against the core dataset in the Antibiotic Resistance Genes Database [11]. Multisequence alignments and visualization were carried out using Clustal Omega [12] and ESPript [13] software.

## EanT-1 expression and purification

The promoter of the ampicillin-resistance gene (ampR) from pMD18-T was PCR amplified using primers Pamp-F3 and Pamp-R3. The eanT-1 sequence was PCR amplified from PL221A genomic DNA using primers EanT-1-F and EanT-1-R. Both PCR products were then mixed and used as the template for overlap extension PCR with with primers Pamp-F3 and EanT-1-R. The resulting PampeanT product was then digested with KpnI and Xba I and inserted into pMD18-T digested with the same enzymes. The resulting recombinant plasmid pMD-EanT was transformed into E. coli DH5α to generate strain EcEanT.

E. coli DH5α and DH5α harboring pMD18-T (strain DT) were used as controls. DNA fragments encoding EanT-1 variants with the following alanine substitution mutations were synthesized by Sangon Biotech (Shanghai) Co., Ltd.: N26A, D43A, V44A, T45A, R84A, D98A, T100A, R102A and D114A. Primer sequences are listed in Table S1. Production and purification of histidine (His)-tagged EanT-1 proteins for activity assays and binding studies were performed as previously described [14]. Briefly, the eanT−1 gene was amplified from PL221A genomic DNA by PCR using primers EanT-1-His-For and EanT-1-His-Rev (Table S1) and then cloned into pMD18T to generate pMD18T-EanT. After confirmation by DNA sequencing, eanT-1 was subcloned into pET-15b and was transformed into E. coli BL21 (DE3) to obtain E. coli BL21/ pET-EanT. To induce the production of the His-tagged EanT-1, 0.5  mM isopropyl-β-D-1-thiogalactopyranoside (IPTG) was added to the culture when the optical density at 600  nm reached 0.6–0.8. The His-tagged EanT-1 was purified using a Ni–NTA-Sefinose column (Sangon) and the protein was analyzed by 10% SDS-PAGE.

## Molecular docking of EanT-1 with kanamycin

Protein homology modeling and molecular docking analyses were performed as previously described [15]. Briefly, the EanT-1 structure was constructed using the α-fold 2 protocol in MaXFlow, a web-based workflow tool developed by Neotrident (https://www.neotrident.com/). Vacuum electrostatics analysis was operated by Discovery Studio [16]. Hydrophobic surface features were analyzed using Discovery Studio [16]. The ligand structure of kanamycin was retrieved from ChemSpider (http://www .chemspider.com/). Binding interaction between EanT-1 and kanamycin was simulated using AutoDock Vina in MaXFlow. Predicted chemical bonds between EanT-1 and kanamycin were visualized using both 3D and 2D representations.

## Screening for inhibitors from the traditional chinese medicine (TCM) active compound library

The TCM Active Compound Library (MedChemExpress, Shanghai, China), comprising 221 compounds, was screened in silico for potential inhibitors of EanT-1. A virtual compound database was constructed on the MaXFlow platform, and molecular docking simulations were performed to predict binding interactions between EanT-1 and candidate inhibitors. Ultimately, 24 screened compounds were evaluated for inhibitory activity at concentrations of $5 \mu \mathrm { M } , 1 5 \mu \mathrm { M }$ , and 25 μM. MICs for kanamycin were then determined as described above. All experiments were conducted in triplicate using independent biological replicates.

## Time-kill assays

Time-kill assays were performed as previously reported [17]. Briefly, a single colony from an overnight culture of strain EcEanT was inoculated into LB medium and grown at $3 7 ~ ^ { \circ } \mathrm { C }$ for 18 h. The resulting bacterial suspension was centrifuged for 10 min at 10,000 rpm, and the pellet was resuspended in fresh pre-warmed LB medium. The culture was diluted to a concentration of $1 0 ^ { 5 } – 1 0 ^ { 6 } \mathrm { C F U / m L }$ then exposed to no drug (control), 50 μg/mL kanamycin, 0–25  μM inhibitor, or both for 24  h. Samples were collected from each suspension at 0, 1, 2, 4, 8, and 24  h to count viable bacteria. All experiments were performed in duplicate.

## EanT-1 enzyme activity assessment

The continuous EnzChek Pyrophosphate Assay (Life Technologies, Shanghai, China) was used to assess the kinetic parameters of wild type and mutant EanT-1 enzymatic activity, as previously reported [3, 18, 19]. Briefly, 5 μg EanT-1, 10 mM ATP, and kanamycin (0.5–100 μM) were added into reaction buffer (50 mM HEPES pH 7.5, 100 mM KCl, 1 mM DTT, 10 mM $\mathrm { { M g C l } _ { 2 } ) }$ and incubated with shaking for 3 min at 25 °C. The reaction was monitored at 360 nm using a microtiter plate reader to detect pyrophosphate release. Bicuculline alone or combined with kanamycin was tested using the same procedure.

## Results

## EanT-1 contributes to the notable aminoglycoside resistance of Exiguobacterium sp. PL221A

Strain PL221A was isolated from hospital sewage under selection with 16  mg/L kanamycin. MIC analysis of PL221A against five other aminoglycosides (streptomycin, neomycin, gentamicin, netilmicin, and amikacin) revealed broad-spectrum resistance (Table S3), with notably high MICs for neomycin, kanamycin, and gentamicin (> 128 mg/L each), but low MICs for streptomycin (8 mg/L) and amikacin (4 mg/L).

To investigate the mechanisms of aminoglycoside resistance in Exiguobacterium sp. PL221A, we screened for antimicrobial resistance genes in its genome. ABKJ26_01265 was predicted to encode an aminoglycoside 6-O-nucleotidyltransferase (ANT [6]-I) exhibiting low sequence identities (23.9–33.7%) with known ANT(6)-I homologs (Figs.  1A and S1). However, such enzymes confer resistance to streptomycin but not to kanamycin (Table S3). Thus, ABKJ26_01265 was renamed eanT−1 to reflect its origin from Exiguobacterium and its predicted function as an ANT. Next, we evaluated the potential role of eanT−1 in aminoglycoside resistance by expressing the gene in E. coli. MICs for six aminoglycosides were subsequently determined for the recombinant strain EcEanT. Compared with the control strains DH5α and DT (MICs < 2  mg/L), EcEanT exhibited high-level resistance to kanamycin (128 mg/L) (Fig. 1B). This result indicates that $e a n T { - } 1$ is a kanamycin resistance gene.

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 1 Contribution of the novel ANT EanT-1 to the notable aminoglycoside resistance of Exiguobacterium sp. PL221A. A Heatmap showing sequence homology between EanT-1 (ABKJ26_01265) and ANT(6)-I family proteins. B MICs of aminoglycosides against the indicated strains. $\mathsf { C E C } _ { 5 0 }$ of kanamycin against the indicated strains. DH5α: E. coli DH5α (control); DT: E. coli DH5α with pMD18-T (control); EcEanT: E. coli DH5α expressing EanT-1

The half maximal effective concentration $( \mathrm { E C } _ { 5 0 } )$ of kanamycin was significantly lower for E. coli DH5α (1.089±0.3051 mg/L) and DT (0.94±0.2992 mg/L), than for PL221A (42.91 ± 1.89 mg/L), indicating greater sensitivity in the DH5α strains. Expression of eanT−1 in E. coli markedly raised the kanamycin $\mathrm { E C } _ { 5 0 }$ (Fig.  1C), supporting its role in conferring kanamycin-specific resistance.

## Predicted structure of EanT-1 and its interaction with kanamycin

EanT-1 consists of an N-terminal domain and C-terminal domain, connected by an extended polypeptide (Fig. 2A). The N-terminal domain contains a six-stranded beta sheet (β1–β6) that is predominantly antiparallel, except for the parallel orientation between strands β2 and β5, as is typical of this protein family. The N-terminal domain also has five interspersed alpha helices (α1–α5) and four loops. The C-terminal domain contains the typical helical bundle (α6–α11) observed in the structures of other ANT enzymes [3].

Molecular simulations identified the kanamycin binding site of EanT within the β-sheet and a loop of the N-terminal domain (Fig.  2B). In the EanT–kanamycin complex structure, the antibiotic molecule is anchored in the enzyme active site through two hydrogen bonds formed between Val44 and Thr45 (Fig. 2C). On the substrate side, hydrogen bonds are formed by hydroxyl groups facing the interior of the active site (Figs. 2C and S3).

To investigate the role of active-site residues in catalysis and substrate recognition, we replaced each with an alanine residue and tested the enzymatic activities of the resulting variants in vitro. To evaluate their influence on kanamycin binding, we also performed virtual alanine scanning at residues N26, D43, V44, T45, D98, T100, R84, R102, and D114 using MaXFlow, generating the corresponding mutant models: N26A, D43A, V44A, T45A, D98A, T100A, R84A, R102A, and D114A.

A  
<!-- image-->

<!-- image-->

C  
<!-- image-->

<!-- image-->

D  
<!-- image-->  
E

<!-- image-->  
Fig. 2 Structure of EanT-1 and its interaction with kanamycin. A Structure of EanT-1. B, C Predicted interactions between kanamycin (purple sticks) and amino acid residues of EanT-1 (colored lines). Hydrogen bonds are shown as green dashed lines. D Variation in ΔG values of virtual alanine mutations generated by MaXFlow. E Relative enzymatic activity of alanine substitution mutants, normalized to the activity of wild type (WT) EanT-1 (set to 100%); \* p < 0.05

Compared to the wild-ype EanT-1, all 9 alanine mutants exhibited increased binding free energies (ΔG total, kcal/mol), with half showing increases exceeding 10 kcal/mol (Table S4). Threonine T45 exhibited the greatest impact, with a ΔG increase of 14.69  kcal/mol. Mutants D43A, D98A, and D114A presented ΔG values of 3.97  kcal/mol, 13.32  kcal/mol, and 10.23  kcal/mol, respectively (Fig.  2D). Extracellular enzyme assays confirmed the reduced activity across the EanT-1 mutants (Fig. 2E). Alanine substitutions at D43 and D98 individually abolished enzymatic function, while mutations at N26, V44, T45, R102, and D114 resulted in partial loss of catalysis. In contrast, the alanine substitutions at R84 and T100 had no significant impact on enzymatic function (Fig. 2E and Table S5).

## EanT-1 inhibitors screened from TCM compounds

Next, we performed virtual screening for inhibitors targeting the active pocket of EanT-1 using a library of TCM compounds. Of 158 candidates predicted to bind effectively to EanT-1 (Table S6), 24 compounds with stronger binding affinities than kanamycin (< ˗7.51  kcal/mol) were selected for evaluation of their inhibitory potential. First, the effects of these 24 compounds on the MICs of kanamycin were tested in EcEanT and PL22A. Nine compounds markedly reduced kanamycin resistance (Table S7). When added at 20 μg/mL, these compounds lowered the MICs of PL22A against kanamycin by 2- to 32-fold (from 64  μg/mL to 4  μg/mL) compared with untreated controls (Fig.  3A). Likewise, for EcEanT, the kanamycin resistance gained from eanT−1 expression was decreased by 2- to 64-fold (from 64 μg/mL to < 2 μg/mL) (Fig. 3B). Of these compounds, bicuculline (20  μg/mL) exhibited the strongest inhibitory effect, reducing the MICs of PL22A and EcEanT against kanamycin to 4  μg/mL and < 2 μg/mL, respectively (Fig. 3A and B).

The nine TCM compounds were grouped into four categories: lignans (etoposide, and licarin B), alkaloids (bicuculline and reserpine), glycosides (phillyrin, verbascoside, and phlorizin) and phenolic acids (chlorogenic acid and chebulinic acid). Molecular docking predicted that these potential EanT-1 inhibitors bind near the enzyme’s catalytic center (Fig. 3C). Low molecular weight compounds, such as bicuculline and verbascoside, are predicted to tightly attach within the catalytic center, whereas larger compounds, such as chebulinic acid and etoposide, could occupy the entire space of the active center or extend beyond it (Fig. 3C).

Among the screened compounds, the alkaloids bicuculline and reserpine were predicted to exert strong inhibitory effects on EanT-1–mediated kanamycin resistance. Unlike the other candidates, bicuculline and reserpine lack hydroxyl groups (Figure S3), a known nucleotidyltransferase catalytic target. Thus, hydroxyl-free structures and stronger predicted binding affinities relative to kanamycin may contribute to the inhibition of EanT-1– mediated kanamycin resistance.

A  
<!-- image-->

c  
<!-- image-->

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

<!-- image-->  
Fig. 3 Screening of EanT-1 inhibitors from a TCM compound library. (A, B) Effect of EanT-1 inhibitor candidates (20 μg/mL) on the MICs of strains PL22A (A) and EcEanT (B) against kanamycin. (C) Predicted binding of inhibitor candidates (purple sticks) docked within the kanamycin-binding pocket (yellow) of EanT-1. Molecular surfaces were colored

## Inhibition of EanT-1 activity via preferential active site binding by bicuculline

Given its strong inhibitory effect on EanT-1–mediated kanamycin resistance (Fig.  3A and B), bicuculline was further analyzed. Firstly, EanT-1 enzymatic activity was analyzed using kanamycin, bicuculline, or kanamycin combined with bicuculline as substrates. EanT-1 presented no detectable activity on bicuculline alone, nor on kanamycin in the presence of bicuculline (Table S8). In contrast to 7-OH kanamycin, bicuculline is a hydroxyl-free isoquinoline alkaloid (Fig.  4A) and functions as a competitive antagonist of receptors for the inhibitory neurotransmitter GABA [20]. In this study, molecular simulations identified bicuculline as a potential inhibitor of EanT-1, binding adjacent to the kanamycin interaction site (Fig. 4B).

The bicuculline binding pocket was localized at the EanT-1 N-terminal domain, close to the beta sheet region (β1–β6) (Fig. 4C), and predicted to form a narrow, curved structure with a maximum diameter of 27.4 Å and an angle of 91.9°, in contrast to the kanamycin-binding pocket, predicted to be 17.2 Å in diameter with an angle of 87.4° (Fig. 4D). A cross-sectional comparison revealed a substantial overlap between the two binding pockets (Fig.  4D). Thus, considering bicuculline's stronger predicted binding affinity to EanT-1 (−8.72 kcal/mol) relative

<!-- image-->  
Fig. 4 Bicuculline-mediated inhibition of EanT-1 activity. A Structural formulas of kanamycin and bicuculline. B Predicted binding of kanamycin (CAS:59– 01–8; red sticks) and bicuculline (CAS:485–49-4; green sticks) within the cartoon representation of the EanT-1 complex. C Predicted locations of the kanamycin and bicuculline binding pockets. D Comparison and superposition of the kanamycin (red) and bicuculline (green) binding pockets, with the overlapping regions highlighted in brown. E Vacuum electrostatics analysis of EanT-1, showing the kanamycin and bicuculline binding pockets. F EanT-1 amino acid residues interacting with kanamycin (red sticks) and bicuculline (green sticks), with residues shared by both binding interfaces shown as blue sticks

<!-- image-->

<!-- image-->

<!-- image-->

D  
<!-- image-->  
Fig. 5 Reduction in EanT-1–mediated kanamycin resistance achieved by bicuculline–kanamycin combination treatment. (A, C) MICs of E. coli EcEanT (A) and Exiguobacterium sp. PL221A (C) against kanamycin in the presence of the indicated concentrations of bicuculline. (B, D) Time-kill curves of EcEanT (B) and PL221A (D) exposed to no treatment (Growth control), kanamycin, bicuculline (10 μg/ml for EcEanT and10 μg/ml for PL221A), or a combination of kanamycin and bicuculline; \* p < 0.05

to that of kanamycin (−7.51 kcal/mol) (Table S6), it may competitively occupy the kanamycin binding site.

Electrophilic polarization of the chemical environment can increase nucleophilicity, serving as a key factor in catalytic activity [18]. Vacuum electrostatics analysis of EanT-1 revealed electrophilic polarization at the catalytic active center and its surrounding area (Fig.  4E). Bicuculline was predicted to preferentially bind with EanT-1 within this highly polarized area (Fig.  4E). Additionally, six amino acid residues (N26, D43, D98, V44, T45, and D114) were identified as common interaction sites for kanamycin (11 residues) and bicuculline (10 residues) (Fig.  4E). Notably, the three Asp residues, which are homologs of those responsible for electrophilic polarization in ANT(2'')-Ia [18], are predicted to be engaged in bicuculline binding to EanT-1, which prevents kanamycin adenylation.

## Reduction of EanT-1–mediated kanamycin resistance by bicuculline–kanamycin combination

To confirm that bicuculline could reverse EanT-1–mediated kanamycin resistance, the MICs of E. coli EcEanT and Exiguobacterium sp. PL221A against kanamycin were measured in the presence of 0–25  μg/mL bicuculline. Bicuculline at 10  μg/mL lowered the MIC for EcEanT to < 2  μg/mL (Fig.  5A), whereas 15  μg/mL was needed to achieve an equivalent effect for PL221A (Fig. 5C).

Next, time-kill curves were obtained for the two strains exposed to kanamycin, bicuculline, or a combination of the two. After 24  h incubation without treatment, bacterial counts for EcEanT and PL221A reached 8.4 (Fig.  5B) and 8.65 log CFU/mL (Fig.  5D), respectively. Treatment with kanamycin or bicuculline alone had no significant effect on bacterial growth. In contrast, combination treatment with kanamycin and bicuculline (10 μg/ mL in EcEanT and 15  μg/mL in PL221A) exhibited marked antibacterial activity, reducing bacterial counts to 1.297 and 1.123 log CFU/mL, and achieving a reduction exceeding 6 log -fold (Fig. 5B and D).

## Discussion

AMEs play a significant role in antibiotic resistance by modifying at − OH or − NH groups of the 2-deoxystreptamine nucleus or the sugar moieties. ANTs, inactivate aminoglycosides by transferring an AMP group from ATP to a hydroxyl group on the aminoglycoside molecule [2]. Although ANT(6) genes are highly prevalent among Gram-positive bacteria, Gram-negative opportunistic pathogen such as Morganella morganii strain UM869, also harbored this genetic determinant [21]. In this study, we identified EanT-1, a novel ANT that was found to mediate substantial kanamycin resistance. Based on gene annotation, EanT-1 was classified as an a member of ANT(6)-I family, despite its low sequence identity (23.9– 33.7%) with known representatives. It showed no meaningful sequence similarity with ANT(9) [22], ANT(4′) [23], ANT(2′′) [18], and ANT(3′′) [24]. In contrast to streptomycin, which possesses a 6-OH group targeted by ANT(6) for adenylation, kanamycin presents a 2-deoxystreptamine core at this position. The occupation of the C6-OH in kanamycin implies that EanT-1 may belong to a different or novel class of ANTs [3].

Moreover, EanT-1 residues predicted to interact with kanamycin (N26, D43, V44, T45, D98, T100, R84, R102, A110, A113, and D114) exhibit an aspartate (Asp)-rich characteristic, similar to that in the interaction between ANT(2′′)-Ia and kanamycin B [18]. Additionally, amino acid residues implicated in ATP interaction during streptomycin modification by ANT(6)-Ib [18] (R167, D41, D43, S29 and D99) are conserved in EanT-1. It indicated that EanT-1 exhibits catalytic properties more consistent with ANT(2′′), although structurally similar to ANT(6). This variation may underlie the selective recognition of kanamycin over streptomycin and influence nucleotidyl transfer specificity. Therefore, further investigation into its catalytic site and reaction mechanism is needed. Enzymatic inhibitors could be utilized to counteract widely disseminated AMEs, reducing or eliminating the need to discard aminoglycosides. Herbal remedies within TCM offer a promising yet underexplored source of potential antimicrobial drugs [25], such as natural flavonoids that are effective against multidrug-resistant pathogens [26]. Moreover, ligand-based virtual screening is an efficient way to identify standard features of active compounds that can be used as pharmacophore models to screen and identify new active compounds. Potential adjuvant candidates for overcoming AcrB mediated colistin resistance were screened out [27]. Utilizing a similar approach, a comprehensive collection of 664 extracts from 132 TCM plant species is available from the National Cancer Institute [25, 28]. Research into the antimicrobial properties of plants used in TCM has increased dramatically over the past several years. Of the two alkaloids identified via virtual screening of the TCM compound library in this study, bicuculline demonstrated stronger inhibitory activity against EanT-1 in vitro, lowering the MICs of PL22A and EcEanT against kanamycin to 4  μg/mL and < 2  μg/mL, respectively. Reserpine, despite its high predicted binding affinity EanT-1, did not exhibit comparable inhibitory effects under the tested conditions, warranting further validation.

Mechanistic analysis of enzyme inhibition revealed three bicuculline-induced effects. First, bicuculline exhibited stronger binding affinity to EanT-1 (˗8.72 kcal/ mol) than kanamycin (˗7.51  kcal/mol). Second, it occupied Asp residues, disrupting electrophilic polarization required for catalytic activity. Third, its hydroxyl-free isoquinoline alkaloid scaffold renders bicuculline an unsuitable substrate for ANTs. Taken together, these features enable bicuculline to competitively bind the active center, resulting in functional inactivation of Eant-1, which parallels the mechanism of clavulanic acid against β-lactamase [29]. Although further validation is required, the synergistic combination of kanamycin and bicuculline shows promising efficacy against bacteria carrying eanT−1, offering a potential therapeutic strategy for kanamycin-resistant infections.

## Conclusions

The newly identified ANT enzyme, EanT-1, was found to confer substantial resistance to kanamycin. Site-directed mutagenesis of key amino acid residues (D43 and D98) resulted in complete loss of enzymatic activity, underscoring their importance in catalysis. Bicuculline, a hydroxyl-free isoquinoline alkaloid and non-substrate for ANTs, demonstrated preferential binding to EanT-1 over kanamycin and disrupted catalytic function by occupying key Asp residues, thereby preventing electrophilic polarization. Consequently, the synergistic combination of kanamycin and bicuculline effectively inhibited the growth of eanT−1–expressing bacteria, offering a promising strategy to overcome kanamycin resistance.

## Supplementary Information

The online version contains supplementary material available at https://doi.or g/10.1186/s12866-026-04746-w.

Additional file 1: Table S1. Primer sequences used in this study. Table S2. Substrate profile of different ANT(6)-Is. Table S3. MICs of antibiotics (mg/L)

against different strains. Table S4. Virtual mutations of EanT-1 proteins. Table S5. EanT-1 steady-state kinetic parameters at 25°C. Table S6. Virtual screening of EanT-1 inhibitors from the TCM compound library. Table S7. MICs of kanamycin in the presence of traditional Chinese medicinal compounds (20 mg/L). Figure S1. Neighbor-joining tree generated on the basis of amino acid sequence. Figure S2. Alignment of amino acid sequences of EanT-1 and ANT(6)-I family members. Figure S3. Amino acid residues involved in substrate binding. Figure S4. Structures of selected TCM compounds.

## Acknowledgements

We thank Michelle Kahmeyer-Gabbe, PhD, from Liwen Bianji (Edanz) (www.   
liwenbianji.cn) for editing the English text of a draft of this manuscript.

## Author’s contributions

JHW prepared the hospital sewage samples, led the data analysis, and wrote the manuscript. MHY and ZHM co-led the bioinformatics analysis. MZZ and XYC co-led the data and bioinformatics analyses. PTY and ZQY helped with data analyses. YAW co-led the data analysis and edited the manuscript. GLZ co-led the project and revised the manuscript. All authors read and approved the final manuscript.

## Funding

This work was supported by the Natural Science Foundation of Shandong Province (grant numbers ZR2024MC006 [2024] and ZR2023MC068 [2023], the Shandong Province Undergraduate Teaching Reform Research Project

– Key Project (grant number Z2024215), and the National College Students’ Innovation and Entrepreneurship Training Program (grant number 2025–50 [2025]).

## Data availability

The complete sequence of the Exiguobacterium sp. PL221A genome is available in the NCBI GenBank under accession number CP158590 and is available at the following URL: https://www.ncbi.nlm.nih.gov/nuccore/CP15 8590.1/.

## Declarations

Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Author details

1 Biomedical Sciences College & Shandong Medicinal Biotechnology Center, Key Lab for Genetic Engineering and Synthetic Biology of Shandong Province, Shandong First Medical University & Shandong Academy of Medical Sciences, Ji’nan 250117, Shandong, China 2 NHC Key Laboratory of Biotechnology Drugs (Shandong Academy of Medical Sciences), Ji’nan 250117, Shandong, China 3 School of Laboratory Animal & Shandong Laboratory Animal Center, Shandong First Medical University, Shandong Academy of Medical Sciences, Ji’nan 250117, Shandong, China

Received: 17 September 2025 / Accepted: 9 January 2026

Published online: 03 February 2026

## References

1. Dezanet C, Kempf J, Mingeot-Leclercq M-P, Décout J-L. Amphiphilic aminoglycosides as medicinal agents. Int J Mol Sci. 2020;21(19):7411.

2. Ramirez MS, Tolmasky ME. Aminoglycoside modifying enzymes. Drug Resist Updat. 2010;13(6):151–71.

3. Nalam P, Cook Paul D, Smith Brian A. Structural and biochemical characterization of aminoglycoside nucleotidyltransferase(6)‐Ib from Campylobacter fetus subsp. fetus. Proteins. 2024;93(2):413–419.

4. Boehr DD, Draker KA, Koteva K, Bains M, Hancock RE, Wright GD. Broad-spectrum peptide inhibitors of aminoglycoside antibiotic resistance enzymes. Chem Biol. 2003;10(2):189–96.

5. Welch KT, Virga KG, Whittemore NA, Ozen C, Wright E, Brown CL, et al. Discovery of non-carbohydrate inhibitors of aminoglycoside-modifying enzymes. Bioorg Med Chem. 2005;13(22):6252–63.

6. Elsheshtawy A, Clokie BGJ, Albalat A, Beveridge A, Hamza A, Ibrahim A, et al. Characterization of external mucosal microbiomes of Nile tilapia and grey mullet co-cultured in semi-intensive pond systems. Front Microbiol. 2021;12:773860.

7. Chen X, Wang L, Zhou J, Wu H, Li D, Cui Y, et al. Exiguobacterium sp. A1b/ GX59 isolated from a patient with community-acquired pneumonia and bacteremia: genomic characterization and literature review. BMC Infect Dis. 2017;17(1):508.

8. Pitt TL, Malnick H, Shah J, Chattaway MA, Keys CJ, Cooke FJ, et al. Characterisation of Exiguobacterium aurantiacum isolates from blood cultures of six patients. Clin Microbiol Infect. 2007;13(9):946–8.

9. Tena D, Martínez NM, Casanova J, García JL, Román E, Medina MJ, et al. Possible Exiguobacterium sibiricum skin infection in human. Emerg Infect Dis. 2014;20(12):2178–9.

10. CLSI. Performance standards for antimicrobial susceptibility testing, M100, 31st ed. Clinical and Laboratory Standards Institute, Wayne, PA. 2020.

11. Liu B, Pop M. ARDB–antibiotic resistance genes database. Nucleic Acids Res. 2009;37(37):443–7.

12. Madeira F, Park Ym, Buso JLN, Gur T, Madhusoodanan N, Basutka P, et al. The EMBL-EBI search and sequence analysis tools APIs in 2019. Nucleic Acids Res. 2019;47:636–41.

13. Xavier R, Patrice G. Deciphering key features in protein structures with the new ENDscript server. Nucleic Acids Res. 2014;42(1):320–4.

14. Zong G, Cao G, Fu J, Zhang P, Chen X, Yan W, et al. Novel mechanism of hydrogen peroxide for promoting efficient natamycin synthesis in Streptomyces. Microbiol Spectr. 2023;11(5):e0087923.

15. Zong G, Zhong C, Fu J, Zhang Y, Zhang P, Zhang W, et al. The carbapenem resistance gene blaOXA-23 is disseminated by a conjugative plasmid containing the novel transposon Tn6681 in Acinetobacter johnsonii M19. Antimicrob Resist Infect Control. 2020;9(1):182.

16. Dassault Systèmes BIOVIA. Discovery Studio Modeling Environment, Release 2017. San Diego, CA: Dassault Systemes 2017.

17. Ferro BE, van Ingen J, Wattenberg M, van Soolingen D, Mouton JW. Time-kill kinetics of antibiotics active against rapidly growing mycobacteria. J Antimicrob Chemother. 2014;70(3):811–7.

18. Cox G, Stogios PJ, Savchenko A, Wright GD, Bush K. Structural and molecular basis for resistance to aminoglycoside antibiotics by the adenylyltransferase ANT(2″)-Ia. MBio. 2015;6(1):e02180–02114.

19. Semper C, Stogios P, Meziane-Cherif D, Evdokimova E, Courvalin P, Savchenko A. Structural characterization of aminoglycoside 4′-O-adenylyltransferase ANT(4′)-IIb from Pseudomonas aeruginosa. Protein Sci. 2020;29(3):758–67.

20. Johnston GAR. Advantages of an antagonist: bicuculline and other GABA antagonists. Br J Pharmacol. 2013;169(2):328–36.

21. Behera DU, Dixit S, Gaur M, Mishra R, Sahoo RK, Sahoo M, et al. Sequencing and characterization of M. morganii strain UM869: a comprehensive comparative genomic analysis of virulence, antibiotic resistance, and functional pathways. Genes. 2023;14(6):1279.

22. Sheng X, Lu W, Li A, Lu J, Song C, Xu J, et al. ANT(9)-Ic, a novel chromosomally encoded aminoglycoside nucleotidyltransferase from Brucella intermedia. Microbiol Spectr. 2023;11(3):e0062023.

23. Selvaraj B, Kocaman S, Trifas M, Serpersu EH, Cuneo MJ. “Catch and Release”: a variation of the archetypal nucleotidyl transfer reaction. ACS Catal. 2020;10(6):3548–55.

24. Liang J, Zhou K, Li Q, Dong X, Zhang P, Liu H, et al. Identification and characterization of a novel aminoglycoside 3"-nucleotidyltransferase, ANT(3")-IId, from Acinetobacter lwoffii. Front Microbiol. 2021;12:728216.

25. Ellward GL, Binda ME, Dzurny DI, Bucher MJ, Dees WR, Czyż DM. A screen of traditional Chinese medicinal plant extracts reveals 17 species with antimicrobial properties. Antibiotics. 2024;13(12):1220.

26. Song M, Liu Y, Li T, Liu X, Hao Z, Ding S, et al. Plant natural flavonoids against multidrug resistant pathogens. Adv Sci (Weinh). 2021;8(15):e2100749.

27. Behera DU, Gaur M, Sahoo M, Subudhi E, Subudhi BB. Development of pharmacophore models for AcrB protein and the identification of potential

adjuvant candidates for overcoming efflux-mediated colistin resistance. RSC Med Chem. 2024;15(1):127–38.

28. Eisenberg DM, Harris ES, Littlefield BA, Cao S, Craycroft JA, Scholten R, et al. Developing a library of authenticated traditional Chinese medicinal (TCM) plants for systematic biological evaluation–rationale, methods and preliminary results from a Sino-American collaboration. Fitoterapia. 2011;82(1):17–33.

29. Ortega-Balleza JL, Vázquez-Jiménez LK, Ortiz-Pérez E, Avalos-Navarro G, Paz-González AD, Lara-Ramírez EE, et al. Current strategy for targeting

metallo-β-lactamase with metal-ion-binding inhibitors. Molecules.   
2024;29(16):3944.

## Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.