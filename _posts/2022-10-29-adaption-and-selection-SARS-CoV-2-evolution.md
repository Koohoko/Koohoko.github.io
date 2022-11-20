---
title: "Paper digest: Adaption and Selection in SARS-CoV-2 evolution"
date: 2022-10-30
permalink: /posts/2022-10-29/2022-10-29-adaption-and-selection-SARS-CoV-2-evolution
categories:
  - Paper digest
tags:
  - Bioinformatics
  - Virus evolution
# last_modified_at: 2022-09-01
---

The paper titled [Contributions of adaptation and purifying selection to SARS-CoV-2 evolution](https://www.biorxiv.org/content/10.1101/2022.08.22.504731v1) analysed the evolutionary patterns of SARS-CoV-2 using a large dataset of genomic sequences. The author estimated rates of evolution (synoymous and non-synonymous mutations) using consensus sequences within clades. The results suggest that: 
1. synonymous mutation rates are similar between variants; 
2. non-synonymous rates slowed down in 2021 and 2022; 
3. the *overall* non-synonymous rate is higher than the within-clade non-synonymous rate, indicating adaptive evolution (in addition to typical transmission chinas); 
4. the higher non-synonymous mutation rates suggest that there is a overall positive selection, but short-time (a few weeks) purifying selection in some ORFs were also identified.

Also I found the modelling methods in this paper is interesting. 

## Background
> adaptive evolution of influenza viruses tends to be gradual without large jumps in sequence space, while new variants of SARS- CoV-2 with tens of novel mutations emerged suddenly without intermediate genomes being observed, the most dramatic being the emergence of Omicron in late 2021 (Viana et al., 2022)

> Here, I build on these results and investigate the patterns of SARS-CoV- 2 diversification within variants and compare these to the global dynamics of evolution and adaptation. This comparison reveals a consistent dichotomy between slow within-variant evolution and rapid adaptive evolution giving rise to new variants. This difference in evolution- ary rate is only seen for non-synonymous changes – the rate of synonymous evolution within variants is compat- ible with that seen between variants. Furthermore, early variants display more rapid non-synonymous evolution than later variants suggesting more ubiquitous adaptive evolution early on. I further quantify the level of func- tional constraint of different open reading frames and in- fer a map of mutational tolerance across the genome.

## Useful methods
> A simple model for diversity within a growing variant is a super-critical branching process with growth rate $α$ and an embedded mutation process. Offspring of genomes with $i$ mutations contain $i + j$ mutations, where $j$ is a Poisson distributed number with mean $μt$ (mutation rate $μ$ and generation time $t$). The probability that offspring genomes are identical to their parents is $u = e^{−μt}$.

> Since the above branching process is linear, the mean number of cases $n$ will increase exponentially with rate $α$, while the number of genomes with $i$ mutations relative to the founder $m_i$ grows with rate $α − u$ per generation with solution $m_i = e^{(α−u)t}\frac{(ut)^i}{i!}$.

The overall number of cases is $e^{αt}$, so the above formula can also be interpreted as $m_i = $ *(overall number of cases)* $*$ $Poisson(i$ *events in interval* $t)$.

> At time $t$ after the emergence of the variant, the number of mutations in the population is expected to be Poisson distributed with mean $ut$.


## Other notes
> Evolutionary rates and divergence times are typically estimated using phylogenetic approaches (Drummond et al., 2006). These methods, *however, cannot handle the volume of SARS-CoV-2 data available and data have to be dramatically down-sampled*. Furthermore, phylogenetic methods impose an hierarchical structure on the data and are thus very sensitive to problematic sequences or metadata.

In my mind, a shortcoming of this simple branching process model is it can not deal with reverse mutations, and it treated every mutation with the same weights, which may be overly simplified.
