---
title: "Book notes: "
date: 2024-03-09
permalink: /posts/2024-03-09/Coalescent-theory
categories:
  - Book notes
tags:
  - Coalescent theory
  - Phylogenetics
toc: true
last_modified_at: 2024-03-10
---

The book *Coalescent theory: An introduction* by John Wakeley stays in my bookshelf for more than 3 years. I have tried started reading it several times, but I always got stuck in the first two chapters. This time I decided to read it for preparing my attendance to the workshop on coalescent theory at the University of Warwick in the next month. Here let us start.

## 1. Gene genealogies

The goal of population genetics is to understand the forces that produce and maintain genetic variation within species. The forces include mutation, recombination, natural selection, population structure, and random transmission of genetic material from parents to offspring. Coalescent theory is a part of theoretical population genetics.

- Nonfunctional parts of the genome are especially informative about ancestry because mutations in these regions accumulate at a more constant rate and are more abundant than those within protein-coding or otherwise functional loci.
- Mutations are rare, so the record of ancestry in DNA is incomplete. Still, when we observe some number of differences between a pair of sequences at the same locus, we know that the time back to their common ancestor must be long enough for the observed number of mutations to have occurred with reasonable probability.
- Coalescent model considers the variation in times to common ancestry, which can be heavily influenced by the population-level process.
- The genetic ancestry of a sample, or the *gene genealogy*, is the set of ancestral relationships among the members of the sample.
- Gene genealogies are by the nature unobservable, and they are treated as random variables in a statistical setting.
- Thus, while in phylogenetics the tree structure itself is significant, within species it is often the case that particular gene genealogies provide little information about population-level processes and events.

### 1.1 Genealogies and genealogical thinking

- The shapes of *inter-species* gene genealogies, often called gene trees, for the most part coincide with the phylogenetic trees of the species from which the samples were taken. In contrast, gene genealogies for samples from a *single species* are more strongly influenced by the random process of genetic transmission and of birth and death of individuals within populations. The outcome of thess processes is called *genetic drift*.
- Coalescent genealogies without recombination are rooted bifurcating trees.
- We count a total of $2n-3$ branches in an unrooted tree with $n$ tips. There are $n-1$ coalescent events. The number of internal branches is $n-2$. Internal branches partition the sample into subsets that both contain at least two members (view from the perspective of a unrooted tree).
- Mutations can happen on the branches of the genealogy. 
- Because there are $2n-2$ branches in each genealogy, a single mutation placed on a genealogy will produce one of $2n-2$ possible patterns. Or $2n-3$ in a unrooted tree.
- We can access compatibility between two polymorphic sites directly, by comparing the subsets each makes of the sample. If both subsets at one site overlap with both subsets at the other site, then they are incompatible. 

### 1.2 Mutation and mutation models

Mutation is the bridge from genealogies to genetic data because the structure of the genealogy, in which each branch divides the sample into two groups, is revealed only if polymorphisms exist among the sampled sequences.

- Mutation models can be divided roughly into two groups: allele-based models and nucleotide-sequence models. Allele-based models typically do not encode any information about the historical relationships among alleles in a sample, whereas models for nucleotide sequences naturally generate such information in the patterns of polymorphism they among sites in the sample.
- An important simplifying assumption in modelling mutations within the coalescent is that all variation is selectively neutral, meaning that mutation does not affect the reproductive success of organism and has no influence on the genealogy structure. Thus, the genealogical process and mutation process can be separated, and any mutation model can in principle be applied by considering changes along the branches of each genealogy. In practice, analytical results can be easily found under the infinite-alleles and infinite-sites models, while other models are generally implemented using computer simulations.
- The infinite-sites assumption may be acceptable for nuclear DNA sequences as a first approximation, when the mutation rate is low. However, if a great deal of time has passed between the ancestor and its descendant, it will be likely that multiple mutations will have occurred. In this case, we must use detailed models of DNA sequence change and take the possibility of homoplasy, or convergence in state, into account.

### 1.3 Measures of DNA sequence polymorphism

