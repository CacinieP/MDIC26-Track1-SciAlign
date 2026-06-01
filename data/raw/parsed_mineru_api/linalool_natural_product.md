OPEN

Check for updates

# Activity of linalool based silver nanoconjugates against brain tumor through in silico, in vitro and in vivo evaluations

Hina Manzoor1, Muhammad Umer Khan 1, Fariha Javaid2, Abida Khan3, Tahir Ali Chohan4, Mohd Imran3, Abdullah R. Alzahrani5 & Zia Ur Rehman6,7

Brain tumor is an incurable brain malignancy categorized by high invasiveness and resistance to conventional treatments. This study uses a multidisciplinary approach that includes computational analysis, in vitro gene expression profiling, and an in vivo ENU-induced brain tumor rat model to assess the anti-brain tumor potential of linalool (LN), a natural monoterpene alcohol, and its silver nanoparticle-conjugated form (LN@AgNPs). The 3D structure of linalool was obtained from PubChem, and structure of linalool-based AgNP was constructed using Avogadro software. The target proteins structure was retrieved from the PDB database, followed by molecular docking using AutoDock Vina and molecular dynamics simulations using the AMBER20 software. Protein expression analysis was performed in the SF-767 cell line at the IC₅₀ concentrations of the compounds. For biological validation, the compounds were evaluated using a rat brain tumor model. Molecular docking and molecular dynamics simulations demonstrated robust and consistent interactions of LN and LN@ AgNPs with CDK4 and mutant p53. LN@AgNPs exhibited improved binding affinity and stability. Favorable binding free energies for CDK4/Linalool were validated by MM/PBSA analysis. Analysis of gene expression revealed downregulation of CDK4 and overexpression of p53, indicating simultaneous targeting of cell cycle and apoptotic pathways. LN@AgNPs decreased tumor volume by 13% in vivo, lowered peritumoral infiltration, and increased survival in rats with gliomas. Tumor shrinkage was confirmed by morphometric analysis, and trends in body weight indicated no systemic damage. The therapeutic advantage of LN@AgNPs over free LN and controls was confirmed by Kaplan-Meier survival analysis. Due to higher bioavailability, tumor targeting, and molecular interaction stability, these results demonstrate the increased therapeutic potential of LN@AgNPs. The research supports the development of LN-based nanomedicine as a viable substitute for brain tumor treatment. Additional clinical and pharmacokinetic research is necessary to evaluate translational applicability.

Keywords Brain tumor, Linalool, Linalool silver nanoparticles, In silico, In vivo

A brain tumor is an abnormal growth of cell mass in or around the brain. Both malignant (cancerous) and noncancerous brain tumors are possible. It is the most prevalent primary intracranial malignant tumor of the central nervous system1 . The most deadly and severe type of primary brain tumor in adults is glioblastoma multiforme (GBM), which accounts for 45.2% of all primary brain and central nervous system cancers and is a common primary brain tumor in the adult population. About 15% of all initial brain tumors are glioblastomas, which have a median life of about 21 months even with vigorous treatment2–4 . Brain tumor’s dismal prognosis emphasizes the ongoing need for novel and effective treatment approaches meant to improve patient outcomes and general quality of life.

1Institute of Molecular Biology and Biotechnology, The University of Lahore, Lahore 54000, Pakistan. 2School of Biochemistry and Biotechnology, University of the Punjab, Lahore 54000, Pakistan. 3Center For Health Research, Northern Border University, Arar 73213, Saudi Arabia. 4Institute of Pharmaceutical Sciences, University of Veterinary and Animal Sciences, Lahore, Pakistan. 5Department of Pharmacology and Toxicology, Faculty of Medicine, Umm Al-Qura University, Al-Abidiyah, P.O. Box 13578, Makkah 21955, Saudi Arabia. 6Health Research Centre, Jazan University, P.O. Box 114, Jazan 45142, Saudi Arabia. 7Department of Pharmaceutical Chemistry and Pharmacognosy, Faculty of Pharmacy, Jazan University, P.O. Box 114, Jazan 45142, Saudi Arabia. email: muhammad.umer4@mlt.uol.edu.pk; umer.khan685@gmail.com

Current treatment options for brain tumor include surgical excision, followed by radiation and chemotherapy, with temozolomide being the most often used alkylating agent5,6 . However, a variety of factors contribute to the limited effectiveness of these traditional therapies including tumor heterogeneity, blood-brain barrier (BBB), neurological problems, and a high recurrence rate7 . The BBB reduces the effectiveness of systemic medication transport to the brain tumor. Increasing the dosage of medications to improve their therapeutic efficacy would make them more toxic to healthy cells, which would raise the possibility of negative side effects8 . Additionally, the effectiveness of radiotherapy is limited by the brain tissue’s sensitivity to radiation. The same elevated risk of side effects also limits the use of many drugs to combat the significant degree of genetic heterogeneity of brain tumors in patients9,10.

The potential of several phytotherapeutics to treat cancer, particularly brain tumor, has been studied. Given these therapeutic concerns, attention has been focused on investigating various medicinal sources, including natural substances, especially essential oils derived from plants, which offer promising approaches to resolving these issues11–13. These substances are attractive candidates for oncological treatment because of their multitargeted modes of action, decreased toxicity, and anticancer properties14. More than 200 plant species contain linalool, a naturally occurring monoterpene alcohol with a pleasant scent. Both green and black teas include linalool, which is either a major or common compound of the majority of herbal essential oils15,16. Linalool has been shown in numerous studies to exhibit anticancer properties against solid tumor cell lines, including hepatic cancer (HepG2), skin cancer, gastric cancer and multiple leukemia cell lines17–19. According to some of these investigations, linalool also demonstrated immunomodulation, caused oxidative stress along with cell cycle arrest, and had an apoptotic effect20. Although linalool and similar phytochemicals have many beneficial pharmacological properties, their therapeutic utility is severely limited by their poor dissolution in water, chemical instability, rapid metabolic deterioration, weak membrane permeability, and reduced levels at the tumor site21,22.

In order to tackle these problems, nanotechnology have emerged as useful platforms for raising the therapeutic index of bioactive substances23. Because of their increased drug loading capacity, longer half-life with primarily low systemic toxicity, improved internalization into the tumor through endocytosis, sustained and controlled release of cytotoxic drugs over the proper duration and time, and body excretion, nanoparticles (NPs) are significant as therapeutic agents in cancer treatments24,25. Silver nanoparticles are naturally harmful to tumor cells and they have shown promise in the treatment of cancer. Linalool incorporation into silver nanocarriers may improve their anticancer efficacy26.

The disturbance of vital signaling pathways that are necessary for maintaining cellular homeostasis is a hallmark of brain tumor growth. These pathways are especially crucial for controlling cell cycle checkpoints, cell death, and proliferation27. In this regard, the p53/p21-CDK4/6 axis is a crucial regulatory system that is essential for regulating the course of the cell cycle and preserving genomic integrity. When p53 is active, it causes the synthesis of p21 leading to suppression of CDK4/6 activity, which results in cell cycle arrest at the G1 phase28,29. Thus, restoring or enhancing p53 function and its downstream effectors is a feasible therapeutic strategy for the treatment of brain tumor.

Currently, in silico molecular docking and simulations are reliable techniques for screening drugs, comprehending their modes of action, and forecasting how they will interact with biological targets30. With the help of computational techniques and in vivo experimental validation, this integrated strategy advances drug development and finds efficient treatments for brain tumor.

This study uses both in vivo and computational approaches to examine the anti-brain tumor effectiveness of linalool-based silver nanoconjugates. Our main goal was to examine the nanoconjugates’ cytotoxic and anticancer effects in vivo as well as their impact on the p53/p21-CDK4/6 signaling pathway modification for development of a dual targeting approach.

## Materials and methods

## In Silico analysis

## Structure retrieval and preparation of target proteins

The important proteins involved in the cell cycle arrest and apoptotic pathways that lead to brain tumor formation were selected. The 3D structures of the target proteins for CDK4 were accessed from AlphaFold with ID: AF ID: AF-P11802-F1-v4 and p53 from the PDB databases with PDB ID: 8DC8. The proteins were prepared by removing all non-essential molecules including water molecules, heteroatoms, and co-crystallized ligands using the Biovia Discovery Studio 2021 software. Cleaned proteins were prepared to reduce the possibility of interference during docking processes. Kollman charges and polar hydrogen were then allocated using AutoDock Tools. After that, the protein structures were saved in PDBQT format so that they could be used for molecular docking.

## Ligand selection and preparation

The PubChem database (https://pubchem.ncbi.nlm.nih.gov/) provided the three-dimensional structure of lead compound linalool (CID: 6549) in SDF format. Linalool based silver nanoconjugate structure was created using Avogadro software environment (http://avogadro.cc/) and MMFF94 force field in the Avogadro software environment (http://avogadro.cc/) was used to minimize the ligand’s energy. Discovery Studio was then used to convert it to PDB format, and the file was saved with the .pdb extension. AutoDock v1.5.7 was employed to allocate torsional flexibility and Gasteiger charges, and the resulting structure was transferred to PDBQT format for further docking investigations31.

## Identification of active sites

CASTpFold (https://cfold.bme.uic.edu/castpfold/), a platform that mainly served to assist the analytical identification of the pockets and cavities of the proteins, was utilized to predict the active sites of the target

receptors. This tool evaluates pocket volumes, surface areas, and topological features in order to validate the predicted binding sites. The binding residues were used to create grid box coordinates for docking studies after being cross-checked with the literature review32.

## Molecular Docking of ligands with target proteins

AutoDock Vina v1.5.7 was used to conduct the docking investigation of ligands with the target proteins (https:// autodock.scripps.edu/). To control different factors including grid dimensions, search space, and the number of output conformations, we have employed a command-line interface for docking. Stable and repeatable docking conditions were made possible by this method. The target protein’s binding location was carefully incorporated into the docking grid. The grid box’s measurements (26 $\mathring { \mathrm { A } } \times 2 6 \mathring { \mathrm { A } } \times 2 6 \mathring { \mathrm { A } } )$ and the center’s coordinates $\bar { ( \mathbf { x } } = - 1 2 ,$ $\begin{array} { r } { \mathrm { y } = - 1 4 , \mathrm { z } = - 1 1 ) } \end{array}$ were specified, which ensures thorough coverage of the binding pocket. The exhaustiveness parameter was set at 8. “Vina --config conf.txt –log log.txt” was the command used to implement the docking process. For each target protein, a maximum of nine binding postures were created, carefully rated based on their lowest binding affinity. Using Discovery Studio Visualizer, visualization was carried out, and two- and three-dimensional diagrams were produced to illustrate the geometry and type of interactions, including π-π stacking interactions, hydrogen bonds, and hydrophobic contacts. The stability and suitability of linalool within the binding pocket of the target proteins was measured using the binding affinities and interaction patterns33,34.

## Molecular dynamic simulations

MD simulations were performed using the Amber tool. An orthorhombic simulation box was created, and a system was built using the ligand-target complex. The ligand topology was constructed using the AMBER force field-GAFF2. The solvated model was then subjected to a salt concentration of 0.15 M. The temperature and pressure were set to 310 K and 1 Pa, respectively. The number of runs was set to 50,000,000, and the simulation period was set to 100 ns to use the Number Volume and Temperature (NVT) and Number Pressure and Temperature (NPT) ensembles. The data were analyzed using root mean square deviation (RMSD), radius of gyration (Rg), and root mean square fluctuation (RMSF) plots35.

## MMGBSA and MMPBSA evaluation

The complex, receptor, and ligand’s interaction and solvation-free energies were computed. The binding free energy was computed using mean values. The GB/SA input parameters, which included a 0.15 M salt concentration and “OBC” models (igb = 2), were used to calculate the binding energy using the MM-GBSA and MM-PBSA methods. Amber tools were employed to conduct the analysis at 10-ns intervals for 100-ns simulations. The last 10 ns of the molecular dynamics trajectories yielded a total of 1,000 photos for calculating energy fluctuations and mean values36,37.

## In vitro analysis

## Synthesis and characterization of Linalool-based silver nanoconjugates (LN@AgNPs)

The linalool–silver nanoconjugates (LN@AgNPs) used in this study were created using our previously reported technique (https://doi.org/10.1371/journal.pone.0333617)38. This publication contains comprehensive experimental information on the creation of nanoparticles, including reaction conditions, optimization, and physicochemical characterization (UV–Vis spectroscopy, FTIR, SEM, DLS, zeta potential, and stability study). The batch of LN@AgNPs used in the current in vitro and in vivo studies was subjected to the same standardized method and characterization criteria.

## Real time quantitative PCR

TRIzolTM Reagent (Thermo Fisher Scientific, USA) was used to separate total RNA from the cancer cell lines. The amount and purity of the RNA were measured using a NanoDropTM 2000 spectrophotometer (Thermo Fisher Scientific). As directed by the RevertAid First Strand cDNA Synthesis Kit (Thermo Fisher Scientific), 2 µg of total RNA was used for cDNA synthesis. Thermo Fisher Scientific’s PowerUpTM SYBRTM Green Master Mix was used to perform quantitative real-time PCR on an Applied BiosystemsTM StepOnePlusTM Real-Time PCR System. The reaction mixture (20 µL) was filled with diluted cDNA (2 µL), 10 µL of 2× SYBR Green Master Mix, $0 . 5 ~ \mu \mathrm { M }$ of both gene-specific primers, and nuclease-free water. The qPCR cycling conditions were as follows: 20 cycles of denaturation at $9 5 ^ { \circ } \mathrm { C }$ for 15 s, annealing at $5 6 ~ ^ { \circ } \mathrm { C }$ for 30 s, and extension at $7 2 ^ { \circ } \mathrm { C }$ for 30 s, followed by an initial denaturation at 95 °C for 5 min. Melt curve analysis was performed following amplification to ascertain the specificity of each product. Each experimental reaction was performed in triplicate. Following normalization against the endogenous control β-actin, the expression levels of p53 and CDK4 were measured using the 2^ΔΔCt approach39. Statistical significance was determined using two-way ANOVA with post hoc Tukey’s test (GraphPad v9, San Diego, CA, USA).

## In vivo model

## Ethical approval

The Institute of Molecular Biology and Biotechnology (IMBB) Ethical Review Committee authorized the in vivo animal research (Ref-IMBB/BBBC/24/904). This study was conducted in compliance with the ARRIVE principles, and all experiments were conducted in compliance with pertinent rules and laws.

## Exposure of N-ethyl-N-nitrosourea (ENU)

At 21th days of pregnancy, a particular group of pregnant female Fischer 344 rats was injected with a solution of 0.1 M ENU (50 mg/kg) in citric acid and phosphate buffer (pH 6) through the tail vein. These conditions are favorable for the highest tumor incidence of the Fischer strain40. The pups were weaned at 22 days. The study included both male and female rats (30 males and 22 females), who were observed every week for signs of neurological or health problems. ENU-induced gliomas were rapidly recognized as display a specific developmental pattern because of their extremely slow growth (latency time of 29 ± 5 weeks). To check for brain malignancies, histopathological examinations were conducted after 25 weeks. Once the tumors were identified, the rats were divided into treatment groups.

## Treatment groups

Three distinct diseased-animal groups were established for this study.

Control group: No therapy. The rats in the control group (n = 6) received no therapy.

Group 1. For 21 days, starting on the day that tumor was verified (i.e., day 0), this group of rats (n = 6) received a daily oral dose of Linalool (100 mg/kg) via a gavage needle.

Group 2. For 21 days, starting on the day that tumor was verified (i.e., day 0), this group of rats (n = 6) received a daily oral dose of LN@AgNPs (100 mg/kg) via a gavage needle.

## Histological analysis

Non-invasive MRI imaging was not available at our research facility; therefore, tumor validation prior to treatment and after treatment relied on histopathological examination. One rat from each experimental group was euthanized (Supplementary Method S1). After being submerged in 4% paraformaldehyde for an entire day, the insulated brains were preserved in paraffin. Hematoxylin and eosin (H&E) staining was applied to 5 μm slices of the brain to histologically demonstrate the development of brain tumor. The presence of a tumor, infiltration pattern, and inherent features in the right entorhinal cortex were examined. Semi-quantitative morphometric analysis using ImageJ software was performed to complement the qualitative assessment.

## Statistical analysis

GraphPad Prism software v9 (San Diego, CA, USA) was used to assess the data statistically (mean ± SD) with a 95% confidence interval41,42. Survival curves were built using the Kaplan-Meier curve, and the statistical differences between them were evaluated using a log-rank (Mantel-Cox) test. Welch’s correction was applied to two-tailed, unpaired Student’s t-tests in order to assess further group differences. Differences were considered statistically significant at p < 0.05 (\*), p < 0.01 (\*\*), or p < 0.001 (\*\*\*).

## Results

## In silico study

## Ligand-protein interaction analysis

To validate the docking process, co-crystallized ligand (CCL) was used to re-dock into the active site of respective protein. Docking procedures were successful against all targets (Supplementary Figure S1), figure displays the redocked stacked structures of CCL of the corresponding proteins along with the number of interaction residues. Molecular docking studies were conducted to gain insight into the various types of amino acid residues and binding interactions that contribute a molecule its biological function. In this work, the binding pockets of the chosen protein receptors p53 with PDB ID: 8DC8 and CDK4 with AlphaFold ID: AF-P11802-F1-v4 were docked with linalool (LN) and its manufactured nanoconjugates (LN@AgNPs). Additionally, temozolomide (TMZ), the reference medication, was added for comparison with the chosen ligands. The results are shown in Table 1.

The p53 protein structure reveals critical functional areas, such as the DNA-binding domain, dimerization, and zinc-binding sites. The Y220C mutation creates a hydrophobic pocket that can bind drugs because it is far from the location where p53 interacts with DNA. Labeling structural elements, such as coils, β helices, and β- sheets, makes it easy to see how the protein is arranged and where the docking target is located (Supplementary Figure S2). The p53-ligand complex’s active site usually featured residues Leu145, Trp146, Val147, Cys220, Pro222, Pro223, and Pro151, according to graphical analysis.

<table><tr><td rowspan=1 colspan=1>Ligand</td><td rowspan=1 colspan=1>Receptor</td><td rowspan=1 colspan=1>Docking score (kcal/mol)</td><td rowspan=1 colspan=1>Type of interaction</td><td rowspan=1 colspan=1>Interacting residues</td><td rowspan=1 colspan=1>Distance (Å)</td></tr><tr><td rowspan=2 colspan=1>LN</td><td rowspan=2 colspan=1> p53</td><td rowspan=2 colspan=1>-4.9</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V147, P222, P223, P151, W146, C220</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>LN@AgNPs</td><td rowspan=3 colspan=1> p53</td><td rowspan=3 colspan=1>-4.5</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1>E221, T230</td><td rowspan=1 colspan=1>2.75, 3.25</td></tr><tr><td rowspan=1 colspan=1>Metal-Bond</td><td rowspan=1 colspan=1>L145</td><td rowspan=1 colspan=1>2.45</td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V147, P222, P223, P151, W146, C220</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>TMZ</td><td rowspan=2 colspan=1>p53</td><td rowspan=2 colspan=1>-5.5</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1>L145, P151</td><td rowspan=1 colspan=1>2.81, 3.41</td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V147, P223, P222, C220, P151,</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>LN</td><td rowspan=2 colspan=1>CDK4</td><td rowspan=2 colspan=1>-5.7</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1>D158</td><td rowspan=1 colspan=1>2.24</td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V20, F93, A33, A157, L147, I12, K35, V72</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>LN@AgNPs</td><td rowspan=3 colspan=1>CDK4</td><td rowspan=3 colspan=1>-5.7</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Metal-Bond</td><td rowspan=1 colspan=1>D158</td><td rowspan=1 colspan=1>2.42</td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V20, F93, A33, A157, L147, I12, K35, V72</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=2 colspan=1>TMZ</td><td rowspan=2 colspan=1>CDK4</td><td rowspan=2 colspan=1>-6.0</td><td rowspan=1 colspan=1>H-Bonds</td><td rowspan=1 colspan=1>H95, V96</td><td rowspan=1 colspan=1>2.03, 2.47</td></tr><tr><td rowspan=1 colspan=1>Hydrophobic</td><td rowspan=1 colspan=1>V20, I12</td><td rowspan=1 colspan=1></td></tr></table>

Table 1. Docking score and target protein amino acid interactions (H-bond, metal acceptor and hydrophobic) of selected compounds against respective receptors.

The binding score for reference (temozolomide − 5.5 kcal/mol) similar to those of linalool (-4.9 kcal/mol) and LN@AgNPs (-4.5 kcal/mol). Like temozolomide (Fig. 1c, f, i), linalool mostly interacts hydrophobically with crucial residues to bind to the hydrophobic pocket of the p53 binding site. The hydrophobicity of the binding pocket plays an essential role for p53 restoration and ligand stability, as these interactions enable persistent binding without the hydrogen bonds formation. (Fig.  1a). No amino acid was found in the hydrogen bond acceptor and donor moiety, according to additional hydrogen bond map analysis (Fig.  1d). In contrast, the hydrophobic map (Fig. 1g) highlights Cys220, Pro222, Pro223, and Trp123 residues. These interactions have the potential to stabilize the ligands within the receptor’s active site.

However, LN@AgNPs formed a more stable complex by forming strong coordination connections with the oxygen atoms in the leucine residue. Ag reacted with the O atoms in cysteine, as it provided electron pairs to Ag (Fig. 1b). LN@AgNPs are more stable toward protein p53 with metal-acceptor connections with residues Leu145 because metallic bonds are more resilient and long-lasting than other interactions, which gives metals their unique strength and stability. At a distance of 2.75 and 3.25 A, which is less than that of TMZ H-bonding residues, LN@AgNPs also established hydrogen bonds with residues Glu221, Thr230. Additionally, the hydrogen bond map (Fig. 1e) demonstrations that residues Glu221, Thr223 generates an acceptor motif with LN@AgNPs. The hydrophobic map was further verified the hydrophobic nature of Trp146, Val147, Cys220, Pro222, Pro223, and Pro151 residues. (Fig. 1h).

The ATP-binding domain comprising the structure of the CDK4 protein (ID: AF-P11802-F1-v4) was obtained from AlphaFold (Supplementary Fig. 3). Many research organizations have reported drug ideas that target this pocket. The amino acid residues Ile12, Gly13, Glu144, Asn145, Leu147, Gly15, Ala157, Asp158, Gly18, Val20, Ala33, Lys35, Val72, Phe93, Glu94, His95, Val96, and Asp99 were commonly found in the CDK4 active site.

<!-- image-->  
Fig. 1. Linalool (a), LN@AgNPs (b), and TMZ (c) complexes with p53 in three dimensions. A succession of color-coded maps demonstrating the binding cavity of the p53 protein, each of which shows a separate physicochemical attribute relevant to the interaction with possible ligands, (d–f) H-bond map (g–i) hydrophobic map.

In Table 1, the binding scores of specific ligands against CDK4 are displayed. At distance 2.24 A, linalool (-5.7 kcal/mol) forms an H-bond with the adjacent CDK4 residues Asp158 (Fig. 2a). Aspartic acid’s donor motif, the hydroxyl group (Asp158), is further validated by the H-bond map (Fig. 2d). Moreover, the hydrophobic residues Val20,Phe93, Ala157, Ile12, Lys35, and Val72 are shown in Fig.  2g. The π-orbital system of phenyl (Phe93) donated its pi-orbital electron to the carbon atom of linalool in the CDK4 binding pocket to create a pi-alkyl bond (Fig. 2a, g).

Additionally, the stability of the CDK4 complex including LN@AgNPs (-5.7 kcal/mol) was superior to that of free linalool. This happens as a result of the silver atoms’ metal-acceptor linkages in LN@AgNPs formed with Asp158 (Fig. 2b). Additionally, alkyl and pi-alkyl interactions improved the stability of the LN@AgNPs complex (Fig. 2h).

Temozolomide, the reference medication, showed a comparable binding affinity (-6.0 kcal/mol); however, because it was encircled by fewer interacting residues, it formed a less stable complex with CDK4 (Fig. 2c, f,i). This suggests that compared to temozolomide, linalool and its nanoconjugates may have superior binding stability.

These compounds exhibit promise as strong CDK4 ligands since CDK4 has more contacts and docking scores than p53 (Table 1). Regarding pathway response, their impact on p53 might support upstream regulatory processes, which would further affect the signaling cascade.

## Molecular dynamic simulation

The dynamic stability and intermolecular interactions of linalool in association with p53 and CDK4 target proteins were evaluated for 100 ns using traditional MD simulations. Significant structural modifications were observed in the overlapping conformations of p53 during the simulation, and all the selected ligands were

<!-- image-->  
(a)

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

(h)  
<!-- image-->

<!-- image-->  
Fig. 2. Linalool (a), LN@AgNPs (b), and TMZ (c) complexes with CDK4 in three dimensions. A succession of color-coded maps demonstrating the binding cavity of the CDK4 protein, each of which shows a separate physicochemical attribute relevant to the interaction with possible ligands, (d–f) H-bond map (g–i) hydrophobic map.

<!-- image-->  
Fig. 3. Stable binding of linalool with p53 (a) and CDK4 (b) throughout the simulation.

(a) p53  
RMSD Analysis for Protein, Pocket, and Ligand  
<!-- image-->  
(b) CDK4

RMSD Analysis for Protein, Pocket, and Ligand  
<!-- image-->  
Fig. 4. RMSD plots for linalool complexed with p53 (a) and CDK64 (b); each docked complex’s distinct 100 ns MD simulation trajectory was used to calculate the ligand RMSD values as the protein-fit ligand.

bound in close proximity to key residues, such as Thr60, Thr140, Val57, Val67, Cys130, Trp56, Pro131, and Pro132 (Fig. 3a). Residue numbering in the molecular dynamics simulation starts at 1, but docking maintains the original protein sequence numbering. As a result, residue Cys130 in the simulation and residue Cys220 in the docking data matched. Therefore, residue Cys220 (Cys130 in simulation) maintained a crucial function in p53, demonstrating the importance in ligand interactions. Throughout the simulation, ligands maintained strong hydrogen bonds and hydrophobic contacts while displaying stable binding inside the CDK4 ATP-binding domain (Fig. 3b).

Protein RMSD values range from 1.5 to 2.5 Å for p53 and 0.5 to 1.5 Å for CDK4, indicating that both proteins are stable, according to the RMSD analysis. Additionally, the binding pockets are maintained, ranging between 1.0 and 2.0 Å. In the p53 complex, linalool exhibits greater variability (0.5–2.5 Å), suggesting less stable binding; when compared to the CDK4 complex, it is more constant (1.0–2.0 Å) (Fig. 4).

The RMSF values of the ligand-protein complexes were also investigated. The RMSF values of linalool with respect to p53 and CDK4 are shown in Fig. 5(a-b). Except for the binding site, most of the RMSF values were less than 3 Å, suggesting that both proteins remained stable during the 100 ns simulation. The C-termini of the protein tail changed in the CDK4 complex, but the N-terminus of the protein revealed modifications in the p53 complex. However, there was a noticeable difference in CDK about residues 30–60 and 90–120, which are roughly 4 Å and 2.5 Å, respectively. At the same time, it is significant that the p53 mutations close to residues 124–140 lie around 3.5 Å. Additionally, the p53 (\~ 16.3–16.7 Å) and CDK4 (\~ 20.1–20.7 Å) radius of gyration (Rg) values (Fig. 5c and d, respectively) stay constant, indicating retained compactness.

<!-- image-->

<!-- image-->

(c)  
<!-- image-->

(d)  
<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 5. The two complexes were compared using 100 ns molecular dynamics (MD) simulations. This comparison focused on three aspects: (a and b) RMSF values of structural residues, (c and d) radius of gyration with time, and (e and f) SASA over the 100 ns period for the protein. The p53/linalool complex data are displayed in (a, c, and f), whereas (b, d, and f) correspond to the CDK4/linalool complex.

<!-- image-->

<!-- image-->  
Fig. 6. Cross-correlation matrix depicting coordinate variations for Cα atoms around the mean coordinates during MD simulation: positive correlations in red whilst negative correlations in blue for complexes of linalool with p53 (a) and CDK4 (b).

SASA values for CDK4 (Fig. 5f) complexes (550–720 Å²) were much greater than those for p53 (340–440 Å²) (Fig. 5e), which is consistent with their distinct functional roles in cancer pathways. This suggests that CDK4 has more solvent exposure and structural modification than p53.

The mobility of residues along the protein chain was correlated using a Dynamic Cross-Correlation Matrix (DCCM). The plots in Fig. 6 (a and b) show distinct DCCM patterns for both complexes. The degree of connection between the nobilities was depicted by a color-coded scheme; blue indicates a low correlation with the residues, while red to pale green hues reveal substantially related mobility. The action of the p53 complex appears to be more consistent and well-coordinated across the protein structure. Less dynamic flexibility is indicated by the weaker negative correlation (blue) (Fig. 6a). Conversely, the CDK4 complex’s associated motions displayed a balance between regions with strong positive (red) and negative (blue) correlations, which may suggest that some residue pairs are flexible and work together. Since the residues are perfectly connected to one another, the diagonal line (red) denotes self-correlation (Fig. 6b).

Both p53 and CDK4 exhibit wider conformational sampling in the PCA projection plots $( \mathrm { F i g . } 7 \mathbf { a } , \mathbf { d } )$ , with p53 showing more scattered clusters, suggesting greater structural flexibility. The 3D free energy landscapes (Fig. 7b, e) show that, in contrast to p53, which exhibits several shallow minima, CDK4 has a deeper and more distinct global minimum, indicating stronger thermodynamic stability. More restricted motions in CDK4 are highlighted by structural changes along PC1 and PC2 (Fig. 7c, f), demonstrating that the CDK4–linalool complex is less flexible and more stable than the p53 complex.

## Binding free energy calculations

Figure 8 illustrates the breakdown of the binding free energy for two systems, likely p53 (Fig. 8a) and CDK4 (Fig.  8b), using MM/PBSA analysis. In the CDK4 complex, van der Waals forces (-21.58  kcal/mol) and electrostatic interactions (-11.16  kcal/mol) were the main contributors to binding, whereas polar solvation added a penalty (+ 20.15 kcal/mol). This resulted in a total binding free energy of -12.59 kcal/mol (PB model) and − 22.12 kcal/mol (GB model). In contrast, the p53 complex showed a binding free energy of -11.34 kcal/mol (PB model) and − 17.97 kcal/mol (GB model), with solvation penalties being much less significant. Here, the van der Waals forces (-21.53 kcal/mol) remained dominant, but the electrostatic interactions were notably smaller (-3.49 kcal/mol). In general, the CDK4 complex exhibited greater binding capacity than the p53 complex due to its beneficial hydrophobic and electrostatic interactions. These outcomes aligned with the docking findings.

## In vitro analysis

Linalool effect on P53 and CDK4 expression in brain tumor cell line (SF-767) using real time quantitative PCR In RT-PCR analysis, the β-actin gene was used as a reference standard to measure gene expression in cells after a 24-hour exposure to the IC50 concentrations of the drugs, as established in our previous study43. A significant negative correlation between p53 and CDK4 expression was identified among the treatment cohorts $( p \leq$ 0.0001). The putative pro-apoptotic mechanism of linalool and its nanoparticle formulations (LN@AgNPs) was corroborated by the observation of a 2 to 2.5-fold increase in P53 expression $( p \leq 0 . 0 0 0 1 )$ (Fig. 9). Conversely, both treatment groups manifested a notable reduction in CDK4 expression $( p \leq 0 . 0 0 0 1 ) .$ , resulting in CDK4 levels being diminished by approximately 1.5 to 2-fold in comparison to the control group $( p \leq 0 . { \dot { 0 } } 0 0 1 )$ . The downregulation of CDK4, a pivotal regulator of cell cycle progression, signifies a potential mechanism underlying cell cycle arrest. These findings validate the efficacy of linalool-based therapeutics and their nanoformulations in facilitating P53-mediated tumor suppression while concurrently inhibiting CDK4-driven cellular proliferation, thereby elucidating their anticancer capabilities (Fig. 9).

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 7. Linalool has two primary eigenvectors with complex p53 (a–c) and CDK4 (d–f) Gibbs free energy landscape (FEL). The purple region represents lower-energy conformations, the green region represents metastable states, and the yellow zone represents high-energy conformations.

p53 Energy Components from MMPBSA Analysis  
<!-- image-->

CDK4 Energy Components from MMPBSA Analysis  
<!-- image-->  
Fig. 8. Binding free energies calculations, (a) p53/linalool and (b) CDK4/linalool.

## In vivo model

## Determination of tumor growth pattern and morphology

The progeny were delivered via natural parturition and subsequently weaned at 22 days of age following exposure to N-ethyl-N-nitrosourea (ENU) in pregnant female Fischer 344 rats. A total of 28 male and 18 female subjects were selected for participation in the study, with weekly monitoring conducted to assess any signs of neurological impairment, health complications, or weight reduction. The subjects were further categorized into smaller cohorts of six individuals, in addition to a control group comprised of naturally born subjects on the same day without any pathological conditions, to ensure precise validation of brain tumor proliferation. At the conclusion of 25 weeks, two rats from each cohort were euthanized for the purpose of histological validation of tumor development (Fig. 10).

Brain tissues collected at week 25 showed characteristic features of tumor development, including pyknosis, vacuolations, gliosis, and cellular atypia, which confirmed the establishment of a brain tumor model. (Fig. 11). Each histological slide was subjected to three distinct types of observational analysis.

Marked histopathological changes suggestive of inflammatory processes and neuronal damage were evident in the rat cerebral photomicrographs. The observation of a pale, enlarged neuropil interspersed with sporadically occurring pyknotic and atrophied neurons indicated the presence of vacuolation alongside neuronal degeneration. A particularly significant finding was the establishment of perivascular cuffs surrounding a blood vessel, which implies neuroinflammatory responses attributed to the infiltration of inflammatory cells (star), predominantly lymphocytes and possibly microglia. This phenomenon is characteristic of neurodegenerative processes. In conjunction with regions exhibiting disrupted neuropil architecture, the tissue appeared to be edematous (Fig. 11A).

Significant histopathological modifications were recognized in the photomicrographs of rat brain specimens. The presence of shrunken neurons exhibiting dark pigmentation (pyknosis) is indicative of neuronal degeneration. In specific regions, the neuropil appears vacuolated (star), which may suggest the occurrence of spongiform alterations, tissue disintegration, or edema. A heightened density of glial cells dispersed throughout the tissue slice signifies reactive gliosis, which is a response to tissue injury. The existence of edema was further corroborated by the manifestation of enlarged interstitial spaces in certain areas. No discernible hemorrhagic changes or inflammatory infiltrates were detected (Fig. 11B).

## Body weight analysis

Subsequent to tumor confirmation, the body weight of the subjects was meticulously monitored, with the findings illustrated in Fig.  12. Following the affirmation of brain tumor, group 1 was administered a dosage of 100 mg/kg of free linalool, while group 2 received 100 mg/kg of nanoformulations on days 3, 5, 7, 9, and 21. Among the control cohorts, the negative control (healthy rats) and the positive control (diseased group without therapeutic intervention) were established. Up to 21 days post-tumor confirmation, the body weight of the brain tumor group exhibited an 8% reduction relative to that of the healthy control group. The subjects in group 1, which received linalool, demonstrated a 6% reduction in body weight until day 15, followed by a subsequent increase of 1.4% and 1.2%, respectively, by day 21. Upon administration of LN@AgNPs, the body weight of group 2 showed a 4% decline until day 13 and an alteration of less than 2.5% from their baseline weights (Supplementary Table S1).

<!-- image-->  
Fig. 9. RT-PCR was used to examine the relative expression levels of p53 (green) and CDK4 (red) in cells treated with linalool and LN@AgNPs. The results are presented as means with 95% confidence intervals. A two-way ANOVA was conducted to determine statistical significance, followed by Tukey’s post-hoc test to compare each treatment group with the control.

<!-- image-->  
Fig. 10. Tissue Collection for Histopathological Analysis: Representative images of rat dissection for tumor evaluation. Brain tissues were harvested for histopathological examination to assess tumor progression.

<!-- image-->  
Fig. 11. Histological features of two different groups in the F344 brain tumor rat model.

<!-- image-->  
Fig. 12. Effects of various treatments on changes in body weight during a 21-day period in rats with brain tumor. The body weight of tumor-bearing (untreated) rats decreased, whereas that of control (healthy) rats remained constant. Linalool (group 1) and LN@AgNPs (group 2). To evaluate treatment-associated toxicity and protective effects, body weight percentages were measured regularly.

## Survival trends in experimental groups (Kaplan-Meier survival Analysis)

Overall survival was calculated commencing on day 0 (tumor confirmation) and concluding on day 21 (either death or termination of the trial) (Supplementary Table S2). Subjects in the LN@AgNPs group exhibited superior survival outcomes compared to those in the free linalool group (Fig. 13). The findings indicated that the administration of free phytochemicals did not significantly influence animal survival duration, as evidenced in the Kaplan-Meier survival plot (Fig. 13). The utilization of linalool-based nanoconjugates markedly prolonged survival time in comparison to the free form, according to the results.

## Quantitative morphometric analysis

Brain tissues were collected for histopathological evaluation to investigate tumor progression subsequent to treatment. Rat brain tissues subjected to linalool and its silver nanoconjugates underwent morphometric analysis utilizing ImageJ software to assess tumor volume, alterations in peritumoral intensity, and histological modifications. Regions of Interest (ROI) were designated for precise measurements to quantify tumor growth and peritumoral edema.

Histological slides were scrutinized to evaluate fluctuations in intensity within the peritumoral regions. Distinct infiltration patterns between the treatment groups are denoted by the pixel intensity gradient. Rats harboring untreated gliomas displayed a definitive tumor boundary characterized by a sharp transition between tumor tissue (high-intensity pixels) and healthy tissue (low-intensity pixels) (Fig.  14). The intensity gradient exhibited a more gradual decline following treatment with LN@AgNPs, suggesting diminished tumor infiltration and potential therapeutic advantages (Fig. 15).

Following linalool nanoconjugate treatment, tumor volume measurement revealed a 13% decrease in tumor growth when compared to untreated controls (positive control), which exhibited a total volume of 315µm3. Using ImageJ-based evaluation, linalool nanoconjugates were identified as the three most successful therapies among the treatment groups, as shown in Fig. 16. However, there was no appreciable reduction in tumor size when using free phytochemicals, indicating that nanoconjugation is a highly effective at inhibiting tumors (Fig. 17) (Supplementary Table S3). Since each part of histological slices has a thickness (Z-depth) of 5 μm, the tumor volume is calculated utilizinf the following formula, which is based on ImageJ estimation:

$$
\mathrm { { T u m o r } \ V o l u m e } = \sum \left( \mathrm { { A r e a } \ i n \ \mu m ^ { 2 } \right) \times \mathrm { { S l i c e } \ T h i c k n e s s \ ( \mu m ) } }
$$

## Discussion

The current standard of care for individuals with brain tumor usually includes a multimodal strategy after surgical resection. This typically entails the use of radiation and chemotherapeutic drugs like TMZ. The average survival rate for patients with tumor (less than 9.8%) has not improved much in the last ten years using these therapeutic approaches. One of the main obstacles in the treatment of brain tumor is the emergence of resistance and adverse effects caused by traditional treatments. As a result, the scientific community is becoming more interested in determining potential novel therapeutic approaches and assessing the effectiveness of novel active compounds44. Numerous preclinical and clinical investigations have demonstrated the advantages of combining a variety of phytocompounds with traditional anticancer therapies. The main components of therapeutic herbs are essential oils which are widely used in the pharmaceutical sector45,46. Linalool is an essential component of many essential oils exhibiting significant biological qualities such as antiviral, antioxidant, and antibacterial effects. Some studies showing that linalool may prevent, stop, or even reverse the growth of malignant cells, they have also been suggested as possible anticancer adjuvants15,47. Another hindrance for effective treatment of brain tumor is reduce drug penetration across BBB, oxidation of phytochemicals and unstability in water48,49. Hence, there is a need to develop nanoformulations to encounter these limitations. We have investigated the anticancer impact of linalool and synthesized linalool coupled silver nanoconjugates through a comprehensive study involving computational docking, molecular dynamics simulations, in vitro biological assays, gene expression profiling, and an in vivo model of brain tumor induced by ethylnitrosourea (ENU).

<!-- image-->  
Fig. 13. Kaplan-Meier survival analysis of a rat model of brain tumor after 21 days of treatment. While the treatment groups demonstrated varying degrees of enhanced survival, the control group (tumor, untreated) showed the lowest survival probability, while linalool (Group 1) and LN@AgNPs (Group 2) were among the treatment groups.

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 14. Comparison of histological slides of (A) healthy brain tissue and (B) brain tumor tissue, analyzed using ImageJ plot profile. The plot profiles show signal intensity variations across the selected regions. Healthy tissue exhibits a smooth intensity gradient, indicating uniform cellular distribution, whereas tumor tissue shows fluctuating intensity, highlighting structural heterogeneity and the presence of extracellular or necrotic areas.

<!-- image-->  
Fig. 15. Signal intensity plot profiles of regions of interest (ROI) for the treatment groups using nanoconjugates. The variations in signal intensity across pixel positions indicate differences in cellular architecture and treatment effects.

<!-- image-->  
Fig. 16. Histological analysis of brain tumor and treatment groups. (a) Tumor (control), (b) LN@AgNPs, and (c) linalool. ImageJ-based quantification confirms these nanoconjugates as the most effective therapies.

<!-- image-->

<!-- image-->  
Fig. 17. Tumor volume analysis and heatmap representation of treatment groups. (a) Total tumor volume across different treatment groups, including tumor (control), LN@AgNPs and their free counterparts. (b) Heatmap visualization of tumor volume variations, highlighting the differences in response among the treatment groups.

We have conducted molecular docking of linalool with mutant p53 and CDK4 proteins. P53 is a tumor suppressor protein which causes more than half of human cancers. Mutations in the p53 gene mostly affect the DNA-binding domain, leading to loss of function and the buildup of defective p53 protein in tumors. LN@ AgNPs binds with p53 near Y220C mutation which is responsible for impairing its ability to control tumors in brain50,51. Our results confirm activation of p53 signaling pathway using linalool coupled silver nanoparticles by direct binding of linalool in hydrophobic part of mutant protein leading to structural alterations and proper functioning of p53. Another study shows binding of small drug like molecules with mutant p53 and its activation based on docking scores52. The complex’s stabilization and strong binding are further facilitated by the silver core of LN@AgNPs. Rath et al. also described similar effects after binding of phytochemicals extracted from moringa sp. with p53 protein53. The aberrant growth of tumor cells is typically linked to the unchecked cyclin CDK4/6- RB (cyclin-dependent kinases 4/6-retinoblastoma protein) signaling pathway. Additionally, the unchecked signal pathway causes excessive phosphorylation of RB and disassociation of E2F transcription factors during the G1 stages of the cell cycle, which ultimately results in unchecked cell proliferation54,55. According to our docking studies, LN@AgNPs interacts with CDK4 via Asp158 and Phe93 residues, which promotes hydrogen bonding and π stacking interactions. Our predicted docking score of -5.7 kcal/mol is in good agreement with values reported for curcumin, eugenol and catechin56–58. According to molecular dynamics simulations, radius of gyration (Rg) and root mean square deviation (RMSD) analyses verified that the CDK4–linalool complex maintained stability and compactness during the simulation. Our findings are supported by other investigations that reported plant based polyphenols like quercetin/curcumin or chemicals derived from marine sources effectively stabilize kinase structures55,59.

We have observed that p53–linalool complex showed weaker binding and less stability compared to CDK4- linalool complex. According to Ahammad et al., phytochemicals extracted from neem plants have inhibitory activity in CDK-targeting, which is confirmed by strong binding, cooperative movement, and reduced flexibility60. In contrast to the p53 complexes, CDK4–linalool complexes inhabited energy minima of greater depth and stability, as shown by principal component analysis61. Because mutant p53 is intrinsically unstable, the p53– linalool complex showed reduce energetics and minimum electrostatic interactions. Kinase inhibitors heavily rely on hydrophobic and electrostatic interactions for efficient binding exhibited lowest binding energies62. The binding free energy calculations using MM/PBSA further supported the strong electrostatic and van der waals interactions between linalool and CDK4, resulting in estimated energies of − 12.59 kcal/mol (PB) and − 22.12 kcal/mol (GB)63.

Furthermore, we have assessed the effects of linalool and LN@AgNPs on cellular proliferation and apoptosis. LN@AgNPs exhibit strong anticancer potential compared to free linalool. According to a few earlier studies, linalool demonstrated significant inhibition on liver, colorectal, and breast cancer cells18,64. Linalool induces cell cycle arrest at G stage in liver cancer, suppresses CDK4 and cyclin A activity, enhances p21 tumor suppressor protein expression, and boosts ROS production leading to cell death65. By reducing cell growth and tumor spread through a ROS-mediated pathway, linalool has demonstrated potent antiproliferative and chemosensitizing effects against specific solid tumor cells, including adenocarcinoma cells66. Linalool was particularly harmful to human ovarian cancer cell line (A2780) cells, causing apoptosis by activating the p53 protein and caspase-8 through both internal and external pathways. Lavender essential oil decreases oxidative stress in GBM U87 cells and hinders cell migration and proliferation. Terpinen-4-ol could replicate the oil’s effects on GBM cells and can be useful adjuncts to traditional treatments for GBM67,68.

We also found that linalool and LN@AgNPs gene expression analysis showed elevated levels of the p53 protein and reduced levels of CDK4. Salimi et al. reported that linalool induces its antitumor effects by activating p53 through ROS mediated pathway69. According to numerous studies, linalool inhibits CDK4 expression, which slows down the progression of the cell cycle and tumor migration. It also activates the p53 protein, which promotes cell death70. Our findings offer thorough insights into the intricate mechanism of action and are in line with previous research. Our findings supported the use of dual targeting therapy to treat brain tumor by promoting cell death and stopping the cell cycle.

We have utilized LN@AgNPs in glioma-induced rat models to further validate our findings. Tumor validation was performed using histology, which remains a basic and often used technique for verifying tumor growth71. Histopathology is still used as a major assessment method before or in conjunction with imaging modalities, even in current preclinical brain tumor research72. Cellular anomalies, such as pyknosis, vacuolation, and gliosis, observed in our model verified the successful creation of a brain tumor. LN@AgNPs demonstrated a 13% increase in tumor load reduction and increased overall survival when compared to free linalool. According to our findings, LN@AgNPs considerably reduced tumor size, stopped peritumoral infiltration, and increased survival in rats that developed induced gliomas. Our findings are in line with other research that found that using galactomannan in conjunction with silver nanoparticles to target solid tumors increased survival while decreasing tumor size and migration to neighboring cells73. Similar outcomes were reported by Lee et al. using resveratrol coupled gold NPs, which also increased the survival rate of mice in PANC-1 pancreatic cells and decreased tumor size by apoptosis74. Our morphometric analysis confirmed the reduction in tumor size as well as cellular infiltration in surrounding tissues, which is in line with the anti-angiogenic and antiinvasive effects previously documented with thymol carbon nanodot and daphnetin-loaded nanoparticles based delivery systems in ovarian and breast cancer75,76. LN@AGNPs also depict stability in body weight and other relevant parameters indicating lower systemic effects. Methotrexate-loaded chitosan nanoparticles significantly decreased tumor weight, multiplication, and systemic toxicity77. In a different study, methotrexate-coupled gold nanoparticles demonstrated increased cell death, decreased proliferation, and minimal tumor burden in lung cancer78. Although the 21-day follow-up provided reliable indications of treatment efficacy, it may not have captured long-term tumor progression. Future studies with extended follow-up are warranted to assess the longterm efficacy and survival benefits.

In conclusion, we have shown that LN@AgNPs are a promising phytochemical-based nanomedicine with strong potential for treating brain tumor. This formulation targets both the apoptotic and cell proliferation pathways, demonstrating its therapeutic potential. Pharmacokinetics, biodistribution, and long-term safety in patient-derived models should be examined in future research. To bring this promising strategy closer to clinical use, it will also be required to enhance nanoparticle design and investigate combination therapies with conventional drugs.

The lack of direct biodistribution or blood–brain barrier penetration data for LN@AgNPs is a limitation of this study. The quantitative evaluation of nanoparticle dispersion and accumulation in the brain and tumor tissues will be the main focus of future research.

## Data availability

All datasets analyzed in this study are included in the main manuscript and the supplementary files.

Received: 10 October 2025; Accepted: 9 December 2025

Published online: 10 April 2026

## References

1. Pichaivel, M. et al. An Overview of Brain Tumor (IntechOpen, 2022).

2. Kumari, S. & Kumar, P. Design and computational analysis of an mmp9 inhibitor in hypoxia-induced glioblastoma multiforme. ACS Omega. 8 (11), 10565–10590 (2023).

3. Holland, E. C. Glioblastoma multiforme: the terminator. Proc. Natl. Acad. Sci. 97 (12), 6242–6244 (2000).

4. Stupp, R. et al. Effect of tumor-treating fields plus maintenance Temozolomide vs maintenance Temozolomide alone on survival in patients with glioblastoma: a randomized clinical trial. Jama 318 (23), 2306–2316 (2017).

5. Alifieris, C. & Trafalis, D. T. Glioblastoma multiforme: pathogenesis and treatment. Pharmacol. Ther. 152, 63–82 (2015).

6. Yang, L. J., Zhou, C. F. & Lin, Z. X. Temozolomide and radiotherapy for newly diagnosed glioblastoma multiforme: a systematic review. Cancer Invest. 32 (2), 31–36 (2014).

7. Cha, G. D. et al. Advances in drug delivery technology for the treatment of glioblastoma multiforme. J. Controlled Release. 328, 350–367 (2020).

8. Rajendran, A. T. et al. Selection of potential natural compounds for poly-ADP-ribose polymerase (PARP) Inhibition in glioblastoma therapy by in Silico screening methods. Saudi J. Biol. Sci. 30 (7), 103698 (2023).

9. Wang, Y. et al. Remodelling and treatment of the blood-brain barrier in glioma. Cancer Manage. Res., : pp. 4217–4232. (2021).

10. Galstyan, A. et al. Blood–brain barrier permeable nano immunoconjugates induce local immune responses for glioma therapy. Nat. Commun. 10 (1), 3850 (2019).

11. Ağagündüz, D. et al. Cruciferous vegetables and their bioactive metabolites: from prevention to novel therapies of colorectal cancer. Evidence-based Complement. Altern. Med. 2022 (1), 1534083 (2022).

12. Sharma, M. et al. Essential Oils as Anticancer Agents: Potential Role in malignancies, Drug Delivery mechanisms, and Immune System Enhancement Vol. 146, p. 112514 (Biomedicine & Pharmacotherapy, 2022).

13. Mahboob, A. et al. Food-derived phytochemicals from functional food (Allium sativum) as VEGF-R1 inhibitors: A novel approach for triple-negative breast cancer therapy. Food Bioscience. 63, 105663 (2025).

14. Valizadeh, A. et al. Anticarcinogenic effect of Chitosan nanoparticles containing syzygium aromaticum essential oil or Eugenol toward breast and skin cancer cell lines. BioNanoScience 11 (3), 678–686 (2021).

15. Ravizza, R. et al. Linalool, a plant-derived monoterpene alcohol, reverses doxorubicin resistance in human breast adenocarcinoma cells. Oncol. Rep. 20 (3), 625–630 (2008).

16. Elbe, H. et al. Anticancer activity of linalool: comparative investigation of ultrastructural changes and apoptosis in breast cancer cells. Ultrastruct. Pathol. 46 (4), 348–358 (2022).

17. Gu, Y. et al. Linalool preferentially induces robust apoptosis of a variety of leukemia cells via upregulating p53 and cyclin-dependent kinase inhibitors. Toxicology 268 (1–2), 19–24 (2010).

18. Xie, L. et al. α-Linalool from coriander root inhibits the proliferation and invasion of a human gastric cancer cell line. Clin. Cancer Invest. J. 12 (5-2023), 6–14 (2023).

19. Gunaseelan, S. et al. The preventive effect of Linalool on acute and chronic UVB-mediated skin carcinogenesis in Swiss albino mice. Photochem. Photobiol. Sci. 15, 851–860 (2016).

20. Mansour, K. A. et al. Nanoemulsions of Jasminum humile L. and Jasminum grandiflorum L. essential oils: an approach to enhance their cytotoxic and antiviral effects. Molecules 27 (11), 3639 (2022).

21. Jana, S. et al. Antitumorigenic potential of Linalool is accompanied by modulation of oxidative stress: an in vivo study in sarcoma-180 solid tumor model. Nutr. Cancer. 66 (5), 835–848 (2014).

22. An, Y. et al. Preparation and application of a novel pH-responsive Linalool carboxymethyl Chitosan hydrogel. J. Macromolecular Sci. Part. A. 60 (5), 336–345 (2023).

23. Ishiguro, K. et al. Targeting liver cancer stem cells using engineered biological nanoparticles for the treatment of hepatocellular cancer. Hepatol. Commun. 4 (2), 298–313 (2020).

24. Sanoff, H. K. et al. Phase I/II trial of nano-camptothecin CRLX101 with capecitabine and radiotherapy as neoadjuvant treatment for locally advanced rectal cancer. Nanomed. Nanotechnol. Biol. Med. 18, 189–195 (2019).

25. Hsing, M. T. et al. Improved delivery performance of n-butylidenephthalide-polyethylene glycol-gold nanoparticles efficient for enhanced anti-cancer activity in brain tumor. Cells 11 (14), 2172 (2022).

26. Bin-Jumah, M. et al. Effects of green silver nanoparticles on apoptosis and oxidative stress in normal and cancerous human hepatic cells in vitro. Int. J. Nanomed., : pp. 1537–1548. (2020).

27. Afjei, R. et al. A new Nrf2 inhibitor enhances chemotherapeutic effects in glioblastoma cells carrying p53 mutations. Cancers 14 (24), 6120 (2022).

28. Ding, J. et al. EGFR suppresses p53 function by promoting p53 binding to DNA-PKcs: a noncanonical regulatory axis between EGFR and wild-type p53 in glioblastoma. Neuro-oncology 24 (10), 1712–1725 (2022).

29. Villano, J. L. et al. Association of CDK4 Amplification with Duration of Response To Bevacizumab in Glioblastoma (American Society of Clinical Oncology, 2023).

30. Tharamelveliyil Rajendran, A. et al. Uncovering naringin’s anticancer mechanisms in glioblastoma via molecular Docking and network Pharmacology approaches. Sci. Rep. 14 (1), 21486 (2024).

31. Butt, S. S. et al. Molecular Docking using chimera and Autodock Vina software for nonbioinformaticians. JMIR Bioinf. Biotechnol. 1 (1), e14232 (2020).

32. Fernandez, M. & Goud, D. K. In-Silico Studies of RBP7, CALML3, C35, LGALSL, S100A3 Proteins Involved in Breast Cancer. Convergence of Technology & Biology Transforming Life Sciences, : pp. 127–142. (2025).

33. Feng, Y. et al. A network Pharmacology prediction and molecular docking-based strategy to explore the potential Pharmacological mechanism of astragalus Membranaceus for glioma. Int. J. Mol. Sci. 24 (22), 16306 (2023).

34. Sakhawat, A. et al. Natural compound targeting BDNF V66M variant: insights from in Silico Docking and molecular analysis. Amb Express. 13 (1), 134 (2023).

35. Vyshnavi, A. M. In Silico analysis of the effect of hydrastis Canadensis on controlling breast cancer. Medicina 59 (8), 1412 (2023).

36. Chahal, V. & Kakkar, R. A combination strategy of structure-based virtual screening, MM-GBSA, cross docking, molecular dynamics and metadynamics simulations used to investigate natural compounds as potent and specific inhibitors of tumor linked human carbonic anhydrase IX. J. Biomol. Struct. Dynamics. 41 (12), 5465–5480 (2023).

37. Jabeen, S. et al. Identifying novel inhibitors against drug-resistant mutant CYP-51 Candida albicans: A computational study to combat fungal infections. PLoS One. 20 (3), e0318539 (2025).

38. Manzoor, H. et al. Novel Linalool-Silver nanoparticles: Synthesis, characterization, and dual approach evaluation via computational Docking and antibacterial assays. PLoS One. 20 (10), e0333617 (2025).

39. Chen, S. et al. LncRNA RMST suppresses the progression of colorectal cancer by competitively binding to miR-27a-3p/RXRα axis and inactivating Wnt signaling pathway: RMST suppresses the progression of colorectal cancer. Acta Biochim. Biophys. Sin. 55 (5), 726 (2023).

40. Kish, P. E. et al. Magnetic resonance imaging of ethyl-nitrosourea-induced rat gliomas: a model for experimental therapeutics of low-grade gliomas. J. Neurooncol. 53, 243–257 (2001).

41. Osanloo, M. et al. Comparison effects of ferula gummosa essential oil and Beta-pinene alginate nanoparticles on human melanoma and breast cancer cells proliferation and apoptotic index in short term Normobaric hyperoxic model. BMC Complement. Med. Ther. 23 (1), 428 (2023).

42. Mirabdaly, S. et al. Effects of Temozolomide on U87MG glioblastoma cell expression of CXCR4, MMP2, MMP9, VEGF, antiproliferatory cytotoxic and apoptotic properties. Mol. Biol. Rep. 47, 1187–1197 (2020).

43. Manzoor, H. et al. Linalool-based silver nanoconjugates as potential therapeutics for glioblastoma: in Silico and in vitro insights. PloS One. 20 (6), e0325281 (2025).

44. Sabouri, M. et al. Survival rate of patient with glioblastoma: a population-based study. Egypt. J. Neurosurg. 39 (1), 42 (2024).

45. McAleenan, A. et al. Prognostic Value of Test (s) for O6-methylguanine–DNA Methyltransferase (MGMT) Promoter Methylation for Predicting Overall Survival in People with Glioblastoma Treated with Temozolomide. Cochrane Database of Systematic Reviews, 2021(3).

46. Smerdi, D. et al. Overcoming resistance to Temozolomide in glioblastoma: a scoping review of preclinical and clinical data. Life 14 (6), 673 (2024).

47. Silva, B. I. et al. Anticancer activity of monoterpenes: A systematic review. Mol. Biol. Rep. 48, 5775–5785 (2021).

48. Lu, Y. et al. Bioavailability and brain-targeting of Geniposide in gardenia-borneol co-compound by different administration routes in mice. Int. J. Mol. Sci. 13 (11), 14127–14135 (2012).

49. Wang, L. et al. Improved brain delivery of pueraria flavones via intranasal administration of borneol-modified solid lipid nanoparticles. Nanomedicine 14 (16), 2105–2119 (2019).

50. Radhakrishnan, N. et al. Caffeic acid phenethyl ester (CAPE) confers wild type p53 function in p53 Y220C mutant: bioinformatics and experimental evidence. Discover Oncol. 12, 1–13 (2021).

51. Shefrin, S. et al. Comparative computational and experimental analyses of some natural small molecules to restore transcriptional activation function of P53 in cancer cells harbouring wild type and P53Ser46 mutant. Curr. Res. Struct. Biology. 4, 320–331 (2022).

52. Liu, X. et al. Small molecule induced reactivation of mutant p53 in cancer cells. Nucleic Acids Res. 41 (12), 6034–6044 (2013).

53. Rath, S., Jagadeb, M. & Bhuyan, R. Molecular Docking of bioactive compounds derived from Moringa Oleifera with p53 protein in the apoptosis pathway of oral squamous cell carcinoma. Genomics Inf. 19 (4), e46 (2021).

54. Wood, D. J. & Endicott, J. A. Structural insights into the functional diversity of the CDK–cyclin family. Open. Biology. 8 (9), 180112 (2018).

55. Luo, L., Wang, Q. & Liao, Y. The inhibitors of CDK4/6 from a library of marine compound database: A pharmacophore, ADMET, molecular Docking and molecular dynamics study. Mar. Drugs. 20 (5), 319 (2022).

56. Wu, C. et al. Exploring the mechanism of Curcumin on retinoblastoma based on network Pharmacology and molecular Docking. Evidence-Based Complement. Altern. Med. 2022 (1), 2407462 (2022).

57. Kusumorini, A. et al. In-Silico Analysis of Eugenol and Beta-Caryophyllene Compounds in Clove (Syzygium aromaticum L.) on NFkB Protein As Anti-inflammatory Agent In Atherosclerosis. Elkawnie: Journal of Islamic Science and Technology, 10(1): pp. 88–102. (2024).

58. Metibemu, D. S. 3D-QSAR and molecular Docking approaches for the identification of novel phyto-inhibitors of the cyclindependent kinase 4. Sci. Lett. 9 (2), 42–48 (2021).

59. Patil, P. H. et al. Molecular dynamics simulation and in vitro evaluation of herb–drug interactions involving dietary polyphenols and CDK inhibitors in breast cancer chemotherapy. Phytother. Res. 36 (10), 3988–4001 (2022).

60. Ahammad, F. et al. Pharmacoinformatics and molecular dynamics simulation-based phytochemical screening of Neem plant (Azadiractha indica) against human cancer by targeting MCM7 protein. Brief. Bioinform. 22 (5), bbab098 (2021).

62. Nagare, S., Lokhande, K. B. & Swamy, K. V. Docking and simulation studies on Cyclin D/CDK4 complex for targeting cell cycle arrest in cancer using Flavanone and its congener. J. Mol. Model. 29 (4), 90 (2023).

63. Rani, N. & Kumar, P. Exploring natural compounds as potential CDK4 inhibitors for therapeutic intervention in neurodegenerative diseases through computational analysis. Mol. Biotechnol., : pp. 1–20. (2024).

64. Zhang, Q. & Chen, D. Validating Linalool as a potential drug for breast cancer treatment based on machine learning and molecular Docking. Drug Dev. Res. 85 (4), e22223 (2024).

65. Tamilmani, P. et al. Linalool attenuates lipid accumulation and oxidative stress in metabolic dysfunction-associated steatotic liver disease via Sirt1/Akt/PPRA-α/AMPK and Nrf-2/HO-1 signaling pathways. Clin. Res. Hepatol. Gastroenterol. 47 (10), 102231 (2023).

66. Huda, R. et al. Role of terpenoids in breast cancer prevention and therapy. Curr. Pharmacol. Rep. 10 (6), 436–446 (2024).

67. Russo, M. et al. Lavender essential oil and its terpenic components negatively affect tumor properties in a cell model of glioblastoma. Molecules 29 (24), 6044 (2024).

68. Sahib Abed, H. et al. Inhibition the growth of human ovarian cancer cells (A2780) via cell proliferation and angiogenesis by viola odorata essential oil nanoemulsion. Waste Biomass Valoriz. 15 (4), 2417–2426 (2024).

69. Salimi, A. et al. Linalool reverses benzene-induced cytotoxicity, oxidative stress and lysosomal/mitochondrial damages in human lymphocytes. Drug Chem. Toxicol. 45 (6), 2454–2462 (2022).

70. Ding, H. et al. Linalool suppresses proliferation and promotes apoptosis in gastric cancer cells via activation of reactive oxygen Species-Mediated P53 pathway. Curr. Top. Nutraceutical Res., 18(4). (2020).

71. Candolfi, M. et al. Intracranial glioblastoma models in preclinical neuro-oncology: neuropathological characterization and tumor progression. J. Neurooncol. 85 (2), 133–148 (2007).

72. Sahu, U. et al. Rat and mouse brain tumor models for experimental neuro-oncology research. J. Neuropathology Experimental Neurol. 81 (5), 312–329 (2022).

73. Syama, H. et al. Bio fabrication of Galactomannan capped silver nanoparticles to apprehend Ehrlich Ascites carcinoma solid tumor in mice. J. Drug Deliv. Sci. Technol. 76, 103649 (2022).

74. Lee, D. G. et al. Resveratrol-loaded gold nanoparticles enhance caspase-mediated apoptosis in PANC-1 pancreatic cells via mitochondrial intrinsic apoptotic pathway. Cancer Nanotechnol. 13 (1), 34 (2022).

75. Seçme, M. & İlhan, H. Synthesis and characterization of thymol carbon nanodot functionalized silver nanoparticles (ThCND-AgNPs) and evaluation of their Antiproliferative, Anti‐Invasive, and apoptotic effects on OVCAR‐3 ovarian cancer cells. Microsc. Res. Tech. 88 (3), 668–677 (2025).

76. Homaeii, S., Kavousi, M. & Asgari, E. A. Investigating the apoptotic and antimetastatic effect of daphnetin-containing nano niosomes on MCF-7 cells. Adv. Cancer Biology-Metastasis. 14, 100139 (2025).

77. Verma, R., Rani, V. & Kumar, M. -vivo anticancer efficacy of self-targeted methotrexate-loaded polymeric nanoparticles in solid tumor-bearing rat. Int. Immunopharmacol. 119, 110147 (2023).

78. Vasil’kov, A. et al. Evolution of gold and iron oxide nanoparticles in conjugates with methotrexate: synthesis and anticancer effects. Materials 16 (8), 3238 (2023).

## Acknowledgements

The authors extend their appreciation to the Deanship of Scientific Research at Northern Border University, Arar, Saudi Arabia, for funding this research work through the project number NBU-FFR-2026-2042-01.

## Author contributions

M.U.K. supervised the study and revised the manuscript. H.M. performed experiments and data analysis. F.J. assisted in biological assays. A.K. and M.I. conducted computational studies. T.A.C. contributed to molecular modeling. A.R.A. and Z.U.R. assisted in data interpretation and manuscript editing. All authors approved the final version.

## Declarations

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary Information The online version contains supplementary material available at https://doi.org/1 0.1038/s41598-025-32335-w.

Correspondence and requests for materials should be addressed to M.U.K.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommo ns.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2026