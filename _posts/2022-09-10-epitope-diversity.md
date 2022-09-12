---
title: "Estimating the haplotype diversity within a genomic region (e.g. epitope) "
date: 2022-09-12
permalink: /posts/2022-09-10/epitope-diversity
categories:
  - Bioinformatics
tags:
  - Rust
  - Sequence analysis
  - Nucleotide diversity
  - Shannon entropy
# last_modified_at: 2022-09-01
---

### Introduction
When deep sequencing data is available, sometimes it is interesting to check the mutation diversity of reads within a specific genomic region. A frequent example would be studying the mutation diversity of a [immune epitope](https://en.wikipedia.org/wiki/Epitope) region. 

I first came across this problem in a [study on flu virus population under T cell–activating vaccination](https://www.science.org/doi/full/10.1126/sciadv.abl5209). At that time, I wrote a [R script]((https://github.com/Koohoko/T-cell-activating-vaccines-flu-mutation/blob/5bcf43cc406463ae2e7254c870209cfbb05d0bf1/scripts/diveristy.r#L161-L164)) diving into the alignment BAM file and calculated the Shannon entropy and Gini-Simipson's index for epitope haplotypes observed in the alignment. One main problem for the R scripts is that it runs too slow and took too much memory, so I recently developed a likewise tool called [epitope_diversity](https://github.com/Koohoko/epitope_diversity) using [Rust](https://www.rust-lang.org), and I believe this tool is more fast-running, memory efficient, and easier to use. For the installation and usage of the software, please check [this link](https://github.com/Koohoko/epitope_diversity#usage). 

In the below section, I will briefly describe methods used for estimating mutation diversity.

### Methods
There are two levels of methods for calculating mutation diversity:
  1. Nucleotide/Locus level
     Useful when haplotypes are not available. For example when you only have the vcf files (mutations for discrete genomic sites), or when you want to calculate the whole-genome genomic diversity, but you only have short-read sequencing data so you don't know the full-length haplotypes.
  2. Haplotype level
     Good to use when haplotypes are available.
![](/files/diversity_measurement/diversity_measurement_SFLU.003.jpeg)

#### Nucleotide/Locus level
Basically we calculate the diversity for every nucleotide position (locus), then take average over the whole epitope region. For details please refer to [this paper](https://academic.oup.com/ve/article/5/1/vey041/5304643).
>  Supposing that full haplotype information for the virus is not available, a genome-wide measure of entropy may then be calculated, computing the mean of this statistic across all sites (McCrone and Lauring 2016).

![](/files/diversity_measurement/diversity_measurement_SFLU.004.jpeg)

#### Haplotype level
We first tried to count the frequencies of different haplotypes, then we calculate the metrics like Shannon entropy or nucleotide diversity. Details please see [this paper](https://www.sciencedirect.com/science/article/pii/S004268221630037X)
![](/files/diversity_measurement/diversity_measurement_SFLU.006.jpeg)

I also summarize and illustrate the essential six steps into the below slides:
![](/files/diversity_measurement/diversity_measurement_SFLU.008.jpeg)
![](/files/diversity_measurement/diversity_measurement_SFLU.009.jpeg)
![](/files/diversity_measurement/diversity_measurement_SFLU.010.jpeg)
![](/files/diversity_measurement/diversity_measurement_SFLU.011.jpeg)
![](/files/diversity_measurement/diversity_measurement_SFLU.012.jpeg)
![](/files/diversity_measurement/diversity_measurement_SFLU.013.jpeg)

Please feel free to contribute to the project and raise issues [here](https://github.com/Koohoko/epitope_diversity).

---