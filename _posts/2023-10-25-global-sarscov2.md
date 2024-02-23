---
title: "Paper digest: Global spread and invasion dynamics of SARS-CoV-2"
date: 2024-02-25
permalink: /posts/2024-02-25/2024-02-25-global-sarscov2
categories:
  - Paper digest
tags:
  - Phylogenetics
# last_modified_at: 2024-09-01
---

Today I will be discussing three papers: 1. [Dispersal patterns and influence
of air travel during the global expansion of SARS-CoV-2 variants of concern](https://doi.org/10.1016/j.cell.2023.06.001) published on Cell; 2. [Genomic assessment of invasion dynamics of SARS-CoV-2 Omicron BA.1](https://doi.org/10.1126/science.adg6605) published on Science; and 3. [Establishment and lineage dynamics of the SARS-CoV-2 epidemic in the UK](https://www.science.org/doi/10.1126/science.abf2946). All use phylogenetic methods to understand the global spread locally introduction events of SARS-CoV-2. I wanted to know how they modelled the importation events using tree model, and this info will facilitate my modelling study on a metapopulation compartmental model.

# Dispersal patterns and influence of air travel during the global expansion of SARS-CoV-2 variants of concern

The Alpha, Beta, and Gamma SARS-CoV-2 variants of concern (VOCs) co-circulated globally during 2020 and 2021, fueling waves of infections. They were displaced by Delta during a third wave worldwide in 2021, which, in turn, was displaced by Omicron in late 2021. In this study, we use phylogenetic and phylogeographic methods to reconstruct the dispersal patterns of VOCs worldwide. We find that source-sink dynamics varied substantially by VOC and identify countries that acted as global and regional hubs of dissemination. 

## Introduction
The logic of the introduction section is as follows:
- Different VOCs was associated initially with increasing SARS-CoV-2 incidence in their presumed countries of origin, then being displaced by other VOCs.
- Global transmission continued despite PHSMs and vaccination efforts.
- Understanding the global spread pattern of VOCs is critical. GISAID is helpful.
- We combine phylogenetic models that leverage multiple sets of ~20,000 genomes per VOC from >100 countries with global air passenger data in order to reconstruct the global spread of each VOC.

## Results
### VOC global dissemination patterns

- To quantify the global dissemination patterns of each VOC, we performed ancestral state reconstruction of discrete spatial locations using dated phylogenetic trees that were inferred from a subset of representative sampled genomes (for which sequence sampling locations were known).
- A limiting factor of this analysis is that countries with under-reported incidence and low sequencing proportions, but high global connectivity would have been missed as important global or regional VOC disseminators (given the reliance of our methods on genomic data and underlying testing patterns).
- It is important to note that due to subsampling and uneven sampling, viral importation numbers presented in this manuscript need to be interpreted as relative measures and will underestimate the actual number of importations. Additionally, country-specific differences in testing rates and sequencing efforts could also introduce potential biases in the estimated numbers of international exports, particularly when testing is low or sequencing intensity is much lower in proportion to recorded cases, where our method would underestimate the numbers of viral imports and exports.

Figure 1. Spatiotemporal dispersal patterns of VOCs
![Figure 1](https://www.cell.com/cms/attachment/37334cd2-9c27-4240-8774-dd89f1f84684/gr1.jpg)
In Figure 1, mean dates of all viral movements inferred along the routes were draw. The number of exports is inferred from case-sensitive phylogeographic analysis. Also refer to [Figure S1](https://www.cell.com/cms/attachment/75729758-1c32-4e20-8e54-cbe2a1d90829/figs1.jpg).

### Quantifying regional and global dissemination hubs

- The share of contributions to international exportations is highly correlated with countries’ total air travel passenger volume.

[Figure 2](https://www.cell.com/cms/attachment/6038408d-5e6a-441a-9c78-eff58b969f13/gr2.jpg) showed Regional and global dissemination hubs of VOCs.

### Role of first-reporting countries in global VOC dispersal

Figure 3. Inferred origins of global VOC dissemination events
![Figure 3](https://www.cell.com/cms/attachment/17a5c298-5eee-4530-8afc-b6ac10fce4ed/gr3.jpg)

### Impact of international travel on VOC dispersal

To examine how air travel has influenced the speed of dissemination of VOCs worldwide, we investigated global air travel passenger volumes between February 2020 and March 2022 and *the network structure* of the global airline network and compared them with the speed of dispersal of VOCs in countries reporting VOCs using genomic data. 

Figure 4. Impact of global air travel on VOC dissemination
![Figure 4](https://www.cell.com/cms/attachment/516612de-93be-46b1-a7dc-c573375515f0/gr4.jpg)
The radial distance of each node from the presumed origin location along the connecting branches represents the effective distance $D_{eff}$.

## Useful methods

The phylogenetic methods used in this study are highly relevant to my study. Importantly, the inferred the introduction and exportation events based on the **ancestral state changes**. The ancestral states (locations) were reconstructed based on time scaled phylogenetic tree. Specifically, he `mugration` package extension of `TreeTime` was then used to map discrete country locations to tips and infer country locations for internal nodes under a GTR model. Trees were build with `NextAlign` and `FastTree`, on subsampled sequences (using [subsampler](https://github.com/andersonbrito/subsampler)).

They used datasets of approximately 20,000 sequences for each VOC, and repeated the analysis for ten times (ten subsampled datasets).

## Other notes

# Genomic assessment of invasion dynamics of SARS-CoV-2 Omicron BA.1

## Background

## Results

## Useful methods

## Other notes

