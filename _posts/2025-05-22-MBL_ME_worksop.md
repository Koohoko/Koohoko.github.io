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

Course materials are available at [here](https://molevolworkshop.github.io/schedule/).

# Day 1
## Introduction to phylogenetics - Tracy Heath

- The Metazoa Phylogeny
  - There is scientific controversy over whether sponges (Porifera) or ctenophores (Ctenophora) are the earliest-diverging animal lineage; traditional morphological evidence supports sponges, but some molecular studies suggest ctenophores may be more basal.
  - This debate impacts our understanding of early animal evolution—especially whether complex traits like nervous systems evolved early and were later lost in sponges, or evolved independently in multiple lineages.
  - Check [this](https://www.nature.com/articles/s41586-023-05936-6) new evidence in Nature.

## Scientific ethics - Joseph Bielawski

- Ethical reasoning focus on what *I* (or *we*) should do, but not blaming others.
- Normalization of Deviance, you should not start doing something just because it is common, or you think it has small consequences.
- Take the anti-vax movement as an example, at first it was a small group of people (deviance, Andrew Wakefield etc.), but then it became normalized and now it is a big problem.
- If you do noting, you can be contributing to normalization of deviance.
- Scientist have social privilege, and they have obligations.

##	Introduction to Likelihood - Paul Lewis

- Why do we need the term likelihood?
  - Probability is describing the chance of an **event/outcome/data** given one model.
  - Likelihood is describing the **model/hypothesis/parameter** given data.
- Transition-transversion rate ratio = 1 equivalent to transition-transversion rate = 0.5.
- Site specific rate variation, e.g. $r_1$ for codon positions 1 and 2, $r_2$ for codon position 3.
- He said that even though the parameter in the Gamma and invariable site models can have correlation, a successful bayesian search algorithm should be able to deal with this, and there are no issue with identifiability. 

## Model-based phylogenetics - John Huelsenbeck

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

## Simulating molecular evolution - John Huelsenbeck

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

## [Model selection - David Swofford](https://molevolworkshop.github.io/faculty/swofford/pdf/swofford_WH2024_modsel.pdf)

- Models don't need to reflect reality, but they need to be useful (think about using map vs. the real world) .
- He mentioned Felsenstein's zone and consistency of the ML methods, compared to the Parsimony methods.
- ![alt text](/files/2025_mole_workshop/gtr.png)
- [Should we use model-based methods for phylogenetic inference when we know that assumptions about among-site rate variation and nucleotide substitution pattern are violated?](https://pubmed.ncbi.nlm.nih.gov/12116942/)
- BIC penalizes models with more parameters more strongly than AIC. BIC performs well when true model is contained in model set, and among a set of simple-ish models, AIC often selects a more complex model than the truth (indeed, AIC is formally statistically inconsistent); But in phylogenetics, no model is as complex as the truth, and the true model will never be contained in the model set; BIC often chooses models that seem too simple!; One should consider preferring AIC over BIC in phylogenetics?
- Over-partitioning: Looking closely at the estimated parameters, it is possible that one model is sufficient to explain the data.
- You can use AIC to choose the partitioning scheme, e.g., Rob Lanfear’s PartionFinder. If there are too many partitions combinations, you can use a greedy algorithm to find the best partitioning scheme. 

## [Introduction to PAUP* - David Swofford](http://paup.phylosolutions.com/)

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

# Day 3

## Bayesian inference - Paul Lewis

- Joint probability, conditional probability, marginal/total probability.
- Baye's rule: the joint probability can be written as the product of the conditional probability and the marginal/total probability: $P(A|B)P(B)=P(B|A)P(A)$.
- Note that the **likelihood** $L(\theta|D)$ is the **probability** of the data given the model $P(D|\theta)$.
- Prior can have huge impact on the posterior distribution, consider the HIV screening test example.
- A continous case: 
  $$
  \underbrace{p(\theta \mid D)}_{\text{Posterior probability density}} \;
  =
  \frac{
    \underbrace{p(D \mid \theta)}_{\text{Likelihood}}
    \;\times\;
    \underbrace{p(\theta)}_{\text{Prior probability density}}
  }{
    \underbrace{\displaystyle \int p(D \mid \theta)\,p(\theta)\,\mathrm{d}\theta}_{\text{Marginal probability of the data (evidence)}}
  }
  $$
- A **informative** prior have **low variance** (not necessarily low bias), and a vague prior have high variance.
- The y-axis of a PDF is not a probability, but a probability density.
- When you use posterior ratio, you can ignore the denominator.
- Metropolis algorithm allows us to explore and characterize the posterior probability distribution $p(θ,ϕ∣D)$ without ever needing to compute the intractable denominator $P(D)$.
- [A nice demonstration of the MCMC robot](https://plewis.github.io/applets/mcmc-robot/).
- MCMCMC is a "team effort" where different chains with different "perspectives" (temperatures) on the landscape help each other to map out the entire territory effectively. By adjusting the temperatures, we can control how the posterior distribution being flattened or sharpened, which can help us to explore the posterior distribution more efficiently.

## MCMC proposals in phylogenetics - Paul Lewis

- The Largest-Simon move:
  - Step 1: Pick 3 contiguous edges randomly, defining two subtrees, X and Y.
  - Step 2: Shrink or grow selected 3-edge segment by a random amount.
  - Step 3: Choose X or Y randomly, then reposition randomly (NNI).
  - After NNI, we get a proposed tree, we will decide whether to accept basing on the log-posterior.
  - While the strategy of optimizing topology and then branch lengths iteratively is key to finding a single optimal tree in ML, Bayesian MCMC aims to explore the entire landscape of possibilities. A key of the MCMC proposal is to maintain symmetricly, and making sure that the time it stays at the higher posterior region is longer than the time it stays at the lower posterior region.
- Remember that MCMC is primarily about deciding whether to accept a randomly proposed move. 
  - The proposal mechanism itself is generally "blind" to whether the new state will have a higher or lower posterior probability. It just generates a candidate state. The Metropolis-Hastings acceptance step then evaluates the proposed state's posterior probability relative to the current state's and decides whether to accept the move. This acceptance step is what guides the chain towards regions of higher posterior probability over time.
- 95% HPD interval: highest posterior density interval, the region of parameter space that contains 95% of the posterior probability mass.
- Prior distributions:
  - Gamma(a, b): appropriate for parameters that range from 0 to infinity, such as branch lengths or rates.
  - Lognormal: ranges from 0 to infinity, yields a paticular mean and variance.
  - Beta(a,b) distributions are appropriate for proportions, which must lie between 0 and 1 (inclusive).
  - A Dirichlet(a,b,c,d) distribution is ideal for nucleotide relative frequencies.
  - Discrete uniform can be used for tree topologies.
  - Gamma-Dirichlet can be used for branch lengths
    - Gamma prior on Total Tree Length (TL), then Dirichlet Prior on Edge Length Proportions.
    - It solves the problem of overestimation by default i.i.d. exponential priors (which implicitly enforce an unwanted informative prior) (the prior mean and variance of the total tree length can increase linearly with the number of taxa, sometimes leading to unrealistically long trees ("branch length overestimation") if the data is sparse or sequences are highly similar, see [Ziheng's](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://abacus.gene.ucl.ac.uk/ziheng/pdf/2012ZhangRannalaYang.SBv61p779.pdf)):
  - Yule (pure birth) prior: a prior distribution that can jointly specify both the tree topology and its edge lengths.
- Check **distribution explorer**! https://distribution-explorer.github.io/
- Hierarchical models: some parameters of the prior distributions (called hyperparameters) are themselves drawn from another distribution (a hyperprior). 
- Empirical Bayes: 
  - Instead of setting a hyperprior on a parameter of the prior distribution (like the mean of the branch length prior), the Empirical Bayes uses the data (e.g. MLEs) to get an estimate for this parameter.
  - This approach uses the data "twice": once to inform the prior and again in the likelihood calculation. It's a pragmatic approach but differs from a fully Bayesian hierarchical model where all parameters, including hyperparameters, have prior distributions.
- rjMCMC: a type of Markov Chain Monte Carlo algorithm that allows the MCMC chain to jump between models of different dimensions. Useful for:
  -  Substitution model averaging/selection
  -  Species delimitation
- Marginal likelihood and Bayes factors
  - The marginal likelihood is higher in models when they are true.
  - Marginal likelihood inherently penalizes models that are overly complex and do not fit the data well, often favoring models that better capture the true underlying process that generated the data.
- Dirichlet process (DP) prior
  - The Dirichlet Process prior is presented in the context of analyzing data from multiple loci (e.g., genes A, B, C, D) and wanting a prior that can model the situation where:
    - Some loci might share the same tree topology (concordance).
    - Other loci might have different tree topologies (discordance), possibly due to processes like incomplete lineage sorting.
  - BUCKy model: Ané et al. 2007. Molecular Biology and Evolution 24:412–426.
  - Use Concentration Parameter($\alpha$) to suggest how frequent different loci share the same tree.
  - https://plewis.github.io/applets/dpp/

## Intro. to Graphical Models and RevBayes - Jeremy Brown

- In Rev language, `z ~ dnBernoulli(0.5)` is creating a random variable `z` which is fundamentally a stochastic node in the model graph.
- `z.clamp(1)` then `z.probability()` will return the probability of `z` being 1.
- Graphical models provide a means of depicting the dependencies among parameters in probabilistic models. 
  - Squared boxes represent constant nodes: `x <- 2.3`
  - Dashed circles represent deterministic nodes: `y := 2 * x`
  - Solid circles represent stochastic nodes: `z ~ dnExponential(1)`
  - Filled solid circles represent clamped stochastic nodes: `z.clamp(1)`
  - Plates are used to indicate replication (for loop) in the model.
- Setting up MCMC in RevBayes
  - We use the `=` assignment operator for “workspace” variables: `myModel = model(n)`
  - We need to define a proposal distribution (move) for any parameters we are trying to infer. `moves = VectorMoves()` `moves.append( mvSlide(p,delta=0.1,weight=1) )`.
  - We need to keep track of our progress and sampled parameter values. To do that we use monitors. `monitors = VectorMonitors()` `monitors.append( mnScreen(printgen=1000,p) )` `monitors.append( mnModel(filename=“myMCMC.log", printgen=10) )`
  - Next we create an MCMC object. `myMCMC = mcmc(myModel,moves,monitors)`, and start it with `myMCMC.run(10000)`.
- We tested a simple example for inferring a parameter in binomial process in RevBayes:
  ```r
  p ~ dnUnif(0,1)
  n <- 50
  k ~ dnBinomial(n,p)
  k.clamp(30)
  myModel = model(n)
  moves = VectorMoves()
  moves.append( mvSlide(p,delta=0.1,weight=1) )
  monitors = VectorMonitors()
  monitors.append( mnScreen(printgen=1000,p) )
  monitors.append( mnModel(filename="myMCMC.log", printgen=100) )
  myMCMC = mcmc(myModel,moves,monitors)
  myMCMC.run(2000000)
  quit()
  ```
  Run it by `rb myMCMC.rb`.

- It is nice that he demonstrated the Gamma-Dirichlet model in RevBayes.
- There are example Rev scripts for JC, HKY, GTR, GTR+G+I available.
- ![alt text](/files/2025_mole_workshop/Gamme_dirchlet.png)
- The weights in moves determine the probability of different moves being selected.
- An MCMC iteration isn't just one move; it's typically a series of these individual parameter update attempts (each involving a proposal, likelihood calculation, and an accept/reject decision) for many, if not all, of the parameters in the model.
- Below is an example script for the GTR+G+I model:

```python
################################################################################
#
# RevBayes Example: Bayesian inference of phylogeny using a GTR+Gamma+Inv
#                   substitution model on a single gene.
#
# authors: Sebastian Hoehna, Michael Landis, and Tracy A. Heath
#
################################################################################


### Read in sequence data for the gene
data = readDiscreteCharacterData("data/primates_and_galeopterus_cytb.nex")

# Get some useful variables from the data. We need these later on.
num_taxa <- data.ntaxa()
num_branches <- 2 * num_taxa - 3
taxa <- data.taxa()


moves    = VectorMoves()
monitors = VectorMonitors()


######################
# Substitution Model #
######################

# specify the stationary frequency parameters
pi_prior <- v(1,1,1,1) 
pi ~ dnDirichlet(pi_prior)
moves.append( mvBetaSimplex(pi, weight=2) )
moves.append( mvDirichletSimplex(pi, weight=1) )


# specify the exchangeability rate parameters
er_prior <- v(1,1,1,1,1,1)
er ~ dnDirichlet(er_prior)
moves.append( mvBetaSimplex(er, weight=3) )
moves.append( mvDirichletSimplex(er, weight=1) )


# create a deterministic variable for the rate matrix, GTR
Q := fnGTR(er,pi) 


#############################
# Among Site Rate Variation #
#############################

# among site rate variation, +Gamma4
alpha ~ dnUniform( 0.0, 10 )
sr := fnDiscretizeGamma( alpha, alpha, 4 )
moves.append( mvScale(alpha, weight=2.0) )


# the probability of a site being invariable, +I
p_inv ~ dnBeta(1,1)
moves.append( mvSlide(p_inv) )

##############
# Tree model #
##############

out_group = clade("Galeopterus_variegatus")
# Prior distribution on the tree topology
topology ~ dnUniformTopology(taxa, outgroup=out_group)
moves.append( mvNNI(topology, weight=num_taxa/2.0) )
moves.append( mvSPR(topology, weight=num_taxa/10.0) )

# Branch length prior
for (i in 1:num_branches) {
    bl[i] ~ dnExponential(10.0)
    moves.append( mvScale(bl[i]) )
}

TL := sum(bl)

psi := treeAssembly(topology, bl)




###################
# PhyloCTMC Model #
###################

# the sequence evolution model
seq ~ dnPhyloCTMC(tree=psi, Q=Q, siteRates=sr, type = "DNA")
seq ~ dnPhyloCTMC(tree=psi, Q=Q, siteRates=sr, pInv=p_inv, type="DNA")

# attach the data
seq.clamp(data)


############
# Analysis #
############

mymodel = model(psi)

# add monitors
monitors.append( mnScreen(printgen=100, alpha, p_inv, TL) )
monitors.append( mnFile(filename="output/primates_cytb_GTRGI.trees", printgen=10, psi) )
monitors.append( mnModel(filename="output/primates_cytb_GTRGI.log", printgen=10) )

# run the analysis
mymcmc = mcmc(mymodel, moves, monitors)
mymcmc.run(generations=20000)


# summarize output
treetrace = readTreeTrace("output/primates_cytb_GTRGI.trees", treetype="non-clock")
# and then get the MAP tree
map_tree = mapTree(treetrace,"output/primates_cytb_GTRGI_MAP.tre")


# you may want to quit RevBayes now
q()
```

- https://revbayes.github.io/tutorials/ctmc/

## Bayesian Divergence time estimation - Tracy Heath

