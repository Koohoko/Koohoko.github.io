---
title: "Book notes: Molecular Evolution: A Statistical Approach by Ziheng Yang"
date: 2025-01-18
permalink: /posts/2024-01-18/mol_evo_stat_appr # this was a typo, should be 2025, but I will keep it for consistency as I already shared it.
categories:
  - Book notes
tags:
  - Molecular evolution
  - Statistical methods
toc: true
last_modified_at: 2025-02-19
---

We decide to read the book [*Molecular Evolution: A Statistical Approach*](http://abacus.gene.ucl.ac.uk/MESA/) by Ziheng Yang, to gether on a weekly basis. 

# Models of nucleotide substitution

- We define $p$ distance as thr proportion of sites that differ between two sequences.
- The true evolutionary distance $d$ is the expected number of substitutions per site between two sequences.
- CTMC (Continuous Time Markov Chain): four nucleotides are *states* of the chain, it will reach to *steady state* with a *stationary distribution*, via a *substitution rate matrix*.

## Markov models of nucleotide substitution and distance estimation

### The JC69 model

- Jukes-Cantor 1969 model.
- The substitution rate matrix $Q$ is
  $$
  Q = \begin{pmatrix}
  -3\lambda & \lambda & \lambda & \lambda \\
  \lambda & -3\lambda & \lambda & \lambda \\
  \lambda & \lambda & -3\lambda & \lambda \\
  \lambda & \lambda & \lambda & -3\lambda
  \end{pmatrix}
  $$
- The matrix of transition probability: $P(t) = e^{Qt}$. This is using Kolmogorov forward/backward? equation, where $\frac{dP(t)}{dt} = QP(t)$.
- We then use Taylor expansion to get $P(t) = I + Qt + \frac{Q^2t^2}{2!} + \cdots$.
  - [Essense of calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) by 3Blue1Brown.
    - [Taylor polynomial](https://www.youtube.com/watch?v=3d6DsjIBzJ4)
- Chapman–Kolmogorov equation: $P_ij(t+s) = \sum_k P_ik(t)P_kj(s)$. This account for the multiple (hidden) states between $i$ and $j$.
- As $d=3\lambda t$, then $p(d) = 3p_1(t)=\frac{3}{4}-\frac{3}{4}e^{-4\lambda t}=\frac{3}{4}-\frac{3}{4}e^{-4d/3}$, then $\hat{d}=-\frac{3}{4}log(1-\frac{4}{3}\hat{p})$.

### The K80 model

- Kimura 1980 model.
- Transitions: pyrimidine (T $\leftrightarrow$ C), purine (A $\leftrightarrow$ G).
- Transversion: (T, C $\leftrightarrow$ A, G).
- $d = (\alpha + 2\beta)t$.
- $\kappa = \frac{\alpha}{\beta}$.
- $E(S) = p_1(t)$.
- $E(V) = 2p_2(t)$.
- $\hat{d} = -\frac{1}{2} \log(1 - 2S - V) - \frac{1}{4} \log(1 - 2V)$.

### HKY85, F84, TN93, etc.

#### TN93

- Tamura-Nei 1993 model.
- 7 parameters and 6 free parameters.
- $\pi_Y = \pi_T + \pi_C$ and $\pi_R = \pi_A + \pi_G$.
- $P(t)$ can be solved using spectral decomposition of $Q$.
  - $Q = U \Lambda U^{-1}$.
  - $\Lambda = \text{diag}\lbrace \lambda_1, \lambda_2, \lambda_3, \lambda_4 \rbrace$.
  - $P(t) = U e^{\Lambda t} U^{-1} = U \text{diag}\lbrace e^{\lambda_1 t}, e^{\lambda_2 t}, e^{\lambda_3 t}, e^{\lambda_4 t} \rbrace U^{-1}$.
  - [Essense of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) by 3Blue1Brown.
    - [Eigenvectors and eigenvalues](https://www.youtube.com/watch?v=PFDu9oVAE-g) with prerequisites:
      - [Linear transformations](https://www.youtube.com/watch?v=kYB8IZa5AuE)
      - [Matrix multiplication](https://www.youtube.com/watch?v=XkY2DOUCWMU)
      - [Determinants](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
      - [Linear systems](youtube.com/watch?v=uQhTuRlWMxw)
      - [Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA), Jennifer is a French as indicated in 3:21 of this video :D
- $\lambda = -\sum_i \pi_i q_{ii} = 2\pi_T \pi_C \alpha_1 + 2\pi_A \pi_G \alpha_2 + 2\pi_Y \pi_R \beta$.
- $d = \lambda t$.
- Using $E(S_1), E(S_2), E(V)$ to estimate $\alpha_1, \alpha_2, \beta$.
- $\hat{d}$ can be represented as a function of nucleotide frequencies and $E(S_1), E(S_2), E(V)$.

#### HKY85 and F84

- 6 parameters and 5 free parameters.

- Hasegawa-Kishino-Yano 1985 model.
  - Interesting fact: it should be called HKY84, misnamed in *Yang 1994*.
  - Setting $\alpha_1 = \alpha_2 = \alpha$ or $\kappa_1 = \kappa_2 = \kappa$ in TN93 model.
- Felsenstein 1984 model.
  - Setting $\alpha_1 = (1+\kappa/\pi_Y)\beta$ and $\alpha_2 = (1+\kappa/\pi_R)\beta$ in TN93 model.
  - It is easier to derive a distance formula for F84 than for HKY85.
- Felsenstein 1981 model.
  - Setting $\alpha_1 = \alpha_2 = \beta$ in TN93 model.
  - A distance formula was derived by *Tajima and Nei (1982)*.
    - On a side note, *Tajima and Nei (1984)* is a classic paper on nucleotide diversity.

### The transition/transversion rate ratio

- Three definitions:
  - $E(S)/E(V) = p_1(t)/2p_2(t)$ under the K80 model (the uncorrected method).
  - $\kappa = \alpha/\beta$ under the K80 model (corrected).
  - $R = \alpha/2\beta$ under the K80 model (corredted). It's called *average transition/transversion ratio*. More generally, $R = \frac{\pi_T q_{TC} + \pi_C q_{CT} + \pi_A q_{AG} + \pi_G q_{GA}}{\pi_T q_{TA} + \pi_T q_{TG} + \pi_C q_{CA} + \pi_C q_{CG} + \pi_A q_{AT} + \pi_A q_{AC} + \pi_G q_{GT} + \pi_G q_{GC}}$ under UNREST.

## Variable substitution rates among sites

- Assuming the rate $r$ for any site is drawn from a gamma distribution.
- Models with *Gamma distance* denoted by a suffix '$+\Gamma$'.
- Gamma distribution have two parameters: shape $\alpha$ and scale $\beta$. The mean is $\alpha/\beta$, and the variance is $\alpha/\beta^2$. You can also consider them as number of Poisson process events of $\alpha$ with rate $1/\beta$.
- Note that the gamma distribution here sets $\alpha = \beta$ so that the mean equals to $1$.
- If a site has a rate $r$, the distance between sequences becomes $d = r t$.
- $p(d\cdot r)$ can be calculated by integrating the gamma distribution.
- For JC69 model, $p = \int_0^\infty \left( \frac{3}{4} - \frac{3}{4} e^{-4d \cdot r / 3} \right) g(r) \, dr 
= \frac{3}{4} - \frac{3}{4} \left( 1 + \frac{4d}{3\beta} \right)^{-\alpha}$.
- Similarly, one can derive a gamma distance under virtually every model for which a one-rate distance formula is available.
- It is well known that ignoring rate variation among sites leads to underestimation of both the sequence distance and the transition/transversion rate ratio.

## Maximum likelihood estimation of distance

- The likelihood function is $L(\theta; X) = f(X\vert\theta)$.
- MLE is the value of $\theta$ that maximizes the likelihood function.
- Probability vs. Likelihood:
  - Likelihood $\ne$ Probability: Likelihood does not sum to 1, unlike probability.
  - Interpretation: Probability is understood by area under the curve, while likelihood is compared at specific points.
  - Reparametrization: Likelihood is invariant under monotonic transformations, so MLEs remain unchanged.
  - Nonlinear Effects: Nonlinear transformations alter probability density shapes, potentially changing modality.

### The JC69 model

- The single parameter is the distance $d = 3\lambda t$. The data are two aligned sequences, each $n$ sites long, with $x$ differences.
- $p = 3p_1(t) = \frac{3}{4} - \frac{3}{4} e^{-4d/3}$.
- The likelihood function is $L(d; X) = {n\choose x}p^x(1-p)^{n-x}$.
- After reparametrization: $L(d; X) = (\frac{1}{4}p_1)^x (\frac{1}{4}p_0)^{n-x}$. (I think $\frac{1}{4}$ can be further dropped.)
- Two approaches to estimate confidence intervals:
  - Normal approximation: $\hat{d} \pm 1.96 \sqrt{var({d})}$.
  - Likelihood interval, based on likelihood ratio test: $\frac{1}{2}\chi^2_{1, 5\%} = 3.841/2 = 1.921$.

### The K80 model

- $L(d, \kappa; n_S, n_V) = \left( \frac{p_0}{4} \right)^{(n - n_S - n_V)} \times \left( \frac{p_1}{4} \right)^{n_S}  \times \left( \frac{p_2}{4} \right)^{n_V}.$
- $\frac{1}{2}\chi^2_{2, 5\%} = 5.991/2 = 2.995$.

### Likelihood ratio test of substitution models

- For model comparison, if two models are **nested**, then the likelihood ratio test can be used.

### Profile and integrated likelihood

- The above approaches, estimating one parameter while ignoring the other, are called *relative likelihood*, *pseudo likelihood* or *estimated likelihood*.
- A more respective approach is *profile likelihood*.
  - $\ell(d) = \ell(d, \hat{\kappa}_d)$, where $\hat{\kappa}_d$ is the MLE of $\kappa$ for the given $d$.
  - This is a pragmatic approach that most often leads to reasonable answers.
- *Integrated likelihood* or *marginal likelihood* is the likelihood of the data given the model, averaged over the parameter space.
  - It is possible to use a improper prior, such as a uniform distribution, to calculate the marginal likelihood.
  - Integrated likelihood is always smaller than the profile likelihood.

## Markov chains and distance estimation under general models

### Distance under the unrestricted (UNREST) model

- Unlike the **GTR model**, UNREST does not assume time-reversibility.
- Here we consider a strand-symmetry model, where $q_{TC} = q_{AG}$.
- Equilibrium nucleotide frequencies $\{\pi_T, \pi_C, \pi_A, \pi_G\}$ perhaps by coincidence, can be estimated analytically.

1. **Identifiability Issues and Distance Calculation**
   - The **model can, in theory, identify the root** of a two-sequence tree.
   - However, **estimating both $t_1$ and $t_2$ separately** leads to **high correlation** between estimates.
   - The model has **13 parameters**:  
     - **11 rate parameters** in $Q$.
     - **2 branch lengths** $t_1, t_2$.
   - **Challenges:**
     - No analytical solution for MLEs.
     - Complex eigenvalues make numerical estimation difficult.
     - Many datasets do not provide enough information to estimate so many parameters.
   - **Conclusion:**  
     - Although $t_1$ and $t_2$ are **identifiable**, their estimates are **highly correlated**.
     - The UNREST model **is not recommended for distance calculations**.

### Distance under the general time-reversible model
1. **Time-Reversibility in Markov Chains**
   - A Markov chain is **time-reversible** if:
     $$
     \pi_i q_{ij} = \pi_j q_{ji}, \quad \text{for all } i \neq j.
     $$
     This condition is known as **detailed balance**.
   - **Reversibility is a mathematical convenience**, not necessarily a biological property.
   - Models such as **JC69, K80, F84, HKY85, and TN93** are all **time-reversible**.

2. **Rate Matrix for GTR Model**
   - The **GTR (General Time-Reversible) model** is defined using the rate matrix:
     $$
     Q = 
     \begin{bmatrix}
     \cdot & a\pi_C & b\pi_A & c\pi_G \\
     a\pi_T & \cdot & d\pi_A & e\pi_G \\
     b\pi_T & d\pi_C & \cdot & f\pi_G \\
     c\pi_T & e\pi_C & f\pi_A & \cdot
     \end{bmatrix}
     $$
     - It has **nine free parameters** (six substitution rates + three equilibrium frequencies).

3. **Simplification of Likelihood Computation**
   - Reversibility simplifies likelihood computation:
     $$
     f_{ij}(t_1, t_2) = \sum_k \pi_k p_{ki}(t_1) p_{kj}(t_2) = \pi_i p_{ij}(t_1 + t_2).
     $$
     - The second equality follows from **reversibility**.
     - The third equality follows from the **Chapman-Kolmogorov theorem**.
     - This allows estimation of **total branch length** instead of individual times.

4. **Log-Likelihood Formulation**
   - The log-likelihood function is:
     $$
     \ell(t, a, b, c, d, e, f, \pi_T, \pi_C, \pi_A) = \sum_i \sum_j n_{ij} \log(\pi_i p_{ij}(t)).
     $$
   - After scaling, the **distance** is defined as:
     $$
     d = -t \sum_i \pi_i q_{ii} = t.
     $$

- Note that **distance formulae are not MLEs**.
  - Observed base frequencies are not MLEs of the base frequency parameters.
  - All 16 site patterns have distinct probabilities in the likelihood function but are collapsed in distance formulae (e.g., TT, CC, AA, GG).
  - Despite this simplification, distance formulae still approximate MLEs well.
- Pairwise comparisons **sum up branch lengths** but may **overestimate distances**.
- Likelihood-based methods (**ML, Bayesian**) provide **better phylogenetic estimates**.

# Models of amino acid substitution and codon substitution

## Models of amino acid replacement

### Empirical models

- Empirical models: 
  - The rates of substitution are estimated directly from observed sequence variations, without explicitly considering the biological processes that drive these substitutions.
  - They are statistical and data-driven, without needing detailed knowledge of the underlying biological mechanisms.
- Mechanistic models:
  - They are based on the underlying biological processes that drive sequence evolution.
  - They offer more interpretative power, helping to understand the biological mechanisms and evolutionary forces that shape protein sequences.
- Empirical models of amino acid substitution are ***all*** constructed by estimating the relative substitution rates between amino acids under the GTR model.
- Under GTR, $\pi_i q_{ij} = \pi_j q_{ji}$ and $\pi_i p_{ij}(t) = \pi_j p_{ji}(t)$, with $i,j \in \{1,2,\ldots,20\}$.
- $q_{ij}$ or $s_{ij}$ are the amino acid *exchangeabilities*.
- Dayhoff (1978) and JTT (1992): fixed estimates.
- Dayhoff+F, JTT+F, add 19 free parameters by replacing the $\pi_i$
in the empirical matrices by the frequencies estimated from the data.
- WAG (2001), LG (2008) etc. use maximum likelihood to estimate the exchangeabilities.
- BLOSUM (1992) focus on more conserved regions in protein families.
- BLOSUM62 is often considered roughly equivalent to PAM250.
- Some features in the estimated exchangeabilities are in fact as expected from the physico-chemical properties of amino acids. Also the larger number of substitution events needed to change between two amino acids, the lower the exchangeability. Evidence by comparing the exchangeabilities in normal proteins and mitochondrial proteins (codon table is different).

### Mechanistic models

- Yang et al. (1998) implemented a few mechanistic models, taking account of e.g. different mutation rates between nucleotides, translation of the codon triplet into amino acid, and acceptance or rejection of the amino acid due to selective pressure on the protein.
- The improvement was not extraordinary, perhaps reflecting our poor understanding of which of the many chemical properties are most important and how they affect amino acid substitution rates

### Among-site heterogeneity

- Dayhoff+$\Gamma$, JTT+$\Gamma$, etc. are similar to the nucleotide models with among-site rate variation. $rQ$ is the rate matrix for a site.
- Recall that in the Gamma model, we delibrately set $\alpha = \beta$ so that the mean is 1. The higher the $\alpha$, the more concentrated the distribution is around the mean.
- Site-specific amino acid frequency parameters is also possible. For each (group of) site, this reflects how likely different amino acids are to appear (different patterns). However, this approach adds many parameters, making it challenging for maximum likelihood (ML) analysis.

## Estimation of distance between two protein sequences

### The Poisson model

- The number of substitutions over time $t$ can be a Poisson-disributed random variable under rate $\lambda$.
- Similar to JC69 model, the expected number of substitutions is $d = 19\lambda t$.
- Similarly, the expected distance is $\hat{d} = -\frac{19}{20}\log(1-\frac{20}{19}\hat{p})$. If $p > \frac{19}{20}$, then $\hat{d} = \infty$.

### Empirical models

- We deliberately set $-\sum_i \pi_i q_{ii} = 1$ so that $d = 1 \times t$, the mean distance is 1.
- Under GTR, the log-likelihood function is $\ell(t) = \sum_i \sum_j n_{ij} \log(\pi_i p_{ij}(t))$.
- We can also use $p$ distance, $p = 1 - \sum_i \pi_i p_{ii}(t)$, but this will lose information, nevertheless, should approximate the MLE well.

### Gamma distance

- Under something similar to JC69, adding a gamma distribution to the rate of substitution, we have $\hat{d} = \frac{19}{20} \alpha [(1 - \frac{20}{19}\hat{p})^{-\frac{1}{\alpha}} - 1]$. This is obtained by integration of the gamma distribution over the formula for $p$ distance (see formula 1.35).
- For empirical models, use ML to estimate the distance.

## Models of codon substitution

### The basic model

- The instantaneous rate matrix $Q$ is a $61 \times 61$ matrix.
- 
  $$
  q_{IJ} = \begin{cases}
  0, & \text{if I and J differ at two or three codon positions,} \\
  \pi_J, & \text{if I and J differ by a synonymous transversion,} \\
  \kappa\pi_J, & \text{if I and J differ by a synonymous transition,} \\
  \omega\pi_J, & \text{if I and J differ by a nonsynonymous transversion,} \\
  \omega\kappa\pi_J, & \text{if I and J differ by a nonsynonymous transition.}
  \end{cases}
  $$
- $\omega$ is the nonsynonymous/synonymous rate ratio. If $\omega > 1$, it indicates positive selection, if $\omega < 1$, it indicates purifying selection.
- Fequal model: $\pi_i = 1/61$.
- F1x4 model, F3x4 model, and F61 model: $\pi_i$ are estimated from the data.
- The rate matrix $Q$ time-reversible as it meets the detailed balance condition.

### Variations and extensions

- The Muse-Gaut model (1994) is a generalization of the basic model.
  - Simialr to F3x4 with omega?
- The mutation-selection (FMutSel) model.
  - mutation bias: $\mu_{ij} = a_{ij} \pi^*_j$.
  - selection: $S_{IJ} = f_J - f_I$.
  - The probability of fixation of the mutation is $P_{IJ} = \frac{2S_{IJ}}{1 - e^{-2NS_{IJ}}}$.
- The $\omega$ ratio does not have to be a single parameter, it can be modelled by physico-chemical properties, e.g. $\omega_{IJ} = ae^{-bd_{IJ}}$, where $d_{IJ}$ is the chemical distance between amino acids.
- Or you can model $\omega$ by a few pre-specified categories of nonsynonymous substitutions.
- Allowing double or triple mutations should be more realistic. It is common to observe ‘synonymous’ differences between the two sets of serine codons (TCN and AGY) which cannot exchange by a single nucleotide mutation. Some people argue this is because separate lines of descent rather than multiple mutations.

## Estimation of $d_S$ and $d_N$

- Recall that the evolutionary distance $d$ focuses on the entire sequence, now we want to separate the distance by synonymous and nonsynonymous mutations, then we get $d_S$ and $d_N$.
- Definitions: The number of synonymous/nonsynonymous substitutions per synonymous/nonsynonymous site.
- Methods: Counting and ML.

### Counting methods

- Three steps:
  1. Count the number of synonymous and nonsynonymous sites.
  2. Count the number of synonymous and nonsynonymous differences.
  3. Calculate the proportions of differences and correct for multiple hits.
- A basic model is Nei and Gojobori (1986) (NG86), which used equal weights for all codon positions.

#### Counting sites ($S$ and $N$)

- Introducing NG86 model, then relax the model with unequal transition and transversion rates and
unequal codon usage. Different methods often produce very different estimates.
- There are three sites in a codon, and nine immediate neighbors.
- To calculate the synonymous and nonsynonymous sites, we need to multiply the synonymous/nonsynonymous probabilities (from the nine neighbors) by 3 sites. (Check Table 2.5)

#### Counting differences ($S_d$ and $N_d$)

- If two codons only differ by one nucleotide, then it is trivial to count the synonymous and nonsynonymous differences. (Check Table 2.6)
- If two codons differ by two or three nucleotides, there exist two or six possible paths to reach the codon, respectively.
- Weighting the paths needs knowledge.

#### Correcting for multiple hits

- We now have the $p$ distance, $p_S = S_d/S$ and $p_N = N_d/N$.
- The Jukes-Cantor correction is $d_S = -\frac{3}{4}\log(1 - \frac{4}{3}p_S)$ and $d_N = -\frac{3}{4}\log(1 - \frac{4}{3}p_N)$.
- This is logically flawed (Lewontin 1989), as JC69 assumes equal rates of substitution for all three other nucleotides, but when focusing on synonymous/nonsynonymous sites only, each nucleotide does not have *three* other nucleotides to change into.

#### Transition–transversion rate difference and codon usage

- From codon table, we see transitions at the third codon positions are more likely to be synonymous than transversions are. Therefore, a higher transition/transversion rate can lead to more synonymous substitutions, not necessarily due to selection. Ignoring this can lead to underestimation of $S$ (not $S_d$) and overestimation of $N$, and overestimation of $d_S$ and underestimation of $d_N$.
- The below methods classified codon positions into *nondegenerate, two-fold degenerate, and four-fold degenerate sites*, based on the number of synonymous substitutions possible. Note that some of the codons in fact do not fall into these categories, different methods may have different ways to deal with them.
- LWL85 Method (Li, Wu, and Luo, 1985):
  - Counts two-fold degenerate sites as 1/3 synonymous and 2/3 nonsynonymous under the assumption of equal mutation rates.
  - The distances are calculated using the total numbers of sites in different degeneracy classes and the estimated transition and transversion counts.
- LPB93 Method (Li, Pamilo, and Bianchi, 1993):
  - Adjusts for transition–transversion rate bias (which was ignored by 1/3 and 2/3 approximation in LWL85). 
  - Uses the transition distance at four-fold sites to estimate $d_S$​ and an averaged transversion distance at nondegenerate sites for $d_N$.
  - Assuming that the transition rate is the same at the two-fold and four-fold sites; the transversion rate is the same at the nondegenerate and two-fold sites.
- LWL85m Method:
  - A refinement of LWL85 that replaces the 1/3 assumption with an estimated proportion ($\rho$) of two-fold degenerate sites that are synonymous.
  - Uses the ratio of transition and transversion distances at four-fold sites to estimate $\kappa$ (transition/transversion rate ratio).
- Alternative Approaches:
  - Ina (1995) proposed not partitioning sites by codon degeneracy but instead weighting transitions and transversions based on neighboring codons (See Table 2.5).
  - Consideration of *unequal codon frequencies* was introduced by Yang and Nielsen (2000), as previous models assumed equal codon frequencies, which is unrealistic.
- Example 2.2 is useful for understanding the above calculations.
- In Table 2.8, we see S are larger in LWL85m and Ina95, as they accounted for underestimation of S by considering ts/tv ratio, but **ironically**, they led to even more biased results, because they did not consider codon usage bias at the same time.

### Maximum likelihood methods

- Under the [basic model for codon substitution](#the-basic-model), which is a GTR again.
- Parameters estimated:
  - $t$ (sequence divergence time or distance),
  - $\kappa$ (transition/transversion rate ratio),
  - $\omega$ (nonsynonymous/synonymous rate ratio),
  - Codon frequencies (either fixed or estimated from the data), can be Fequal, F1x4, F3x4, or F61.
- $d_S$ and $d_N$ are then computed based on these ML estimates.
- Refer to Table 2.8, the Fequal with $\kappa=1$ is similar to NG86, and Fequal with $\kappa$ estimated is similar to LWL85, LPB93 and Ina95.
- Note that incorporating the transition–transversion rate difference has had much greater effect on the numbers of sites ($S$ and $N$) than on the numbers of substitutions ($S_d$ and $N_d$).

### Comparing methods

- Estimation Bias and Model Effects:
  1. Ignoring Transition–Transversion Rate Differences: 
     - Leads to underestimation of synonymous sites ($S$) and overestimation of nonsynonymous sites ($N$).
     - Results in overestimation of $d_S$ and underestimation of $\omega = d_N/d_S$.
  2. Ignoring Unequal Codon Usage:
     - Has the opposite effect compared to ignoring transition–transversion rates.
     - Leads to overestimation of $S$ and underestimation of $d_S$, which in turn overestimates $ω$.
     - Codon frequency biases can sometimes override the effects of transition–transversion biases.
     - The NG86 method, which ignores both transition–transversion differences and codon usage, sometimes produces more reliable estimates than models that only accommodate transition–transversion biases but ignore codon usage.
  3. Effect of Model Assumptions on Similar Sequences:
     - When sequences are highly similar, different methods can produce very different estimates.
     - Unlike nucleotide models, where distance estimates converge at low sequence divergences, codon-based models remain highly sensitive to assumptions.
  4. Importance of Model Assumptions:
     - At low or moderate sequence divergences, different (counting or ML) methods produce similar results if they share the same assumptions.
     - However, different counting/likelihood methods produce highly variable results because of differnt assumptions (e.g., $\kappa = 1?$ and codon bias).
- Advantages of the Likelihood Method Over Counting Methods:
  1. Conceptual simplicity
     - Counting methods struggle with different transition/transversion rates and **unequal codon frequencies**.
     - Some counting methods **attempt to estimate $\kappa$**, but this is challenging.
     - Counting methods rely on **nucleotide-based corrections for multiple hits**, which can be logically flawed (mentioned under formula 2.15).
     - Likelihood methods **incorporate these complexities naturally** without requiring correction formulas.
     - No need for **manual classification of synonymous vs. nonsynonymous substitutions**, as these are **inferred probabilistically**.
  2. Easier to Incorporate Realistic Codon Models
     - Likelihood methods can **incorporate sophisticated codon substitution models**.
     - Example: **GTR-style mutation models** or **HKY85-type models** can be used in likelihood calculations.

### More distances and interpretation of the dN/dS ratio

#### More distances based on the codon model
- Additional Distance Measures in the Codon Model
  - Since we can get the expected number of substitutions from **codon $i$ to codon $j$** over time $t$ is given by $\pi_i q_{ij} t$.
  - We can calculate many other distances, not limited to $d_N$ and $d_S$, based on:
    - Transition vs. transversion substitutions.
    - Codon position-specific changes (first, second, third codon positions).
    - Conservative or radical amino acid changes, etc.
- Distances at Different Codon Positions
  - Distances at the first, second, and third codon positions can be calculated separately:
    - $d_{1A}, d_{2A}, d_{3A}$ → **After** selection on the protein.
    - $d_{1B}, d_{2B}, d_{3B}$ → **Before** selection on the protein (fixing $\omega = 1$).
- Distance $d_4$ (Four-Fold Degenerate Sites)
  - **$d_4$** represents substitutions at **four-fold degenerate sites** in the third codon position.
  - Used as an **approximation of the neutral mutation rate**.


### Estimation of dS and dN in comparative genomics

# phylogenetic reconstruction: overview

# Maximum likelihood methods

# Comparison of phylogenetic methods and tests on trees

# Bayesian theory

# Bayesian computation (MCMC)

# Bayesian phylogenetics

# Coalescent theory and species trees

- Statistical analysis of sequence data from a few closely related species (statistical phylogeography, Knowles 2009) lies at the interface between population genetics and phylogenetics. 
- Trends in theoretical population genetics:
  - In the time of R.A. Fisher, J.B.S. Haldane, and S. Wright (1920–1930s), or of G. Malecot and M. Kimura (1950–1970s), there was much theory but little data, and the work was mostly concerned with probabilistic predictions of the model behaviour, i.e. how allele frequencies change over generations when the parameters in the model take certain values.
  - Nowadays there is more data than we can analyse, and the focus of the field has shifted to statistical inference, i.e. parameter estimation and hypothesis testing using genomic sequence data. 
  - Coalescent approach became central.
  - More computation for modern inference methods.

## The coalescent model for a single species

### The backward time machine

- The coalescent theory, also known as Kingman’s coalescent, was developed in the early 1980s.
- Classical population genetics models are forward in time, making predictions about allele frequencies changes over generations under the influence of mutation, genetic drift, population sub-division, and selection.
- Coalescent approaches are backward, tracing the genealogical relationships of the samples until MRCA is reached.
- Advantages:
  - Usually easier to model the genealogy, as we can ignore the rest of the population and simply focus on the lineages that are ancestral to the sample.
  - Separating genealogy from neutral mutations allows us to derive the tree likelihood under many population genetic models. We can 'drop' the mutations onto the tree afterwards.
- Molecular phylogenetics focuses on reconstructing the species tree, showing how species or genes diverged.
- Coalescent theory uses genetic variation data, reconstructing the unobserved genealogies backward in time to infer population dynamics and evolutionary forces.

### Fisher–Wright model and the neutral coalescent

- Idealized population: constant population size ($N$), non-overlapping generations, random mating (panmixia), and neutral evolution.
- Number of genes $2N$ in diploid, no recombination.
- The coalescent waiting time is shorter when the population size is smaller.
- If the population size is changing over generations, $N_e$ is given by the harmonic mean, which is dominated by small values (population bottlenecks) and is much smaller than the arithmetic mean.
- The probability that two genes coalesce in the $i$ generation is $(1 - \frac{1}{2N})^i \times \frac{1}{2N} \approx \frac{1}{2N}e^{-\frac{i}{2N}}$. 
  - If viewing under that time unit of $2N$ generations ($T = \frac{i}{2N}$), with mean and variance 1 (in $2N$ generations), the probability density is $e^{-T}$.
  - If using a time scale with mean and variance $2N\mu$, the probability density is $\frac{1}{2N\mu}e^{-\frac{1}{2N\mu}T}$.
- Population size parameter $\theta = 4N\mu$. It is the expected number of mutations per site between two genes.

### A sample of $n$ genes

