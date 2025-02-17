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
last_modified_at: 2025-01-19
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
- Empirical models of amino acid substitution are all constructed by estimating the relative substitution rates between amino acids under the GTR model.
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

TODO