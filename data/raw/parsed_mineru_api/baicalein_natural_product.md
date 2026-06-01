RESEARCH ARTICLE

# In-silico prediction of multi-target mechanisms of Pinellia ternata phytochemicals in lung cancer: Evidence from a graph-attention-guided virtual screening and multi-scale simulations

Guoqiang Bian1,2,3☯, Yuanbin Zhang1,2,3☯, Yuanhao Shen1 , Pengcheng Xiao1 , Daifeng Zhang1 , Jiadong Xie1,2,3 , Xiong Li1 , Duo Chen1 , Kongfa Hu1,2,3 , Chenjun Hu 1,2,3 \*

<!-- image-->

Citation: Bian G, Zhang Y, Shen Y, Xiao P, Zhang D, Xie J, et al. (2026) In-silico prediction of multi-target mechanisms of Pinellia ternata phytochemicals in lung cancer: Evidence from a graph-attention-guided virtual screening and multi-scale simulations. PLoS One 21(5): e0349376. https://doi.org/10.1371/journal. pone.0349376

Editor: Taye Beyene Demissie, University of Botswana, BOTSWANA

## OPEN ACCESS

Received: November 19, 2025

Accepted: April 28, 2026

Published: May 18, 2026

1 School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine, Nanjing, China, 2 Jiangsu Collaborative Innovation Center of Traditional Chinese Medicine in Prevention and Treatment of Tumor, Nanjing, China, 3 Jiangsu Province Engineering Research Center of TCM Intelligence Health Service, Nanjing University of Chinese Medicine, Nanjing, China

Copyright: © 2026 Bian et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data availability statement: The code of the initial candidate gene set and HERBGAT model used in this research is publicly available and can be downloaded through GitHub at: https:// github.com/labnjucm/HERBGAT.

☯ These authors contributed equally to this work.

\* hcjhyl@njucm.edu.cn

## Abstract

Pinellia ternate has long been used to treat respiratory diseases, possessing potential anti-tumor activity and exhibiting multi-component, multi-target characteristics. This study prioritized lung cancer-related targets using the HERBGAT framework based on graph attention networks (GAT). High-quality PDB structures were retrieved, and diffusion-generative docking was performed to construct complex conformations and assess their confidence levels. Molecular dynamics simulations of representative complexes were conducted over 200 ns, and binding free energies were estimated using the MM/PBSA method. The pharmacokinetic characteristics of the bioactive compounds were evaluated using Swiss ADME and PreADMET computational tools, and density functional theory (DFT) analysis using ORCA software was combined to explore their electronic structure and properties. In this study, the potential targets of Pinellia ternata highly overlap with lung cancer pathological genes, with FGFR4, CDK2, JAK2, KDR, PAK4, PTK2 and PDGFRA being the core. Baicalein exhibits a conserved binding mode of “hinge hydrogen bond-aromatic interlayer-hydrophobic groove” at targets such as PTK2/KDR/JAK2. Energy decomposition indicates that van der Waals forces and nonpolar solvation are the main thermodynamic driving forces for complex formation. Density functional theory (DFT) analysis further reveals that the high electronic “softness” of baicalein and its sensitive response to the environment in terms of frontier orbitals and electrostatic potential may be related to its high affinity, which is ubiquitous in different pockets. This study provides a computational chain of evidence for the intervention of Pinellia ternata’s active ingredient on lung cancer-related targets. The well-defined cross-target migratory pharmacophore of baicalein, consistent energy and kinetics, and the oral pharmacodynamics

Funding: This study was financially supported by the National Natural Science Foundation of China (82575255), the National Science and Technology Innovation 2030 Major Program (2025ZD0544900), the Frontier Technology Research and Development Program of Jiangsu Province (BF2025076), the Jiangsu Province Postgraduate Research Innovation Project (KYCX24_2144) and the Jiangsu Province Postgraduate Research Innovation Project (KYCX25_2271).

Competing interests: The authors have declared that no competing interests exist.

of ADMET indicate that it can serve as a multi-target lead compound targeting the PTK2/KDR migration-angiogenesis pathway, while also affecting JAK2 and CDK2. Given that the current evidence is based on in-silico predictions, further validation through target enzymology, binding thermodynamics, and cellular pathway experiments is needed.

## Introduction

Lung cancer remains the leading cause of cancer-related deaths worldwide, with its high mortality rate primarily due to diagnostic delays and the limited efficacy and tolerability of late-stage treatments [1]. Although targeted therapy and immunotherapy have significantly improved the prognosis for some patients, the prevalenc e of acquired drug resistance and toxic reactions underscores the urgent need to develop novel intervention strategies with lower toxicity and broader effects. In this context, natural products and traditional ethnic medicines, with their multi-component and multi-target features, are considered an important complement to modern singletarget drugs; among them, traditional Chinese medicine offers a unique approach to the systemic intervention of complex diseases through the holistic regulation of multiple pathological pathways in synergistic compounds.

Pinellia ternata has been highly regarded in traditional medicinal formulas for generations, used to expel phlegm, stop coughs, alleviate asthma, and other respiratory symptoms. It is also often used as a component of adjuvant therapy for cancer patients. Previous reports suggest that preparations related to Pinellia ternata can affect key pathways such as PI3K/Akt [2], demonstrating potential anti-tumor activity. However, the specific molecular targets and mechanisms by which Pinellia ternata exerts its anti-lung cancer effects are still not systematically elucidated. The integration of modern systems pharmacology and computational biology provides a feasible path for deciphering the multi-layered association of “herb-component-targetpathway”, especially network analysis based on graph representation learning [3], which can capture potential herb-disease-gene coupling relationships in heterogeneous biological networks. Network pharmacology which based on systems biology and centered on multi-target and multi-pathway approaches, emphasizes explaining and utilizing the overall regulatory potential of multi-component natural products in complex diseases by starting from a multi-level map of compound-targetpathway-phenotype. Drug efficacy is not determined solely by individual high-affinity nodes, but rather than shaped by the relationships of multiple nodes and edges. In the context of tumor immunology, an integrated “computational evidence chain” has recently emerged as a consensus [4]. In the direction of immune checkpoints, natural small molecules have been shown to form a conserved pharmacophore across targets, involving “hinge hydrogen bonds-aromatic gating-hydrophobic grooves”, thus exhibiting stable binding at different receptor sites primarily driven by ∆EvdW. The consistency of molecular docking, MD simulations, energetics, and bioinformatics provides important support for preliminary validation [5,6].

The study bases on the frameworks of network pharmacology and graph attention networks, pick up diseaseassociated genes for lung cancer from databases including TCGA [7], HGNC [8], OMIM, STRING and GeneCards. And then construct a complex network connecting traditional Chinese medicine(TCM) [9], genes, and proteins, perform mining through this network and output potential TCM-associated genes. We search the active components of Pinellia ternata from the TCMSP database. Screening based on oral bioavailability and drug likeness yielded a set of natural compounds with development potential. This study focuses on 12 compounds in Pinellia ternata: baicalein, Baicalin, Xanthosine, (-)-beta-Sitosterol, Cavidine, coniferin, Cycloartenol, cis-11-Eicosenoic acid, Stigmasterol, 10,13-Eicosadienoic acid, 12,13-Epoxy-9-hydroxynonadeca-7,10-dienoic acid and 24-Ethylcholest-4-en-3-one. Studies have shown that baicalin exerts antitumor activity through multiple pathways, such as inhibiting angiogenesis and cell proliferation. While phenylpropanoid glycosides typically exhibit antioxidant and antiproliferative potential; and nucleoside compounds can affect rapidly dividing cells by interfering with nucleotide metabolism and signal transduction. These compounds complement each other in terms of skeleton, polarity, and polarizability, forming a chemical basis for potential synergistic effects.

In methodology, we constructed a hierarchical integrated computational evidence chain which named CrossScale-Herb as is shown in Fig 1, utilizing virtual screening and molecular docking to obtain the initial binding posture, verifying the stability of the complex in the aqueous solution system through molecular dynamics, and estimating the relative binding free energy with MM/PBSA. Combining in vivo and in vitro ADMET exploitability prediction [10] and DFT electronic structure analysis, we systematically evaluated the possibility and rationale for the key components of Pinellia ternata to act on lung cancer-related targets, especially CDK2/JAK2/KDR/PAK4/PTK2 etc.

## Materials and methods

## Ethics statement

This study did not involve interaction with human participants or access to identifiable private information. All analyses were performed on publicly available, de-identified datasets, including TCGA (accessed the GDC on 1 May 2024; project(s): TCGA-LUAD/LUSC; only open-access data were used), HGNC (accessed on 1 May 2024), OMIM (accessed on 15 May 2024), STRING (accessed on 30 May 2024), and GeneCards (accessed on 30 June 2024). According to the policies and applicable regulations, the use of publicly available de-identified data does not constitute human subjects research and does not require IRB review; therefore, informed consent was not required. The authors had no access to information that could identify individual participants during or after data collection. The study posed no risks to individual privacy, and all repository terms of use were followed.

<!-- image-->  
Fig 1. The process of CrossScale-Herb.

https://doi.org/10.1371/journal.pone.0349376.g001

## Network pharmacology target identification

The starting point for this study was a gene set containing potential target genes associated with Pinellia ternata treatment for lung cancer. This gene set was constructed based on the HERBGAT [11] model, the architecture of which is shown in Fig 2. In previous studies, researchers used the HERBGAT graph neural network model with an attention mechanism and the improved EMOGI algorithm to predict genes associated with Pinellia ternata and lung cancer, respectively, and obtained the high-confidence target list by taking the intersection of the two. Given that previous studies have verified the biological relevance of this gene set through bioinformatics analysis, this study used it as an unscreened comprehensive target set, aiming to systematically evaluate the potential binding ability of key active components of Pinellia ternata to various proteins in this target set through large-scale virtual screening.

## Protein structure and compounds identification

The Pinellia ternata compounds were obtained from the TCMSP database, which initially contained 116 phytochemical components. The 12 compounds ultimately selected were obtained through a rigorous pharmacokinetic screening process, using standard thresholds of oral bioavailability (OB≥30%) and drug-likeness (DL≥0.18) to exclude candidate compounds with poor pharmacological properties. Structural data were obtained from the RCSB Protein Database (PDB). We prioritized high-resolution (≤3.0 Å) structures of target genes resolved by X-ray crystallography or cryo-electron microscopy (cryo-EM). When multiple PDB entries existed for the same gene, we prioritized structures co-crystallized with small molecule ligands to accurately define the active pocket. Proteins with only key functional domains resolved (e.g., kinase domains) were also included in our analysis. All acquired PDB structures were filtered using a text pattern matching-based filter to remove all non-canonical biopolymer entities from the PDB files, resulting in a clean set of protein atomic coordinates. These structures were then submitted to the PDBFixer module for structural integrity repair and normalization. Finally, we optimized the hydrogen bond network using the Reduce module. Simultaneously, using the Traditional Chinese

<!-- image-->  
Fig 2. HERBGAT overall architecture.

https://doi.org/10.1371/journal.pone.0349376.g002

Medicine Systems Pharmacology Database (TCMSP) and PubChem as primary data sources, we applied a pharmacokinetic-based screening method, i.e., oral bioavailability (OB)≥30% and drug-likeness (DL)≥0.18, to enrich molecules with potential in vivo activity. This screening strategy ultimately yielded 12 candidate compounds(S1 Fig). For the few targets in the PDB that lacked experimental structures or had poor structural quality, we considered using the Alpha-Fold3 prediction model [12] as a supplement. However, preliminary screening revealed that the targets most strongly associated with Pinellia ternata-lung cancer, such as FGFR4, CDK2, BTK, AR, and PDGFRA, all possessed high-quality crystal structures. This allowed our high-throughput molecular docking studies to be primarily based on experimentally resolved structures, thus ensuring the reliability of the receptor conformation.

## Diffusion-based molecular docking

This study defines molecular docking as a generative modeling task to explore the interaction patterns between active compounds of Pinellia ternata and lung cancer-related target proteins. The study employs the DiffDock [13] method, which generates precise binding postures of small molecules and target proteins based on a diffusion model, rather than relying on traditional search paradigms that optimize scoring functions. This avoids deviations between predicted results and actual physical conditions caused by model uncertainties. The core of DiffDock is a diffusion-generative model defined on the ligand posture manifold. To ensure consistency between the posterior distribution of the final combined postures and the model’s learning results, the model iteratively “denoises” the prior distribution of information loss through a reversible stochastic process and progressively optimizes the training of the translational, rotational, and torsional degrees of freedom of the ligands. For each target protein, the binding pocket is defined based on its crystal structure and the resolved cocrystal ligands. If prior information is lacking, the surface cavity with the most significant geometric meaning identified by the CASTp server is used as a substitute. The docking computation process comprises two main stages: First, DiffDock’s generative model simultaneously generates dozens of candidate conformations for each compound-protein pair. Then, a separately trained confidence model evaluates and ranks these generated conformations. This confidence model aims to predict the probability that a given conformation has a root mean square deviation (RMSD) of less than 2 Å from the native structure. The confidence score can be used to screen for high-quality binding modes.

## Molecular dynamics simulations

Simulations were performed using GROMACSv2024 (http://www.mdtutorials.com/gmx/complex/index.html) and an AMBER force field [14]. The system was subjected to three-dimensional periodic boundary conditions (PBC). First, energy minimization was performed using the steepest descent method [15]. Then, the system was equilibrated under NVT and NPT ensembles, respectively. A 100 ps constant isochoric equilibrium (NVT) was performed at a steady-state temperature of 300 K using the Berendsen thermostat algorithm with a coupling constant of 0.1 ps. Subsequently, a 1 ns constant pressure equilibrium (NPT) was performed at 1 bar using a Parrinello-Rahman barostat with a coupling constant of 5.0 ps. The range of interactions was calculated using the particle mesh Ewald (PME) method. The calculated cutoff radius for long-range electrostatic interactions and short-range nonbonding interactions was 12 Å. The simulation was repeated twice, each lasting 200 ns. Molecular dynamics trajectory analysis was used to calculate the root mean square deviation (RMSD), root mean square fluctuation (RMSF), radius of gyration (Rg), number of hydrogen bonds, and principal component analysis (PCA) [16].

## MM-PBSA calculations

The total binding free energy between ligand and protein is measured by combining molecular dynamics simulations and thermodynamic techniques (mechanical/Poisson-Boltzmann surface area (MM-PBSA) method) [17]:

$$
\Delta G _ { \mathrm { b i n d i n g } } = \Delta G _ { \mathrm { M M } } + \Delta G _ { \mathrm { s o l } } - T \Delta S\tag{1}
$$

where G(complex) is the total free energy of the protein-ligand complex, and G(receptor) and G(ligand) are the free energies of the isolated protein and ligand in the solvent, respectively. The total free energy of the three entities (complex, receptor, or ligand) can be calculated by adding their molecular mechanical potential $( \Delta G _ { M M } )$ to their solvation energy $( \Delta G _ { s o l } )$ [18]. Intermolecular van der Waals forces $( \Delta E _ { v d W } )$ , electrostatic interactions $( \Delta E _ { e I e c } )$ , and nonpolar solvation energy $( \Delta E _ { n p } )$ all favor binding. However, polar solvation free energy $( \Delta E _ { p o l } )$ and configurational entropy (-T∆S) are unfavorable for ligand-protein binding. Therefore, the total free binding energy of the ligand-protein complex was calculated using the MM/PBSA GROMACS program via MD trajectory [19].

## ADMET profile

The physicochemical and pharmacokinetic properties, including absorption, distribution, metabolism, excretion, and toxicity, of selected baicalein, Baicalin, Xanthosine, (-)-beta-Sitosterol, Cavidine, coniferin, Cycloartenol, cis-11-Eicosenoic acid, Stigmasterol, 10,13-Eicosadienoic acid, 12,13-Epoxy-9-hydroxynonadeca-7,10-dienoic acid and 24-Ethylcholest-4-en-3-one were investigated. Results were obtained through the Swiss ADME and pre-ADME online servers (http://preadmet.bmdrc.org/).

## DFT study

Density functional theory (DFT) analysis of the active components of Pinellia ternata was performed using ORCA 5.0.1 [20–33], and visualization was performed using Multiwfn [34,35] and VMD [36]. The structural coordinates of the selected compounds were optimized using the B3LYP-D3/def2-TZVP basis set without imposing any symmetry constraints. From the optimized geometry, the optimized surface potential, HOMO-LUMO energy levels, and thermochemical parameters (thermal energy, enthalpy, Gibbs free energy, thermal entropy, hardness, softness, and electron affinity) of baicalein, Baicalin, Xanthosine, (-)-beta-Sitosterol, Cavidine, coniferin, Cycloartenol, cis-11-Eicosenoic acid, Stigmasterol, 10,13- Eicosadienoic acid, 12,13-Epoxy-9-hydroxynonadeca-7,10-dienoic acid and 24-Ethylcholest-4-en-3-one were obtained.

## Results and discussion

## Herbal-disease target prediction

Network pharmacology analysis shows a significant overlap between the potential targets of Pinellia ternata and the pathological gene network of lung cancer. Among the top 500 genes in both groups, we identified common molecular targets. This high degree of overlap strongly suggests that the active components of Pinellia ternata can broadly intervene in key signaling pathways in lung cancer. Further analysis of these co-occurring targets indicates that most are oncogenes, tumor suppressor genes, and signaling kinases closely related to tumorigenesis and development. Among them, targets such as FGFR4 [37,38], CDK2 [39,40], JAK2 [41,42], KDR [43,44], PAK4 [45,46], PTK2 [47,48] and PDGFRA [49,50] are particularly prominent because they play crucial roles in core cancer processes such as cell proliferation, cell cycle regulation, tumor microenvironment and angiogenesis which is strongly associated with tumors as lung cancer and colorectal cancer. Furthermore, we mapped the identified disease targets to the STRING database (v12.0). Under the conditions of setting the species to Homo sapiens, minimum required interaction score >0.7, and including all evidence sources, we constructed a high-confidence PPI network. This network was then imported into Cytoscape v3.10.4 for visualization and reconstruction, and integrated with TCMSP and KEGG data to construct a component-target-pathway network (S5 and S6 Figs). Based on the PPI network, we used the CytoHubba plugin to analyze the network topology, and employed the MCC (Maximal Clique Centrality) algorithm as the core evaluation metric to screen and identify key hub nodes (S7 Fig).

## Molecular docking studies

We used DiffDock to dock the active ingredient of Pinellia ternata with target proteins. The resulting model generated a set of energy-favorable conformations for each ligand-protein complex(S1 Table). We selected the optimal binding posture based on a docking scoring function for further interaction analysis(S3 Fig). From the docking results, we found that the docking confidence of baicalein with some lung cancer-related genes was high(S1 File). Among them, the binding states of baicalein with PTK2 and KDR with JAK2 were the most stable at the lung cancer-related gene targets. The threedimensional and two-dimensional complexes and internal interactions of these three complexes are shown in Fig 3. PTK2 dominates the adhesion-migration-invasion axis and is an important node in lung cancer metastasis and colorectal cancer invasion. In the PTK2 complex, baicalein forms a strong anchorage with the NH of the Cys89 backbone in the hinge region (H-O approximately 2.46 Å), and the adjacent Glu87 provides a short-range polar boost in the range of 2.6–3.6 Å, forming a two-point fixed posture. Meanwhile, the aromatic plane of baicalein is enclosed by Leu88, Leu140, Ile15, and Met86, and the two-dimensional plot also shows the additional hydrophobic attachment of Leu154, which constitutes a well-solvent-shielded microcavity. This geometry reduces the cost of desolvation and reduces conformational entropy loss through the $\pi - \pi / { \mathsf { C } } { \mathsf { H } } { - \pi }$ network. The function of KDR in mediating tumor angiogenesis can serve as one of the focal points for anti-metastasis and anti-angiogenesis. The complex of baicalein and KDR exhibits a Type I adenine pocketoccupancy mode. We found that the carbonyl group of baicalein forms a bond of about 2.85 Å with the NH group of the hinge Cys104 backbone, and the distal aromatic core forms a stable π – π stack with Phe175. Val101, Ala51, Leu163, and Val33 form a continuous hydrophobic trench in the lateral direction. The density of the contact network and the geometrical coaxiality of the aromatic interlayer indicate significant contributions from van der Waals forces and dispersion in the binding interaction. Although the DFG remains in the “in” state and the post-cavity is not fully utilized, the matching of the anterior cavity-gatekeeper channel is sufficient to support high-quality docking. JAK2 is highly correlated with the JAK/ STAT signal axis in the inflammation-survival-proliferation circuit. Its corresponding complex is based on the 2.69 Å hydrogen bonds of the NH group in the Leu100 backbone. The gatekeeper region Met97/Tyr99 forms a tight aromatic interlayer with the ligand. Leu23, Ala48, Val79, and Leu151 transform the channel into a narrow cavity, thus maintaining a highaffinity, hydrophobic-π-interaction-dominated binding posture even in the absence of significant salt bridges. Based on this, this study prioritizes PTK2 and KDR as the main targets in lung cancer-related targets, with JAK2 as a key auxiliary target. Baicalein shares a conserved binding core of “hinge receptor hydrogen bond and gatekeeper aromatic interlayer” across these three targets, while also gaining potential selective space through differences in lateral cavity geometry. Subsequently, molecular dynamics and free energy perturbation can be carried out on the basis of these three complexes to verify the residence time of hinge hydrogen bonds and the degree of water network substitution. Then, site-directed modification can be carried out based on the receptivity of the gatekeeper lateral cavity to complete the lead optimization from multi-target framework to disease pathway guidance.

## Molecular dynamics simulation results

We used molecular dynamics simulations to investigate the stability of molecular docking complexes [45] under dynamic conditions. Molecular dynamics simulations were performed on selected protein-ligand complexes over a period of 200 ns. Trajectory analysis showed that most complexes were indeed stable, with ligands remaining bound and key interactions preserved. We focused on the docking complexes of top-ranked baicalein with CDK2, JAK2, KDR, PAK4, and PTK2. Fig 4 shows the root mean square deviation (RMSD), root mean square smoothness coefficient (RMSF), relative molecular mass (Rg), and number of hydrogen bonds. RMSD calculations were used to assess conformational fluctuations of the protein-ligand backbone atoms and the stability of the simulated systems over a 200 ns simulation period [51]. As shown in Fig 4, all systems reached a final stable state after experiencing initial minor fluctuations caused by dynamic shocks. Almost all systems experienced initial dynamic shocks during molecular dynamics studies. The RMSD results indicate that the selected ligands reached a stable level in all systems, demonstrating consistent stability of the ligands at the protein active sites. Therefore, it can be concluded that the ligand-protein complex did not cause any significant conformational changes in the protein structure.

RMSF analysis determines the variation of amino acid residues by calculating the average value of amino acid residue atoms [52]. The smaller the RMSF value, the smaller the conformational change of the protein-ligand complex.

<!-- image-->  
Fig 3. Interaction and orientation of baicalein in A) PTK2, B) KDR, and C) JAK2.

https://doi.org/10.1371/journal.pone.0349376.g003

<!-- image-->  
Fig 4. RMSD backbones of baicalein in complex with different receptor proteins.

Fig 5 shows the RMSF results of baicalein complexes with corresponding proteins. The RMSF of all amino acid residues in the receptor active site does not exceed 0.4 nm. It is expected that the variation amplitude of the loop region, C-terminus, and N-terminus regions will be greater than that of the residues at the binding site and will participate in ligand-protein interactions. The RMSF plots of unbound and bound proteins confirm that the binding of the ligand to the protein does not change the protein structure [53]. In addition, the residual variation is less than 0.4 nm, indicating that the ligand-protein complex has no significant effect on the protein backbone, which is consistent with the RMSD results.RMSF analysis determines the variation of amino acid residues by calculating the average value of amino acid residue atoms [52]. The smaller the RMSF value, the smaller the conformational change of the protein-ligand complex. Fig 5 shows the RMSF results of baicalein complexes with corresponding proteins. The RMSF of all amino acid residues in the receptor active site does not exceed 0.4 nm. It is expected that the variation amplitude of the loop region, C-terminus, and N-terminus regions will be greater than that of the residues at the binding site and will participate in ligand-protein interactions. The RMSF plots of unbound and bound proteins confirm that the binding of the ligand to the protein does not change the protein structure [53]. In addition, the residual variation is less than 0.4 nm, indicating that the ligand-protein complex has no significant effect on the protein backbone, which is consistent with the RMSD results.

The Rg parameter is used to calculate the size change or tightness of the protein-ligand binding during molecular dynamics simulations [54]. The lower the Rg value, the tighter the protein-ligand complex and the better the system stability. As shown in Fig 6, the Rg values of the baicalein complex are all within the reference range.

Fig 7 also shows the total hydrogen bond interactions between each receptor protein and baicalein during the simulation. The calculation results indicate that the number of hydrogen bonds formed by baicalein during the simulation ranged from 0 to 4; therefore, the selected ligands formed a higher number of hydrogen bonds than the internal ligands. Overall, the results of the molecular dynamics simulation are consistent with the results of the molecular docking studies.

Principal component analysis (PCA), or eigendynamics, is an advanced method in molecular dynamics simulations [55]. For example, biomacromolecules with numerous degrees of freedom, such as proteins, can undergo significant conformational changes, resulting in complex shapes and exhibiting a wide range of activities [56]. PCA analysis helps to study significant coordination motions that occur during ligand binding. In this study, eigenvectors were obtained through matrix diagonalization. Fig 8 shows the eigenvalues obtained by diagonalizing the atomic fluctuation covariance matrix

<!-- image-->  
Fig 5. RMSF plots of baicalein in complexes with different receptor proteins.

https://doi.org/10.1371/journal.pone.0349376.g005

<!-- image-->  
Fig 6. Rg of baicalein complexed with different receptor proteins over the simulation time.  
https://doi.org/10.1371/journal.pone.0349376.g006

of the baicalein complex, arranged in descending order, corresponding to the respective eigenvectors. Fig 9 shows the two-dimensional projections of the trajectories of the first three principal components, PC1 and PC3, of the baicalein complex in phase space. According to the PCA results, the studied baicalein complex exhibits relatively small motions and maintains stable interactions.

## MM-PBSA binding free energy results

Table 1 lists the binding free energies of the natural compound baicalein and its respective protein targets. As shown in Fig 10, the MM/PBSA results show that baicalein exhibits high binding free energies with JAK2 (−88.32 kJ mol−1) and PTK2 (−112.51 kJ mol−1), while its interactions with BTK and FGFR4 are weaker(S8 Fig and S2 Table). Van der Waals

<!-- image-->  
Fig 7. Total number of hydrogen bonds between baicalein complexes with different ligand-proteins.

<!-- image-->  
Fig 8. Ranking of characteristic values of baicalein complexes.

https://doi.org/10.1371/journal.pone.0349376.g008

forces contribute significantly to the total free energy, while electrostatic energy contributes less. The binding site is primarily dominated by non-polar hydrophobic interactions, which is consistent with the hydrophobic embedding characteristics observed in the docking results. Solvent accessible surface area (SASA) [57] represents the degree of solvent exposure. The total binding free energy of baicalein suggests that it can effectively bind to lung cancer-related gene targets such as JAK2 and PTK2.

## Pharmacokinetic profile

In recent years, researchers have used several techniques to predict the druggability of lead compounds, such as the Lipinski rule (Ro5) and the ADMET parameter [58]. The three parameters of Ro5 include molecular weight, hydrogen bond acceptor, and hydrogen bond donor, which are related to the interaction between the ligand and the active site of the

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
Fig 9. The scree plot for PC1 versus PC3 of baicalein and receptor.

https://doi.org/10.1371/journal.pone.0349376.g009

Table 1. The MM/PBSA binding free energy of baicalein corresponding proteins (KJ mol−1).
<table><tr><td rowspan=1 colspan=1>Proteins</td><td rowspan=1 colspan=1> $\Delta { E _ { \mathrm { v d w } } }$ </td><td rowspan=1 colspan=1> $\Delta E _ { \mathrm { e l e } }$ </td><td rowspan=1 colspan=1> $\Delta G _ { \mathsf { P B } }$ </td><td rowspan=1 colspan=1> $\Delta G _ { \mathsf { s A } }$ </td><td rowspan=1 colspan=1> $\Delta \ S A S A / \eta \mathbf { m } \mathbf { m } ^ { 2 }$ </td><td rowspan=1 colspan=1> $\Delta G _ { \mathrm { b i n d i n g } }$ </td></tr><tr><td rowspan=1 colspan=1>AR</td><td rowspan=1 colspan=1>-167.11±8.20</td><td rowspan=1 colspan=1>-16.69±10.33</td><td rowspan=1 colspan=1> $1 1 0 . 7 5 { \scriptstyle \pm 8 . 2 8 }$ </td><td rowspan=1 colspan=1>-13.72±0.29</td><td rowspan=1 colspan=1>-4.56±0.10</td><td rowspan=1 colspan=1>-86.73±12.30</td></tr><tr><td rowspan=1 colspan=1>BTK</td><td rowspan=1 colspan=1>-125.19±9.33</td><td rowspan=1 colspan=1> $- 2 9 . 9 2 \pm 1 9 . 9 2$ </td><td rowspan=1 colspan=1> $9 2 . 3 4 \pm 2 3 . 1 8$ </td><td rowspan=1 colspan=1>-11.72±0.46</td><td rowspan=1 colspan=1>-3.89±0.15</td><td rowspan=1 colspan=1> $- 7 4 . 4 8 \pm 1 3 . 1 0$ </td></tr><tr><td rowspan=1 colspan=1>CDK2</td><td rowspan=1 colspan=1> $- 1 4 3 . 4 7 \pm 1 0 . 8$ </td><td rowspan=1 colspan=1> $- 2 5 . 0 2 \pm 9 . 6 2$ </td><td rowspan=1 colspan=1> $9 6 . 7 3 \pm 1 1 . 7 2$ </td><td rowspan=1 colspan=1> $- 1 3 . 6 0 \pm 0 . 5 0$ </td><td rowspan=1 colspan=1> $- 4 . 5 1 \pm 0 . 1 7$ </td><td rowspan=1 colspan=1> $- 8 5 . 4 0 \pm 1 0 . 9 2$ </td></tr><tr><td rowspan=1 colspan=1>FGFR4</td><td rowspan=1 colspan=1>-106.65±14.27</td><td rowspan=1 colspan=1>-21.63±14.10</td><td rowspan=1 colspan=1> $7 3 . 4 3 \pm 1 6 . 3 6$ </td><td rowspan=1 colspan=1> $- 1 0 . 9 6 \pm 1 . 6 3$ </td><td rowspan=1 colspan=1> $- 3 . 6 4 \pm 0 . 5 4$ </td><td rowspan=1 colspan=1> $- 6 5 . 8 6 \pm 1 1 . 6 3$ </td></tr><tr><td rowspan=1 colspan=1>ITK</td><td rowspan=1 colspan=1>-131.38±9.71</td><td rowspan=1 colspan=1>-16.78±9.67</td><td rowspan=1 colspan=1> $8 5 . 6 9 \pm 1 0 . 8 4$ </td><td rowspan=1 colspan=1> $- 1 2 . 5 9 \pm 0 . 3 3$ </td><td rowspan=1 colspan=1>-4.18±0.11</td><td rowspan=1 colspan=1> $- 7 5 . 0 6 \pm 1 1 . 3 0$ </td></tr><tr><td rowspan=1 colspan=1>JAK2</td><td rowspan=1 colspan=1>-137.24±8.66</td><td rowspan=1 colspan=1>-34.60±11.84</td><td rowspan=1 colspan=1> $9 6 . 3 6 \pm 1 0 . 6 3$ </td><td rowspan=1 colspan=1>-12.89±0.38</td><td rowspan=1 colspan=1>-4.28±0.12</td><td rowspan=1 colspan=1>−88.32±11.51</td></tr><tr><td rowspan=1 colspan=1>KDR</td><td rowspan=1 colspan=1>-146.82±7.36</td><td rowspan=1 colspan=1>-30.75±10.71</td><td rowspan=1 colspan=1> $9 8 . 2 4 \pm 1 0 . 7 1$ </td><td rowspan=1 colspan=1>-13.01±0.25</td><td rowspan=1 colspan=1>-4.32±0.08</td><td rowspan=1 colspan=1>-92.34±9.41</td></tr><tr><td rowspan=1 colspan=1>PAK4</td><td rowspan=1 colspan=1>-120.42±7.49</td><td rowspan=1 colspan=1>-41.00 ± 12.93</td><td rowspan=1 colspan=1>95.23±12.18</td><td rowspan=1 colspan=1>-12.72±0.46</td><td rowspan=1 colspan=1>-4.22±0.15</td><td rowspan=1 colspan=1> $- 7 8 . 8 7 \pm 1 0 . 9 2$ </td></tr><tr><td rowspan=1 colspan=1>PDGFRA</td><td rowspan=1 colspan=1>-156.77±7.91</td><td rowspan=1 colspan=1>-29.04±17.15</td><td rowspan=1 colspan=1>105.69±14.90</td><td rowspan=1 colspan=1>-13.77±0.29</td><td rowspan=1 colspan=1>-4.57±0.10</td><td rowspan=1 colspan=1> $- 9 3 . 8 9 \pm 1 1 . 6 7$ </td></tr><tr><td rowspan=1 colspan=1>PTK2</td><td rowspan=1 colspan=1>-123.55±11.72</td><td rowspan=1 colspan=1>-93.97±43.51</td><td rowspan=1 colspan=1>117.78±24.73</td><td rowspan=1 colspan=1>-12.72±0.46</td><td rowspan=1 colspan=1>-4.22±0.15</td><td rowspan=1 colspan=1> $- 1 1 2 . 5 1 \pm 1 5 . 0 2$ </td></tr></table>

https://doi.org/10.1371/journal.pone.0349376.t001

<!-- image-->  
Fig 10. MM/PBSA binding free energy and energy components for different target protein complexes.

https://doi.org/10.1371/journal.pone.0349376.g010

protein. The lipophilicity parameter (Log P), unlike the other three parameters, is independent of the biophysical properties of the target and can be calculated experimentally. Topological polar surface area (TPSA) characterizes the ability of a compound to penetrate cells [59]. When the TPSA value is greater than 140 Å2 [60], the compound’s ability to penetrate the cell membrane decreases. Predicting drug distribution in the human body depends on several parameters related to in vivo distribution, namely human intestinal absorption rate (HIA%), in vitro plasma protein binding rate, and blood-brain barrier (BBB) permeability [61].

The physicochemical properties and pharmacokinetic characteristics of the screened natural compounds of Baicalein, namely baicalein, Baicalin, Xanthosine, (-)-beta-Sitosterol, Cavidine, coniferin, Cycloartenol, cis-11-Eicosenoic acid, Stigmasterol, 10,13-Eicosadienoic acid, 12,13-Epoxy-9-hydroxynonadeca-7,10-dienoic acid and 24-Ethylcholest-4-en-3-one, were investigated using Swiss ADME and PreADMET software. As shown in Table 2, baicalein conformed to Lipinski’s rule (violation count =0) and had few rotatable bonds (1–2), indicating a reasonable basic structure for oral lead compounds. The LogP value (1.71) and TPSA value (90.9 Å²) of baicalein were both within the range favorable for membrane permeability. Baicalein is a small, compact compound with suitable hydrophilic and hydrophobic properties, fitting the “template image” of early oral lead compounds.

As shown in Table 3, baicalein exhibits a high intestinal absorption rate (HIA) (88.1%), but is significantly weak in the human Caco-2 permeability model (12.8 nm·s−1) and low skin permeability (0.26 cm h−1). Regarding distribution, baicalein has extremely high plasma protein binding (PPB ≈ 99% − 97.8%) and very low free fraction. Blood-brain barrier prediction indicates that baicalein (0.77%) more readily enters the central nervous system, which is significant for peripheral administration to tumors and represents a distribution pattern that is relatively “peripherally safe”.

Table 4 lists the toxicity analysis results of natural compounds in Pinellia ternata. Baicalein showed Ames positivity and a moderate risk of hERG inhibition, but did not exhibit carcinogenicity in mice; however, these two points need to be addressed in structural optimization and further validation. In the algal acute toxicity score, baicalin scored 0.051, suggesting that the environmental toxicological burden of coniferin may be relatively low.

Table 2. Physical and chemical properties of compounds in Pinellia ternata.
<table><tr><td rowspan=1 colspan=1>Compounds</td><td rowspan=1 colspan=1>MW(g mol1)</td><td rowspan=1 colspan=1>LogP</td><td rowspan=1 colspan=1>HBD</td><td rowspan=1 colspan=1>HBA</td><td rowspan=1 colspan=1>TPSA(Å²)</td><td rowspan=1 colspan=1>n-RB</td><td rowspan=1 colspan=1>Lipinski violation</td></tr><tr><td rowspan=1 colspan=1>10,13-Eicosadienoic acid</td><td rowspan=1 colspan=1>308.5</td><td rowspan=1 colspan=1>6.18</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>37.3</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>12,13-Epoxy-9-hydroxy nonadeca-7,10-dienoic acid</td><td rowspan=1 colspan=1>324.45</td><td rowspan=1 colspan=1>4.01</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>70.06</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>24-Ethylcholest-4-en-3-one</td><td rowspan=1 colspan=1>412.69</td><td rowspan=1 colspan=1>7.36</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>17.07</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>baicalein</td><td rowspan=1 colspan=1>270.24</td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>90.9</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Baicalin</td><td rowspan=1 colspan=1>444.35</td><td rowspan=1 colspan=1>0.07</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>192.78</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Xanthosine</td><td rowspan=1 colspan=1>284.23</td><td rowspan=1 colspan=1>-1.85</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>153.46</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>(-)-beta-Sitosterol</td><td rowspan=1 colspan=1>414.71</td><td rowspan=1 colspan=1>7.24</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20.23</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Cavidine</td><td rowspan=1 colspan=1>353.41</td><td rowspan=1 colspan=1>3.23</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>40.16</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>coniferin</td><td rowspan=1 colspan=1>342.34</td><td rowspan=1 colspan=1>-0.48</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>128.84</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>Cycloartenol</td><td rowspan=1 colspan=1>426.72</td><td rowspan=1 colspan=1>7.51</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20.23</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>cis-11-Eicosenoic acid</td><td rowspan=1 colspan=1>310.51</td><td rowspan=1 colspan=1>6.41</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>37.3</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Stigmasterol</td><td rowspan=1 colspan=1>412.69</td><td rowspan=1 colspan=1>6.98</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20.23</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr></table>

https://doi.org/10.1371/journal.pone.0349376.t002

Table 3. In silico ADME analysis of compounds in Pinellia ternata.
<table><tr><td rowspan=1 colspan=1>Entry</td><td rowspan=1 colspan=2>Absorption</td><td rowspan=1 colspan=3>Distribution</td></tr><tr><td rowspan=1 colspan=1>compounds</td><td rowspan=1 colspan=1>%HIA</td><td rowspan=1 colspan=1>In vitro Caco-2 cellpermeability (nm s1)</td><td rowspan=1 colspan=1>In vitro skin permeability(lookup, cm h-1)</td><td rowspan=1 colspan=1>% in vitro plasmaprotein binding</td><td rowspan=1 colspan=1>%BBB</td></tr><tr><td rowspan=1 colspan=1>10,13-Eicosadienoic acid</td><td rowspan=1 colspan=1>98.2089</td><td rowspan=1 colspan=1>304.198</td><td rowspan=1 colspan=1>1103.6885</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>10.56</td></tr><tr><td rowspan=1 colspan=1>12,13-Epoxy-9-hydroxy nonadeca-7,10-dienoic acid</td><td rowspan=1 colspan=1>95.2753</td><td rowspan=1 colspan=1>225.507</td><td rowspan=1 colspan=1>430.5162</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>1.4158</td></tr><tr><td rowspan=1 colspan=1>24-Ethylcholest-4-en-3-one</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>538.178</td><td rowspan=1 colspan=1>929.8427</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>19.559</td></tr><tr><td rowspan=1 colspan=1>baicalein</td><td rowspan=1 colspan=1>88.105491</td><td rowspan=1 colspan=1>12.8026</td><td rowspan=1 colspan=1>0.2635</td><td rowspan=1 colspan=1>98.983295</td><td rowspan=1 colspan=1>0.7708</td></tr><tr><td rowspan=1 colspan=1>Baicalin</td><td rowspan=1 colspan=1>25.3336</td><td rowspan=1 colspan=1>5.7073</td><td rowspan=1 colspan=1>0.1207</td><td rowspan=1 colspan=1>51.7322</td><td rowspan=1 colspan=1>0.015</td></tr><tr><td rowspan=1 colspan=1>Xanthosine</td><td rowspan=1 colspan=1>24.7163</td><td rowspan=1 colspan=1>136.448</td><td rowspan=1 colspan=1>0.0215</td><td rowspan=1 colspan=1>12.7683</td><td rowspan=1 colspan=1>0.291</td></tr><tr><td rowspan=1 colspan=1>(-)-beta-Sitosterol</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>523.734</td><td rowspan=1 colspan=1>918.044</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>19.888</td></tr><tr><td rowspan=1 colspan=1>Cavidine</td><td rowspan=1 colspan=1>97.7466</td><td rowspan=1 colspan=1>560.997</td><td rowspan=1 colspan=1>0.2723</td><td rowspan=1 colspan=1>81.8264</td><td rowspan=1 colspan=1>0.0544</td></tr><tr><td rowspan=1 colspan=1>coniferin</td><td rowspan=1 colspan=1>52.107</td><td rowspan=1 colspan=1>141.527</td><td rowspan=1 colspan=1>0.1219</td><td rowspan=1 colspan=1>37.6157</td><td rowspan=1 colspan=1>0.0456</td></tr><tr><td rowspan=1 colspan=1>Cycloartenol</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>500.256</td><td rowspan=1 colspan=1>34.7922</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>20.37</td></tr><tr><td rowspan=1 colspan=1>cis-11-Eicosenoic acid</td><td rowspan=1 colspan=1>98.3144</td><td rowspan=1 colspan=1>305.319</td><td rowspan=1 colspan=1>1099.8501</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>12.743</td></tr><tr><td rowspan=1 colspan=1>Stigmasterol</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>523.376</td><td rowspan=1 colspan=1>689.6607</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>19.894</td></tr></table>

https://doi.org/10.1371/journal.pone.0349376.t003

## DFT analysis

DFT calculations further revealed the intrinsic properties of the compounds’ reactivity and interactions [62,63]. Frequency and optimization calculations were performed on baicalein, Baicalin, Xanthosine, (-)-beta-Sitosterol, Cavidine, coniferin, Cycloartenol, cis-11-Eicosenoic acid, Stigmasterol, 10,13-Eicosadienoic acid, 12,13-Epoxy-9-hydroxynonadeca-7,10- dienoic acid and 24-Ethylcholest-4-en-3-one using the B3LYP-D3/def2-TZVP method, yielding the total electron density (Etot), electron affinity A, hardness η, and softness σ (as shown in Table 5). The HOMO and LUMO molecular orbitals were used to predict the reactivity and physical and structural properties of the compounds. The HOMO and LUMO energies and the energy difference between the HOMO and LUMO are shown in Fig 11. The band gap energy of baicalein is

Table 4. Toxicity analysis of compounds in Pinellia ternata.
<table><tr><td rowspan=1 colspan=1>Entry</td><td rowspan=1 colspan=1>algae_at</td><td rowspan=1 colspan=1>Ames_test</td><td rowspan=1 colspan=1>Carcino_Mouse</td><td rowspan=1 colspan=1>hERG_inhibition</td></tr><tr><td rowspan=1 colspan=1>10,13-Eicosadienoic acid</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>12,13-Epoxy-9-hydroxy nonadeca-7,10-dienoic acid</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>24-Ethylcholest-4-en-3-one</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>baicalein</td><td rowspan=1 colspan=1>0.051</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>negative</td><td rowspan=1 colspan=1>medium_risk</td></tr><tr><td rowspan=1 colspan=1>Baicalin</td><td rowspan=1 colspan=1>0.066</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>ambiguous</td></tr><tr><td rowspan=1 colspan=1>Xanthosine</td><td rowspan=1 colspan=1>0.354</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>negative</td><td rowspan=1 colspan=1>medium_risk</td></tr><tr><td rowspan=1 colspan=1>(-)-beta-Sitosterol</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>Cavidine</td><td rowspan=1 colspan=1>0.025</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>negative</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>coniferin</td><td rowspan=1 colspan=1>0.081</td><td rowspan=1 colspan=1>mutagen</td><td rowspan=1 colspan=1>negative</td><td rowspan=1 colspan=1>medium_risk</td></tr><tr><td rowspan=1 colspan=1>Cycloartenol</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>cis-11-Eicosenoic acid</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>negative</td><td rowspan=1 colspan=1>low_risk</td></tr><tr><td rowspan=1 colspan=1>Stigmasterol</td><td rowspan=1 colspan=1>0.001</td><td rowspan=1 colspan=1>non-mutagen</td><td rowspan=1 colspan=1>positive</td><td rowspan=1 colspan=1>low_risk</td></tr></table>

https://doi.org/10.1371/journal.pone.0349376.t004

Table 5. The calculated total energy (Etot), Enthalpy (H), Gibbs free energy (G), hardness (η), softness (σ, and electron affinity (A) of compound from Pinellia ternata at B3LYP/6-31 + G(d,p) level of theory [a in Hartree/ particle, bin cal/mol K, c in ev, din ev−1].
<table><tr><td rowspan=1 colspan=1>Compounds</td><td rowspan=1 colspan=1> $\mathsf { E } _ { t o t } ^ { a }$ </td><td rowspan=1 colspan=1> $\mathsf { H } ^ { a }$ </td><td rowspan=1 colspan=1> $\pmb { G } ^ { a }$ </td><td rowspan=1 colspan=1> $\bullet ^ { b }$ </td><td rowspan=1 colspan=1> $\eta ^ { \mathfrak { c } }$ </td><td rowspan=1 colspan=1> $\sigma ^ { d }$ </td><td rowspan=1 colspan=1> $\pmb { \mathsf { A } } ^ { \pmb { c } }$ </td></tr><tr><td rowspan=1 colspan=1>10,13-Eicosadienoic acid</td><td rowspan=1 colspan=1>-934.091</td><td rowspan=1 colspan=1>-933.537</td><td rowspan=1 colspan=1>-933.623</td><td rowspan=1 colspan=1>182.19</td><td rowspan=1 colspan=1>3.289</td><td rowspan=1 colspan=1>0.304</td><td rowspan=1 colspan=1>-0.02</td></tr><tr><td rowspan=1 colspan=1>12,13-Epoxy-9-hydroxy nonadeca-7,10-dienoic acid</td><td rowspan=1 colspan=1>-1043.986</td><td rowspan=1 colspan=1>-1043.474</td><td rowspan=1 colspan=1>-1043.560</td><td rowspan=1 colspan=1>181.61</td><td rowspan=1 colspan=1>3.096</td><td rowspan=1 colspan=1>0.322</td><td rowspan=1 colspan=1>0.70</td></tr><tr><td rowspan=1 colspan=1>24-Ethylcholest-4-en-3-one</td><td rowspan=1 colspan=1>-1209.001</td><td rowspan=1 colspan=1>-1208.250</td><td rowspan=1 colspan=1>-1208.339</td><td rowspan=1 colspan=1>186.18</td><td rowspan=1 colspan=1>2.555</td><td rowspan=1 colspan=1>0.391</td><td rowspan=1 colspan=1>1.33</td></tr><tr><td rowspan=1 colspan=1>baicalein</td><td rowspan=1 colspan=1>-953.675</td><td rowspan=1 colspan=1>-953.437</td><td rowspan=1 colspan=1>-953.495</td><td rowspan=1 colspan=1>121.85</td><td rowspan=1 colspan=1>1.94</td><td rowspan=1 colspan=1>0.52</td><td rowspan=1 colspan=1>2.13</td></tr><tr><td rowspan=1 colspan=1>Baicalin</td><td rowspan=1 colspan=1>-1638.436</td><td rowspan=1 colspan=1>-1638.032</td><td rowspan=1 colspan=1>-1638.115</td><td rowspan=1 colspan=1>174.47</td><td rowspan=1 colspan=1>1.813</td><td rowspan=1 colspan=1>0.551</td><td rowspan=1 colspan=1>2.20</td></tr><tr><td rowspan=1 colspan=1>Xanthosine</td><td rowspan=1 colspan=1>-1058.590</td><td rowspan=1 colspan=1>-1058.328</td><td rowspan=1 colspan=1>-1058.390</td><td rowspan=1 colspan=1>131.20</td><td rowspan=1 colspan=1>2.796</td><td rowspan=1 colspan=1>0.357</td><td rowspan=1 colspan=1>0.64</td></tr><tr><td rowspan=1 colspan=1>(-)-beta-Sitosterol</td><td rowspan=1 colspan=1>-1210.196</td><td rowspan=1 colspan=1>-1209.422</td><td rowspan=1 colspan=1>-1209.51</td><td rowspan=1 colspan=1>188.83</td><td rowspan=1 colspan=1>3.403</td><td rowspan=1 colspan=1>0.293</td><td rowspan=1 colspan=1>-0.47</td></tr><tr><td rowspan=1 colspan=1>Cavidine</td><td rowspan=1 colspan=1>-1169.536</td><td rowspan=1 colspan=1>-1169.107</td><td rowspan=1 colspan=1>-1169.180</td><td rowspan=1 colspan=1>152.70</td><td rowspan=1 colspan=1>2.622</td><td rowspan=1 colspan=1>0.381</td><td rowspan=1 colspan=1>0.3</td></tr><tr><td rowspan=1 colspan=1>coniferin</td><td rowspan=1 colspan=1>-1224.57</td><td rowspan=1 colspan=1>-1224.172</td><td rowspan=1 colspan=1>-1224.249</td><td rowspan=1 colspan=1>163.01</td><td rowspan=1 colspan=1>2.376</td><td rowspan=1 colspan=1>0.420</td><td rowspan=1 colspan=1>1.14</td></tr><tr><td rowspan=1 colspan=1>Cycloartenol</td><td rowspan=1 colspan=1>-1248.253</td><td rowspan=1 colspan=1>-1247.473</td><td rowspan=1 colspan=1>-1247.564</td><td rowspan=1 colspan=1>189.93</td><td rowspan=1 colspan=1>3.418</td><td rowspan=1 colspan=1>0.292</td><td rowspan=1 colspan=1>-0.55</td></tr><tr><td rowspan=1 colspan=1>cis-11-Eicosenoic acid</td><td rowspan=1 colspan=1>-935.317</td><td rowspan=1 colspan=1>-934.738</td><td rowspan=1 colspan=1>-934.826</td><td rowspan=1 colspan=1>184.13</td><td rowspan=1 colspan=1>3.307</td><td rowspan=1 colspan=1>0.302</td><td rowspan=1 colspan=1>-0.06</td></tr><tr><td rowspan=1 colspan=1>Stigmasterol</td><td rowspan=1 colspan=1>-1208.969</td><td rowspan=1 colspan=1>-1208.220</td><td rowspan=1 colspan=1>-1208.308</td><td rowspan=1 colspan=1>187.01</td><td rowspan=1 colspan=1>3.356</td><td rowspan=1 colspan=1>0.297</td><td rowspan=1 colspan=1>-0.42</td></tr></table>

https://doi.org/10.1371/journal.pone.0349376.t005

3.87 eV. This indicates that baicalein exhibits higher chemical reactivity than other active components of Pinellia ternata due to its lower band gap between the HOMO and LUMO(S3 Fig).

The electronic responses were analyzed using frontier orbitals and electrostatic potentials (ESPs), as shown in Fig 11. The red spheres on the ESP plots represent negatively charged sites. The ESP spectra specify the equilibrium charge distribution in baiaclein, which is beneficial for the compound’s binding to biological enzymes. Baicalein’s ground-state energy and thermodynamic free energy are in a relatively stable range, with low conformational entropy and a relatively compact spatial configuration. Among natural Pinellia ternata compounds, it belongs to a class of compounds with high softness and strong electron affinity(S4 Fig). This explains the highly polarizable and easily stable ligand-forming properties of baicalein as demonstrated in the molecular docking and kinetic simulations described earlier.

The present study is computational and does not include in vitro or in vivo experimental validation of the predicted compound-target interactions and downstream biological effects. Accordingly, our results should be interpreted as providing a prioritized set of candidate mechanisms rather than definitive evidence of efficacy or causality. Future studies are warranted to substantiate these predictions using appropriate experimental models, for instance, binding and enzymatic

<!-- image-->  
Fig 11. A) DFT calculated LUMO, HOMO, and their energies for baicalein at the B3LYP-D3/def2-TZVP level of theory. B) ESP of the corresponding conformations of baicalein at B3LYP-D3/def2-TZVP level of theory.

https://doi.org/10.1371/journal.pone.0349376.g011

assays for the proposed targets, cellular assays for pathway-level effects, and dose-response evaluations, and to assess their pharmacological feasibility and potential off-target effects.

## Conclusion

This study constructs a hierarchical integrated computational evidence chain which named CrossScale-Herb to employ comprehensive computational methods to systematically evaluate the potential interactions between natural compounds in Pinellia ternata and lung cancer-related targets. Through using the HERBGAT network, we identified protein targets with cross-targeting effects on lung cancer and reveal the multi-target mechanisms of these natural compounds. By integrating evidence from PPI topological hubs, docking confidence, dynamic stability, and energy decomposition, we identified a highly correlated migration-angiogenesis-cell cycle node axis centered on PTK2, KDR, JAK2, and CDK2.

Among these compounds, baicalein exhibited consistent mechanistic characteristics across targets such as PTK2/ KDR/JAK2. Besides, molecular dynamics simulations and binding free energy calculations showed that baicalein forms stable complexes with lung cancer-related targets, considering binding energy values consistently falling within the ideal range. These complexes are core-driven by hydrophobic interactions and anchored by local polar interactions, while a gatekeeper aromatic layer provides a selective entry site. This complex possesses cross-targeting, transferable pharmacophore features, facilitating targeted optimization in the side pocket dimension. ADMET property predictions further confirmed that although all three compounds comply with drug-likeness rules and have the potential as oral lead compounds, baicalein requires structural optimization to address Ames test and hERG risks, while improvements in its transmembrane permeability and excessive protein binding are needed. This provides strong computational evidence for the anti-cancer mechanisms of natural compounds in Pinellia ternata. DFT analysis revealed high electronic softness, frontier orbital distribution, and electrostatic potential responses that highly correlate with ligand-receptor electronic matching in multi-target cavities, providing electronic corroboration for the energy and conformational study results.

Baicalein can serve as a preferred chemical starting point for experimental validation of lead compound optimization and combination intervention hypotheses centered on tumor-related nodes such as PTK2/FGFR4/CDK2/PDGFRA/AR. This can be extended to other ethnomedicinal resources and diseases, thereby accelerating the discovery of innovative therapies inspired by traditional medicine.

## Supporting information

S1 File. Supplementary method description. (DOCX)

S1 Fig. Selected natural compounds of Pinellia ternate. (TIF)

S2 Fig. Interaction and orientation of baicalein in A) AR, B) BTK, C) FGFR4, D) ITK, E) PAK4 and F) PDGFRA. (TIF)

S3 Fig. DFT calculated LUMO, HOMO, and their energies for compounds of Pinellia ternata at the B3LYP-D3/def2- TZVP level of theory.

S4 Fig. ESP of the corresponding conformations of compounds of Pinellia ternata at B3LYP-D3/def2-TZVP level of theory.

S5 Fig. PPI network of all identified genes. (TIF)

S6 Fig. Network of all the metabolites of Pinellia ternata, their targets and signalling pathways. (TIF)

S7 Fig. Hub targets identified by using Cytohubba plugin of the Cytoscape software.

S8 Fig. MM/GBSA binding free energy and energy components for different target protein complexes.

S1 Table. Ranking of candidate targets based on the weighted confidence index. (XLSX)

S2 Table. The MM/GBSA binding free energy of baicalein corresponding proteins (KJ mol-1). (XLSX)

## Acknowledgments

We thank all the members of the laboratory of the School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine for their contributions to this research.

## Author contributions

Conceptualization: Guoqiang Bian, Daifeng Zhang.

Data curation: Yuanhao Shen, Pengcheng Xiao.

Formal analysis: Yuanbin Zhang, Daifeng Zhang, Chenjun Hu.

Investigation: Xiong Li.

Methodology: Guoqiang Bian, Yuanbin Zhang.

Project administration: Kongfa Hu.

Resources: Chenjun Hu.

Software: Yuanbin Zhang.

Supervision: Duo Chen, Chenjun Hu.

Validation: Guoqiang Bian, Yuanbin Zhang.

Visualization: Guoqiang Bian, Jiadong Xie.

Writing – original draft: Guoqiang Bian, Yuanbin Zhang, Yuanhao Shen, Chenjun Hu.

Writing – review & editing: Guoqiang Bian, Yuanbin Zhang, Yuanhao Shen, Pengcheng Xiao, Jiadong Xie, Xiong Li, Duo Chen, Kongfa Hu, Chenjun Hu.

## References

1. Liu Y, Bai Y, Zhang J, Silva-Filho R, Zhu Q, Lei Z. Utilizing network pharmacology and experimental validation to explore the potential molecular mechanisms of raw Pinellia ternate in treating esophageal cancer. J Gastrointest Oncol. 2023;14(5):2006–17. https://doi.org/10.21037/jgo-23-684 PMID: 37969842

2. Li J, Wang W, Yuan Y, Cui X, Bian H, Wen H, et al. Pinellia ternata lectin induces inflammation through TLR4 receptor and mediates PI3K/Akt/ mTOR axis to regulate NF-κB signaling pathway. Toxicology. 2023;486:153430. https://doi.org/10.1016/j.tox.2023.153430 PMID: 36669722

3. Jin Y, Ji W, Shi Y, Wang X, Yang X. Meta-path guided graph attention network for explainable herb recommendation. Health Inf Sci Syst. 2023;11(1):5. https://doi.org/10.1007/s13755-022-00207-6 PMID: 36660407

4. Khurshid I, Mehraj T, Maqbool A, Aejaz K, Khursheed A, Rather MA, et al. Deciphering the mutagenicity-related toxicity of acrylamide food toxin using computational toxicology, in-silico molecular docking/MD-simulations and bioinformatics. In Silico Res Biomed. 2025;1. https://doi. org/10.1016/j.insi.2025.100143

5. Rather MA, Rasool S, Khursheed A, Ahmed SSSJ, Bashir F, Shalla AH, et al. Decoding the therapeutic potential of apigenin as a nonpeptide PD-1/ PD-L1 immune checkpoint inhibitor in breast cancer: an integrated, multimethod study using network pharmacology, bioinformatics, molecular docking, and dynamics simulations. J Chem. 2025;2025(1). https://doi.org/10.1155/joch/5133015

6. Alsantali RI, Almohyawi AM, Rather MA, Mir JM, Dangroo NA, Almalki FA, et al. From silico to benchtop: cosmosiin as a PD-1/PDL-1 immune checkpoint inhibitor revealed through DFT, network pharmacology analysis, and molecular docking integrated experimental verification. RSC Adv. 2025;15(28):22285–310. https://doi.org/10.1039/d5ra03831f PMID: 40606194

7. Liu J, Lichtenberg T, Hoadley KA, Poisson LM, Lazar AJ, Cherniack AD, et al. An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics. Cell. 2018;173(2):400–416.e11. https://doi.org/10.1016/j.cell.2018.02.052 PMID: 29625055

8. Seal RL, Braschi B, Gray K, Jones TEM, Tweedie S, Haim-Vilmovsky L. Genenames.org: the HGNC resources in 2023. Nucleic Acids Res. 2023;51(D1):D1003-9. https://doi.org/10.1093/nar/gkac888

9. Feng F, Hu P, Peng L, Xu L, Chen J, Chen Q, et al. Integrated network pharmacology and metabolomics to reveal the mechanism of Pinellia ternata inhibiting non-small cell lung cancer cells. BMC Complement Med Ther. 2024;24(1):263. https://doi.org/10.1186/s12906-024-04574-3 PMID: 38992647

10. Zheng F, Wu J, Zhao S, Luo Q, Tang Q, Yang L, et al. Baicalein increases the expression and reciprocal interplay of RUNX3 and FOXO3a through crosstalk of AMPKα and MEK/ERK1/2 signaling pathways in human non-small cell lung cancer cells. J Exp Clin Cancer Res. 2015;34(1):41. https:// doi.org/10.1186/s13046-015-0160-7 PMID: 25948105

11. Zhang D, Bian G, He J, Xie J, Hu C, Hu K. Research on the algorithm of mining information of traditional Chinese herb system biology based on graph neural network. J Nanjing Univ Tradition Chin Med. 2025;41(4):483–93. https://doi.org/10.14148/j.issn.1672-0482.2025.0483

12. Abramson J, Adler J, Dunger J, Evans R, Green T, Pritzel A, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature. 2024;630(8016):493–500. https://doi.org/10.1038/s41586-024-07487-w PMID: 38718835

13. Corso G, Stärk H, Jing B, Barzilay R, Jaakkola T. Diffdock: Diffusion steps, twists, and turns for molecular docking. arXiv preprint. 2022. https://doi. org/10.48550/arXiv.2210.01776

14. Graf J, Nguyen PH, Stock G, Schwalbe H. Structure and dynamics of the homologous series of alanine peptides: a joint molecular dynamics/NMR study. J Am Chem Soc. 2007;129(5):1179–89. https://doi.org/10.1021/ja0660406 PMID: 17263399

15. Abraham MJ, Murtola T, Schulz R, Páll S, Smith JC, Hess B, et al. GROMACS: High performance molecular simulations through multi-level parallelism from laptops to supercomputers. SoftwareX. 2015;1–2:19–25. https://doi.org/10.1016/j.softx.2015.06.001

16. Kumari M, Singh R, Subbarao N. Exploring the interaction mechanism between potential inhibitor and multi-target Mur enzymes of mycobacterium tuberculosis using molecular docking, molecular dynamics simulation, principal component analysis, free energy landscape, dynamic crosscorrelation matrices, vector movements, and binding free energy calculation. J Biomol Struct Dyn. 2022;40(24):13497–526. https://doi.org/10.1080/ 07391102.2021.1989040 PMID: 34662260

17. Petukh M, Li M, Alexov E. Predicting binding free energy change caused by point mutations with knowledge-modified MM/PBSA method. PLoS Comput Biol. 2015;11(7):e1004276. https://doi.org/10.1371/journal.pcbi.1004276 PMID: 26146996

18. Dong L, Qu X, Zhao Y, Wang B. Prediction of binding free energy of protein-ligand complexes with a hybrid molecular mechanics/generalized born surface area and machine learning method. ACS Omega. 2021;6(48):32938–47. https://doi.org/10.1021/acsomega.1c04996 PMID: 34901645

19. Fu H, Chen H, Blazhynska M, Goulard Coderc de Lacam E, Szczepaniak F, Pavlova A, et al. Accurate determination of protein:ligand standard binding free energies from molecular dynamics simulations. Nat Protoc. 2022;17(4):1114–41. https://doi.org/10.1038/s41596-021-00676-1 PMID: 35277695

20. Neese F. Software update: the ORCA program system, version 5.0. WIREs Comput Mol Sci. 2022;12(1):e1606. https://doi.org/10.1002/wcms.1606

21. Neese F. Software update: the ORCA program system, version 4.0. WIREs Comput Mol Sci. 2018;8(1):1–6. https://doi.org/10.1002/wcms.1327

22. Neese F. The SHARK integral generation and digestion system. J Comput Chem. 2023;44(3):381–96. https://doi.org/10.1002/jcc.26942 PMID: 35678278

23. Izsák R, Neese F, Klopper W. Robust fitting techniques in the chain of spheres approximation to the Fock exchange: the role of the complementary space. J Chem Phys. 2013;139(9):094111. https://doi.org/10.1063/1.4819264 PMID: 24028106

24. Izsak R, Hansen A, Neese F. The resolution of identity and chain of spheres approximations for the LPNO-CCSD singles Fock term. Molecular Physics. 2012;110:2413–7. https://doi.org/10.1080/00268976.2012.687466

25. Izsák R, Neese F. An overlap fitted chain of spheres exchange method. J Chem Phys. 2011;135(14):144105. https://doi.org/10.1063/1.3646921 PMID: 22010696

26. Neese F, Wennmohs F, Becker U, Riplinger C. The ORCA quantum chemistry program package. J Chem Phys. 2020;152(22):224108. https://doi. org/10.1063/5.0004608 PMID: 32534543

27. Neese F. The ORCA program system. WIREs Comput Mol Sci. 2012;2(1):73–8. https://doi.org/10.1002/wcms.81

28. Neese F. An improvement of the resolution of the identity approximation for the formation of the Coulomb matrix. J Comput Chem. 2003;24(14):1740–7. https://doi.org/10.1002/jcc.10318 PMID: 12964192

29. Helmich-Paris B, de Souza B, Neese F, Izsák R. An improved chain of spheres for exchange algorithm. J Chem Phys. 2021;155(10):104109. https://doi.org/10.1063/5.0058766 PMID: 34525816

30. Neese F, Wennmohs F, Hansen A, Becker U. Efficient, approximate and parallel Hartree–Fock and hybrid DFT calculations. A ‘chain-of-spheres’ algorithm for the Hartree–Fock exchange. Chem Phys. 2009;356(1–3):98–109. https://doi.org/10.1016/j.chemphys.2008.10.036

31. Grimme S, Ehrlich S, Goerigk L. Effect of the damping function in dispersion corrected density functional theory. J Comput Chem. 2011;32(7):1456–65. https://doi.org/10.1002/jcc.21759 PMID: 21370243

32. Grimme S, Antony J, Ehrlich S, Krieg H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J Chem Phys. 2010;132(15):154104. https://doi.org/10.1063/1.3382344 PMID: 20423165

33. Neese F. Approximate second-order SCF convergence for spin unrestricted wavefunctions. Chem Phys Lett. 2000;325(1–3):93–8. https://doi. org/10.1016/S0009-2614(00)00662-X

34. Lu T. A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn. J Chem Phys. 2024;161(8):082503. https://doi. org/10.1063/5.0216272 PMID: 39189657

35. Lu T, Chen F. Multiwfn: a multifunctional wavefunction analyzer. J Comput Chem. 2012;33(5):580–92. https://doi.org/10.1002/jcc.22885 PMID: 22162017

36. Humphrey W, Dalke A, Schulten K. VMD: visual molecular dynamics. J Mol Graph. 1996;14(1):33–8, 27–8. https://doi.org/10.1016/0263- 7855(96)00018-5 PMID: 8744570

37. Quintanal-Villalonga A, Molina-Pinelo S, Yagüe P, Marrugal Á, Ojeda-Márquez L, Suarez R, et al. FGFR4 increases EGFR oncogenic signaling in lung adenocarcinoma, and their combined inhibition is highly effective. Lung Cancer. 2019;131:112–21. https://doi.org/10.1016/j.lungcan.2019.02.007 PMID: 31027687

38. Chen X, Chen J, Feng W, Huang W, Wang G, Sun M, et al. FGF19-mediated ELF4 overexpression promotes colorectal cancer metastasis through transactivating FGFR4 and SRC. Theranostics. 2023;13(4):1401–18. https://doi.org/10.7150/thno.82269 PMID: 36923538

39. Qu X, Liu J, Zhong X, Li X, Zhang Q. PIWIL2 promotes progression of non-small cell lung cancer by inducing CDK2 and Cyclin A expression. J Transl Med. 2015;13:301. https://doi.org/10.1186/s12967-015-0666-y PMID: 26373553

40. Zhang J, Cui K, Huang L, Yang F, Sun S, Bian Z, et al. SLCO4A1-AS1 promotes colorectal tumourigenesis by regulating Cdk2/c-Myc signalling. J Biomed Sci. 2022;29(1):4. https://doi.org/10.1186/s12929-022-00789-z PMID: 35039060

41. Hsu H-S, Lin J-H, Hsu T-W, Su K, Wang C-W, Yang K-Y, et al. Mesenchymal stem cells enhance lung cancer initiation through activation of IL-6/ JAK2/STAT3 pathway. Lung Cancer. 2012;75(2):167–77. https://doi.org/10.1016/j.lungcan.2011.07.001 PMID: 21802163

42. Park S-Y, Lee C-J, Choi J-H, Kim J-H, Kim J-W, Kim J-Y, et al. The JAK2/STAT3/CCND2 axis promotes colorectal cancer stem cell persistence and radioresistance. J Exp Clin Cancer Res. 2019;38(1):399. https://doi.org/10.1186/s13046-019-1405-7 PMID: 31511084

43. Seto T, Higashiyama M, Funai H, Imamura F, Uematsu K, Seki N, et al. Prognostic value of expression of vascular endothelial growth factor and its flt-1 and KDR receptors in stage I non-small-cell lung cancer. Lung Cancer. 2006;53(1):91–6. https://doi.org/10.1016/j.lungcan.2006.02.009 PMID: 16697074

44. Dong G, Guo X, Fu X, Wan S, Zhou F, Myers RE, et al. Potentially functional genetic variants in KDR gene as prognostic markers in patients with resected colorectal cancer. Cancer Sci. 2012;103(3):561–8. https://doi.org/10.1111/j.1349-7006.2011.02194.x PMID: 22182247

45. Zhao S, Ma S, Zhang Y, Gao M, Luo Z, Cai S. Combining molecular docking and molecular dynamics simulation to discover four novel umami peptides from tuna skeletal myosin with sensory evaluation validation. Food Chem. 2024;433:137331. https://doi.org/10.1016/j.foodchem.2023.137331 PMID: 37678119

46. Huang C, Du R, Jia X, Liu K, Qiao Y, Wu Q, et al. CDK15 promotes colorectal cancer progression via phosphorylating PAK4 and regulating β-catenin/ MEK-ERK signaling pathway. Cell Death Differ. 2022;29(1):14–27. https://doi.org/10.1038/s41418-021-00828-6 PMID: 34262144

47. Schlaepfer DD, Ojalill M, Stupack DG. Focal adhesion kinase signaling - tumor vulnerabilities and clinical opportunities. J Cell Sci. 2024;137(14):jcs261723. https://doi.org/10.1242/jcs.261723 PMID: 39034922

48. Yang H, Li X, Meng Q, Sun H, Wu S, Hu W, et al. CircPTK2 (hsa_circ_0005273) as a novel therapeutic target for metastatic colorectal cancer. Mol Cancer. 2020;19(1):13. https://doi.org/10.1186/s12943-020-1139-3 PMID: 31973707

49. McDermott U, Ames RY, Iafrate AJ, Maheswaran S, Stubbs H, Greninger P, et al. Ligand-dependent platelet-derived growth factor receptor (PDGFR)-alpha activation sensitizes rare lung cancer and sarcoma cells to PDGFR kinase inhibitors. Cancer Res. 2009;69(9):3937–46. https://doi. org/10.1158/0008-5472.CAN-08-4327 PMID: 19366796

50. Kim TW, Hong HK, Lee C, Kim S, Lee WY, Yun SH, et al. The role of PDGFRA as a therapeutic target in young colorectal cancer patients. J Transl Med. 2021;19(1):446. https://doi.org/10.1186/s12967-021-03088-7 PMID: 34702313

51. Parihar A, Sonia ZF, Akter F, Ali MA, Hakim FT, Hossain MS. Phytochemicals-based targeting RdRp and main protease of SARS-CoV-2 using docking and steered molecular dynamic simulation: a promising therapeutic approach for Tackling COVID-19. Comput Biol Med. 2022;145:105468. https://doi.org/10.1016/j.compbiomed.2022.105468 PMID: 35390745

52. da Fonseca AM, Caluaco BJ, Madureira JMC, Cabongo SQ, Gaieta EM, Djata F, et al. Screening of potential inhibitors targeting the main protease structure of SARS-CoV-2 via molecular docking, and approach with molecular dynamics, RMSD, RMSF, H-Bond, SASA and MMGBSA. Mol Biotechnol. 2024;66(8):1919–33. https://doi.org/10.1007/s12033-023-00831-x PMID: 37490200

53. Dey D, Paul PK, Al Azad S, Al Mazid MF, Khan AM, Sharif MA, et al. Molecular optimization, docking, and dynamic simulation profiling of selective aromatic phytochemical ligands in blocking the SARS-CoV-2 S protein attachment to ACE2 receptor: an in silico approach of targeted drug designing. J Adv Vet Anim Res. 2021;8(1):24–35. https://doi.org/10.5455/javar.2021.h481 PMID: 33860009

54. Das N, Sen P. Macromolecular crowding: how shape and interaction affect the structure, function, conformational dynamics and relative domain movement of a multi-domain protein. Phys Chem Chem Phys. 2022;24(23):14242–56. https://doi.org/10.1039/d1cp04842b PMID: 35661170

55. Anbarasu K, Jayanthi S. Identification of curcumin derivatives as human LMTK3 inhibitors for breast cancer: a docking, dynamics, and MM/PBSA approach. 3 Biotech. 2018;8(5):228. https://doi.org/10.1007/s13205-018-1239-6 PMID: 29719770

56. Perez E, Fernandez JR, Fitzgerald C, Rouzard K, Tamura M, Savile C. In vitro and clinical evaluation of cannabigerol (CBG) produced via yeast biosynthesis: a cannabinoid with a broad range of anti-inflammatory and skin health-boosting properties. Molecules. 2022;27(2):491. https://doi. org/10.3390/molecules27020491 PMID: 35056807

57. Saha D, Nath Jha A. Computational multi-target approach to target essential enzymes of Leishmania donovani using comparative molecular dynamic simulations and MMPBSA analysis. Phytochem Anal. 2023;34(7):842–54. https://doi.org/10.1002/pca.3213 PMID: 36760044

58. Lohit N, Singh AK, Kumar A, Singh H, Yadav JP, Singh K. Description and in silico ADME studies of US-FDA approved drugs or drugs under clinical trial which violate the Lipinski’s rule of 5. Lett Drug Design Discov. 2024;21(8):1334–58. https://doi.org/10.2174/1570180820666230224112505

59. Argikar U, Blatter M, Bednarczyk D, Chen Z, Cho YS, Doré M, et al. Paradoxical increase of permeability and lipophilicity with the increasing topological polar surface area within a series of PRMT5 inhibitors. J Med Chem. 2022;65(18):12386–402. https://doi.org/10.1021/acs.jmedchem.2c01068 PMID: 36069672

60. Jayaraj JM, Muthusamy K. Role of deleterious nsSNPs of klotho protein and their drug response: a computational mechanical insights. J Biomol Struct Dyn. 2024;42(6):2886–96. https://doi.org/10.1080/07391102.2023.2214230 PMID: 37216366

61. Ahmad I, Khan H, Serdaroğlu G. Physicochemical properties, drug likeness, ADMET, DFT studies, and in vitro antioxidant activity of oxindole derivatives. Comput Biol Chem. 2023;104:107861. https://doi.org/10.1016/j.compbiolchem.2023.107861 PMID: 37060784

62. Hussein YT, Azeez YH. DFT analysis and in silico exploration of drug-likeness, toxicity prediction, bioactivity score, and chemical reactivity properties of the urolithins. J Biomol Struct Dyn. 2023;41(4):1168–77. https://doi.org/10.1080/07391102.2021.2017350 PMID: 34931599

63. Akintemi EO, Govender KK, Singh T. A DFT study of the chemical reactivity properties, spectroscopy and bioactivity scores of bioactive flavonols. Comput Theoret Chem. 2022;1210:113658. https://doi.org/10.1016/j.comptc.2022.113658