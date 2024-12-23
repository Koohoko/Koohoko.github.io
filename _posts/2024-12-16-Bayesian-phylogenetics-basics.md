---
title: "Course notes: Bayesian phylogenetics basics"
date: 2024-12-16
permalink: /posts/2024-12-16/Bayesian-phylogenetics-basics
categories:
  - Course notes
tags:
  - MCMC
  - Phylogenetics
toc: true
# last_modified_at: 2024-09-01
---

This a short seminar gave by Sebastian Duchene and John Tay. On the basics of Bayesian phylogenetics.

## Main
The overall goal is to calculate the likelihood multiplying the priors, such that we can get the posterior distribution of all parameters given the data. This is done by MCMC.

$P(Tree, \theta, M, \sigma, \alpha, \vec{r}|D) \propto P(D|Tree, \vec{r}, \alpha)P(Tree|\theta)P(\vec{r}|M,\sigma)P(\theta)P(\alpha)P(M)P(\sigma)$

---

\(D\): data

\(\theta\): a parameter in coalescent model

\(P(D|Tree, \vec{r}, \alpha)\): phylogenetic tree likelihood

\(P(Tree|\theta\): tree prior (or coalescent likelihood) with $\theta$ being a parameter related to the tree branching or coalescent process.

\(P(\vec{r}|M,\sigma)\): clock prior, specifying branch rates, can be calculated using `dlognorm` etc.

## Example

Example in a ultrametric time tree.

$Tree$ is in time unit (time tree), but final tree is in genetic distance, so we need to multiply the time tree by the substitution rate tree (in nucleotide/site/time).

$LNORM(M,\sigma)$ for branch rates, specifying a relaxed clock model.

If we only have the genetic distance tree (the only thing we can get from data), the time tree and the substitution rate tree will be unidentifiable, we need to fix some parameters in advance. Brach rates often have a mean of 1 the prior to avoid non-identifiability with the clock rate.

$Q$ is the matrix of transition rates between nucleotides, exampled with JC69 model.

log-likelihood of a coalescent tree under the Kingman’s coalescent model with a constant population size parameter, $\theta$:

$t=\{0,1,2\}$

$n=3$

$\theta=1$ # genetic diversity, "effective population size"

$ln(P(Tree|\theta))=\sum_{i=1}^{n-1}{ln({n-i+1\choose2})-ln(\theta)-{n-i+1\choose2}\frac{t_{i+1}-t_i}{\theta}}$

---