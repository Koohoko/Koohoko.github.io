---
title: "Paper digest: More structured coalescent papers"
date: 2025-01-04
permalink: /posts/2025-01-04/structured-coalescent3
categories:
  - Paper digest
tags:
  - Coalescent theory
  - Structured coalescent
  - Phylogenetics
toc: true
# last_modified_at: 2025-01-05
---

I wanted to get in more details about the structured coalescent model, here I record some notes when I read related papers.

# Overview
Firstly there is a review paper on phylogeographic inference on 2010, then I will go through some papers on structured coalescent models.

Structured coalescent papers are mainly from two authors:
- [Nicola F. Muller](https://muellerlab.io), who developed [MASCOT](https://taming-the-beast.org/tutorials/Mascot-Tutorial/).
- [Nicola De Maio](https://scholar.google.at/citations?user=5qarsrQAAAAJ&hl=en), who developed [SCOTTI](https://taming-the-beast.org/tutorials/SCOTTI-Tutorial/).

# Papers

## [Three roads diverged? Routes to phylogeographic inference](https://www.sciencedirect.com/science/article/pii/S0169534710001965?via%3Dihub) by *Erik W. Bloomquist* et al. on Trends in Ecology & Evolution, 2010.

### Nested clade phylogeographic analysis (NCPA), a comparative approach

- A method to integrate **molecular genealogy** (often a haplotype tree) and **geographic information** in a single framework. Its main goal is to infer **historical processes** that shaped the geographic distribution of genetic variation—things like range expansions, fragmentations, or isolation by distance—using only single-locus (or sometimes multi-locus) sequence data.
- The Three-Step Workflow
  - **Haplotype Tree or Network Construction**: You start by building a haplotype tree or haplotype network from your molecular data (e.g., DNA sequences). Various methods can be used (parsimony, statistical parsimony, median-joining, etc.).
  - **Nesting Clades**: Once you have the haplotype tree, you “nest” clades in a hierarchical manner:
    - The most closely related haplotypes form the first (1‐step) clade.
    - Groups of 1‐step clades form the 2‐step clade, and so on, up to the entire tree.
    - This step is somewhat subjective and follows a set of guidelines by Templeton.
  - **Statistical Tests & Interpretation**: 
    - For each clade, you measure how broadly it is geographically distributed relative to its genetic diversity.
    - A permutation test is used to assess statistical significance (does this clade appear more geographically “spread out” than expected by chance?).
    - Finally, you use an “inference key” (a decision flowchart) to interpret patterns (e.g., “range expansion,” “isolation by distance,” “fragmentation,” etc.).
- Criticisms:
  - **High False-Positive Rate**
    - Multiple studies (e.g., Knowles & Maddison; Panchal & Beaumont) showed that single-locus NCPA tends to over‐detect “significant” phylogeographic patterns, suggesting many false positives.
    - One reason is that multiple clades in the nested design are tested, but the method did not adequately correct for multiple testing (Type I error accumulation).
  - **Pipeline Nature & Overconfidence**
    - NCPA is a sequential pipeline:
      - Build or infer a single haplotype tree.
      - Nest the clades.
      - Do a permutation test and interpret.
    - Errors or uncertainty in earlier stages (e.g., how the tree is constructed or how clades are nested) are not carried forward—thus each subsequent step can overstate confidence in the final inferences.
- **Modern model-based** (particularly Bayesian or coalescent) methods are now preferred, because they:
  - They Incorporate Geography More Rigorously
    - Some methods directly model **migration rates** or **dispersal kernels** in continuous or discrete space.
    - They can handle **population size** changes, gene flow, barriers, and other complexities.
  - They Are Statistically Formal
    - By specifying an explicit **probabilistic model** of evolution + geography, one can **estimate** parameters (e.g., migration rates, times of divergence) and **compare** models via likelihood or Bayesian posterior probabilities.
  - Joint Inference
    - Many modern approaches **jointly** infer genealogies, demographic parameters, and geographic patterns, thus **avoiding** the pipeline problem where each step is conditionally fixed.

### Spatial diffusion approach

1. **Model‐Based Spatial Diffusion**  
   - Unlike traditional “population‐based” spatial coalescent models, **phylogenetic diffusion** focuses on the **ancestral history of a particular sample** of molecular sequences.  
   - It treats **location** as a trait evolving along the branches of a **time‐calibrated phylogeny**, using **continuous‐time Markov chains (CTMC)**.  
   - This permits a *probabilistic* reconstruction of when and where the ancestors of sampled sequences existed, often implemented in **BEAST**.

2. **Discrete vs. Continuous Spatial Models**  
   - **Discrete diffusion**: Each lineage “jumps” among a set of discrete locations. It can handle many possible states (locations), but each additional location increases the number of rate parameters.  
   - **Continuous diffusion**: Lineages move in a continuous spatial landscape (e.g., coordinates modeled via Brownian motion or more flexible “relaxed random walks”).  
   - These approaches can incorporate **geographical context**, such as distance‐dependent dispersal or environmental barriers, and handle **rate heterogeneity** over the phylogeny (relaxed clock style).

3. **Bayesian Statistical Framework**  
   - **Bayesian** methods naturally account for over‐parameterization by placing **priors** on migration rates (e.g., distance‐informed priors).  
   - They can also perform **Bayesian Stochastic Search Variable Selection (BSSVS)** to identify only those migration rates essential to explain the data, reducing complexity.  
   - This framework yields **posterior distributions** reflecting uncertainty in both **phylogenetic** and **geographic** estimates.

4. **Advantages & Use Cases**  
   - More **realistic** than simplistic or purely heuristic (parsimony) ancestral reconstructions.  
   - **Accommodates** uncertainty in tree topology, branch lengths, and location histories.  
   - Useful in **epidemiology** (e.g., viral outbreaks), **biogeography** (e.g., island studies, animal movement), and any case where one wants to see **how lineages spread** over space and time.

- Overall, this **spatial diffusion approach** integrates *time‐scaled phylogenies* with *spatial movement models* to infer how sampled lineages have dispersed geographically. It sidesteps full “population‐based” modeling in favor of **direct ancestral locations** for the sequences under study, offering a flexible, Bayesian way to reconstruct **spatial histories** in evolutionary and epidemiological research.

### Population genetics approach

- The population genetics approach to phylogeography is dominated by methods based on the structured-coalescent framework, which models evolutionary trees as **random draws** from population-level processes like selection, migration, population size changes, and recombination.
- ![](https://ars.els-cdn.com/content/image/1-s2.0-S0169534710001965-gr1.jpg)

### Comparing mugration and structured coalescent (From ChatGPT):
- **Mugration models** treat location as a discrete trait evolving along a single phylogenetic tree via a continuous‐time Markov chain (CTMC). They do not explicitly model different populations (demes) and their internal coalescent events.
- **Structured coalescent** approaches like MASCOT and SCOTTI explicitly model how lineages coalesce within demes (or hosts) and migrate or transmit between demes (or hosts). They incorporate population sizes, migration (transmission) rates, and the coalescent process in each deme.
- In other words, mugration is essentially a *trait-substitution* model for location, whereas structured coalescent models the *population-genetic* process of coalescence within and between subpopulations.

  | **Aspect**                          | **Mugration Model**                                                                                                                   | **Structured Coalescent Model (e.g. MASCOT, SCOTTI)**                                                                                                                           |
  |------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | **Level of modeling**              | Per‐lineage *trait substitution* (no explicit coalescent events in each location).                                                    | Full coalescent with population subdivision: genealogies form via coalescence *within* demes, migration/transmission *between* demes.                                            |
  | **Population sizes & demes**       | Not modeled; “location” is just a discrete character.                                                                                 | Each deme (or host) has an *effective population size*. Coalescent rates depend on deme sizes.                                                                                   |
  | **Migration**                      | A simple CTMC of jumps between states along a single phylogeny.                                                                       | Migration/transmission events between demes/hosts are part of the *structured coalescent process* that generates genealogies.                                                    |
  | **Inferred quantities**            | - Location states at ancestral nodes<br>- Rate matrix of location changes                                                             | - Demic or host‐level coalescent parameters (population sizes)<br>- Migration/transmission rates<br>- Full distribution of genealogies with demic assignment for each lineage. |
  | **Typical usage**                  | Reconstructing **discrete phylogeography**: “Where did the lineages come from and how often did they move among locations?”           | Understanding **population structure**, **host–pathogen** dynamics, or **transmission chains** with explicit coalescent modeling.                                                |



## [New Routes to Phylogeography: A Bayesian Structured Coalescent Approximation](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1005421) by *Nicola De Maio et al.* on PLOS Genetics, 2015.

### Abstract
- In this paper, we show that inference of migration rates and root locations based on **discrete trait** models is extremely unreliable and sensitive to biased sampling. 
- BASTA (BAyesian STructured coalescent Approximation): a approach implemented in BEAST2 that combines the accuracy of methods based on the structured coalescent with the computational efficiency required to handle more than just few populations.

### Background

- Use of the discrete trait analysis (DTA), such as *mugration*, entails a number of assumptions that are unusual or inappropriate when applied to the migration of lineages between geographic locations, for example 
  1. the relative size of subpopulations drifts over time, such that subpopulations can become lost (extinct) or fixed (the sole remaining subpopulation) instead of being constrained, e.g. by local competition, 
  2. sample sizes across subpopulations are proportional to their relative size.

### Methods
- ![](/files/2024-12-28-structured-coalescent/Screenshot%202025-01-03%20at%2019.38.43.webp)

#### The Structured Coalescent
- Key assumptions:
  - Demes are stable in size, with their effective sizes defined by vector $\theta$.
  - Migration occurs at a constant rate over time, defined by matrix $f$.
  - No substructure within demes.
  - No fitness differences between individuals.
  - Within demes, individuals are sampled at random.
  - However, no assumptions are made about the total sample size nor the relative sample sizes per deme.
- $f_{a,b}$ is the *forwards-in-time* migration rate matrix, and conventionally $m_{b,a}$ is the *backwards-in-time* migration rate matrix. Both specifying migration of individuals from deme $a$ to deme $b$. Specifically, $m_{b,a}=f_{a,b}\theta_a/\theta_b$.
- Recall that in [MultiTypeTree (MTT) for Structured coalescent](https://guhaogao.com/posts/2025-01-03/structured-coalescent2):

  - The posterior distribution of the parameters is:

    $$
    P(T, M, \mu, m, \theta \mid S, t_I, L) \propto P(S \mid T, t_I, \mu) P(T, M \mid t_I, L, m, \theta) P(\mu) P(m) P(\theta).
    $$

  - **Components**:
    1. The first term, $P(S \mid T, t_I, \mu)$, is the likelihood of the sequences given the genealogy and substitution model, computed using Felsenstein's pruning algorithm.
    2. The second term, $P(T, M \mid t_I, L, m, \theta)$, represents the probability density of the genealogy and migration history under the structured coalescent, given the migration matrix and effective population sizes.
    3. The third term is the prior distribution of the parameters, potentially factored as independent priors for $\mu$, $m$, and $\theta$.

  - To calculate $P(T, M \mid t_I, L, m, \theta)$, the sequence of $B$ time intervals between successive events (coalescence, sampling, or migration) is considered, starting from the most recent sample back to the root. For a haploid population:

    $$
    P(T, M \mid t_I, L, m, \theta) = \prod_{i=1}^B L_i,
    $$

    where:

    $$
    L_i = \exp \left[ 
    -\tau_i \sum_{d \in D} \left( 
    \binom{k_{i,d}}{2} \frac{1}{\theta_d} + k_{i,d} \sum_{d' \in D, d' \neq d} m_{dd'}
    \right) \right] E_i,
    $$

    and:
    - $k_{i,d}$ is the number of lineages in deme $d$ during interval $i$.
    - $E_i$ is the contribution of the event ending interval $i$:

    $$
    E_i =
    \begin{cases}
    1 & \text{if it is a sampling event}, \\
    m_{dd'} & \text{if it is a migration event from } d \text{ to } d', \\
    \frac{1}{\theta_d} & \text{if it is a coalescence event in deme } d.
    \end{cases}
    $$

#### Discrete Trait Analysis

- **Key Idea**:  
 - Treats a lineage’s “location” as a **discrete trait** (analogous to nucleotides) evolving along an unstructured coalescent tree.  
 - Uses **Felsenstein’s pruning algorithm** to integrate over all trait histories (migration paths) very efficiently.  
- **Model**:  
 - The prior on the tree often assumes a **single, unstructured** population.  
 - “Migration” is just a constant‐rate Markov chain, unrelated to actual subpopulation sizes.  
 - **Sampling fraction $\propto$ subpopulation size is assumed**.  
- **Pros**:  
 - Fast and straightforward to implement (common in BEAST’s “discrete phylogeography”).  
- **Cons**:  
 - Can produce **biased** results if real subpopulation sizes or migration strongly influence tree shape, or if sampling intensity does not match relative deme size.  
   - Allows “loss” or “resurrection” of demes in unrealistic ways.
- Comparison to MTT:
  - In **Discrete Trait Analysis (DTA)**, the *migration rates* do **not** shape the branching times or topology of the genealogy; instead, the genealogical prior is (for the most part) an **unstructured coalescent** (or some other simple tree prior), and “migration” is just treated as a **discrete‐character substitution** process on that fixed genealogy.
  - Hence, in DTA:
    $$
    P(T,\mu,f,\theta \;\big|\; S,t_I,L)
    \;\;\propto\;\;
    \underbrace{P(L \mid T, t_I, f)}_{\substack{\text{location-likelihood via discrete}\\\text{trait (migration) “substitutions”}}}
    \;
    \times
    \underbrace{P(S \mid T, t_I, \mu)}_{\substack{\text{sequence-likelihood via}\\\text{molecular substitutions}}}
    \;
    \times
    \underbrace{P(T \mid t_I,\theta)}_{\substack{\text{unstructured coalescent}\\\text{prior on the tree}}}
    \;
    \times
    P(\mu,f,\theta),
    $$
    
    the “tree prior” $\smash{P(T\mid t_I,\theta)}$ **does not** depend on the migration parameters $f$.

  - By contrast, in a **MultiTypeTree (MTT)** or **structured coalescent** model, migration **does** directly affect the genealogy: if lineages in the same deme coalesce faster, or if migration rates are low, that changes how quickly lineages coalesce and thus reshapes the branching pattern and times of the tree.

  - So in MTT (structured coalescent):
    
    $$
    P(T, M, \mu, m, \theta \;\big|\; S,t_I,L)
    \;\;\propto\;\;
    \underbrace{P(S \mid T, t_I, \mu)}_{\text{sequence-likelihood}}
    \;
    \times
    \underbrace{P(T, M \mid t_I,L,m,\theta)}_{\substack{\text{structured coalescent prior}\\\text{(tree \textit{and} migration events)}}}
    \;
    \times
    P(\mu)\,P(m)\,P(\theta),
    $$
    the genealogical prior $\smash{P(T,M\mid t_I,L,m,\theta)}$ **does** depend on $m$ (migration rates) and $\theta$, because migration directly changes how/when lineages coalesce and how the tree is shaped.
- Again, for DTA, 
  - one concern is that the assumption that sampling intensity is proportional to subpopulation size leads to biased estimates of migration rates when this assumption is not met (PMID: [22190015](http://www.ncbi.nlm.nih.gov/pubmed/22190015), PMID: [24586153](http://www.ncbi.nlm.nih.gov/pubmed/24586153)).
  - Second, ignoring the population structure when calculating the probability of the coalescent tree could lead to bias or lost power. For example, when migration rates are very low, one expects very long branches close to the root. This interdependency between the shape and branch lengths of the genealogy and the migration process is ignored by DTA, which could reduce accuracy.

#### BASTA

- Overall: 
  1. BASTA integrates over migration histories in a simpler way (treating lineages’ locations as partially independent and discretizing time in sub-intervals).
  2. BASTA still allows coalescence rates to depend on whether lineages are in the same deme (unlike DTA).
  3. Because it approximates the exact (and complex) structured‐coalescent integral, it is computationally cheaper than MTT while retaining more accuracy than DTA.

- BASTA Posterior

  $$
  P(T, \mu, m, \theta \mid S, t_I, L)
  \;\;\propto\;\;
  \underbrace{P(S \mid T, t_I, \mu)}_{\text{sequence likelihood}}
  \;\times\;
  \underbrace{P(T \mid t_I, L, m, \theta)}_{\substack{\text{structured coalescent} \\ \text{(approx.)}}}
  \;\times\;
  P(\mu, m, \theta).
  $$

  - $S$: sequence data  
  - $T$: the genealogy (topology + branch lengths)  
  - $\mu$: mutation/substitution parameters  
  - $m$: migration rates  
  - $\theta$: set of effective population sizes for each deme  
  - $L$: tip locations  
  - $t_I$: sampling times (if heterochronous)

- In **MTT**, the genealogy $T$ and the *explicit* migration events $M$ appear:

  $$
  P(T, M, \mu, m, \theta \;\mid\; S, t_I, L)
  \;\;\propto\;\;
  P(S \mid T, t_I, \mu)
  \;\times\;
  \underbrace{P(T, M \mid t_I, L, m, \theta)}_{\text{structured coalescent prior (exact)}}
  \;\times\;
  P(\mu)\,P(m)\,P(\theta).
  $$

  - MTT attempts to **fully** sample each lineage’s migration path in the genealogy, which becomes computationally expensive for large datasets or many demes.


- BASTA’s Approximation 

  1. **Independent Migration**: By writing

    $$
    P(d_l = d, d_{l'} = d \mid t) \approx P(d_l = d \mid t) P(d_{l'} = d \mid t),
    $$

    we ignore any correlation among lineages' locations (e.g., limited carrying capacity, correlated environment, etc.).

  2. **Discrete Subintervals**: Instead of integrating exactly over time, evaluations are performed at only two points (start/end) per interval, assuming probabilities are constant across each half-interval.

  3. **Matrix Exponential**: The update 

   $$
   P_{l, \alpha_i} = P_{l, \alpha_{i-1}} e^{\tau_i \mathbf{m}}
   $$

    is standard for a continuous-time Markov chain, but applying it only at interval boundaries omits any subtle interactions that might occur mid-interval.

- Why It Makes BASTA Faster

  - **Exact MTT**: Must consider **every** possible lineage location at every moment — this grows combinatorially with number of lineages/demes.  
  - **BASTA**:
    1. Uses **matrix exponentials** to update each lineage’s location probabilities over sub-intervals.  
    2. Approximates that lineages migrate independently within those sub-intervals.  
    3. **Only** updates location probabilities at discrete time points (start/end of sub-intervals), skipping continuous integration.
  - Skipping a full enumeration of migration paths drastically reduces computation. BASTA still incorporates subpopulation structure into coalescent rates (unlike DTA, which ignores it altogether).

### Simulation and results

- DTA overestimates migration rates when sampling intensity does not match subpopulation size.
- DTA Under-represents Uncertainty.
- DTA have lowest accuracy in estimating root locations.

## [SCOTTI:Efficient Reconstruction of Transmission within Outbreaks with the Structured Coalescent](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005130) by *Nicola De Maio et al.* on PLOS Computational Biology, 2016.

### Abstract
- This study demonstrates SCOTTI (Structured COalescent Transmission Tree Inference), for modelling each host as a distinct population, and transmissions between hosts as migration events.