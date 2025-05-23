---
title: "Course notes: Molecular Evolution workshop in Marine Biological Laboratory, US"
date: 2025-05-22
permalink: /posts/2025-05-22-MBL_ME_worksop
categories:
  - Course notes
tags:
  - Phylogenetics
  - Molecular evolution
toc: true
# last_modified_at: 2025-09-01
---

# Day 1
## Introduction to phylogenetics - Heath

- The Metazoa Phylogeny
  - There is scientific controversy over whether sponges (Porifera) or ctenophores (Ctenophora) are the earliest-diverging animal lineage; traditional morphological evidence supports sponges, but some molecular studies suggest ctenophores may be more basal.
  - This debate impacts our understanding of early animal evolution—especially whether complex traits like nervous systems evolved early and were later lost in sponges, or evolved independently in multiple lineages.
  - Check [this](https://www.nature.com/articles/s41586-023-05936-6) new evidence in Nature.

## Scientific ethics - Bielawski

- Ethical reasoning focus on what *I* (or *we*) should do, but not blaming others.
- Normalization of Deviance, you should not start doing something just because it is common, or you think it has small consequences.
- Take the anti-vax movement as an example, at first it was a small group of people (deviance, Andrew Wakefield etc.), but then it became normalized and now it is a big problem.
- If you do noting, you can be contributing to normalization of deviance.
- Scientist have social privilege, and they have obligations.

##	Introduction to Likelihood - Lewis

- Why do we need the term likelihood?
  - Probability is describing the chance of an **event/outcome/data** given one model.
  - Likelihood is describing the **model/hypothesis/parameter** given data.
- Transition-transversion rate ratio = 1 equivalent to transition-transversion rate = 0.5.
- Site specific rate variation, e.g. $r_1$ for codon positions 1 and 2, $r_2$ for codon position 3.
- He said that even though the parameter in the Gamma and invariable site models can have correlation, a successful bayesian search algorithm should be able to deal with this, and there are no issue with identifiability. 

## Model-based phylogenetics - Huelsenbeck

- Both likelihood and distance methods can marginalize different histories along the branch (via the CTMC model).
- He revisited the Felsentein pruning algorithm.
- He explained the interpretation of the $Q$ matrix: If the process is in state $i$, we wait an exponentially distributed amount of time with parameter $-q_ii$ until the next substitution occurs; The change (after time of $e^{-q_ii}$) is $\frac{q_ij}{-q_ii}$ if the next state is $j$.
- Explained exponential distribution (waiting time for the first event), the gamma distribution (sum of exponential), the Poisson distribution (number of events in a time interval).
- One can simulate these mutations by simulating the waiting time until the next mutation, and then the change.
- You will arrive at the same result to $P(t)=e^{Qt}$. This accounts for all the ways that the process, starting in state $i$, can end up in state $j$ after time $t$.
- Note that there are two different marginalization: one is the marginalization of the history (Felsenstein), and the other is the marginalization of the multiple hits ($P(t)$).
- Stationary: if the branch length is long enough, no matter where you start, you will end up in one state with equal probability.
- We rescale the Q matrix such that the average rate of the process is $1$, then the time parameter $t$ in $P(t)=e^{Qt}$ directly represents the expected number of substitutions per site (the unit of the branch lengths). When $Q$ is scaled this way, the length of a branch ($v$) is directly interpretable as the expected number of substitutions that have occurred per site along that lineage.




# Day 2

## Simulating molecular evolution - Huelsenbeck