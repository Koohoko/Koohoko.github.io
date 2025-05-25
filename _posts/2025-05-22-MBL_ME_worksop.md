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

- Transform a uniform random variable into an exponential random: $t=-\frac{ln(n)}{\lambda}$ (keeping CDF the same).
- Simulation starts from the $\pi_{A,C,G,T}$ from the root. Then we get a random number $u \in [0,1]$, and we find the first $u$ determines the root state. 
- Below is an example code for simulating the state changes for v1.
- He also talked about codon model, rate variation and covarion models.

```r
Q_matrix <- matrix(c(
  -0.886, 0.19, 0.633, 0.063,
  0.253, -0.696, 0.127, 0.316,
  1.266, 0.19, -1.519, 0.063,
  0.253, 0.949, 0.127, -1.329), nrow=4, byrow=TRUE)

mutation_matrix <-  Q_matrix
diag(mutation_matrix) <- 0
mutation_matrix <- mutation_matrix / rowSums(mutation_matrix)

v1 <- 0.3
v6 <- 0.1
v5 <- 0.1
v4 <- 0.2
v2 <- 0.1
v3 <- 0.1

# I    II   III    IV
#  \  v2 \  /v3   /
#   \     \/     /
#    \     \    /
# v1  \  v5 \  /
#      \     \/
#       \    / 
#        \  / v6
#         \/

pi_vector <- c(A=0.4, C=0.3, G=0.2, T=0.1)
cumsum_pi <- cumsum(pi_vector)

(u <- runif(1))
(root_nuc_index <- max(which(u>cumsum_pi))+1)

(lambda <- -Q_matrix[nuc_index, nuc_index])

# for v1
remaining_time <- v1
current_index <- root_nuc_index
while(remaining_time > 0){
	t = -log(runif(1))/lambda
	print(t)
	# get the next event
	if(t>remaining_time){
		state_I_index <- current_index
		break
	} else{
		remaining_time <- remaining_time - t
		current_index <- sample(1:4, 1, prob=mutation_matrix[current_index,])
	}
}
print(c("A", "C", "G", "T")[state_I_index])

```

## [Model selection - Swofford](https://molevolworkshop.github.io/faculty/swofford/pdf/swofford_WH2024_modsel.pdf)

- Models don't need to reflect reality, but they need to be useful (think about using map vs. the real world) .
- He mentioned Felsenstein's zone and consistency of the ML methods, compared to the Parsimony methods.
- ![alt text](/files/2025_mole_workshop/gtr.png)
- [Should we use model-based methods for phylogenetic inference when we know that assumptions about among-site rate variation and nucleotide substitution pattern are violated?](https://pubmed.ncbi.nlm.nih.gov/12116942/)
- BIC penalizes models with more parameters more strongly than AIC. BIC performs well when true model is contained in model set, and among a set of simple-ish models, AIC often selects a more complex model than the truth (indeed, AIC is formally statistically inconsistent); But in phylogenetics, no model is as complex as the truth, and the true model will never be contained in the model set; BIC often chooses models that seem too simple!; One should consider preferring AIC over BIC in phylogenetics?
- Over-partitioning: Looking closely at the estimated parameters, it is possible that one model is sufficient to explain the data.
- You can use AIC to choose the partitioning scheme, e.g., Rob Lanfear’s PartionFinder. If there are too many partitions combinations, you can use a greedy algorithm to find the best partitioning scheme. 

## [Introduction to PAUP* - Swofford](http://paup.phylosolutions.com/)

- PAUP* is a software package for phylogenetic analysis using parsimony and other methods (*: likelihood, and distance methods).
- [Exploring Models and Hypothesis Testing using Simulation](https://molevolworkshop.github.io/faculty/swofford/pdf/modsel-sim-tutorial.html)
- He confirmed an interesting point for my question: 1. when we do model selection we will need a initial tree (model), but after model selection if we choose a different model (e.g. based on AIC), the best tree may change; And changing of the best tree may further change the likelihood for model selection; that will result in a "loop", and he confirmed that yes, we can do it iteratively.
- PAUP* can often achieve a higher likelihood than RAxML, due to fine-tuning of the optimization algorithm from Swofford.

## [IQ-TREE introduction](https://molevolworkshop.github.io/faculty/mcshea/pdf/MOLE2025-IQ-TREE.pdf)

- IQ-TREE3 is now available.
- MixtureFinder is a new tool for partitioning (TODO).
- Q matrix can be customized via Qmaker or NQmaker.
- Concatenation methods for genome-scale data, and partitioned analysis. `-q`, `-p`, and `-Q` are three different models for linking branch lengths.
- PartitionFinder is used for merging similar partitions, to reduce calculation of considering all possible paris, clustering algorithms are used.
- Q mixture model is available (TODO).
- For species tree, gCF and sCF are useful when bootstrap supports reach 100%.
- IQ-TREE can do K-H, S-H, and AU tests, to compare trees.
- Mixture across sites and trees (MAST) model. MAST assumes that there is a collection of trees, where each site of the alignment can have a certain probability of having evolved under each of the trees. Each tree has its own topology and branch lengths, and optionally different substitution rates, different nucleotide/amino acid frequencies, and even different rate heterogeneities across sites. 

## [IQ-TREE lab](https://iqtree.github.io/workshop/molevol_tutorial2025)

- I like this tutorial, it looks into a real dataset, which historically caused a lot of confusion.
- Where is turtle in the tree? Different papers, different methods led to different results.
- https://doi.org/10.1186/1741-7007-10-65
- https://academic.oup.com/sysbio/article/66/4/517/2950896?login=true
- https://academic.oup.com/mbe/article/42/1/msae264/7931682?login=true
