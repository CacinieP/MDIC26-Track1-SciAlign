ORIGINAL ARTICLE

Open Access

# Natural monoterpenoid geraniol promotes antioxidant defense and stress tolerance via SKN-1/Nrf2 activation in Caenorhabditis elegans

<!-- image-->

Stéfano Romussi1,2, Ailin Lacour1,2, Diego Rayes1,2\* and María José De Rosa1,2\*

## Abstract

Oxidative stress (OS) is a major contributor to aging and the pathogenesis of numerous conditions, including diabetes, neurodegenerative, cardiovascular, and autoimmune disorders. Consequently, therapeutic strategies aimed at enhancing endogenous cytoprotective pathways have gained signifcant interest. Plant-derived essential oils represent attractive sources for such interventions due to their natural origin and low toxicity; specifcally, the monoterpenoid geraniol, a principal component of rose oil, has demonstrated promising antioxidant properties in vitro. In this study, we utilized Caenorhabditis elegans to investigate the in vivo efcacy and molecular mechanisms of geraniol efect. Our results show that geraniol signifcantly reduces intracellular reactive oxygen species and enhances resistance to acute OS induced by juglone. Mechanistic characterization using GFP-reporter strains revealed that geraniol activates the DAF-16/FOXO and SKN-1/Nrf2 transcription factors, while surprisingly causing a slight but consistent downregulation of the HSF-1-mediated heat-shock response. Crucially, genetic epistasis analysis using null/hypomorphic mutants demonstrated that only SKN-1 is strictly essential for geraniol-mediated protection against induced OS. In conclusion, this study underscores the utility of C. elegans as a robust and accessible platform for the pharmacological screening of natural products. Our fndings establish geraniol, a key constituent of rose oil, as a multifunctional modulator of cellular defenses that orchestrates multiple cytoprotective pathways, identifying the SKN-1-dependent response as a critical driver of its antioxidant efcacy in C. elegans. By delineating this specifc genetic requirement, these results provide a mechanistic foundation that supports the therapeutic potential of geraniol in mitigating aging and pathophysiology driven by OS.

Keywords Caenorhabditis elegans, Antioxidant, Essential oil, Cytoprotective mechanism, Oxidative stress

<!-- image-->

## 1 Introduction

Oxidative stress (OS), arising from an imbalance in redox homeostasis, is a major contributing factor in aging and the pathogenesis of a broad spectrum of diseases ranging from neurodegenerative disorders (such as Alzheimer’s and Parkinson’s diseases) and cardiovascular ailments to diabetes and autoimmune pathologies like rheumatoid arthritis [1–3]. OS is characterized by the excessive accumulation of reactive oxygen species (ROS), which infict damage on cellular components and drive chronic infammation [4, 5]. To deal with ROS accumulation, organisms activate endogenous cytoprotective pathways designed to neutralize them and mitigate cellular injury. Terefore, a central therapeutic strategy for modulating aging and disease risk involves enhancing these antioxidant defenses—either by directly inactivating ROS through scavenger molecules or by pharmacologically inducing these intrinsic protective mechanisms [6].

Plant-derived essential oils are natural compounds extracted from various parts of plants, including fowers, leaves, stems, and roots. Tese oils are typically composed of a diverse array of molecules, including terpenoids, phenylpropenes, terpenes, ketones, aldehydes, esters, and phenols [7]. Many of them have gained recognition for their antioxidant properties [8]. Herbal compounds, such as those found in essential oils, are increasingly being explored as potential alternatives to synthetic drugs, owing to their widespread consumption through dietary inclusion and their relatively low toxicity. Despite their potential, the complexity of plant essential oils has made it challenging to isolate specifc bioactive components, hindering a full understanding of their molecular mechanisms and delaying their clinical application.

Geraniol, an acyclic monoterpenoid and a principal component of essential oils from plants such as rose, lemon, and ginger [9], presents a compelling candidate for therapeutic investigation. Beyond its widespread use as a fragrance in cosmetics and household products, geraniol is characterized by low toxicity and favorable bioavailability [10]. Notably, both in  vitro and in  vivo studies have demonstrated promising pharmacological properties, including antioxidant, cytoprotective, and anticancer efects [10, 11]. Tese fndings underscore its potential as a bioactive molecule for intervention in diseases where such mechanisms are relevant. Despite this potential, the specifc cellular and molecular pathways through which geraniol exerts its cytoprotective efects have yet to be fully elucidated.

Te nematode Caenorhabditis elegans has become a powerful model organism in biomedical research, owing to its short lifespan, genetic tractability, and anatomical simplicity, which collectively facilitate the study of fundamental biological processes and disease mechanisms [12, 13]. Its transparency allows for real-time visualization of cellular and molecular events using fuorescent reporters and biosensors [14, 15]. Notably, research in C. elegans has been instrumental in identifying conserved genetic pathways that regulate OS resistance, autophagy, and longevity [16, 17]. A cornerstone fnding in this model is the DAF-2/insulin/IGF-1 signaling (IIS) pathway, a universal key regulator of lifespan and proteostasis [18]. Te IIS pathway converges on key cytoprotective transcription factors, including DAF-16, the C. elegans ortholog of mammalian FOXO; SKN-1, the ortholog of mammalian Nrf1/Nrf2; and HSF-1, the ortholog of mammalian HSF. Teir activation can ameliorate phenotypic defcits in various C. elegans disease models [12, 19–24]. Consequently, C. elegans has become a powerful platform for screening and characterizing genes, drug targets, and compounds with therapeutic potential [25, 26].

In this study, we employed the animal model C. elegans model to investigate the in  vivo antioxidant capacity of the plant-derived compound geraniol and elucidate its underlying molecular mechanisms. Using genetic and transgenic approaches, we demonstrate that geraniol signifcantly reduces intracellular ROS and enhances resistance to induced OS. We found that exposure to geraniol activates two key cytoprotective transcription factors, DAF-16/FOXO and SKN-1/Nrf2. In contrast, it slightly inhibits the activity of the HSF-1 transcription factor. Interestingly, genetic analysis using null/hypomorphic mutants reveals that the antioxidant efect is dependent specifcally on SKN-1, indicating that this pathway is key for geraniol-mediated resistance. Collectively, our fndings establish geraniol as a potent activator of endogenous antioxidant defenses in  vivo, acting primarily through the SKN-1/Nrf2 axis, and highlight its potential as a therapeutic candidate for diseases driven by OS.

## 2 Results

## 2.1 Geraniol reduces oxidative stress under basal conditions and upon exogenous challenge

Given that several essential oils have demonstrated anthelmintic properties, and because Caenorhabditis elegans is a free-living, non-parasitic nematode, we frst performed a dose–response assay (0.2–2  mM) to identify non-toxic concentrations of geraniol for subsequent experiments. To measure potential toxicity, we quantifed locomotor activity at a single time point (165 min) using a WMicrotracker, which allows automated quantifcation of activity in large populations [27]. Continuous exposure from eggs to adult day 1 (AD1) to geraniol concentrations up to 2 mM did not signifcantly alter locomotor activity, indicating an absence of toxicity or locomotor stimulation at these doses (Fig.  1a). Based on these results, we selected 1 mM as an intermediate working concentration for further analyses.

To assess the potential antioxidant properties of geraniol, we frst measured whether chronic exposure to the compound, in the absence of any external stressor, could alter the baseline ROS levels in  vivo. Real-time measurements of $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ were obtained using the genetically encoded HyPer sensor, expressed in established transgenic reporter strains. HyPer is a highly specifc $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 }$ biosensor whose fuorescence properties change upon oxidation [28, 29]. We measured fuorescence using excitation flters of 488 nm for the oxidized state and 400 nm for the reduced state.

As shown in Fig. 1b, animals treated with geraniol from eggs to the L4 stage exhibited a signifcant reduction in basal ROS levels, reaching around 66% of those of control animals (66.09% ± 19.54 compared to control animals). Tis result demonstrates that geraniol possesses intrinsic antioxidant activity in vivo under standard physiological conditions.

To further assess geraniol’s protective efects under exogenous oxidative challenge, we used two experimental approaches. First, using transgenic HyPer animals, we monitored ROS levels after a 20 min exposure to juglone (200 µM) in animals pre-treated with either 1 mM geraniol or vehicle (DMSO) (Fig. 2a). Second, using wild-type animals, we assessed locomotor activity as a proxy for survival over a 20h period following the same pre-treatment and juglone challenge (Fig. 2b).

Juglone induced a marked increase in ROS in untreated animals (around 90% above baseline). In contrast, geraniol-treated animals showed a signifcantly smaller increase (only around 40% above their own baseline) (Additional fle  1: Fig. S1 and S2a). Moreover, while juglone-treated animals gradually lost activity and ultimately died, geraniol-pretreated animals displayed substantially improved survival. Te time to reach 50% activity loss (T50) was 7.06  h (95%CI 6,48–7,63) for untreated animals and 15.30  h (95%CI 13,88–16,59) for geraniol-treated animals (Fig. 2b).

a  
<!-- image-->

<!-- image-->

<!-- image-->  
Fig. 1 Efect of geraniol in wild-type C. elegans. a Locomotion of adult day 1 wild-type animals in the absence of geraniol (control, bars with black lineouts) or in the presence of diferent geraniol concentrations (0.2, 0.3, 0.5, 1.0 and 2.0 mM, bars with grey lineouts), assessed using the WMicrotracker. The graph shows locomotion (in Arbitrary Units (AU)) measured at minute 165 (15-min acquisition interval). The experiment was performed in 3 independent replicates, each including 6–8 wells (approximately 50 worms per well). Statistical signifcance was determined using one-way ANOVA followed by Holm–Sidak’s post hoc test for multiple comparisons against the control group, and no signifcant diferences (ns) were detected. b ROS levels were measured in L4-stage animals previously exposed to DMSO (control condition) or 1 mM geraniol. Left: In vivo microphotographs of JV1 (Hyper) animals using excitation flters at 488 nm (green emission) and 400 nm (blue emission). Right: Intracellular ROS production is expressed as the oxidized/reduced HyPer ratio (green/blue) relative to the control condition. The experiment was performed in 3 independent replicates, each including 10–12 worms. Statistical signifcance was assessed using the Mann–Whitney test (\*\*\*\*) p < 0.0001. Data are presented as mean ± SEM

a  
<!-- image-->

<!-- image-->  
b

<!-- image-->

<!-- image-->  
Fig. 2 Geraniol confers protection against oxidative stress. a ROS levels were measured in L4-stage animals previously exposed to DMSO (control condition) or 1 mM geraniol. Left: In vivo microphotographs of JV1 (Hyper) animals under mild xenobiotic stress (juglone 200 µM, 20 min). Right: Intracellular ROS production is expressed as the oxidized/reduced HyPer ratio (green/blue) relative to control under basal condition. The dashed line indicates the mean of the control under basal conditions. The experiment was performed in 3 independent replicates, each including 10–12 worms. Statistical signifcance was assessed using the Mann–Whitney test (\*\*\*\*) p < 0.0001. Data are presented as mean ± SEM. b Animal locomotion in the presence of the oxidizing agent juglone (240 μM). The experiments were performed on aged-synchronized animals (adult day 1 stage) exposed to 1 mM geraniol (grey line) or DMSO (black line) throughout development. The experiment was repeated at least 3 independent times using 8–12 wells (approximately 50 worms per well). Data are presented as mean locomotor activity normalized to the frst hour of the control condition ± SEM. T50 values were compared using a t-test (\*\*\*\*) p < 0,0001

Together, these fndings indicate that geraniol not only lowers basal OS but also confers signifcant protection against severe, chemically induced oxidative damage.

## 2.2 Geraniol robustly activates SKN‑1/Nrf2 and enhances DAF‑16/FOXO stress signaling

Given that geraniol modulates OS in  vivo, we used C. elegans to investigate the underlying molecular mechanisms. Dietary restriction is known to increase stress resistance and lifespan, and typically manifests as reduced lipid accumulation [17, 30, 31]. We therefore wondered whether geraniol might elicit a dietary restriction-like efect. Oil-Red O lipid staining of AD1-stage worms, however, revealed no signifcant diferences in lipid content between geraniol-treated and control animals, ruling out dietary restriction as the primary mechanism of geraniol’s protective efects (Fig. 3a).

Next, we explored plausible intracellular mechanisms that could explain geraniol-mediated OS protection. To this end, we focused on the cytoprotective activity of transcription factors (TFs) that act downstream of the highly conserved DAF-2/IIS such as DAF-16/FOXO, SKN-1/Nrf-2, and HSF-1/HSF1 [32]. Tese TFs activate a genetic program that ultimately modulate scavenging mechanisms for free radicals and oxidative metabolites and confer enhanced stress resistance and longevity [12, 33]

We further examined the activation of these key cytoprotective TFs, using transgenic reporter strains to assess the expression of their canonical downstream targets.

We frst evaluated HSF-1 activity by measuring the expression of hsp‑70, a canonical transcriptional target and well-established efector of this pathway [34]. Surprisingly, geraniol treatment resulted in a moderate but signifcant downregulation of hsp‑70 expression under basal conditions (Fig.  3b). Tis indicates that geraniol does not activate the HSF-1 pathway and may, in fact, exert a mild suppressive efect on its basal activity.

In contrast, geraniol exposure strongly induced the expression of glutathione S-transferase 4 (GST-4), a direct transcriptional target of SKN-1, nearly doubling its expression compared to control animals. Tis result demonstrates that geraniol robustly activates the SKN-1/Nrf2 pathway under basal conditions (Fig. 3c).

To assess DAF-16 activity, we frst examined the expression of its target gene, superoxide dismutase 3 (SOD-3). Under basal conditions, geraniol induced a modest but detectable increase in SOD-3 expression, suggesting DAF-16 activation (Fig.  3d). To further confrm this, we used a strain expressing a translational reporter (Pdaf‑16::DAF‑16::GFP) to visualize DAF-16 nuclear translocation, a hallmark of its activation. Although nuclear localization of DAF-16 is generally low under basal conditions (consistent with previous reports [35, 36]), we observed enhanced activation of DAF-16 following a mild oxidative stimulus (juglone 200 μM for 10 min). Geraniol-treated animals exhibited a signifcantly greater increase in DAF-16 nuclear translocation compared to controls (Fig. 3e). Tis indicates that geraniol not only activates DAF-16 under basal conditions (as shown by increased SOD-3 expression), but also potentiates its nuclear translocation in response to OS.

Together, these results establish geraniol as a multimodal modulator that diferentially tunes cellular defense programs: it drives constitutive activation of SKN-1/ Nrf2, exerts a context-dependent modulation of DAF-16/FOXO activity that is amplifed under OS, and subtly attenuates the HSF-1/HSP-70 pathway.

## 2.3 SKN‑1/Nrf2 is essential for geraniol‑mediated oxidative stress resistance

To determine which of the transcription factors modulated by geraniol are relevant for its protective efect against OS, we performed a genetic epistasis analysis using mutant C. elegans strains. We frst evaluated survival under lethal juglone-induced OS in strains lacking functional DAF-16/FOXO or SKN-1/Nrf2. skn-1 mutants showed a \~ 57% reduction in locomotor activity—used here as a proxy for viability—compared to wild-type animals, as quantifed by the area under the activity curve (AUC: 487±187 AU for skn-1 mutants vs. 1123±349 AU for wild-type animals; Additional fle 1: Fig. S2). Tis marked decline confrms their heightened sensitivity to OS. In contrast, daf-16 mutants displayed survival profles comparable to wild-type animals (AUC of 1018 ± 278 AU). Interestingly, hypomorphic hsf-1 mutants were unexpectedly resistant to juglone (AUC of 1657 ± 351 AU, Additional fle  1: Fig. S2), consistent with previous reports of age-dependent resistance in this strain [37]. Given that geraniol treatment actually downregulated the HSF-1 target hsp‑70, and considering the complex, potentially confounding resistance of the hsf‑1 mutant itself, we excluded this strain from further mechanistic analysis. Tis decision focuses our investigation on the pathways that geraniol robustly activates.

We next asked whether geraniol could still protect these mutants from juglone-induced OS. Animals were pretreated with 1  mM geraniol or vehicle (DMSO) and then exposed to juglone. Geraniol signifcantly improved survival in daf-16 mutants to an extent comparable to that in wild-type animals (Fig.  4a and b), indicating that DAF-16 is not essential for geraniol-mediated protection. In contrast, the protective efect of geraniol was signifcantly reduced in skn-1 mutants (Fig.  4c and d), which remained highly sensitive to juglone.

Together, these results demonstrate that SKN-1/Nrf2 is key for geraniol’s antioxidant protection against OS, while DAF-16/FOXO—although activated by geraniol— is dispensable in this context.

a  
<!-- image-->

<!-- image-->

b  
<!-- image-->

<!-- image-->

c  
<!-- image-->

<!-- image-->  
d

sod-3::GFP  
<!-- image-->

e  
<!-- image-->

DAF-16::GFP  
<!-- image-->

<!-- image-->  
Fig. 3 Geraniol activates multiple cytoprotective mechanisms. a Left: Representative images of adult day 1 control and geraniol-treated animals after Oil-Red O staining. The circled ROIs indicate the areas in which lipid staining intensity was evaluated. Scale bar, 25 μm. Right: Quantifcation of relative lipid staining intensity. Black open circles: DMSO-treated animals and grey open circles: geraniol-treated animals. b Left: Expression of hsp-70 was determined using the BC10060 dpy-5(e907) I; sEx884 [rCesC12C8.1::GFP + pCeh361] strain. Representative images of control (DMSO) and geraniol-treated animals. Scale bar, 50 μm. Right: Relative hsp-70::GFP fuorescence quantifcation in adult day 1 animals. Brown open circles: DMSO-treated animals and orange open circles: geraniol-treated animals. c Left: Representative images of adult day 1 control (DMSO) and geraniol-treated animals using CL2166 dvIs19 [(pAF15)gst-4p::GFP::NLS] III strain. Scale bar, 100 μm. Right: Quantifcation of $g S t { - } 4 { : = } G F P$ expression in adult day 1 animals relative to the control condition. Purple open circles: DMSO-treated animals and pink open circles: geraniol-treated animals. d Left: Representative images of the head region of CF1553 muIs84 [(pAD76) sod-3p::GFP + rol-6]. Scale bar, 25 μm. Right: Quantifcation of sod-3::GFP expression in adult day 1 animals in the pharyngeal region, expressed relative to the control condition. e Left: Representative images of adult day 1 animals control (DMSO) or geraniol-treated animals using TJ356 zIs356 [daf-16p::daf-16a/b::GFP + rol-6(su1006)] strain. Scale bar, 50 μm. Right: Nuclear DAF-16 quantifcation relative to control condition. For d and e: Dark green open circles: DMSO-treated animals and light green open circles: geraniol-treated animals. For a–e The experiment was performed in at least 3 independent replicates, each including 10–12 worms. Quantifcation graphs show the mean value. Statistical signifcance was assessed using the Mann–Whitney test, (ns: no signifcant diferences, $p > 0 . 0 5 ; \left( ^ { * } \right) p < 0 . 0 5$ $( ^ { * * } ) p < 0 . 0 1 ; ( ^ { * * * } ) p < 0 . 0 0 0 1 )$

a  
<!-- image-->

<!-- image-->  
b

<!-- image-->

C  
<!-- image-->

<!-- image-->  
d

<!-- image-->  
Fig. 4 Geraniol protection against OS involves SKN-1. a–d Animal locomotion at the adult day 1 stage in the presence of the oxidizing agent juglone (240 μM). Animals were exposed throughout development to 1 mM geraniol (light colors) or vehicle (DMSO, dark colors). Results are presented as mean locomotor activity (AU) normalized to hour 1 of the control condition for each strain. a Wild-type (left, black line) and daf-16 null (right, green line) animals. b Relative T50 comparison for both wild-type and daf-16 mutants. c Wild-type (left, black line) and skn-1 hypomorphic (right, purple line) animals. d Relative T50 comparison for both wild-type and skn-1 mutants. For a-d.The experiment was performed in 6 independent replicates, each including 8–12 wells (approximately 50 worms per well). Statistical signifcance was determined using Student’s t-test (ns p > 0.05, \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001, \*\*\*\*p < 0.0001)

## 2.4 In silico pharmacokinetic profling predicts favorable drug‑like properties and bioavailability, supporting translational potential

Our genetic and phenotypic results in C. elegans establish geraniol as a potent activator of the conserved SKN-1/ Nrf2 pathway, conferring signifcant resistance to OS. While invertebrate models provide powerful insights into molecular mechanisms, translation to therapeutic potential in mammals requires evaluation of a compound’s pharmacokinetic profle—encompassing absorption, distribution, metabolism, and excretion (ADME). Tese properties determine whether a bioactive molecule can reach target tissues at efective concentrations in vivo and are critical predictors of clinical success. To bridge this translational gap and assess geraniol’s viability as a lead compound, we performed comprehensive in silico ADME profling using the SwissADME platform, a validated tool for predicting drug-likeness and bioavailability.

Te software analysis showed that geraniol has a bioavailability score greater than zero, indicating that its physicochemical and pharmacokinetic profle is comparable to those of orally administered drugs with established clinical efcacy. Te analysis predicted high gastrointestinal absorption, suggesting efcient uptake after oral administration. Importantly, the model also predicted signifcant blood–brain barrier permeability (Fig.  5b and c), highlighting geraniol’s potential to exert protective efects within the central nervous system—a relevant feature for neurodegenerative conditions associated with OS.

Furthermore, examination of the oral bioavailability radar—which evaluates six fundamental physicochemical properties—revealed that geraniol’s profle for lipophilicity, molecular size, polarity, solubility, fexibility, and saturation falls entirely within the optimal range defned for drug-like compounds (Fig.  5). Tese computational predictions collectively suggest that geraniol possesses favorable ADME characteristics, including metabolic stability and efcient membrane permeation. Tis analysis supports the notion that geraniol is not only bioactive in a model organism but also embodies key molecular properties necessary for further pharmacological development. Tus, our fndings provide a strong rationale for advancing geraniol into preclinical mammalian studies aimed at mitigating OS-related pathologies.

<!-- image-->

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Bioavalabilityscore</td><td rowspan=1 colspan=1>GIabsortion</td><td rowspan=1 colspan=1>BBBpermeant</td><td rowspan=1 colspan=1>Lipinski</td><td rowspan=1 colspan=1>Ghose</td><td rowspan=1 colspan=1>RulesVeber</td><td rowspan=1 colspan=1>Egan</td><td rowspan=1 colspan=1>Muegge</td></tr><tr><td rowspan=1 colspan=1>Geraniol</td><td rowspan=1 colspan=1>0.55</td><td rowspan=1 colspan=1>High</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr></table>

Fig. 5 Predicted drug-likeness profle of geraniol using SwissADME. a Left: Chemical structure of geraniol. Right: Oral viability radar summarizes six key physicochemical properties—lipophilicity, molecular size, polarity, solubility, saturation, and fexibility—that collectively predict the likelihood of oral bioavailability. Geraniol falls within the optimal range for all these parameters (colored in pink), indicating favorable oral bioavailability. b BOILED-Egg (Brain Or Intestinal Estimated permeation predictive model) for geraniol. Geraniol (red point) falls within the yellow (Blood– Brain-Barrier: BBB) region, indicating a high probability of passive BBB permeation and human intestinal absorption (HIA). Geraniol is also predicted to be P-glycoprotein–negative (PGP −), suggesting it is not subject to efux transport. WLOGP (y-axis) represents lipophilicity, and TPSA (x-axis) represents topological polar surface area. c Drug-likeness parameters of geraniol. Predictions were obtained after introducing SMILES structures in the SwissADME web server. Bioavailability score, Gastrointestinal (GI) adsorption and the Lipinski’s, Ghose’s, Veber’s, Egan’s and Muegge’s rules defne the drug-likeness score for each compound

## 3 Discussion

Although plant extracts with antioxidant activity have shown promise in preclinical models, their clinical translation has often been disappointing. Tis is partly due to the inherent complexity of such extracts, whose composition varies with extraction methods, environmental factors, and plant physiology. Terefore, studying purifed constituents is crucial to identify the active molecules, defne their mechanisms of action, and establish the pharmacological basis needed for clinical development.

In this work, we focused on geraniol, a terpene found in more than 250 essential oils [10, 38]. Geraniol is widely recognized for its diverse biological properties, including antimicrobial [39, 40], insect-repellent [41], and anthelmintic activities [42]. Additional reports indicate that geraniol displays a wide array of biological activities [43], including in vitro antioxidant efects. Its favorable pharmacokinetic properties—such as high membrane permeability and low toxicity—further enhance its therapeutic potential. Using Caenorhabditis elegans as a model, we demonstrate that geraniol functions as a potent in vivo antioxidant, reducing basal OS and conferring robust protection against exogenous oxidative insults, primarily through activation of the conserved SKN-1/Nrf2 pathway.

Redox imbalance is a hallmark of aging and numerous diseases [2, 3]; thus, understanding how geraniol modulates OS may reveal actionable therapeutic targets. We took advantage of the experimental strengths of C. elegans—a system with well-conserved stress-response pathways and genetically tractable networks—to dissect the molecular mechanisms underlying geraniol’s efects. Consistent with an antioxidant role, geraniol treatment signifcantly lowered basal reactive oxygen species (ROS) levels, indicating an improved redox homeostasis. While ROS play important signaling and homeostatic roles [44], their levels must be tightly regulated, as excess ROS can damage DNA, proteins, and lipids. Te lower ROS accumulation in geraniol-treated animals suggests that geraniol enhances endogenous stress-management pathways [45]. Following acute OS induced by lethal juglone exposure, geraniol markedly increased survival and reduced ROS accumulation. Tese fndings demonstrate that geraniol improves the organism’s capacity to manage redox balance, and consequently, to protect against oxidative damage, in both physiological and OS conditions [1–3].

To elucidate the protective mechanism, we frst considered whether dietary restriction (DR) could be contributing to the observed efects. DR is a well-established modulator of lifespan and stress resilience [17, 30], and in C. elegans it is typically associated with reduced fat storage, as seen in canonical DR models such as eat-2 mutants [46, 47]. However, geraniol treatment did not alter fat stores, indicating that its protective efects are unlikely to arise from DR-related metabolic adaptations.

We then investigated key cytoprotective transcription factors downstream of the insulin/insulin-like signaling (IIS) pathway [35, 36]. Using transgenic reporter strains, we found that geraniol robustly activates SKN-1 (the C. elegans homolog of mammalian Nrf2) and, to a lesser extent, DAF-16 (the homolog of FOXO). Specifcally, geraniol strongly induced the expression of gst-4, a canonical SKN-1 target, and moderately increased sod-3, a DAF-16 efector. Te activation of these OS–related networks provides a mechanistic basis for geraniol’s protective efects. SKN-1/Nrf2 and DAF-16/FOXO regulate genes involved in antioxidant defense, glutathione metabolism, and proteostasis [48–50]. Although these factors can act synergistically, their interaction under OS is complex and context-dependent [51]. For example, FOXO can downregulate Nrf2 activity by reducing ROS and increasing expression of its inhibitor Keap-1 [52].

To determine which pathway is functionally required for geraniol-mediated protection, we performed genetic epistasis analysis. While geraniol improved survival in daf-16 mutants to wild-type levels, its protective efect was signifcantly reduced in skn-1 mutants. Tis indicates that SKN-1, but not DAF-16, is relevant for geraniol’s antioxidant action against juglone-induced OS.

SKN-1 is essential for embryogenesis and, post-embryonically, activates Phase II detoxifcation genes in both constitutive and stress-dependent manners [53]. Tese enzymes support glutathione synthesis, ROS scavenging, and detoxifcation of xenobiotic metabolites [54, 55]. Similarly, mammalian Nrf2 regulates a core antioxidant and chemoprotective response across tissues [55, 56]. Consistent with this conserved role, skn-1 mutants were more sensitive to juglone than wild-type animals (Additional fle  1: Fig. S2). Analogously, Nrf2-defcient mice show heightened susceptibility to chemical toxicity and carcinogenesis and fail to respond to chemoprotective agents [57–60].

A secondary yet intriguing fnding was the moderate but signifcant downregulation of hsp-70, a primary target gene of the cytoprotective HSF-1 pathway. Tis observation gains relevance in light of the unexpected OS resistance displayed by hypomorphic hsf-1 mutants.

While HSF-1 activation is typically considered protective, its partial inhibition appears to trigger a compensatory adaptation that enhances resilience [21]. Tis aligns with the concept that the inhibition of one pathway can increase the activity of another with similar or partially redundant functions [61, 62]. As HSP-70 functions as a molecular chaperone, reduced expression of this protein may increase the availability of unbound client proteins, including transcription factors, thereby facilitating their nuclear translocation and subsequent activation of gene expression [63]. Consequently, this phenomenon suggests that geraniol’s mechanism may involve a pharmacological rewiring of the cellular stress-defense network, whereby a mild repression of one axis (HSF-1) could potentiate the activation of another (i.e., SKN-1/ Nrf2), resulting in a net protective outcome. Tis model, while consistent with our data, remains speculative and warrants further investigation to establish any potential causal relationship between HSF-1 modulation and the enhanced SKN-1 activity observed.

In conclusion, our study demonstrates that geraniol provides broad-spectrum antioxidant protection by enhancing basal redox homeostasis and specifcally engaging the SKN-1/Nrf2 detoxifcation axis upon challenge. Its ability to diferentially regulate multiple conserved pathways—with SKN-1/Nrf2 serving as a pivotal and non-substitutable mediator—suggests potential for synergistic efects in complex disorders driven by OS. Given the demonstrated efcacy of antioxidant strategies in preclinical models, our fndings support the translational potential of plant-derived compounds such as geraniol for mitigating OS–related pathologies.

## 4 Materials and methods 4.1 Reagents

Geraniol (98%) was purchased from Sigma-Aldrich (St. Louis, MO, USA) and DMSO (≥ 99%) was purchased from Biopack (CABA, ARG).

## 4.2 C. elegans culture and maintenance

Worms were cultured and maintained on Nematode Growth Medium (NGM) agar plates seeded with Escheri‑ chia coli OP50 as a food source [64, 65]. Worm culture and all the experiments were carried out at 20 °C, unless otherwise noted. Te wild-type strain was Bristol N2. Te strains were provided by the Caenorhabditis Genet‑ ics Center (CGC), which is funded by the NIH Ofce of Research Infrastructure Programs (P40 OD010440). Low population density was maintained throughout development and during the assays.

For all experiments, animals were age-synchronized. Te strains used were: N2 (wild-type), JV1 jrIs1 [rpl-17p::HyPer+unc-119(+)], CL2166 dvIs19 [(pAF15)

gst-4p::GFP::NLS] III, BC10060 dpy-5(e907) I; sEx884 [rCesC12C8.1::GFP+pCeh361], CF1553 muIs84 [(pAD76) sod-3p::GFP+ rol-6], TJ356 zIs356 [daf-16p::daf-16a/b::GFP+rol-6(su1006)], QV225 skn-1(zj15) IV, PS3551 hsf-1(sy441) I, GR1307 daf-16(mgDf50) I.

## 4.3 Geraniol exposure

Te pharmacological assays were performed as described before [35, 66]. Geraniol was diluted in DMSO. As DMSO has an infuence on relevant parameters, we excluded DMSO efects for our read-outs by adjusting the solvent concentration in all experimental groups to the respective concentration of the highest treatment group. In all experiments, DMSO did not exceed 0.2%, a concentration at which no self-efect was reported [67]. 1  mM geraniol stocks were prepared with DMSO and diluted into NGM agar. Plates were seeded with OP50  (with geraniol), stored at $4 ~ ^ { \circ } \mathrm { C }$ and used within 1 week. In all experiments, age-synchronized individuals were used. To achieve this synchronization, gravid adults were placed on NGM plates containing geraniol, allowed to lay eggs for 3 h, and then removed. Descendants were maintained on these plates until the stage of interest.

## 4.4 Locomotor activity

Adult day  1 worms (AD1) were transferred to 96 multiwell plates (50 worms per well) with M9 bufer and E. coli OP50 culture at $\mathrm { O D 6 0 0 } \approx 0 , 1$ . Locomotor activity was then monitored as a proxy for viability using an infrared tracking system (WMicrotracker MINI, PhylumTech, Argentina), which detects infrared microbeam interruptions due to worm movement in liquid media [27].

## 4.5 Oxidative resistance assay

Oxidative resistance was evaluated following the locomotion protocol described above, with one modifcation. After exposure to the drug, worms were transferred to 96 multiwell plates (50 worms per well) containing 240 µM juglone, a naphthoquinone derived from Juglans regia used as an oxidative stressor. Worm motility was assessed using the same infrared tracking device (WMicrotracker MINI, PhylumTech, Argentina) as a proxy for survival. N2 (wild-type), QV225 (skn-1 hypomorphic mutant), PS3551 (hsf-1 hypomorphic mutant), and GR1307 (daf-16 null mutant) strains were evaluated under oxidative conditions to determine their importance for geraniol protection.

## 4.6 Microscopy and image analysis

For microscopy analysis, animals were grown on NGM plates containing the compound. At the proper age for each experiment, worms were immobilized in sodium azide (0.25 M) and mounted onto slides with 2% agarose pads. Images were obtained using an epifuorescence microscope (NIKON ECLIPSE TE2000-S) coupled to a monochrome CMOS Nikon DS-Qi2 Camera (NIS-Elements acquisition software) at × 10, × 20 and × 40 mag. Images were analyzed using Image J FIJI software (ImageJ, National Institutes of Health, Bethesda, MD, United States).

## 4.7 ROS production

Te JV1 strain genetically expresses HyPer, a hydrogen peroxide–specifc sensor composed of a circularly permuted yellow fuorescent protein (cpYFP) inserted into the regulatory domain of the prokaryotic $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 } .$ -sensing protein OxyR. Upon selective and sensitive oxidation by $\mathrm { H } _ { 2 } \mathrm { O } _ { 2 } ,$ HyPer forms a disulfde bridge between the separated regions of the OxyR regulatory domain, thereby altering its fuorescent properties. Animals were agesynchronized and maintained on NGM plates containing either 1 mM geraniol or vehicle. Images were acquired at the L4 stage using excitation flters of 488 nm (oxidized) and 400 nm (reduced) [68]. For each animal, the Ox/Red ratio was calculated as a proxy for the redox state [28].

## 4.8 Nutritional state

To assess fat storage in C. elegans, we followed the Oil-Red O (ORO) staining protocol described by  Wang et., al [47]. Briefy, synchronized AD1 animals were fxed in paraformaldehyde, permeabilized by repeated freeze– thaw cycles, and incubated with freshly prepared ORO working solution. After incubation, worms were washed thoroughly to remove excess dye, mounted, and contrast-mode images were acquired for analysis. Quantifcation was performed in ImageJ FIJI software. For each animal, we measured the average pixel intensity within a 40-pixel-radius region immediately posterior to the pharynx. A 40-pixel-radius background region was also measured, and this value was subtracted from the staining intensity to obtain background-corrected measurements.

## 4.9 gst‑4, hsp‑70 and sod‑3 expression

Gst-4 expression was analyzed in the transgenic strain containing a transcriptional GFP reporter: CL2166 dvIs19 [(pAF15)gst-4p::GFP::NLS] III; hsp-70 expression was analyzed in the transgenic strain BC10060 dpy-5(e907) I; sEx884 [rCesC12C8.1::GFP+pCeh361] and sod-3 expression was analyzed in the transgenic strain CF1553 muIs84 [(pAD76) sod-3p::GFP+rol-6].

Images of AD1 animals were taken at 10 × objective magnitude and mean fuorescence intensity was measured in the whole body (for GST-4 and HSP-70) or at 20 × for SOD-3 (head animals, same-sized Regions of Interest (ROIs)). Fluorescence intensity was quantifed using ImageJ FIJI software and was relativized to the control condition for analysis.

## 4.10 Subcellular DAF‑16 localization

DAF-16 translocation was analyzed using strains containing the translational Pdaf-16::DAF-16a/b::GFP reporter. AD1 animals exposed to mild stress (200 µM juglone for 10  min) were analyzed. Te number of GFP-labeled nuclei per animal was quantifed using Image J FIJI software and normalized to the control condition within the day.

## 4.11 In silico evaluation of ADME profle

Geraniol structure and SMILES (Simplifed Molecular Input Line Entry System) notation were generated using the structure fle generator available in the Open Chemistry Database of the National Institutes of Health (NIH) (https://pubchem.ncbi.nlm.nih.gov/). Te resulting SMILES string was exported to the free online tool SwissADME (http://www.swissadme.ch/) [24, 69]. Considering six physicochemical properties such as lipophilicity, molecular size, polarity, solubility, saturation and fexibility, this tool predicts and weights the probability of the oral bioavailability of the drug by building a bioavailability radar. BOILED-Egg graph was also generated to evaluate the capacity of geraniol to passively permeate through the blood–brain barrier.

## 4.12 Statistical analysis

Te results presented in each fgure are the average of at least three independent assays. Bars represent mean ± SEM. All the statistical tests were performed after checking normality. Grubbs’ test was used for outlier analysis (p < 0.05). Typically, one-way analysis of variance was employed for analyzing multiple parametric samples, and Holm–Sidak’s post hoc test was used for comparisons against a control group. In cases where comparisons were made between two independent conditions, a Student’s t-test was utilized for parametric data, while the Mann–Whitney U test was employed for non-parametric data. For T50 analysis, we ftted using Prism 8.0.1 (GraphPad Software Inc., La Jolla, CA, USA) to a Hill equation with four parameters. Te statistical information is indicated in the fgure legends.

## Supplementary Information

The online version contains supplementary material available at https://doi.   
org/10.1007/s13659-026-00604-4.

Additional fle 1.

## Acknowledgements

Some strains were provided by the CGC, which is funded by the NIH Ofce of Research Infrastructure Programs (P40 OD010440).

## Author contributions

DR, and MJDR designed and conceived the study. SR acquired the data. SR and AL analyzed and interpreted the data. SR and AL performed the statistical analysis. DR and MJDR drafted the manuscript. DR and MJDR supervised the study and obtained funding.

## Funding

This work was supported by Grants from: 1) Universidad Nacional Del Sur to DR (PGI: 24/B291), MJDR (PGI: 24/B261) 2) Agencia Nacional de Promoción de la Ciencia y la Tecnología ANPCYT Argentina to DR (PICT 2019-0480 and PICT-2021-I-A-00052), MJDR (PICT 2020 1734) and Consejo Nacional de Investigaciones Científcas y Técnicas, Argentina to DR and MJDR (PIPNo. 11220200101606CO). The funders had no role in the study design, data collection, and analysis, decision to publish, or preparation of the manuscript.

## Data availability

The data that support the fndings of this study are available in the following link: https://osf.io/2fp6s

## Declarations

## Competing interest

The authors declare that the research was conducted in the absence of any commercial or fnancial relationships that could be construed as a potential confict of interest.

## Author details

1 Laboratorio Neurobiología de Invertebrados, Instituto de Investigaciones Bioquímicas de Bahía Blanca (INIBIBB) CCT UNS-CONICET, 8000, Camino La Carrindanga Km 7, Buenos Aires, 8000, Bahía Blanca, Argentina. 2 Departamento de Biología, Bioquímica y Farmacia, Universidad Nacional del Sur (UNS), 8000, San Juan 670, Buenos Aires, 8000, Bahía Blanca, Argentina.

Received: 23 December 2025 Accepted: 5 February 2026   
Published online: 22 April 2026

## References

1. Bordoni M, Scarian E, Rey F, Gagliardi S, Carelli S, Pansarasa O, et al. Biomaterials in neurodegenerative disorders: a promising therapeutic approach. Int J Mol Sci. 2020. https://doi.org/10.3390/ijms21093243.

2. Espinós C, Galindo MI, García-Gimeno MA, Ibáñez-Cabellos JS, Martínez-Rubio D, Millán JM, et al. Oxidative stress, a crossroad between rare diseases and neurodegeneration. Antioxidants. 2020. https://doi.org/10. 3390/antiox9040313.

3. Finkel T, Holbrook NJ. Oxidants, oxidative stress and the biology of ageing. Nature. 2000;408(6809):239–47. https://doi.org/10.1038/35041687.

4. Ewald CY, Hourihan JM, Bland MS, Obieglo C, Katic I, Moronetti Mazzeo LE, et al. NADPH oxidase-mediated redox signaling promotes oxidative stress resistance and longevity through memo-1 in C. elegans. Elife. 2017. https://doi.org/10.7554/eLife.19493.

5. Mittal M, Siddiqui MR, Tran K, Reddy SP, Malik AB. Reactive oxygen species in infammation and tissue injury. Antioxid Redox Signal. 2014;20(7):1126–67. https://doi.org/10.1089/ars.2012.5149.

6. Liguori I, Russo G, Curcio F, Bulli G, Aran L, Della-Morte D, et al. Oxidative stress, aging, and diseases. Clin Interv Aging. 2018;13:757–72. https://doi. org/10.2147/CIA.S158513.

7. Baptista-Silva S, Borges S, Ramos OL, Pintado M, Sarmento B. The progress of essential oils as potential therapeutic agents: a review. J Essent Oil Res. 2020;32(4):279–95. https://doi.org/10.1080/10412905.2020.1746698.

8. Mancianti F, Ebani VV. Biological activity of essential oils. Molecules. 2020. https://doi.org/10.3390/molecules25030678.

9. Banu F, Dawood N, Lakshmi YSL, Sivaraman G, Brinda V. Antioxidant activity of geraniol on N-nitrosodiethylamine-induced hepatocarcinogenesis in wistar albino rats. Ind J Oncol Radiat Biol. 2014;2:4–9.

10. Mączka W, Wińska K, Grabarczyk M. One hundred faces of geraniol. Molecules. 2020;25:3303. https://doi.org/10.3390/molecules25143303.

11. De Fazio L, Spisni E, Cavazza E, Strillacci A, Candela M, Centanni M, et al. Dietary geraniol by oral or enema administration strongly reduces dysbiosis and systemic infammation in dextran sulfate sodium-treated mice. Front Pharmacol. 2016;7:38. https://doi.org/10.3389/fphar.2016.00038.

12. Kenyon C, Chang J, Gensch E, Rudner A, Tabtiang R. A C. elegans mutant that lives twice as long as wild type. Nature. 1993;366(6454):461–4. https://doi.org/10.1038/366461a0.

13. Samuelson AV, Carr CE, Ruvkun G. Gene activities that mediate increased life span of C. elegans insulin-like signaling mutants. Genes Dev. 2007;21(22):2976–94. https://doi.org/10.1101/gad.1588907.

14. Chalfe M, Tu Y, Euskirchen G, Ward WW, Prasher DC. Green fuorescent protein as a marker for gene expression. Science. 1994;263(5148):802–5. https://doi.org/10.1126/science.263.5148.802.

15. Kerr RA, Schafer WR. Intracellular Ca2 ⁺ imaging in C. elegans. In: Strange K, editor. C. elegans. Methods in Molecular Biology. Totowa (NJ): Humana Press; 2006. pp. 253–264. https://doi.org/10.1385/1-59745-151-7:253.

16. Kenyon CJ. The genetics of ageing. Nature. 2010;464(7288):504–12. https://doi.org/10.1038/nature08980.

17. Fontana L, Partridge L, Longo VD. Extending healthy life span--from yeast to humans. Science. 2010;328(5976):321–6. https://doi.org/10.1126/scien ce.1172539.

18. Cohen E, Dillin A. The insulin paradox: aging, proteotoxicity and neurodegeneration. Nat Rev Neurosci. 2008;9(10):759–67. https://doi.org/10.1038/ nrn2474.

19. Hsu AL, KENYy CT, Kenyon C. Regulation of aging and age-related disease by DAF-16 and heat-shock factor. Science. 2003;300(5622):1142–5. https://doi.org/10.1126/science.1083701.

20. Cohen E, Bieschke J, Perciavalle RM, Kelly JW, Dillin A. Opposing activities protect against age-onset proteotoxicity. Science. 2006;313(5793):1604– 10. https://doi.org/10.1126/science.1124646.

21. Anckar J, Sistonen L. Regulation of HSF1 function in the heat stress response: implications in aging and disease. Annu Rev Biochem. 2011;80:1089–115. https://doi.org/10.1146/annurev-bioch em-060809-095203.

22. Steinbaugh MJ, Narasimhan SD, Robida-Stubbs S, Moronetti Mazzeo LE, Dreyfuss JM, Hourihan JM, et al. Lipid-mediated regulation of SKN-1/Nrf in response to germ cell absence. Elife. 2015;4:e07836. https://doi.org/10. 7554/eLife.07836.

23. Teixeira-Castro A, Ailion M, Jalles A, Brignull HR, Vilaca JL, Dias N, et al. Neuron-specifc proteotoxicity of mutant ataxin-3 in C. elegans: rescue by the DAF-16 and HSF-1 pathways. Hum Mol Genet. 2011;20(15):2996– 3009. https://doi.org/10.1093/hmg/ddr203.

24. Andersen N, Veuthey T, Blanco MG, Silbestri GF, Rayes D, De Rosa MJ. 1-mesityl-3-(3-sulfonatopropyl) imidazolium protects against oxidative stress and delays proteotoxicity in C. elegans. Front Pharmacol. 2022;13:908696. https://doi.org/10.3389/fphar.2022.908696.

25. Giunti S, Andersen N, Rayes D, De Rosa MJ. Drug discovery: insights from the invertebrate Caenorhabditis elegans. Pharmacol Res Perspect. 2021;9(2):e00721. https://doi.org/10.1002/prp2.721.

26. Lakso M, Vartiainen S, Moilanen AM, Sirvio J, Thomas JH, Nass R, et al. Dopaminergic neuronal loss and motor defcits in Caenorhabditis elegans overexpressing human alpha-synuclein. J Neurochem. 2003;86(1):165–72. https://doi.org/10.1046/j.1471-4159.2003.01809.x.

27. Simonetta SH, Golombek DA. An automated tracking system for Caenorhabditis elegans locomotor behavior and circadian studies application. J Neurosci Methods. 2007;161(2):273–80. https://doi.org/10.1016/j.jneum eth.2006.11.015.

28. Knoefer D, Thamsen M, Koniczek M, Niemuth NJ, Diederich AK, Jakob U. Quantitative in vivo redox sensors uncover oxidative stress as an early event in life. Mol Cell. 2012;47(5):767–76. https://doi.org/10.1016/j.molcel. 2012.06.016.

29. Back P, Matthijssens F, Vanfeteren JR, Braeckman BP. A simplifed hydroethidine method for fast and accurate detection of superoxide production in isolated mitochondria. Anal Biochem. 2012;423(1):147–51. https:// doi.org/10.1016/j.ab.2012.01.008.

30. Swindell WR. Dietary restriction in rats and mice: a meta-analysis and review of the evidence for genotype-dependent efects on lifespan. Ageing Res Rev. 2012;11(2):254–70. https://doi.org/10.1016/j.arr.2011.12.006.

31. Ching TT, Hsu AL. The impacts of diferent dietary restriction regimens on aging and longevity: from yeast to humans. J Biomed Sci. 2025;32(1):91. https://doi.org/10.1186/s12929-025-01188-w.

32. Murphy CT, Hu PJ. Insulin/insulin-like growth factor signaling in C. elegans. In: WormBook, editor. WormBook. [Place unknown]: WormBook; 2013. pp. 1–43. https://doi.org/10.1895/wormbook.1.164.1

33. Altintas O, Park S, Lee SJ. The role of insulin/IGF-1 signaling in the longevity of model invertebrates, C. elegans and D. melanogaster. BMB Rep. 2016;49(2):81–92.

34. Kumsta C, Chang JT, Schmalz J, Hansen M. Hormetic heat stress and HSF-1 induce autophagy to improve survival and proteostasis in C. elegans. Nat Commun. 2017;8:14337. https://doi.org/10.1038/ncomm s14337.

35. De Rosa MJ, Veuthey T, Florman J, Grant J, Blanco MG, Andersen N, et al. The fight response impairs cytoprotective mechanisms by activating the insulin pathway. Nature. 2019;573(7772):135–8. https://doi.org/10.1038/ s41586-019-1524-5.

36. Veuthey T, Florman JT, Giunti S, Romussi S, De Rosa MJ, Alkema MJ, et al. The neurohormone tyramine stimulates the secretion of an insulin-like peptide from the Caenorhabditis elegans intestine to modulate the systemic stress response. PLoS Biol. 2025;23(1):e3002997. https://doi.org/ 10.1371/journal.pbio.3002997.

37. Kovacs D, Biro JB, Ahmed S, Kovacs M, Sigmond T, Hotzi B, et al. Age-dependent heat shock hormesis to HSF-1 defciency suggests a compensatory mechanism mediated by the unfolded protein response and innate immunity in young Caenorhabditis elegans. Aging Cell. 2024;23(10):e14246. https://doi.org/10.1111/acel.14246.

38. Chen W, Viljoen A. Geraniol—a review of a commercially important fragrance material. S Afr J Bot. 2010;76:643–51. https://doi.org/10.1016/j. sajb.2010.05.008.

39. de Cássia da Silveira e Sá R, Andrade LN, de Sousa DP. A review on antiinfammatory activity of monoterpenes. Molecules. 2013;18(1):1227–54. https://doi.org/10.3390/molecules18011227.

40. Sato K, Krist S, Buchbauer G. Antimicrobial efect of vapours of geraniol, (R)-(–)-linalool, terpineol, γ-terpinene and 1,8-cineole on airborne microbes using an airwasher. Flavour Fragr J. 2007;22(5):435–7. https:// doi.org/10.1002/f.1818.

41. Papachristos DP, Karamanoli KI, Stamopoulos DC, Menkissoglu-Spiroudi U. The relationship between the chemical composition of three essential oils and their insecticidal activity against Acanthoscelides obtectus (Say). Pest Manag Sci. 2004;60(5):514–20. https://doi.org/10.1002/ps.798.

42. Morales-Serna FN, Martínez-Brown JM, Avalos-Soriano A, Sarmiento-Vázquez S, Hernández-Inda ZL, Medina-Guerrero RM, et al. The efcacy of geraniol and β-citronellol against freshwater and marine monogeneans. J Aquat Anim Health. 2020;32(3):127–32. https://doi.org/10.1002/aah. 10109.

43. Galle M, Crespo R, Kladniew BR, Villegas SM, Polo M, de Bravo MG. Suppression by geraniol of the growth of A549 human lung adenocarcinoma cells and inhibition of the mevalonate pathway in vitro and in vivo: potential use in cancer chemotherapy. Nutr Cancer. 2014;66(5):888–95. https://doi.org/10.1080/01635581.2014.916320.

44. Manful CF, Fordjour E, Subramaniam D, Sey AA, Abbey L, Thomas R. Antioxidants and reactive oxygen species: shaping human health and disease outcomes. Int J Mol Sci. 2025;26(15):7520. https://doi.org/10.3390/ijms2 6157520.

45. Wei Y, Jia S, Ding Y, Xia S, Giunta S. Balanced basal-levels of ROS (redoxbiology), and very-low-levels of pro-infammatory cytokines (cold-infammaging), as signaling molecules can prevent or slow-down overt-infammaging, and the aging-associated decline of adaptive-homeostasis. Exp Gerontol. 2023;172:112067. https://doi.org/10.1016/j.exger.2022.112067.

46. Avery L. The genetics of feeding in Caenorhabditis elegans. Genetics. 1993;133(4):897–917. https://doi.org/10.1093/genetics/133.4.897.

47. Wang FY, Ching TT. Oil red o staining for lipid content in Caenorhabditis elegans. Bio Protoc. 2021;11(16):e4124. https://doi.org/10.21769/BioPr otoc.4124.

48. Park SK, Tedesco PM, Johnson TE. Oxidative stress and longevity in Caenorhabditis elegans as mediated by SKN-1. Aging Cell. 2009;8(3):258–69. https://doi.org/10.1111/j.1474-9726.2009.00473.x.

49. Oh SW, Mukhopadhyay A, Dixit BL, Raha T, Green MR, Tissenbaum HA. Identifcation of direct DAF-16 targets controlling longevity,

metabolism and diapause by chromatin immunoprecipitation. Nat Genet. 2006;38(2):251–7. https://doi.org/10.1038/ng1723.

50. Ewald CY, Landis JN, Porter Abate J, Murphy CT, Blackwell TK. Dauerindependent insulin/IGF-1-signalling implicates collagen remodelling in longevity. Nature. 2015;519(7541):97–101. https://doi.org/10.1038/natur e14021.

51. Klotz LO, Steinbrenner H. Cellular adaptation to xenobiotics: interplay between xenosensors, reactive oxygen species and FOXO transcription factors. Redox Biol. 2017;13:646–54. https://doi.org/10.1016/j.redox.2017. 07.015.

52. Gille A, Turkistani A, Tsitsipatis D, Hou X, Tauber S, Hamann I, et al. Nuclear trapping of inactive FOXO1 by the Nrf2 activator diethyl maleate. Redox Biol. 2019;20:19–27. https://doi.org/10.1016/j.redox.2018.09.010.

53. An JH, Blackwell TK. SKN-1 links C. elegans mesendodermal specifcation to a conserved oxidative stress response. Genes Dev. 2003;17(15):1882– 93. https://doi.org/10.1101/gad.1107803.

54. Thimmulappa RK, Mai KH, Srisuma S, Kensler TW, Yamamoto M, Biswal S. Identifcation of Nrf2-regulated genes induced by the chemopreventive agent sulforaphane by oligonucleotide microarray. Cancer Res. 2002;62(18):5196–203. https://doi.org/10.1158/0008-5472.CAN-02-1943.

55. Hayes JD, McMahon M. Molecular basis for the contribution of the antioxidant responsive element to cancer chemoprevention. Cancer Lett. 2001;174(2):103–13. https://doi.org/10.1016/S0304-3835(01)00695-4.

56. Itoh K, Chiba T, Takahashi S, Ishii T, Igarashi K, Katoh Y, et al. An Nrf2/small Maf heterodimer mediates the induction of phase II detoxifying enzyme genes through antioxidant response elements. Biochem Biophys Res Commun. 1997;236(2):313–22. https://doi.org/10.1006/bbrc.1997.6943.

57. Chan K, Kan YW. Nrf2 is essential for protection against acute pulmonary injury in mice. Proc Natl Acad Sci U S A. 1999;96(22):12731–6. https://doi. org/10.1073/pnas.96.22.12731.

58. Chan K, Han XD, Kan YW. An important function of Nrf2 in combating oxidative stress: detoxifcation of acetaminophen. Proc Natl Acad Sci U S A. 2001;98(8):4611–6. https://doi.org/10.1073/pnas.081082098.

59. Ramos-Gomez M, Kwak MK, Dolan PM, Itoh K, Yamamoto M, Talalay P, et al. Sensitivity to carcinogenesis is increased and chemoprotective efcacy of enzyme inducers is lost in nrf2 transcription factor-defcient mice. Proc Natl Acad Sci U S A. 2001;98(6):3410–5. https://doi.org/10.1073/pnas. 051618798.

60. Fahey JW, Haristoy X, Dolan PM, Kensler TW, Scholtus I, Stephenson KK, et al. Sulforaphane inhibits extracellular, intracellular, and antibiotic-resistant strains of Helicobacter pylori and prevents benzo[a]pyrene-induced stomach tumors. Proc Natl Acad Sci U S A. 2002;99(11):7610–5. https:// doi.org/10.1073/pnas.112203099.

61. Perić M, Bou Dib P, Dennerlein S, Musa M, Rudan M, Lovrić A, et al. Crosstalk between cellular compartments protects against proteotoxicity and extends lifespan. Sci Rep. 2016;6:28751. https://doi.org/10.1038/srep2 8751.

62. Deng J, Dai Y, Tang H, Pang S. SKN-1 is a negative regulator of DAF-16 and somatic stress resistance in Caenorhabditis elegans. G3 Genes|Genomes|Genetics. 2020;10(5):1707–12. https://doi.org/10.1534/ g3.120.401203.

63. Nakae J, Park BC, Accili D. Insulin stimulates phosphorylation of the forkhead transcription factor FKHR on serine 253 through a wortmanninsensitive pathway. J Biol Chem. 1999;274(23):15982–5. https://doi.org/10. 1074/jbc.274.23.15982.

64. Brenner S. The genetics of Caenorhabditis elegans. Genetics. 1974;77(1):71–94.

65. Stiernagle T. Maintenance of C. elegans. In: WormBook, editor. WormBook. [Place unknown]: WormBook; 2006. pp. 1–11. https://doi.org/10.1895/ wormbook.1.101.1.

66. Blanco MG, Vela Gurovic MS, Silbestri GF, Garelli A, Giunti S, Rayes D, et al. Diisopropylphenyl-imidazole (DII): a new compound that exerts anthelmintic activity through novel molecular mechanisms. PLoS Negl Trop Dis. 2018;12(12):e0007021. https://doi.org/10.1371/journal.pntd.0007021.

67. AlOkda A, Van Raamsdonk JM. Efect of DMSO on lifespan and physiology in C. elegans: implications for use of DMSO as a solvent for compound delivery. MicroPubl Biol. 2022;2022. https://doi.org/10.17912/micropub. biology.000634.

68. Back P, De Vos WH, Depuydt GG, Matthijssens F, Vanfeteren JR, Braeckman BP. Exploring real-time in vivo redox biology of developing and

aging Caenorhabditis elegans. Free Radic Biol Med. 2012;52(5):850–9. https://doi.org/10.1016/j.freeradbiomed.2011.11.037.

69. Daina A, Michielin O, Zoete V. SwissADME: a free web tool to evaluate pharmacokinetics, drug-likeness and medicinal chemistry friendliness of small molecules. Sci Rep. 2017;7:42717. https://doi.org/10.1038/srep4 2717.

## Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.