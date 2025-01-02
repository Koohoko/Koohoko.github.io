---
title: "Notes: Structured coalescent"
date: 2024-12-28
permalink: /posts/2024-12-28/Structured_coalescent
categories:
  - Paper digest
tags:
  - Structured coalescent
  - Phylogenetics
toc: true
last_modified_at: 2025-01-02
---

I wanted to get in more details about the structured coalescent model, here I record some notes when I read related papers/tutorials, and watch videos.

# Coalescent quick recap

It is a series of short [Youtube videos by Scott Roy](https://www.youtube.com/playlist?list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu).

- Coalescent is about mathematically trace back in time to find a appropriate tree shape / genealogy that can explain the observed data.
- Geometric Series Summation: $\sum_{i=0}^{\infty}{r^i} = \frac{1}{1-r}$ (note that $0<r<1$, and r can be a probability of coalescence). So that $\sum_{i=0}^{\infty}{(1-p)^i} = \frac{1}{p}$. 
- Time for $n=2$ individuals to coalescence is a classic waiting problem:
$$
P(t)=(\frac{N-1}{N})^{t-1}\frac{1}{N}\\
E(t)=\frac{1}{\frac{1}{N}}=N
$$
- Expected waiting time for coalescence (discrete): 
$$
\begin{align*}
E[t] &= 1p+2p(1-p)+3p(1-p)^2+... \\
&=\sum_{i=0}^{\infty}{(i+1)p(1-p)^i} =\sum_{i=1}^{\infty}{ip(1-p)^i} =\sum_{i=0}^{\infty}{ip(1-p)^i}\\
&=\sum_{i=0}^{\infty}{ip(1-p)^i} + \sum_{i=0}^{\infty}{1p(1-p)^i}\\
&=(1-p)\sum_{i=0}^{\infty}{ip(1-p)^{i-1}}+p\sum_{i=0}^{\infty}{(1-p)^i}\\
&=(1-p)E[t]+p\frac{1}{p}\\
&=\frac{1}{p}
\end{align*}
$$
- Time for $n>2$ individuals to coalescence: 
  - First coalescence:
  $$
  E(t)=\frac{1}{\frac{n\choose2}{N}}=\frac{N}{n\choose2}
  $$
  - Second coalescence:
  $$
  E(t)=\frac{N}{n-1\choose2}
  $$
  - Third coalescence:
  $$
  E(t)=\frac{N}{n-2\choose2}
  $$
  - ...
  - Such that the coalescence time is getting longer for deep branches.
- To jointly model mutation process and coalescent process, we need to consider the mutation rate $\mu$ and coalescent rate $\lambda$. The expected number of mutations before the first coalescence is: 
  $$
  \begin{align*}
  E(mut)&=\frac{\mu}{\lambda}\\
  &=\frac{n\mu}{n\frac{n\choose2}{N}}\\
  &=\frac{2N\mu}{n-1}.
  \end{align*}
  $$

  As a result, the expected number of mutations increases backwards in time (as $n$ is decreasing).
- [Coalescent frequency site distribution](https://www.youtube.com/watch?v=fi5Vd83NA4U&list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu&index=13) can be obtained as a neutral model for genetic variation. Comparing the observed FSD with the expected FSD can help to infer the selection pressure.
- [The expected number of singletons](https://www.youtube.com/watch?v=rHRojlmcM8I&list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu&index=14&pp=iAQB) and [the expected ratio between the number of singletons and the number of SNPs](https://www.youtube.com/watch?v=inTcOOq18ko&list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu&index=18&pp=iAQB) surprisingly can be represented by simple formulas, after canceling out the terms. These can be useful for inferring evolutionary history.
- The probability of particular coalescent tree shapes can also be calculated, often also resulted in simple formulas, as exampled [here](https://www.youtube.com/watch?v=R9Sp6P1ENeo&list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu&index=17&pp=iAQB).
- There is also ways to work out the probability and expected tree lengths for **coalescent subdivisions**, as exampled [here](https://www.youtube.com/watch?v=LCbpXCHdtTk&list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu&index=23). After getting the formula numerically, we can easily tell what will happen e.g. if migration rates is much higher than the coalescent rate (or vice versa).

# Coalescent theory by John Wakeley on a workshop (Second Bangalore School on Population Genetics and Evolution)
This is a quite old series of lectures, but should be relevant.

## [Basic Probability theory](https://www.youtube.com/watch?v=lMegBoAG2zM&list=PL04QVxpjcnji2WV8QIB63JfpzJP_1zecC&index=6)

- Using an example from a Nature paper on 2001: [A map of human genome sequence variation containing 1.42 million single nucleotide polymorphisms](https://www.nature.com/articles/35057149), where they sampled 12027 loci, with each loci spanning ~500bp. They get a summarized table of the number of SNPs in different frequency classes. The data can be used to infer the demographic history of human populations. One need to use a random model to explain the observed data.
  | #SNPs | #loci | Proportion of loci |
  |-------|-------|--------------------|
  | 0     | 8796  | 0.731              |
  | 1     | 2247  | 0.187              |
  | 2     | 668   | 0.056              |
  | 3     | 214   | 0.018              |
  | 4     | 102   | 0.008              |
 
- In this lesson, he recalled concepts of probability theory, including expectation, variance, Bernoulli/Binomial random variables. In a Wright-Fisher model, the number of copies of a particular allele in a population is a binomial random variable. The expected number of copies of a particular allele in a population is $2Np$, and the variance is $2Np(1-p)$.
- $Binomial(n,p) \approx Poisson(np)$ when $n$ is large and $p$ is small, and $np$ becomes $$\lambda$$. $P(K=k)=\frac{\lambda^k}{k!}e^{-\lambda}$, $E(K)=\lambda$, $Var(K)=\lambda$.
- Geometric random variable (waiting time of Binomial trials) has $P(K=k)=(1-p)^{k-1}p$, $E(K)=\frac{1}{p}$, $Var(K)=\frac{1-p}{p^2}$.
- Exponential random variable (waiting time of Poisson events) has $P(K=k)=\lambda e^{-\lambda k}$, $E(K)=\frac{1}{\lambda}$, $Var(K)=\frac{1}{\lambda^2}$.

## [Gene genealogies and coalescent processes](https://www.youtube.com/watch?v=lo864lPyszg&list=PL04QVxpjcnji2WV8QIB63JfpzJP_1zecC&index=9)

- A starting example in this lesson is a Nature paper from Li Heng in 2011: [Inference of human population history from individual whole-genome sequences](https://www.nature.com/articles/nature10231). They estimate the effective population size of human populations using the coalescent theory. They also modeled recombination in the coalescent process.
- Some measures of variations:
  - $S$: number of segregating sites.
  - $\pi$: Nucleotide diversity: average pairwise difference.
  - $Z_i$: (Unfolded) Site frequency spectrum, number of sites with $i$ copies of mutant.
  - $\eta_i$: Folded Site frequency spectrum: number of polymorphic sites where the less-frequent (minor allele) allele has frequency $i$.
- The coalescent, notations:
  - Sample size: $n$.
  - Population size: $N$.
- Number of generations to a coalescent event: $P(G=g)=(1- \frac{n\choose2}{2})^{g-1}\frac{n\choose2}{2}$ as a geometric random variable. Or $f_{T_{n}}(t)={n\choose2}e^{-{n\choose2}t}$ as an exponential random variable, where one unit of time is $N$ generations.
- Expected Number of Segregating Sites:
  - $E[S]=\sim_{i=2}^{n}i\cdot E[T_i]\cdot \theta$:
    - $i$: Number of lineages in a coalescent interval.
    - $E[T_i]$: Expected coalescent time for $i$ lineages, $\frac{2}{i(i-1)}$, note that this is in units of $N$ generations.
    - $\theta$: Scaled mutation rate.
  - Simplified formula: $E[S]=\theta \sum_{i=2}^{n}\frac{1}{i-1}=\theta \sum_{i=1}^{n}\frac{1}{i}$.
- Expected total number of mutations:
  - $K$ follows a Poisson distribution with mean $\frac{\theta}{2}$, where $\theta = 4N_e\mu$ is the scaled mutation rate.
  - $P(K = k \mid \theta) = \frac{\left(\frac{\theta}{2}\right)^k e^{-\frac{\theta}{2}}}{k!}$
     - Describes the probability of observing $k$ mutations.
- Number of Mutations Between Two Sequences ($K_2$)
  - Coalescent Time Distribution:
    - The coalescent time $T_2$ follows an exponential distribution with mean $1$ (in coalescent units): $f_{T_2}(t) = e^{-t}.$

  - Conditional Probability of Mutations Given $T_2$:
    - $K_2$ (number of mutations) follows a Poisson distribution conditioned on $T_2$, with mean $\frac{\theta t}{2}\times 2$:
      $$
      P(K_2 = k \mid T_2 = t) = \frac{\left(\theta t\right)^k e^{-\theta t}}{k!}.
      $$
      - Describes the probability of observing $k$ mutations, given coalescent time $T_2 = t$.

  - Unconditional Probability of Mutations:
    - Marginalizing over all possible $T_2$ values, the probability of $K_2 = k$ is:
      $$
      P(K_2 = k) = \int_0^\infty f_{T_2}(t) \cdot P(K_2 = k \mid T_2 = t) \, dt.
      $$
      - Combines the exponential distribution of $T_2$ with the Poisson mutation process.

  - Resulting Probability:
  $$
  P(K_2 = k) = \left(\frac{\theta}{\theta + 1}\right)^{k} \cdot \frac{1}{\theta + 1}
  $$
  - $\theta$: Scaled mutation rate ($4N_e\mu$).
  - Can be viewed as a geometric distribution with parameter $\frac{1}{\theta + 1}$ (waiting problem for multiple mutations and a final coalescent).

## [Gene genealogies with recombination](https://www.youtube.com/watch?v=NYYtDmiMB9Q&list=PL04QVxpjcnji2WV8QIB63JfpzJP_1zecC)

- Recall the the expected number of segregating sites: $E[S]=\theta \sum_{i=1}^{n}\frac{1}{i}$.
- Note that the expected nucleotide diversity $\pi$ is the average pairwise difference, which is $E[\pi]=\theta$, which is the same as the expected number of segregating sites when $n=2$.
- Expected site frequency spectrum: $E[Z_i]=\frac{\theta}{i}$.
- Tajima's D compares two estimates of genetic diversity to infer deviations caused by selection, demographic events, or other evolutionary processes.
- Recombination complicates coalescent theory because it causes different parts of the genome to have different genealogies, breaking the simple tree-like structure of the standard coalescent process.
  - ![](/files/2024-12-28-structured-coalescent/Screenshot%202024-12-31%20at%2021.53.07.webp)
- Covariance Between Coalescent Times ($T_1, T_2$):
  $$
  \text{Cov}[T_1, T_2] = \frac{\rho + 18}{\rho^2 + 13\rho + 18}
  $$
  - $T_1, T_2$: Coalescent times for two loci.
  - $\rho = 4N_e r$: Scaled recombination rate.
- **Sequential Markov Coalescent (SMC)**, is a computationally efficient approximation to the full **Ancestral Recombination Graph (ARG)**. The SMC framework models the genealogy of sequences along a genome, incorporating recombination to simulate how local genealogies change sequentially along the genome.
  - Instead of modeling the entire recombination history, the SMC assumes a Markovian process for genealogies along the genome.
  - Along the genome, recombination causes the genealogical tree to "switch" to a new topology at certain points.
  - These switches happen at recombination breakpoints and are shown in the diagram as transitions between trees.
- **Identity by Descent (IBD)** occurs when two or more genetic segments in different individuals are inherited from a common ancestor without any intervening recombination or mutation. These segments are identical because they have been directly passed down through generations from the same ancestor.
- IBD can also be view distributed along a genome:
  - ![](/files/2024-12-28-structured-coalescent//Screenshot%202024-12-31%20at%2023.47.12.webp)
- We can also model within the IBD segment, giving a focal point:
  - ![](/files/2024-12-28-structured-coalescent/Screenshot%202025-01-01%20at%2000.34.56.webp)

## [Structured coalescent](https://www.youtube.com/watch?v=avSea13o5Gs&t=16s)
- Non-exchangeability of lineages in structured populations:
  - In structured populations, lineages are not exchangeable because they are more likely to coalesce with lineages from the same subpopulation.
  - This non-exchangeability affects the coalescent process and the genealogies of sequences. 
- He revisit the Markov chain model, specified with a *transition probability matrix*.
  - This matrix describes the probability of transitioning between states (generations) in the Markov chain, with each $P$ representing the probability of transitioning from one state (generation with $i$ lineages) to another state (generation $i-1$ lineages).
- Recall that, based on Wright–Fisher (discrete‐generation) model, $P(i \to i-1) = \frac{\binom{i}{2}}{2N} \prod_{k=2}^{i-1} \left(1 - \frac{k}{2N}\right)$ is the probability that, in the next generation, exactly one pair of the $i$ current lineages coalesces (merges), resulting in $i−1$ distinct ancestral lineages (all the others do not coalesce).
  - If we multiply this by $2N \to\infty$, we get $i\choose2$, this result in the coalescent rate in the time scale of $2N$ generations.
- Wright's Island Model:
  - Notations:
    - $D$: demes (subpopulations).
    - $N$: deme size
    - $m$: migration probability (equally likely to every other deme).
  - When $n=2$, the instantaneous transition matrix (for how long does it take to coalesce) can be derived:
    - State 1: both lineages are in the same deme.
    - State 2: lineages are in different demes.
    - State 3: lineage coalesced. 
    - ![](/files/2024-12-28-structured-coalescent/image.webp)
  - If $m\to0$ in this matrix, we can ignore the $m^2$ terms, then we have:
    - ![](/files/2024-12-28-structured-coalescent/Screenshot%202025-01-01%20at%2017.52.01.webp) 
  - It can be further simplified to the below matrix, if multiplied by $2N$:
  $$ 
    Q =
    \begin{bmatrix}
    -M - 1 & M & 1 \\
    \frac{M}{D - 1} & -\frac{M}{D - 1} & 0 \\
    0 & 0 & 0
    \end{bmatrix}
  $$
  - The waiting time in state 1 is $f_1(t)=(m+1)e^{-(M+1)t}$
  - The waiting time in state 2 is $f_1(t)=(\frac{M}{D - 1})e^{-(\frac{M}{D - 1})t}$
  - $T_w$: Coalescent time (within) for state 1: 
    - $$ 
      \begin{align*}
      E[T_w]&=\frac{1}{M+1}+\frac{M}{M+1}\cdot E[T_b]+ \frac{M}{M+1}\cdot 0 \\
      &=D
      \end{align*}
      $$
  - $T_b$: Coalescent time (between) for state 2:
    - $$ 
      \begin{align*}
      E[T_b]&=\frac{D-1}{M}+ E[T_w] \\
      &=D(1+\frac{D-1}{MD})
      \end{align*}
      $$
- A more relaxed model:
  - Notations:
    - $N_i$: size for deme $i$.
    - $q_{ij}$: migration rate from deme $i$ to deme $j$.
  - The $N_i$ can changed, something similar to the traveler matrix in the metapopulation model is happening.
  - Conservative migration: forwards and backwards migration rates are equal. 

