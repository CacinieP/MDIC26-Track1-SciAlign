http://pubs.acs.org/journal/acsodf

Article

# Investigation of Properties and Structure−Activity Relationship of Ketoprofen-Based Ionic Liquids Using Density Functional Quantum Chemical Theory Calculations

Yimei Tang,\* Qian Bai, Tian Tian, Benquan Hu, Jian Zhang, Bo Zhang, Maofang He, Yuzhen Zhang, and Jinjuan Li

<!-- image-->

Cite This: ACS Omega 2026, 11, 5075−5084

<!-- image-->

Read Online

ACCESS

Metrics & More

Article Recommendations

\*sı Supporting Information

<!-- image-->  
ABSTRACT: To improve the bioavailability of ketoprofen and reduce its clinical risks, this study combined density functional theory (DFT) calculations with experiments and investigated the structure−activity relationship of ketoprofen-based ionic liquids (ILs). Using ketoprofen as the anion and choline, 1-butyl-3-methylimidazole, and benzalkonium as the cations, ketoprofen-based ILs were prepared through a two-step method. Their structures, solubilities, critical micelle concentrations (CMC), cytotoxicity, etc., were determined. The results show that the physical and chemical properties of the ketoprofen-based ILs have changed significantly. For example, their critical micelle concentrations in ethanol and water are 10−6 and 10−5 mol·L−1 , respectively, and their solubility (converted to ketoprofen) is more than 103 times that of ketoprofen in water. The IC50 values exhibited the low cytotoxicity of the ketoprofen-based ILs, which was better than 100 μM. The DFT calculation results show that the difference in dipole moments between ketoprofen-based ILs is not significant, but the dipole moment of ketoprofen-based ILs is much larger than that of ketoprofen, which may lead to an increase in the solubility of ketoprofen-based ILs. Both DFT calculations and experimental results indicate that the stronger the ion-pair interaction energy of ILs, the higher their melting points and decomposition temperatures. These preliminary research results can lay a foundation for the application research of ketoprofen ILs (including ketoprofen choline gel and the pharmacokinetics of ketoprofen choline).

## INTRODUCTION

Active pharmaceutical ingredients (APIs) are mainly solid organic drugs, which have advantages in processes such as separation, storage, and evaluation. However, in the preclinical stage, some drugs face problems such as difficult delivery, unstable absorption, and low bioavailability due to poor water solubility.1,2 Some drugs are also affected by polymorphic transformations, which change their dissolution and absorption in the body, thereby affecting their bioavailability and efficacy, and may even cause side effects.3−7 Although scholars have tried to solve these problems through various strategies or other methods, such as the prodrug method,8 crystal engineering,9 s olid dispersions,10,11 colloidal preparations,12 micellar systems,13 s urfactants,1 4 and adsorption on high specific surface area carriers,15 these methods may also lead to new issues, such as drug dilution, dose uncertainty, and stability problems.

To address the aforementioned issues, modifying the chemical structure of drugs is an effective approach. By altering the chemical structure, the desired clinical efficacy can be achieved, polymorphic phenomena can be avoided, and drugs can be endowed with excellent physicochemical properties and biological characteristics. Ionic liquids (ILs) can solve more pharmaceutical problems (such as solubility and polymorphism issues), thereby improving the bioavailability and clinical efficacy of drugs. ILs are low-temperature molten salts composed of organic cations and inorganic or organic anions. They possess unique physicochemical properties, including a wide liquid range, nearly negligible vapor pressure, and designable physicochemical properties such as solubility and surface activity.16,17 In 2007, Rogers and his colleagues reported API-IL for the first time, referring to them as the third-generation ILs.18,19 API-ILs exhibit specific biological activities and favorable physicochemical properties,20 which are beneficial for improving drug solubility21−25 and bioavailability,1726,27 eliminating polymorphic phenomena,17 and altering drug transport modes.27 −29

In 1998, the IL containing miconazole as the API-IL came into being, but it did not attract people’s attention at that time.30 After 2007, reports on API-ILs have increased increasingly. At present, it is a cutting-edge topic in the field of IL research at home and abroad, and also a current research focus. 31−34

Nonsteroidal anti-inflammatory drugs (NSAIDs) are one of the drug classes with the highest prescription volumes, and they exhibit significant efficacy in the treatment of chronic and acute pain as well as inflammation. In addition to other serious side effects, long-term use of NSAIDs may increase the risk of gastrointestinal adverse events, such as gastroduodenal ulcers, gastrointestinal bleeding, perforation, and dyspepsia.35 In recent years, NSAID ILs have included naproxen,36−38 ibuprofen,39 indomethacin40 ILs, etc., with research primarily focusing on the preparation, structure, solubility, toxicity, antibacterial activity, and binding parameters with bovine serum albumin of these ILs.

In this study, ketoprofen was selected as the research subject. Its anti-inflammatory and analgesic effects are significantly superior to those of ibuprofen,41 making it a drug with relatively prominent efficacy among arylpropionic acid-type NSAIDs. Compared with commonly used drugs such as diclofenac and indomethacin, ketoprofen can more easily penetrate the skin barrier, reach the inflammatory focus quickly, and exert analgesic and anti-inflammatory effects.42−44

For the first time, Guncheva et al.45,46 investigated the interactions between API-ILs, composed of amino acid ester cations and ketoprofen anions, namely, L-leucine ethyl ester ketoprofen salt ([L-LeuOEt][Ket]), L-valine butyl ester ketoprofen salt ([L-ValOBu][Ket]), L-valine propyl ester ketoprofen salt ([L-ValOPr][Ket]), L-valine isopropyl ester ketoprofen salt ([L-ValOiPr][Ket]), and L-valine ethyl ester ketoprofen salt ([L-ValOEt][Ket]), with human serum albumin (HSA). Compared with ketoprofen, the effects of these ketoprofen ILs on the thermal denaturation and unfolding of HSA were negligible. In contrast to the ketoprofen-bovine serum albumin (BSA) system, the ILs containing L-LeuOEt, L-ValOBu, and L-ValOEt cations exhibited significantly stronger binding affinity to BSA.45 Fluorescence spectroscopy was employed to evaluate the binding affinity and binding mode of this class of ketoprofenbased ILs with BSA. The results demonstrated the existence of strong interactions between the drugs/ILs and BSA.46 Fourier transform infrared (FT-IR) spectroscopy experiments revealed that all tested compounds induced conformational rearrangements of protein molecules after binding to BSA. This finding is consistent with the speculation of the static fluorescence quenching mechanism of BSA and the formation of complexes between proteins and drugs.46

AbouElmagd et al.47 combined ketoprofen with piperine in an equimolar ratio to prepare ketoprofen-piperine ([Ket]-

[Pip]) ILs for the purpose of its transdermal drug delivery. The research results showed that this IL exhibited good stability, and the solubility of ketoprofen was increased by 71 to 83% due to the formation of the IL. Meanwhile, compared with the ketoprofen/piperine mixture, the amount of ketoprofen in the IL form penetrating the rat skin increased by 218%. Importantly, after transdermal administration to rats with the paw edema model, the paw edema degree of rats treated with [Ket][Pip] was 68% lower than that of rats treated with the KP/PI mixture.

Tajber, L. et al.48 used ketoprofen as the acidic component and local anesthetics (lidocaine, mepivacaine, bupivacaine) as the basic components to prepare ketoprofen-based ILs. Infrared spectroscopy was used to analyze the interaction forces and composition involved in the formation of the ILs. Yang et al.49 studied long-acting controlled-release transdermal patches containing weak acid API-ILs and investigated the effect of pressure-sensitive adhesives (PSAs) on the loading capacity and release behavior of API-ILs.

In this study, a series of ILs containing ketoprofen were synthesized, including choline ketoprofen ([Ch][Ket]), Tetradecyldimethylbenzylammonium ketoprofen ([Ben]- [Ket]), and 1-butyl-3-methylimidazolium ketoprofen ([Bmim][Ket]). Their physical and chemical properties, such as solubility, surface activity, and stability, as well as cytotoxicity, were analyzed with DFT. The aim is to clarify that, based on the improvement of the physical and chemical properties of poorly soluble drugs through the IL approach, it can solve the problems in clinical medication. Combined with the inherent surface activity and water solubility of pharmaceutical ILs, the research on ketoprofen-based ILs can lay a foundation for the development of ketoprofen IL gels and the oral administration of ketoprofen ILs (as published in other journals).

## MATERIALS AND METHODS

## Materials

Tetradecyldimethylbenzylammonium chloride (w% ≥ 98%) and choline chloride (w% ≥ 98%) were purchased from Aladdin. Ketoprofen (w% ≥ 99%) was supplied by Bide Pharmatech Ltd. Ethanol (w% ≥ 99%), ethyl acetate (w% ≥ 99%), and n-octanol (w% ≥ 99%) were supplied by Sinopharm Chemical Reagent Co., Ltd. 1- Butyl-3-methylimidazole bromide ([Bmim] Br) was prepared in the lab. Sodium hydroxide (w ≥ 98%) and triethanolamine (w ≥ 98%) were supplied by Tianjin Kemiou Chemical Reagent Co., Ltd. Ketoprofen standard substance (w% ≥ 99%, ID: Y31D6C8363) was supplied by Shanghai Yuanye Bio-Technology Co., Ltd. Methyl thiazolyl tetrazolium (MTT) was supplied by Sigma. Trypsin was supplied by Shanghai Blue Base Biology Co., Ltd. Phosphate buffer (PBS) and trypsin cell digestive juice with 0.02% EDTA were supplied by Beijing Solaibao Technology Co., Ltd. High sugar DMEM medium was supplied by Gibco. Fetal calf serum (FCS) was supplied by Zhejiang Tianhang Biotechnology Co., Ltd. The chemicals mentioned above were analytical grade and used without further purification. Chromatographic methanol was supplied by Fisher Company in the USA.

The investigations were performed with a DDS-307 digital conductometer (Shanghai Dapu Instrument Co., Ltd.), Q600SDT thermogravimetric and differential scanning calorimetry synchronous measuring instrument (TA Instruments, USA), Q1000 differential scanning calorimeter (TA Instruments, USA), ultraviolet−visible spectrophotometer (Cary 60 Agilent, Agilent Technologies (China) Co., Ltd.), clean bench CJ-2S (Tianjin TST Instrument Co., Ltd.), low-speed desktop centrifuge TDL-40B (Shanghai Anting Scientific Instrument Factory), CO carbon incubator Thermo 3111 (Thermo

## Scheme 1. Synthetic Procedure for Ketoprofen-Based ILs

<!-- image-->

<!-- image-->  
R+ X - =choline chloride, [Bmim]Br, and benzalkonium chloride

Fisher Scientific), inverted microscope CKX31SF (Olympus), Agilent Technologies 1260 Infinity high-performance liquid chromatograph, etc.

## Synthesis of Ketoprofen-Based ILs

Ketoprofen (18.79 g, 73.91 mmol) and an appropriate amount of water were placed in the flask, then sodium bicarbonate (6.21 g, 73.80 mmol) was added to the flask. The mixture was shaken vigorously for 24 h until the reaction solution became clear and transparent, and was filtered. Then, the filtrate was collected and freeze-dried to obtain the crude dried sodium ketoprofen, which was purified with a small amount of ethyl acetate. The solid white powder of sodium ketoprofen was obtained with a constant weight under a vacuum at $4 5 \ { } ^ { \circ } { \mathrm { { C } } } .$

Sodium ketoprofen with equimolecular [Bmim] Br, benzalkonium chloride, or choline chloride was dissolved in ethanol. The mixture solution was stirred under the protection of nitrogen at $3 5 ~ ^ { \circ } \mathrm { C }$ for 24 h and then naturally cooled to room temperature and filtered with a sand core funnel (bore diameter 3−4 μm). After the solvent was removed by reduced-pressure distillation, the oily or waxy substances were obtained and dried under reduced pressure at $4 5 ~ ^ { \circ } \mathrm { C }$ to constant weight (about 60 h). The faint yellow viscous liquids ([Ben][Ket] or [Bmim][Ket]) or white waxy ([Ch][Ket]) substances, ketoprofenbased ILs, were obtained (Scheme 1), and the yield was above 90%

## Theoretical Calculation

The Molclus program50 is used to generate a variety of possible conformations of molecules, with the number of generated conformations being at least 200. The 200 collected structures were optimized using the gfn2-xtb method in the xtb software51 (version 6.6.0), and the optimized structures, as well as the corresponding energy data, were collected. Structures with similar energies (energy threshold = 10 kcal/mol) and similar geometries (geometric structure threshold = 0.2 Å) were identified as identical structures. The structures screened out as described above will be used for subsequent geometric structure optimization based on DFT. DFT calculations were performed using the Gaussian 16 software.52 All calculations adopted the B3LYP functional53 combined with the D3BJ dispersion correction.54 In the geometric structure optimization and frequency calculation, the ma-def2-SVP basis set55,56 was used for all atoms. The single-point energy calculation and the Basis Set Superposition Error (BSSE) correction calculation were both carried out at the B3LYP-D3BJ/ma-def2-TZVPP55,56 l evel.

## 1 H NMR Analysis

All ketoprofen-based ILs were completely characterized by 1 H NMR (Bruker AVANCE 600 MHz, DE) to confirm the expected cation/ anion ratios. The sand core funnel can filter the precipitates (NaCl or NaBr) better. HPLC (Agilent 1260, USA) was used to check the structure and final purity of the obtained ketoprofen-based ILs. The purity was above 99% (w%) with the ketoprofen reference substance (ID: Y31D6C8363).

1 H NMR characterization was performed on [Ch][Ket] and [Ben][Ket] using chloroform as the deuterated reagent and conducted on [Bmim][Ket] using dimethyl sulfoxide as the deuterated reagent. The 1 H NMR results are shown in the appendix.

The results of 1 H NMR and HPLC showed that the structure of the cation for the title substance was ketoprofen-based $\mathrm { A P I - I L } s ,$ and the title substance was extremely dry and free of water. 1 H NMR also indicated that the structure of the synthesized API-IL is consistent with that of the corresponding target ketoprofen-based IL.

## Solubility

An excessive amount of ketoprofen or ketoprofen salt was taken and dissolved in water or absolute ethanol to obtain the supersaturated solutions of ketoprofen and ketoprofen salt at 25 or $3 { \dot { 7 } } ^ { \circ } \mathrm { C } ,$ which were centrifuged at 13,000 rpm for 15 min. The upper layer of the solution was taken and diluted, and its concentration was determined by HPLC. Finally, the solubility of ketoprofen and ketoprofen salt in 100 g of water or 100 g of absolute ethanol was calculated.

## Critical Micelle Concentration

For the title ketoprofen-based ILs, the concentrations of standard solutions were prepared in turn with double-distilled water or ethanol as a solvent $( 1 . \dot { 0 } \times 1 0 ^ { - 2 } , 1 . 0 \times 1 0 ^ { - 3 } , 1 . 0 \times 1 0 ^ { - 4 } , 1 . 0 \times 1 0 ^ { - 5 } \mathrm { m o l . L ^ { - 1 } } )$

First, the pure solvent (50 mL, double-distilled water, or ethanol) was placed in a beaker. During different determination phases, the standard solution of different concentrations was chosen. After each addition of standard solution (1.00 mL), the solution was stirred to ensure homogeneous mixing and the electrical conductivities and concentrations of the beaker were recorded with an electrical conductivity meter DDS-307 (DJS-1C platinum black electrode) at $2 5 ~ ^ { \circ } \mathrm { C } .$ The electrical conductivity meter DDS-307 operated at 50 ± 0.5 Hz alternating current. The conductivity value of the ketoprofenbased ILs was determined after subtracting the electrical conductivity of solvents (water, 2.02 μS·cm−1 ; ethanol, 0.35 μS·cm−1 ) from the measured values.38

## Thermal Property Analysis

The thermogravimetric analysis (TGA) was conducted in a nitrogen atmosphere (flow rate of 50 mL·min−1 ) on Q1000DSC + LNCS + FACEQ600 SDT (FA, USA) with a temperature range of 25−800 °C and a heating rate of ${ \bf \Lambda } _ { 1 0 } ^ { \mathrm { o } } { \bf C } { \bf { \cdot } } \operatorname* { m i n } ^ { - 1 } .$ The differential scanning calorimetry (DSC) measurement was carried out in a nitrogen atmosphere (flow rate of 50 mL·min−1 ) on Q1000DSC with a temperature range of −80 (5 min)−100 °C and a heating rate of 10 °C·min−138

## Octanol−Water Partition Coefficients

The n-octanol−water partition coefficient of ketoprofen and choline ketoprofen was determined by the shake flask method.38

<!-- image-->

<!-- image-->

<!-- image-->

<!-- image-->  
a. Ketoprofen b. [Ch][Ket] c. [Ben][Ket] d. [Bmim][Ket]  
Figure 1. Thermogravimetric (TG-DTG) curves of ketoprofen and the ketoprofen-based IL.

## Cytotoxicity

The in vitro cytotoxicity of ketoprofen-based ILs on L929 cells was determined by the MTT (3-(4,5-dimethylthiazol-2-yl)-2,5-diphenyltetrazolium bromide) method. Cells were seeded with a density of 1 × 104 cells·mL−1 cells/well (200 μL) for 24−48 h at $3 7 ^ { \circ } \mathrm { C } ,$ and the 96- well plate contained DMEM, 10% fetal bovine serum, and 1% antibiotic solution. In serum-free DMEM, the wells were rinsed with sterile PBS and treated with API-IL samples at different concentrations. Each sample was replicated three times and cultured at $3 7 ~ ^ { \circ } \mathrm { C }$ for 24 h. Twenty microliters of MTT (5 mg·mL−1 ) was added to each well, and the cells were incubated for 4 h. Purple precipitates could be seen under the microscope. Finally, the medium was gently aspirated and rinsed with 1× PBS (200 μL), and then dimethyl sulfoxide (DMSO) (100 μL) was added to dissolve the formazan crystals; the plate was shaken for 5 min. The absorbance values were measured at 490 nm using a microplate reader (Thermo Fisher Scientific, USA), and the cell viability and IC50 values were calculated using GraphPad Prism 5.0 (USA) software.

## RESULTS AND DISCUSSION

## Thermal Property Analysis

Thermal stability is one of the key indicators for evaluating the applicability of ILs, and it directly affects their service life and performance in high-temperature environments.57 TGA is a thermal analysis technique that measures the relationship between the mass of the substance to be tested and the temperature change under controlled temperature conditions. It is usually used to study the thermal stability, thermal decomposition situation, composition of impurities of substances, etc. From the derivative thermogravimetry (DTG) curve, it is easy to obtain the initial thermal weight loss temperature, the special temperature at which the thermal weight loss rate is the maximum, and the thermal weight loss equilibrium temperature of the substance. The TG-DTG curves of ketoprofen and the ketoprofen-based ILs are shown in Figure 1.

It can be seen from Figure 1 that the IL does not exhibit an obvious phenomenon of thermal weight loss caused by water and solvent. However, due to the high viscosity of the ILs, it is inevitable that there will be encapsulation of trace amounts of water and solvent. Therefore, before conducting other physical and chemical property experiments, the vacuum drying time should be increased so that the residual solvent can be reduced to 3% at approximately $1 2 0 \phantom { + } ^ { \circ } \mathrm { C } .$ Comparing the initial thermal decomposition temperatures, the order of thermal stability between ketoprofen and the ketoprofen-based IL is $[ \mathrm { B m i m } ] [ \mathrm { K e t } ] > [ \mathrm { K e t } ] { \bf \dot { \omega } } > [ \mathrm { C h } ] [ \mathrm { K e t } ] > [ \mathrm { B e n } ] [ \mathrm { K e t } ]$ (Figure 1).

Existing studies have shown that structural characteristics of cations, such as the length of alkyl side chains, functional groups, and alkyl substituents, all affect the thermal stability of $\stackrel { \cup } { \mathrm { I L } } s . ^ { 5 ^ { \frac { 1 } { 7 } } }$ This is because longer alkyl side chains reduce the symmetry of cations and hinder the effective packing of crystals, thereby decreasing the thermal stability of the ILs. When analyzing from the perspective of cation symmetry, the order of cation symmetry is $[ \dot { \mathrm { C h } } ] ^ { + } > [ \mathrm { B m i m } ] ^ { + } > [ \mathrm { B e n } ] ^ { + }$ , which is inconsistent with the results of this experiment and the published experimental results.38 The researchers of this study believe that when analyzing the thermal stability of ILs from the perspective of cation symmetry, the cations must be of the same type. When analyzing from the perspective of cation thermal stability, the order of cation thermal stability is $[ \mathrm { B m i m } ] ^ { + } > [ \mathrm { C h } ] ^ { + } > [ \mathrm { B e n } ] ^ { + }$ , and the thermal stability of ILs is consistent with that of cations. It can be seen that cations with higher stability usually improve the thermal stability of the ILs themselves.

Under the same test conditions and with the same cation, the thermal decomposition temperature of naproxen-based ILs is higher than that of ketoprofen-based ${ \mathrm { I L } } s , { } ^ { 3 8 }$ which indicates that the type and structure of anions have an impact on the thermal stability of $\mathrm { I L } { s . } ^ { 5 7 }$ The naphthalene ring conjugated system in naproxen anions is more conducive to anion stability; in contrast, for ketoprofen anions, the carbonyl group in the benzophenone structure may affect anion stability through electron-withdrawing and repelling effects. It can be seen that anions with higher stability usually improve the thermal stability of ILs.5 57

Ion-pair interaction energy is an important parameter describing the strength of the interaction between cations and anions in ILs, and it directly affects the physicochemical properties of ILs. The interactions in ILs mainly include electrostatic interaction, van der Waals force, hydrogen bond, and other types of forces, among which electrostatic interaction is the main source of interionic attraction.58 Studying the relationship between the thermal stability of ILs and the ion-pair interaction energy is of great significance for understanding the thermal decomposition mechanism of ILs, designing ILs with specific thermal stability, and expanding their applications in high-temperature fields.

With the theoretical calculation method, when the structural optimization of ketoprofen-based ILs and ketoprofen were completed, their dipole moments (μ) were obtained (Table 1

Table 1. DSC, Interaction Energies of Ion Pairs and Dipole Moment of Ketoprofen-Based ILs
<table><tr><td>API-ILs</td><td> $t _ { \mathrm { m } } / { } ^ { \circ } \mathrm { C }$ </td><td> $t _ { \mathrm { d } } / { } ^ { \circ } \mathrm { C }$ </td><td>∆E/kJ·mol-1</td><td>dipole moment/D</td></tr><tr><td>[Ch][Ket]</td><td>84.2</td><td>165.9</td><td>-117.51</td><td>8.88</td></tr><tr><td>[Ben][Ket]</td><td>76.9</td><td>131.1</td><td>-103.56</td><td>7.39</td></tr><tr><td>[Bmin][Ket]</td><td>94.5</td><td>209.5</td><td>-108.13</td><td>9.45</td></tr><tr><td>ketoprofen</td><td>93-96</td><td>203.9</td><td></td><td>2.61</td></tr></table>

and Figure 2). The interaction energy (ΔE) of ion pairs for ketoprofen-based ILs can be evaluated by using the following eq 1

$$
\Delta E \left( \mathrm { \text k J } { \cdot } \mathrm { m o l } ^ { - 1 } \right) = 2 6 2 5 . 5 [ E _ { \mathrm { A X } } ( \mathrm { a u } ) - E _ { \mathrm { X } ^ { - } } ( \mathrm { a u } ) - E _ { \mathrm { A } ^ { + } } ( \mathrm { a u } ) ]\tag{1}
$$

where $E _ { \mathrm { A X } } , E _ { \mathrm { A } ^ { \dagger } } ,$ and $E _ { \mathrm { X } ^ { ' } }$ are the energy of API-ILs, anion, and cation, respectively. ΔE is the interaction energy of ion pairs for ketoprofen-based ILs. The data are listed in Table 1.

Different types of ILs have different ion-pair interaction energies.59,60 It can be seen from Table 1 that the melting points $\left( t _ { \mathrm { m } } \right)$ of [Bmin][Ket], [Ben][Ket], and [Ch][Ket] decrease successively. Since the interaction energy between the anions and cations can reflect the balance between the

Coulombic attractive force of the anions and cations and the van der Waals repulsive force of the alkyl side chains, this interaction directly affects the melting point of the ILs. The ion pair interaction energy (ΔE) of the ketoprofen-based ILs is $\Delta E _ { \mathrm { [ C h ] [ K e t ] } } > \Delta E _ { \mathrm { [ B m i n ] [ K e t ] } } > \Delta E _ { \mathrm { [ B e n ] [ K e t ] } }$ in turn (Table 1 and Figure 2). The $t _ { \mathrm { m } }$ values of [Bmin][Ket], [Ch][Ket], and [Ben][Ket] decrease successively, and the variation law is basically consistent with the change in the magnitude of the ΔE (Table 1 and Figure 2).

ΔE in ILs is positively correlated with its $t _ { \mathrm { m } } .$ Experimental results show that although there is no positive correlation between the ΔE and $t _ { \mathrm { m } }$ changes of [Ch][Ket] and [Bmin]- [Ket] (Table 1 and Figure 2), the differences in both ΔE and $t _ { \mathrm { m } }$ (melting point) between the two are small. The absence of a positive correlation may stem from the effects of ion symmetry, ion packing, and other factors (Supporting Information).

Generally speaking, the stronger the $\Delta E ,$ the higher the $t _ { \mathrm { d } }$ of the IL. The decomposition temperature of ILs tends to be positively correlated with $\Delta E ,$ but this is not a simple linear relationship. It is primarily regulated by multiple factors (Supporting Information). A higher ΔE leads to stronger interactions between ions, which in turn requires more energy to break these interactions, so the $t _ { \mathrm { d } }$ usually increases accordingly. Of course, there are exceptions to this trend: when ions form conjugated structures (such as imidazole rings)61 or hydrogen bond networks,62 the stability of the IL can be further enhanced. The high $t _ { \mathrm { d } }$ of [Bmin][Ket] may be attributed to the conjugated structure of its imidazole ring in the experiment (Table 1 and Figure 2).

It can be seen from Table 1 that the dipole moments of [Ben][Ket], [Ch][Ket], and [Bmin][Ket] decrease successively. From the calculation results, it can be seen that the differences in the dipole moments of the three ketoprofenbased ILs are smaller than that of ketoprofen, and the difference in the dipole moment between ketoprofen-based ILs and ketoprofen is larger. This may be the main reason for increasing the solubility of ketoprofen through the IL approach.

## Critical Micelle Concentration Analysis

Compounds in the medium form micelles through association, and solubilization can occur in the micelle system.63 Therefore, the tendency of compounds to form micelles may be a relevant property determining the degree of solubilization. Compared with the solubility of compounds in an aqueous solution, the degree of solubilization for compounds in the fast state simulated intestinal fluids (FaSSIF) is related to their surface activity.63 Studies have demonstrated that the CMC can describe the ability of compounds to self-aggregate in micelles and can better predict the solubilization of compounds in FaSSIF than lipophilicity. If the tendency of compounds to accumulate in micelles is considered as a way to increase the intestinal absorption of drugs, then the optimization strategy of drugs may benefit from it.

<!-- image-->  
Figure 2. Optimized stable structure of ketoprofen-based ILs.

<!-- image-->  
a. [Ch][Ket] (water); b. [Ben][Ket](water); c. [Bmin][Ket] (water)  
d. [Ch][Ket] (ethanol) e. [Ben][Ket](ethanol) f. [Bmin][Ket](ethanol)  
Figure 3. Curves of molar conductance vs the square root of concentration for ketoprofen-based ILs in different solvents.

In this study, the conductometry method was used to determine the electrical conductivity of ketoprofen-based ILs at different concentrations in ultrapure water or absolute ethanol at $2 5 ~ ^ { \circ } \mathrm { C } .$ . Then, the square root of the concentration $\big ( c ^ { 1 / 2 } \big )$ for ketoprofen-based ILs was performed and plotted against molar conductivity $\left( \Lambda m \right) ^ { 3 8 }$ (Figure 3).

Figure 3 shows that, using water or ethanol as the solvent, as the concentration of ketoprofen-based ILs increases, the $\Lambda _ { \mathrm { m } }$ of ketoprofen-based ILs decreases and a sudden change occurs at a certain concentration. The concentration corresponding to the inflection point is the CMC of ketoprofen-based ILs (Table 2).

Table 2. Critical Micelle Concentrations (CMC) of the Surfactant Ketoprofen-Based ILs Calculated from Conductivity Measurements in Water or Ethanol at ${ \bf 2 5 \ S }$
<table><tr><td>API-ILs</td><td>water/mol·L-1</td><td>ethanol/mol·L-1</td></tr><tr><td>[Ch][Ket]</td><td> $1 . 6 2 \times 1 0 ^ { - 5 }$ </td><td> $3 . 6 9 \times 1 0 ^ { - 6 }$ </td></tr><tr><td> $[ \mathrm { B e n } ] [ \mathrm { K e t } ]$ </td><td> $1 . 9 6 \times 1 0 ^ { - 5 }$ </td><td> $2 . 1 8 \times 1 0 ^ { - 6 }$ </td></tr><tr><td> $[ \mathrm { B m i n } ] [ \mathrm { K e t } ]$ </td><td> $3 . 5 1 \times 1 0 ^ { - 5 }$ </td><td> $1 . 6 8 \times 1 0 ^ { - 6 }$ </td></tr></table>

It can be seen from Table 2 that at $2 5 \ ^ { \circ } \mathrm { C } ,$ the cmc of ketoprofen-based ILs in water is $1 0 ^ { - 5 }$ mol·L−1 , and the CMC in ethanol is $1 0 ^ { - 6 }$ mol·L−1 . Both CMC values are relatively smaller, indicating that only a small amount of concentration is required to achieve the effects of wetting, emulsification, solubilization, foaming effects, etc. As can be seen from Table 2, the cmc values of the three ketoprofen-based ILs in ethanol are all smaller than those in water. Evidently, the surface activity of the three ketoprofen-based ILs in ethanol is greater than that in water.

The reason is as follows: The dielectric constants (ε) of water and ethanol are water (78.5 F·m−1 ) and ethanol (24.3 F· $\mathbf { m } ^ { - 1 } )$ respectively, and the calculated μ are 2.07 and 1.61 D in sequence. The corresponding μ in the literature are 1.87 and 1.66 D. The greater the polarity of the solvent (higher ε), the easier it is to break the interaction force (coulomb force) between ion pairs, which is more conducive to the dissociation of the electrolyte, and the greater the CMC. The viscosity of water is smaller than that of ethanol. The greater the viscosity of the solvent, the more it restricts the movement of surfactant molecules, strengthens the interaction between molecules, and makes it easier for surfactant molecules to aggregate and form micelles, thus reducing CMC. For different ketoprofen-based ILs, CMC is related to molecular structure (the ability to form hydrogen bonds), molecular size, polarity, viscosity, etc., in water and ethanol. The interaction force between solvent molecules and surfactant molecules increases, which will cause the CMC to decrease. Generally, the larger the molecule ${ \mathrm { i } } s ,$ the lower the CMC is. Many aspects, such as the perspective of intermolecular forces, the hydrophobic effect, the steric hindrance, and so on, will all affect the CMC. Due to the combined effects of these influencing factors, the cmc of ketoprofen-based ILs in water is as follows: $[ \mathrm { C h } ] [ \mathrm { K e t } ] \ < $ $[ \mathrm { B e n } ] [ \mathrm { K e t } ] < [ \mathrm { B m i n } ] [ \mathrm { K e t } ]$ . The CMC in water is exactly the opposite, $[ \mathrm { C h } ] [ \mathrm { K e t } ] > [ \mathrm { B e n } ] [ \mathrm { K e t } ] > [ \mathrm { B m i n } ] [ \mathrm { K e t } ]$

## Analysis of Solubility and Octanol−Water Partition Coefficient

The solubility of drugs affects their absorbance, bioavailability, therapeutic effect, etc. To a certain extent, poor solubility may also cause toxic side effects during application. Therefore, in the process of drug research, it is of great significance to master the solubility properties of drugs. The water solubility of drugs is closely related to their behaviors, such as adsorption, migration, and enrichment. The octanol/water partition coefficient is an important physicochemical characteristic parameter that can reflect the migration ability of organic compounds from the aqueous phase to organisms.

The solubilities of ketoprofen and ketoprofen-based ILs are listed in Table 3. As can be seen from Table 3, in water or

Table 3. Solubility of Ketoprofen and Ketoprofen Salts (Mean and Standard Deviation), in Water or Ethanol at 25 $^ { \circ } \mathbf { C }$ and $3 7 ~ ^ { \circ } \mathbf { C }$
<table><tr><td>ketoprofen and ketoprofen salts</td><td> $\begin{array} { r } { \mathsf { s o l u b i l i t y / g : } ( 1 0 0 \ { \mathrm { g } } ) ^ { - 1 } , } \\ { 2 5 \mathrm { ~ ^ \circ C ~ } } \end{array}$ </td><td> $\begin{array} { r } { \mathsf { s o l u b i l i t y } / \mathsf { g } { \cdot } ( 1 0 0 \mathrm { \ g } ) ^ { - 1 } , } \\ { 3 7 \mathsf {  { \mathrm { \Sigma } } } ^ { \circ } \mathsf { C } } \end{array}$ </td></tr><tr><td>ketoprofen</td><td> $( 9 . 2 1 \pm 0 . 2 1 ) \times 1 0 ^ { - 3 }$ </td><td> $( 9 . 6 1 \pm 0 . 2 0 ) \times 1 0 ^ { - 3 }$ </td></tr><tr><td>[Ch][Ket]</td><td> $5 1 . 3 1 \pm 1 . 1 4$ </td><td> $5 7 . 4 7 \pm 0 . 6 7$ </td></tr><tr><td>[Ben][Ket]</td><td> $4 2 . 5 5 \pm 0 . 7 7$ </td><td> $4 8 . 6 0 \pm 1 . 1 2$ </td></tr><tr><td>[Bmim][Ket]</td><td> $5 0 . 2 3 \pm 0 . 4 7$ </td><td> $5 7 . 2 1 \pm 1 . 3 4$ </td></tr><tr><td>Ketoprofen(ethanol)</td><td> $2 . 6 0 \pm 0 . 4 3$ </td><td> $3 . 7 0 \pm 0 . 2 3$ </td></tr><tr><td>[Ch][Ket](ethanol)</td><td> $3 5 . 4 3 \pm 0 . 7 1$ </td><td> $4 2 . 3 1 \pm 0 . 7 6$ </td></tr><tr><td>[Ben][Ket](ethanol)</td><td> $2 0 . 2 6 \pm 0 . 3 5$ </td><td> $3 1 . 6 3 \pm 0 . 6 4$ </td></tr><tr><td>[Bmin][Ket](ethanol)</td><td> $4 2 . 0 6 \pm 1 . 0 9$ </td><td> $5 0 . 9 8 \pm 0 . 8 0$ </td></tr></table>

ethanol, the solubility of ketoprofen-based ILs at $3 7 ~ ^ { \circ } \mathrm { C }$ is greater than that at $2 { \dot { 5 } } ^ { \circ } \mathrm { C } .$ The solubility of ketoprofen-based ILs in water is $S _ { [ \mathrm { C h } ] [ \mathrm { K e t } ] } ~ > ~ S _ { [ \mathrm { B m i n } ] [ \mathrm { K e t } ] } ~ > ~ S _ { [ \mathrm { B e n } ] [ \mathrm { K e t } ] } ^ { } ,$ and their solubility in ethanol is $S _ { [ \mathrm { C h } ] [ \mathrm { K e t } ] } < S _ { [ \mathrm { B m i n } ] [ \mathrm { K e t } ] } < S _ { [ \mathrm { B e n } ] [ \mathrm { K e t } ] }$ (Table 3).

<!-- image-->

<!-- image-->

When the anions are the same, the choline cation contains a hydroxyl group, which endows it with relatively strong polarity $( \dot { \mu } = \dot { 8 } . 8 \dot { 8 } \mathrm { ~ D } )$ . Compared with ethanol, water has a greater polarity $\left( \varepsilon _ { \mathrm { w a t e r } } = 7 8 . 5 \mathrm { { 0 } F { \cdot } m ^ { - 1 } } , \varepsilon _ { \mathrm { { e t h a n o l } } } = 2 4 . 3 0 ~ \mathrm { { F \cdot } m ^ { - 1 } } \right)$ at $\bar { 2 } 5 ^ { \circ } \mathrm { C } .$ Therefore, the ability of the choline cation to form hydrogen bonds with stronger polar water $\left( \mu = 2 . 0 7 ~ \mathrm { D } \right)$ is greater than that to form hydrogen bonds with ethanol $\left( \mu = 1 . { \overset { \cdot } { 6 } } 1 ~ \mathrm { { D } } \right)$ . As a result, the solubility of [Ch][Ket] in water is higher than that in ethanol. In polar solvents, there is usually a positive correlation between the dipole moment of ILs and their solubility, which is the most fundamental principle affecting solubility. The types of intermolecular forces and the degree of strength matching are also crucial, such as the interaction between hydrogen bond donors and acceptors, the degree of matching of van der Waals forces, and the dipole−dipole interactions.

The benzalkonium cation and 1-butyl-3-methylimidazolium cation do not contain a hydroxyl group, and it is not easy to form hydrogen bonds with water. Moreover, the alkyl chain of the benzalkonium cation is longer than that of the 1-butyl-3- methylimidazolium cation, which increases the hydrophobicity of the benzalkonium cation, resulting in the lowest solubility of [Ben][Ket] $\left( \mu = 7 . 3 9 \mathrm { D } \right)$ in water and ethanol. As can be seen from Table 3, the solubilities of ketoprofen-based ILs in water are higher than 100 $\mu \mathrm { g } \cdot \mathrm { m L } ^ { - 1 }$ , which indicates that the ketoprofen-based ILs have the similar solubility in water and FaSSIF medium.63

Combining the laws of CMC and solubility for ketoprofen and ketoprofen-based IL in water and ethanol (Tables 2 and 3), there is a positive correlation between the lipophilicity of the compound and $\mathrm { C M C } . ^ { 6 3 }$ Although the lipophilicity of a drug can be expressed by the octanol/water partition coefficient, the results showed that it cannot fully explain and predict the SE values of compounds within this lipophilicity range. Therefore, in this study, only the $K _ { \mathrm { o w } }$ values of ketoprofen and [Ch][Ket] were determined to be $2 . 5 0 \pm 0 . 0 6$ and $1 . 9 5 \pm 0 . 0 3 ,$ respectively. This result indicates that [Ch][Ket] retains lipophilicity similar to that of the original drug. This means that the IL approach can improve drug solubility while still maintaining its excellent biofilm penetration ability. It is speculated that the $K _ { \mathrm { o w } }$ values of other ILs in this study may be between the two values.

Due to its structural characteristics, the ketoprofen anion forms a relatively weak ion-pair interaction (ΔE) with the choline cation, which dissociates more easily in water, thereby improving solubility (Table 3). Ibuprofen contains an isobutylphenyl group, while ketoprofen contains a benzoyl group. This structural difference gives the salt formed by ibuprofen and choline better water solubility (123.80 ± 0.047 g·100 g−1 , which has been collected by our group). The ionpair interaction formed by the naproxen anion and the choline cation is relatively strong, resulting in a lower degree of dissociation, so the increase in solubility is relatively small.38 Considering the application advantages of ketoprofen42 44 and the degree of solubility improvement of [Ch][Ket], the future application of [Ch][Ket] cannot be ignored.

<!-- image-->  
a. [Ch][Ket] b. [Ben][Ket] c. [Bmim][Ket]  
Figure 4. Cytotoxicities of ketoprofen-based ILs toward L929 cell lines $( n = 3 , \mathbf { x } \pm \mathbf { S D }$ for nonsignificant, \*\*for P < 0.01, \*\*\*\* for $P < 0 . 0 0 0 1 )$

## Evaluation of Cytotoxicity

L929 cells were grown for 48 h under different concentrations of ketoprofen-based IL, and the MTT assay was performed using GraphPad Prism 5.0 to determine the cell viability (Figure 4). Treating L929 cells with the ketoprofen-based IL resulted in a dose-dependent decrease in the level of cell proliferation (Figure 4). The most suitable IC50 values for [Ch][Ket], [Ben][Ket], and [Bmim][Ket] were 857, 598, and 575 μM, respectively. The MTT assay showed that the ketoprofen-based IL at a concentration of 100 μM had no toxicity to L929 cells, that is, the ketoprofen-based IL has no cytotoxicity.38

There are differences in the toxicity of ketoprofen-based ILs, which stem from differences in the toxicity of the cations. Due to the aromaticity of the imidazole ring, imidazolium cations not only damage cell membranes but also more easily undergo π−π stacking interactions with biomolecules (such as enzymes and cell membranes), affecting protein structure and DNA function. Their toxicity is generally higher than that of the aliphatic quaternary ammonium salt cations. Benzalkonium cations have relatively long chain lengths, which make them more likely to insert into the hydrophobic regions of biomembranes, destroy the structure of cell membranes, and cause cell lysis. When a polar hydroxyl group is introduced into the choline cation, its toxicity is significantly reduced. It can be seen that the stronger the aromaticity of the cation and the longer the alkyl chain, the higher the toxicity; the introduction of polar substituents can reduce toxicity.64

## CONCLUSION

Compared with ketoprofen, the thermal stability, solubility, and surface activity of [Ch][Ket] have been significantly improved. According to IC50, all of the ILs investigated have no cytotoxicity. [Ch][Ket] has a larger IC50 value, a smaller octanol−water partition coefficient (Kow) value, and good surface activity. The calculation results of DFT show a correlation with the experimental results, which can provide a reference for an in-depth study of ILs.

The results indicate that designing and preparing waterinsoluble APIs into corresponding drug API-ILs can improve their water solubility. Meanwhile, it can effectively utilize the special properties of ILs to provide the conditions for APIs absorption in the body and then solve the problems existing in the clinical application of poorly soluble drugs. In particular, these preliminary research results can lay a foundation for the application research of ketoprofen ILs (including ketoprofen choline gel and the pharmacokinetics of ketoprofen choline)

## ASSOCIATED CONTENT

## \*sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsomega.5c06480.

1 H NMR of the ketoprofen-based ILs is appended (Figures S1−S3) (PDF)

## AUTHOR INFORMATION

## Corresponding Author

Yimei Tang − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China; orcid.org/0000-0003-3501-8158; Phone: +86 13488136413; Email: tangymhkf@163.com

## Authors

Qian Bai − School of Life Sciences, Key Laboratory of Space Bioscience & Biotechnology, Northwestern Polytechnical University, Xi’an 710072, P. R. China

Tian Tian − College of Materials Science and Engineering, Hebei University of Engineering, Handan, Hebei 056038, P. R. China

Benquan Hu − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Jian Zhang − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Bo Zhang − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Maofang He − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Yuzhen Zhang − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Jinjuan Li − School of Pharmacy, Institute of Medicine, Xi’an Medical University, Xi’an 710021, P. R. China

Complete contact information is available at: https://pubs.acs.org/10.1021/acsomega.5c06480

## Author Contributions

Y.T.: Writing�original draft, investigation, funding acquisition, and conceptualization. Q.B.: Investigation and data curation. T.T.: Data curation and software. B.H.: Writing� review and editing. J.Z.: Investigation and supervision. B.Z.: Formal analysis. M.H.: Investigation. Y.Z.: Investigation. J.L.: Investigation.

Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work was supported by the Special Funds of the National Natural Science Foundation of China (No. 81903579), the Natural Science Basic Research Program of Shaanxi Province (No. 2025JC-YBMS-853), and the Innovation and Entrepreneurship Training Program for College Students in Shaanxi Province (No. S202411840066).

## REFERENCES

(1) Byrn, S. R.; Pfeiffer, R. R.; Stephenson, G.; Grant, W. J. D.; Gleason, W. B. Solid-State Chemistry of Drugs; SSCI: West Lafayette, IN, 1999.

(2) Schuster, D.; Laggner, C.; Langer, T. Why drugs fail-a study on side effects in new chemical entities. Curr. Pharm. Des. 2005, 11, 3545−3549.

(3) Censi, R.; Martino, P. Di. Polymorph impact on the bioavailability and stability of poorly soluble drugs. Molecules 2015, 20, 18759−18776.

(4) Brittain, H. G.; Grant, D. J. R. Effects of polymorphism and solid-state solvation on solubility and dissolution rate. In Poly-

morphism in Pharmaceutical Solids; Taylor and Francis: Abingdon, U.K., 2009; pp 436−480.

(5) Bauer, J.; Spanton, S.; Henry, R.; Quick, J.; Dziki, W.; Porter, W.; Morris, J. Ritonavir: an extraordinary case of conformational polymorphism. Pharm. Res. 2001, 18, 859−866.

(6) Hulme, A. T.; Price, S. L.; Tocher, D. A. A new polymorph of 5- fluorouracil found following computational crystal structure predictions. J. Am. Chem. Soc. 2005, 127, 1116−1117.

(7) Aguiar, A. J.; Krc, J.; Kinkel, A. W.; Samyn, J. C. Effect of polymorphism on the absorption of chloramphenicol from chloramphenicol palmitate. J. Pharm. Sci. 1967, 56, 847−853.

(8) Li, Q.; Cao, J.; Wang, Q.; Zhang, J.; Zhu, S.; Guo, Z.; Zhu, W. H. Nanomized tumor-microenvironment-active NIR fluorescent prodrug for ensuring synchronous occurrences of drug release and fluorescence tracing. J. Mater. Chem. B 2019, 7, 1503−1509.

(9) El-Zhry El-Yafi, A. K.; El-Zein, H. Technical crystallization for application in pharmaceutical material engineering: review article. Asian J. Pharm. Sci. 2015, 10, 283−291.

(10) Madgulkar, A.; Bandivadekar, M.; Shid, T.; Rao, S. Sugars as solid dispersion carrier to improve solubility and dissolution of the BCS class II drug: clotrimazole. Drug Dev. Ind. Pharm. 2016, 42, 28− 38.

(11) Okada, K.; Hirai, D.; Hayashi, Y.; Kumada, S.; Kosugi, A.; Onuki, Y. A novel approach to evaluate amorphous-to-crystalline transformation of active pharmaceutical ingredients in solid dispersion using time-domain NMR. Chem. Pharm. Bull. 2019, 67, 265−270.

(12) Poovi, G.; Damodharan, N. Lipid nanoparticles: a challenging approach for oraldelivery of BCS Class-II drugs. Future J. Pharm. Sci. 2018, 4, 191−205.

(13) Zhang, D.; Xu, Q.; Wang, N.; Yang, Y.; Liu, J.; Yu, G.; Yang, X.; Xu, H.; Wang, H. A complex micellar system co-delivering curcumin with doxorubicin againstcardiotoxicity and tumor growth. Int. J. Nanomedicine 2018, 13, 4549−4561.

(14) Park, S. H.; Choi, H. K. The effects of surfactants on the dissolution profiles of poorly water-soluble acidic drugs. Int. J. Pharm. 2006, 321, 35−41.

(15) Kumar, A.; Davern, P.; Hodnett, B. K.; Hudson, S. P. Carrier particle mediatedstabilization and isolation of valsartan nanoparticles. Colloids Surf., B 2019, 175, 554−563.

(16) Wang, Y.; Liu, J.; Yuan, X.; Wang, M.; Nie, Y.; Zhang, S.; He, H. Y. Ionic liquid-based aggregation towards the mesoscale mechanism and their applications. Chem. Eng. J. 2023, 455, No. 140370.

(17) Yin, J.; Fu, W. D.; Zhang, J. R.; Zhang, X. M.; Qiu, W. X.; Jiang, W.; Zhu, L. H.; Li, H. P.; Li, H. M. Bifunctional pyridinium-based Brønsted acidic porous ionic liquid for deep oxidative desulfurization. Chem. Eng. J. 2024, 492, No. 152349.

(18) Hough, W. L.; Smiglak, M.; Rodriguez, H.; Swatloski, R. P.; Spear, S. K.; Daly, D. T.; Pernak, J.; Grisel, J. E.; Carliss, R. D.; Soutullo, M. D.; Davis, J. H., Jr.; Rogers, R. D. The third evolution of ionic liquids: active pharmaceutical ingredients. New J. Chem. 2007, 31, 1429−1436.

(19) Hough, W. L.; Rogers, R. D. Ionic liquids then and now: From solvents to materials to active pharmaceutical ingredients. Bull. Chem. Soc. Jpn. 2007, 80, 2262−2269.

(20) Egorova, K. S.; Gordeev, E. G.; Ananikov, V. P. Biological activity of ionic liquids and their application in pharmaceutics and medicine. Chem. Rev. 2017, 117, 7132−7189.

(21) Florindo, C.; Pereiro, A. B.; Vieira, N. S. M.; Matias, A. A.; Duarte, C. M. M.; Rebelo, P. N.; Marrucho, I. M. Cholinium-based ionic liquids with pharmaceutically active anions. RSC Adv. 2014, 4, 28126−28132.

(22) Sahbaz, Y.; Williams, H. D.; Nguyen, T.; Saunders, J.; Ford, L.; Charman, S. A.; Scammells, P. J.; Porter, C. J. H. Transformation of Poorly Water-Soluble Drugs into Lipophilic Ionic Liquids Enhances Oral Drug Exposure from Lipid Based Formulations. Mol. Pharmaceutics 2015, 12, 1980−1991.

(23) Viciosa, M. T.; Santos, G.; Costa, A.; et al. Dipolar motions and ionic conduction in an ibuprofen derived ionic liquid. Phys. Chem. Chem. Phys. 2015, 17, 24108−24120.

(24) Ferraz, R.; Branco, L. C.; Marrucho, I. M.; Araujo, J. M. M.; Rebelo, L. P. N.; da Ponte, M. N.; Prudencio, ̂ C.; Noronha, J. P.; Petrovski, Z. Development of novel ionic liquids based on ampicillin. Med. Chem. Commun. 2012, 3, 494−497.

(25) Florindo, C.; Araujo, ́ J. M.; Alves, F.; Matos, C.; Ferraz, R.; Prudencio, ̂ C.; Marrucho, I. M.; et al. Evaluation of solubility and partition properties of ampicillin-based ionic liquids. Int. J. Pharm. 2013, 456, 553−559.

(26) Berton, P.; Di Bona, K. R.; Yancey, D.; Rizvi, S. A. A.; Gray, M.; Gurau, G.; Shamshina, J. L.; Rasco, J. F.; Rogers, R. D. Transdermal bioavailability in rats of lidocaine in the forms of ionic liquids, salts, and deep eutectic. ACS Med. Chem. Lett. 2017, 8, 498−503.

(27) Johansson, K. M.; Izgorodina, E. I.; Forsyth, M.; Macfarlane, D. R.; Seddon, K. R. Protic ionic liquids based on the dimeric and oligomeric anions AcO)(x) H(x-)](−). Phys. Chem. Chem. Phys. 2008, 10, 2972−2978.

(28) Bica, K.; Rogers, R. D. Confused ionic liquid ions�a ″liquification″ and dosage strategy for pharmaceutically active salts. Chem. Commun. 2010, 46, 1215−1217.

(29) Stoimenovski, J.; Dean, P. M.; Izgorodina, E. I.; Macfarlane, D. R. Protic pharmaceutical ionic liquids and solids: aspects of protonics. Faraday Discuss. 2012, 154, 335−352.

(30) Davis, J. H.; Forrester, K. J.; Merrigan, T. Novel organic ionic liquids (OILs) incorporating cations derived from the antifungal drug miconazole. Tetrahedron Lett. 1998, 39, 8955−8958.

(31) Zhang, Y.; Liu, C.; Wang, J. Q.; Ren, S. J.; Song, Y. L.; Quan, P.; Fang, L. Ionic liquids in transdermal drug delivery system: Current applications and future perspectives. Chin. Chem. Lett. 2023, 34, No. 107631.

(32) Hough, W. L.; Rogers, R. D. Ionic liquids then and now: From solvents to materials to active pharmaceutical ingredients. Bull. Chem. Soc. Jpn. 2007, 80, 2262−2269.

(33) Świątek, E.; Ossowicz-rupniewska, P.; Janus, E.; Nowak, A.; Sobolewski, P.; Duchnik, W.; Kucharski, L.; Klimowicz, A. Novel naproxen salts with increased skin permeability. Pharmaceutics 2021, 13, No. 2110.

(34) Pedro, S. N.; Freire, C. S. R.; Silvestre, A. J. D.; Freire, M. G. The role of ionic liquids in the pharmaceutical field: An overview of relevant applications. Int. J. Mol. Sci. 2020, 21, 8298−8348.

(35) Wongrakpanich, S.; Wongrakpanich, A.; Melhado, K.; Rangaswami, J. A comprehensive review of non-steroidal antiinflammatory drug use in the elderly. Aging Dis. 2018, 9, 143−150.

(36) Świątek, E.; Ossowicz-Rupniewska, P.; Janus, E.; Nowak, A.; Sobolewski, P.; Duchnik, W.; Kucharski, L.; Klimowicz, A. Novel naproxen salts with increased skin permeability. Pharmaceutics 2021, 13, No. 2110.

(37) Ossowicz, P.; Janus, E.; Klebeko, J.; Swiatek, E.; Kardaleva, P.; Taneva, S.; Krachmarova, E.; Rangelov, M.; Todorova, N.; Guncheva, M. Modulation of the binding affinity of naproxen to bovine serum albumin by conversion of the drug into amino acid ester salts. J. Mol. Liq. 2020, 319, No. 114283.

(38) Tang, Y. M.; Yang, K.; Zhao, S. Y.; Chen, Q. Q.; Qin, L.; Qin, B. Evaluation of solubility, physicochemical properties, and cytotoxicity of naproxen-based ionic liquids. ACS Omega 2023, 8, 8332−8340.

(39) Frizzo, C. P.; Wust, K.; Tier, A. Z.; Vaucher, R. A.; Bolzan, L. P.; Terra, S.; Martins, M. A. P.; et al. Novel ibuprofenate and docusate-based ionic liquids: Emergence of antimicrobial activity. RSC Adv. 2016, 6, 100476−100486.

(40) Fernandez-Stefanuto, V.; Tojo, E. In New Active Pharmaceutical Ingredient-Ionic Liquids (API-ILs) Derived from Indomethacin and Mebendazole, 22nd International Electronic Conference on Synthetic Organic Chemistry; MDPI, 2018; p 48.

(41) Sarzi-Puttini, P.; Atzeni, F.; Lanata, L.; Bagnasco, M. Efficacy of ketoprofen vs ibuprofen and diclofenac: a systematic review of the

literature and meta-analysis. Clin. Exp. Rheumatol. 2013, 31 (5), 731− 738.

(42) Komatsu, T.; Sakurada, T. Comparison of the efficacy and skin permeability of topical NSAID preparations used in Europe. Eur. J. Pharm. Sci. 2012, 47 (5), 890−895.

(43) Cordero, J. A.; Alarcon, L.; Escribano, E.; Obach, R.; Domenech, J. A comparative study of the transdermal penetration of a series of nonsteroidal antiinflammatory drugs. J. Pharm. Sci. 1997, 86 (4), 503−508.

(44) Bock, U.; Krause, W.; Otto, J.; Haltner, E. Comparative in vitro and in vivo studies on the permeation and penetration of ketoprofen and ibuprofen in human skin. Arzneimittel Forschung/Drug Res. 2004, 54 (9), 522−529.

(45) Kardaleva, P.; Guncheva, M.; Todinova, S.; Angelov, I.; Ossowicz, P.; Janus, E. Effect of ketoprofen-based ionic liquids on secondary structure and thermal stability of human serum albumin. J. Therm. Anal. Calorim. 2020, 142 (5), 1911−1917.

(46) Ossowicz, P.; Kardaleva, P.; Guncheva, M.; Klebeko, J.; Swiatek, E.; Janus, E.; Yancheva, D.; Angelov, I. Ketoprofen-based ionic liquids: synthesis and interactions with bovine serum albumin. Molecules 2020, 25 (1), No. 90.

(47) Hassan, S. A.; Gad, S. F.; Abdu-Allah, H. H. M.; Qayed, W. S.; AbouElmagd, S. A.; Ibrahim, E. A. Ionic liquid of ketoprofen-piperine modulates the pharmaceutical and therapeutic characters of ketoprofen. Int. J. Pharm. 2022, 620, No. 121724.

(48) Umerska, A.; Zotova, J.; Tajber, L. Formation of low melting point binary systems comprising ketoprofen and an amide local anaesthetic. Int. J. Pharm. 2021, 607, No. 120969.

(49) Yang, D. G.; Fang, L.; Yang, C. R. Roles of molecular interaction and mobility on loading capacity and release rate of drugionic liquid in long-acting controlled release transdermal patch. J. Mol. Liq. 2022, 352, No. 118752.

(50) Lu, T. Molclus Program, Version 1.9.9.9; http://www.keinsci. com/research/molclus.html. (accessed 08, 03, 2022).

(51) Bannwarth, C.; Ehlert, S.; Grimme, S. GFN2‑xTB an accurate and broadly parametrized self-consistent tight-binding quantum chemical method with multipole electrostatics and density-dependent dispersion dontributions. J. Chem. Theory Comput. 2019, 15, 1652− 1671.

(52) Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.et al. Gaussian16, Revision A.01; Gaussian, Inc.: Wallingford CT, 2016.

(53) Stephens, P. J.; Devlin, F. J.; Chabalowski, C. F.; Frisch, M. J. Ab initio calculation of vibrational absorption and circular dichroism spectra using density functional force fields. J. Phys. Chem. A 1994, 98, 11623−11627.

(54) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J. Chem. Phys. 2010, 132, No. 154104.

(55) Zheng, J.; Xu, X.; Truhlar, D. G. Minimally augmented Karlsruhe basis sets. Theor. Chem. Acc. 2011, 128 (3), 295−305.

(56) Weigend, F. Accurate coulomb-fitting basis sets for H to Rn. Phys. Chem. Chem. Phys. 2006, 8 (9), 1057−1065.

(57) Xu, C.; Cheng, Z. Thermal stability of ionic liquids: current status and prospects for future development. Processes 2021, 9 (2), No. 337.

(58) Tsuzuki, S.; Tokuda, H.; Hayamizu, K.; Watanabe, M. Magnitude and directionality of interaction in ion pairs of ionic liquids: relationship with ionic conductivity. J. Phys. Chem. B 2005, 109 (24), 11933−11939.

(59) Zhao, X. Y.; Pan, Y.; Jiang, J. C.; Xu, S. Y.; Jiang, J. J.; Ding, L. Thermal hazard of ionic liquids: modeling thermal decomposition temperatures of imidazolium ionic liquids via QSPR method. Ind. Eng. Chem. Res. 2017, 56 (24), 4185−4195.

(60) Shmukler, L. E.; Fedorova, I.; Fadeeva, Y. A.; Gruzdev, M. S.; Safonova, L. P. Alkylimidazolium Protic ionic liquids: structural features and physicochemical properties. ChemPhysChem 2022, 23 (4), No. e202100772.

(61) Wasserscheid, P. Ionic Liquids in Synthesis.; Wiley-VCH: Weinheim, c2003.

(62) Samet, M.; Wang, X. B.; Kass, S. R. A. preorganized pydrogen bond network and its effect on anion stability. J. Phys. Chem. A 2014, 118 (31), 5989−5993.

(63) Ottaviani, G.; Wendelspiess, S.; Alvarez-Sánchez, R. Importance of critical micellar concentration for the prediction of solubility enhancement in biorelevant media. Mol. Pharmaceutics 2015, 12, 1171−1179.

(64) Kuroda, K. A simple overview of toxicity of ionic liquids and designs of biocompatible ionic liquids. New J. Chem. 2022, 46 (42), 20047−20052.