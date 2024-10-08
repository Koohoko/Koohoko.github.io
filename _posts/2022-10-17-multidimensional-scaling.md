---
title: "Paper digest: Antidbody cross-reactome against flu surface glycoproteins (Nat Immunol, 2017)"
date: 2022-10-17
permalink: /posts/2022-10-17/multidimensional-scaling
categories:
  - Paper digest
tags:
  - Bioinformatics
  - Biostatistics
# last_modified_at: 2022-09-01
---

I heard that there is a method called *Multidimensional scaling* to study antibody response to multiple HA proteins (e.g. Fig 4 & 5 of this paper: [Defining the antibody cross-reactome directed against the influenza virus surface glycoproteins](https://pubmed.ncbi.nlm.nih.gov/28192418/). I hereby marked down some important notes when studying this method. 

## Background
Protective humoral immune responses to influenza virus are usually associated with antibodies to its surface glycoproteins hemag-glutinin (HA) and neuraminidase (NA), and generally includes four types of antibodies:
1. antibodies that exhibit hemag-glutination-inhibition (HI) activity;
2. NA-inhibition-activate antibodies;
3. HA-stalk-reactive antibodies;
4. antibodies that confer protection in vivo without showing neutralizing activity in vitro.

> "Here we analyzed the titers and breadth of antibodies to the influenza virus surface glycoproteins HA and NA induced by infection in three animal models and in humans, as well as the prevalence of cross-reactive antibodies in the general human population"

## Results
In **Figure 1 and Figure 2**, the authors use a heat-map-tree combination to show the cross-reactive profiles in animal models.

In **Figure 3**, they suggest amino acid differences can be representative of antigenic distances. They also found Guinea pigs exhibited a very broad plateau of cross-reactivity.

In **Figure 4**, they showed the human antibody responses in a 3-D manner:
> We thus plotted reactivity (presented as endpoint titers) against the percent difference in amino acids of the HAs compared with the sequence of the infection strain's HA. The resulting plots showed two-dimensional reactivity profiles that allowed visual comparison of the magnitude and breadth of responses in various animal models.
![Fig_4](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fni.3684/MediaObjects/41590_2017_Article_BFni3684_Fig4_HTML.jpg)

In **Figure 5**, they shown the antigenic landscape in human cohorts of different age groups (Young, Middle-aged and Experienced), and discussed about "original antigenic sin".
> ![Fig_5](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fni.3684/MediaObjects/41590_2017_Article_BFni3684_Fig5_HTML.jpg)

In Figure 6, they studied
1. direct inhibition or neutralization assessed by micro-neutralization assays *in vitro*.
2. *in vivo* potency of serum (protection mediated by Fc and its receptor FcR?) by serum-transfer-challenge experiments using mouse model.

## Useful methods
![](/files/2022-10-18-multidimensional-scaling/Screenshot%202022-10-17%20at%206.11.55%20PM.png)

## Other notes
I am not sure whether this paper is among the earliest to study "original antigenic sin" in flu infections in humans, but it is very interesting. I heard for SARS-CoV-2, there is also some evidence supporting similar effects.

