---
title: "Paper digest: Fast placing new genomes onto a existing phylogenetic tree"
date: 2022-09-20
permalink: /posts/2022-09-20/usher-paper
categories:
  - Paper digest
tags:
  - Usher
  - Phylogenetics
  - Bioinformatics
toc: true
last_modified_at: 2022-09-21
---

The paper titled [Ultrafast Sample placement on Existing tRees (UShER) enables real-time phylogenetics for the SARS-CoV-2 pandemic](https://doi.org/10.1038/s41588-021-00862-7) introduced a tool ([UShER](https://usher-wiki.readthedocs.io/en/latest/) for fast sample placement on existing trees.). Now this software is wildly used in SARS-CoV-2 genome placement.

## Background
Typical phylogenetic applications re-infer the full phylogeny every time when new viral genome sequence is collected, which takes too long time. If a new genome sequence could be contextualized by placing samples onto an existing "reference phylogeny", that would be great. Existing methods are far too slow.

## Results in this paper
### Efficient data structure
  1. [mutation-annotated tree](https://www.nature.com/articles/s41588-021-00862-7/figures/1)
  2. [preprocessed protocol buffer](https://developers.google.com/protocol-buffers).

### Maximum parsimony addition of samples onto an existing phylogeny
  1. Branch parsimony score (BPS), which is the minimum number of additional mutations (the parsimony score) required to accommodate a sample placement at a given branch.
  2. Fitch–Sankoff algorithm to infer the placement of mutations on a given tree and on the variant list.

### Missing data and errors affect placement of SARS-CoV-2 genomes
  1. **Low genome coverage**: When we randomly masked between 0 and 50% of positions in samples to be placed by UShER, all measures of placement accuracy were negatively impacted. With 50% of all sites masked, only 41.9% of samples were assigned identical sister nodes as their true placement on the reference tree. Based on these observations, we recommend that the reference tree should ideally be maintained using only genomes with nearly complete sequences regardless of the tree inference method (for example, by filtering data obtained from the GISAID database using ‘complete’ and ‘high coverage’ tags).
  2. **Stochastic errors**: With 10 errors on average, placement is approximately 20% less likely to select the correct sister node; other distance metrics are similarly impacted (Fig. 2). Our results indicate that especially low-quality samples should be rigorously identified and excluded from analyses using UShER.
  3. **Systematic errors**: a single systematic error present in all 10 samples had a similar overall effect on placement accuracy as 50% missing data in error-free sequences. Systematic errors should be rigorously identified and removed before sample placements are performed. We refer readers to methods that we developed previously to detect and eliminate such errors. 

### Quantifying uncertainty in sample placement
1. The number of equally parsimonious placements.
2. The minimum number of additional mutations required to accommodate a single sample placed on each branch of the reference tree, a measure that we call the BPS. (Only for single sample placement)

### UShER is congruous with standard methods on SARS-CoV-2 data
The authors measures the consistency of placement between more typical tree-building approaches (Fasttree) and the UShER placement algorithm.

## Useful methods
- *Fitch–Sankoff algorithm* to infer the placement of mutations on a given tree and on the variant list

- *Robinson–Foulds distance* to measure congruence with the correct tree. ([TreeCmp: Comparison of Trees in Polynomial Time](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3422086/))

- Detect and eliminate systematic errors: [Stability of SARS-CoV-2 phylogenies](https://pubmed.ncbi.nlm.nih.gov/33206635/), and [post](https://virological.org/t/issues-with-sars-cov-2-sequencing-data/473).

- A *tie-breaking strategy* was used when multiple node placements are equally parsimonious.

- Tool for *simulating genome evolution along a phylogeny*: [pyvolve](https://pubmed.ncbi.nlm.nih.gov/26397960/)

- [TreeShrink](https://pubmed.ncbi.nlm.nih.gov/29745847/) to remove sequences on very long branches.

- [goalign](https://github.com/evolbioinfo/goalign) to create 100 bootstrap alignments.

## Other notes
- Sequential placement of new samples using UShER is possible (multiple rounds of placements can be carried out over and over again). The authors state that the placements *could potentially be worse than a full de novo tree inference procedure. However, in practice, we have found UShER’s accuracy over iterated placements to be reasonably high.*

- The UShER family also have helper tools including [matUtils](https://usher-wiki.readthedocs.io/en/latest/matUtils.html) (for interacting with Mutation Annotated Tree (MAT)), [matOptimize](https://usher-wiki.readthedocs.io/en/latest/matOptimize.html) (for optimizing phylogenies using parsimony score), and [RIPPLES](https://usher-wiki.readthedocs.io/en/latest/ripples.html) (to detect recombination events in large mutation annotated tree (MAT) files).

- Personal perspective: Maybe considering different DNA substitution models for sample placements (especially when multiple node placements are equally parsimonious) can improve accuracy.



