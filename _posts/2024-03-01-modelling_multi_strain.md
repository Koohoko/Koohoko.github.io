---
title: "Paper digest: Modelling pathogens with many strains"
date: 2024-03-01
permalink: /posts/2024-03-01/modelling_multi_strain
categories:
  - Paper digest
tags:
  - Infectious Disease Modelling
# last_modified_at: 2024-09-01
---

How to model pathogens with many strains? Particularly what are the appropriate model settings. Here I revisit a few papers on this topic. They include:
  1. [Makau, Dennis N., et al. "Ecological and evolutionary dynamics of multi-strain RNA viruses." Nature Ecology & Evolution 6.10 (2022): 1414-1422.](https://www.nature.com/articles/s41559-022-01860-6)
  2. [Kucharski, Adam J., Viggo Andreasen, and Julia R. Gog. "Capturing the dynamics of pathogens with many strains." Journal of mathematical biology 72 (2016): 1-24.](https://link.springer.com/article/10.1007/s00285-015-0873-4)
  3. [Gog, Julia R., and Bryan T. Grenfell. "Dynamics and selection of many-strain pathogens." Proceedings of the National Academy of Sciences 99.26 (2002): 17209-17214.](https://www.pnas.org/doi/abs/10.1073/pnas.252512799)

## Ecological and evolutionary dynamics of multi-strain RNA viruses

In this Review, we describe multi-strain dynamics from ecological and evolutionary perspectives, outline scales in which multi-strain dynamics occur and summarize important immunological, phylogenetic and mathematical modelling approaches used to quantify interactions among strains.

### Ecological versus evolutionary dynamics

- Ecological multi-strain dynamics: a discrete number of antigenic alternatives or strains exist in the population and strains are assumed not to evolve phenotypically (only neutral or nearly neutral evolution occurs on the timescale of interest). *Probably exhibit more symmetrical/balanced phylogenetic trees with longer branches.*
- Evolutionary multi-strain dynamics: focusing on how competition and natural selection among genetic variants can drive genetic change, allowing for the emergence of new genetic variants or strains through time. ‘Immune escape’ occurs when a novel antigenic variant evolves that is no longer controlled by individual/herd-level immunity. *Often exhibit ladder-like phylogenetic trees wherein older strains go extinct and are replaced by newer strains.*

![](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41559-022-01860-6/MediaObjects/41559_2022_1860_Fig1_HTML.png?as=webp)

### Scales of action and impact of multi-strain dynamics

We can consider multi-strain dynamics at different scales, including the within-host, between-host, and between-population scales. 

### Quantifying immunogenic interactions between strains

Partial immunity among genetically/immunogenically similar strains can shape the fitness of different strains and influence the likelihood that multiple strains co-circulate in a population.

To quantify antigenic distance between strains, binding and cross-neutralization assays are often used to measure the cross-reactivity of immune reactions elicited by different strains. Antigenic cartography, a computational technique used for graphical visualization of antigenic distances obtained from inhibition assays, can be used to visualize the genetic and antigenic differences among co-circulating variants and identify clusters of variants with similar immune profiles.

### Evolutionary processes of multi-strain pathogens

Phylogenetic branching patterns can be analysed to provide insights on multi-strain dynamics and immune-mediated selection, e.g., different phylogenetic patterns (tree shapes) can be observed in Fig 1.

Selection pressures and resulting mutations responsible for adaptation or immune evasion are not always easily identifiable from phylogenetic trees alone. Therefore, we describe four approaches that can complement phylodynamic models to evaluate rates of viral evolution depicted on phylogenetic trees: 
1. Tajima’s D statistic
2. local branching index
3. The fixation index (FST)
4. dN/dS ratio

### Mathematical models of multi-strain pathogens

Multi-strain disease models can track either individuals (agent-based models) or changing proportions of different infection states (compartmental models), but the underlying dynamics are similar: individuals/groups of the population are divided into a finite set of possible classes on the basis of their exposure history. 

Challenges:
1. Proper number ans resolution of strains
2. Cross-immunity (degree, duration, and implementation)
3. The incorporation of evolution into models (current practices include (i) allowing epidemiological parameter values to evolve (for example, transmissibility) or (ii) to adding a new parameter corresponding to an abstract phenotype or genotype space)

### Population structure and stochasticity

The spreading success of a strain may be more related to host behavioural or physiological attributes than to the fitness of that particular viral strain.

### Outstanding questions
Numerous unresolved questions need to be addressed to understand multi-strain dynamics in different host–virus systems. 
1. (*Different scales of multi-strain dynamics*) With complex host immune responses and interaction with co-circulating strains, how do co-infection and co-evolution influence the effectiveness of disease management such as vaccination or other control strategies? 
2. (*Different models*) Although we have described different phylodynamic tools useful for understanding genetic evolution of co-circulating strains, what are the best approaches to investigate and contextualize antigenic evolution in those strains? In addition, are there distinct and measurable phylogenetic tree topologies characteristic of ecological multi-strain dynamics, and how do perturbations in host populations affect tree structure? 
3. (*Host genetic influence*) Host genotypes may non-uniformly influence susceptibility to certain pathogens. How do these host differences affect multi-strain pathogen dynamics at the population level? 
4. (*Host population structure*) Host populations may be stratified or substructured for many reasons (natural or artificial). Since strains theoretically evolve to balance transmissibility–virulence trade-offs specific to a given subpopulation, how do changes in host population structure affect the co-evolution/co-circulation of different strains in a population? 
5. (*How to predict*) How quickly and to what extent does the fitness of a particular strain vary between individual hosts and across space and time? What are the most suitable approaches to quantify and predict the role of viral fitness in the establishment of multiple strains in a population or subpopulation? Can these tools be used to predict future success or invasion potential of different strains?

## Capturing the dynamics of pathogens with many strains

This is also a review article: We provide a comprehensive outline of the benefits and disadvantages of available frameworks, and describe what biological information is preserved and lost under different modelling assumptions. We also consider the emergence of new disease strains, and discuss how models of pathogens with multiple strains could be developed further in future.

### Introduction

Many human pathogens can be categorized into distinct strains, each defined by its antigenic properties. This results in a highly complex system, with pathogens interacting through the partial cross-immunity they generate in the host population. Examining the effect of this interaction on disease outbreaks has therefore posed a major challenge, both theoretically and biologically.

### Multiple-strain models

