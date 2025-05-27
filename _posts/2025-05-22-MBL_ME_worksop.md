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
- Baye's rule: the joint probability can be written as the product of the conditional probability and the marginal/total probability: $P(A\vert B)P(B)=P(B\vert A)P(A)$.
- Note that the **likelihood** $L(\theta\vert D)$ is the **probability** of the data given the model $P(D\vert \theta)$.
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

- The global molecular clock - Assume that the rate of evolutionary change is constant over time, for all lineages.
- However, rates of evolution vary across lineages and over time.
- Sequence data alone provide branch lengths, in the unit of expected substitutions per site. The rate and time are not identifiable by sequence data alone.
- Tree-time priors (e.g., Yule, Birth-Death) for molecular phylogenies are only informative on a relative time scale.
- $f(R, A, \Psi, \theta_R, \theta_A, \theta_s \vert  D) = \frac{f(D \vert  R, A, \theta_s) f(R \vert  \theta_R) f(A, \Psi \vert  \theta_A) f(\theta_s)}{f(D)}$
  - The parameters involved are:
    * **$R$**: A vector representing the evolutionary **rates on each branch** of the tree.
    * **$A$**: A vector representing the **ages of the internal nodes** in the tree (divergence times).
    * **$\Psi$ (Psi)**: The **tree topology** (the branching pattern).
    * **$\theta_R$**: Hyperparameters for the model of how branch rates ($R$) evolve or are distributed (e.g., parameters of a relaxed clock model).
    * **$\theta_A$**: Hyperparameters for the tree prior, which models how topologies ($\Psi$) and node ages ($A$) arise (e.g., parameters of a birth-death process like speciation/extinction rates).
    * **$\theta_s$**: Parameters of the substitution model describing how sequences change (e.g., GTR rates, base frequencies, gamma shape parameter for among-site rate variation).
    * **$D$**: The observed **character data** (e.g., DNA or protein sequence alignment).
  * **$f(D \vert  R, A, \theta_s)$ - The Likelihood:**
    * This is the probability (or probability density) of observing the sequence data $D$, given a specific tree (defined by topology $\Psi$ and node ages $A$, which together yield branch durations), the rates of evolution along each branch ($R$), and the substitution model parameters ($\theta_s$).
    * Branch lengths in units of expected substitutions per site (which the likelihood calculation uses) are obtained by multiplying the rate on a branch ($R_i$) by the duration of that branch (derived from $A$ and $\Psi$).
  * **$f(R \vert  \theta_R)$ - The Prior on Branch Rates:**
  * **$f(A, \Psi \vert  \theta_A)$ - The Joint Prior on Node Ages and Topology (The "Tree Prior"):**
  * **$f(\theta_s)$ - The Prior on Substitution Model Parameters:**
- **Independent/Uncorrelated Rates**: Lineage-specific rates are uncorrelated when the rate assigned to each branch is **independently drawn** from an underlying distribution (you can do it in a for loop for every **branch**).
- **Autocorrelated Rates**: closely related lineages have similar rates. The rate at a **node** is drawn from a distribution with a mean equal to the parent rate.
  - Note that the $\mu$ in log-normal distribution is the **mean** of the log-transformed rates, **not** the mean of the rates themselves.
  - The correlation between parameters in this model makes it hard for MCMC to explore the parameter space.
- Tree priors:
  - The Birth-Death Process: $\lambda$ is the speciation rate, $\mu$ is the extinction rate.
  - The Yule Process: $\lambda$ is the speciation rate, $\mu$ is 0.
  - We also have the origin time $\phi$, and the sampling fraction $\rho$.
- Conceptual debate in fossil calibration: Calibrations as Priors vs. Calibrations as Data (Likelihoods):
  - **Node Calibrations as Priors**: One approach is to directly treat these calibration densities as defining the prior distribution for the age of the calibrated node(s). The overall tree prior (e.g., from a birth-death process) is then conditioned on these specified node ages
    - Commonly, a **parametric probability distribution** (e.g., Uniform, Lognormal, Gamma, Exponential) is placed on the age of an internal node. This distribution is typically offset by the age of the oldest fossil confidently assigned to that clade, effectively setting a minimum age for that node.
    - While minimum age bounds from fossils are common, reliable maximum age bounds are often difficult to establish.
    - Problems with multiple calibrations as priors: Rannala (2016) showed this conditional prior approach can lead to "counterintuitive topologically inconsistent realized priors" (the effective prior on tree shapes and other node ages can be strange). Dos Reis (2016) also demonstrated that this can be computationally intractable with many calibrations.
  - **Node Calibrations as Likelihoods (Fossil Data Likelihood)**: An alternative view is to treat the fossil information (e.g., fossil age $F$) as data. The probability of observing this fossil data is then expressed as a likelihood function conditional on the age of the relevant node ($t$) in the tree, $f(F\vert t,parameters)$. This approach is argued to be conceptually simpler and more easily manageable with multiple fossil calibrations.
  - **Common Misinterpretation**: Even if the mathematical implementation of a calibration effectively treats the fossil as data (i.e., a likelihood component), it is often misinterpreted by users as directly setting the prior distribution for the node's age. The mathematical form for $f(t\vert F)$ (a prior on node age $t$ given fossil $F$) and $f(F\vert t)$ (likelihood of fossil $F$ given node age $t$) can be identical for certain distributions (like a shifted exponential), contributing to this confusion.
- Improving Fossil Calibration:
  - The goal is to use all available fossil information in a more cohesive way.
  - This is achieved by recognizing that fossils are not just isolated time points but are products of the same underlying diversification (speciation, extinction, and fossilization) process that generated the extant taxa.
- The Fossilized Birth-Death (FBD) Process (by Stadler 2010)
  - The FBD process is a generative model that describes the birth of new lineages (speciation, rate $λ$), the death of lineages (extinction, rate $μ$), and the recovery of fossils (fossil sampling or recovery rate, $ψ$) through time.
  - It allows all relevant fossils to contribute to the analysis, not just those used to set minimum bounds on specific nodes.
  - It explicitly models the processes of speciation, extinction, and fossilization.
- [From fossils to phylogenies: exploring the integration of paleontological data into Bayesian phylogenetic inference](https://www.cambridge.org/core/journals/paleobiology/article/from-fossils-to-phylogenies-exploring-the-integration-of-paleontological-data-into-bayesian-phylogenetic-inference/BF7DB160A01BDD5183252BFB89A9699F)
- FBD was used in a detailed penguin phylogeny with geological time, highlighting known fossils, significant paleoclimatic events, and the estimated divergence times of crown penguins, illustrating the rich evolutionary narrative that can be reconstructed (Thomas et al. Proc. Roy Soc. B 2020; Cole et al, Nature Comm. 2022; .Ksepka et al. J. Paleontology 2023)

## Tutorial: Estimating a Time-Calibrated Phylogeny of Fossil and Extant Taxa using Morphological Data

- https://revbayes.github.io/tutorials/fbd_simple/

# Day 4

## Deep phylogenomics - Laura Eme

- Protein models of evolution
  - Empirical models
    - Based on alignment data.
    - Typically 20*20 matrix assuming stationarity and reversibility.
    - Dayhoff, JTT, WAG, LG etc.
    - One can also use AIC/BIC based methods (e.g. ModelFinder) to compare empirical models.
    - FreeRate model (+R): more parameters than (+G). Does not follow a parametric distribution. Not all categories will have the same number of sites.
    - Model misspecification (single-matrix models) often means systematic error (LBA).
  - Fully parameterized time-reversible model
    - GTR: estiamte 189 rate parameters from your data.
  - Mixture model
    - As reflected in Wang et al. (2008) BMC Evolutionary Biology 8: 331, the simulated data does not match the real data well, suggesting that JTT+F+G is not enough.
    - Standard protein substitution models: single Q matrix
    - Mixture models: combine several amino-acid replacement matrices
    - Can mixtured among sites, or among branches
    - Standard LG+gamma: Q matrix is the same.
    - LG4M: each gamma rate category gets its own Q matrix
    - LG4X: each rate category gets its own Q matrix BUT rates and weights are left out of the gamma distribution assumption
    - CAT: Infinite mixture model, Bayesian framework only.
    - C10, C20, …, C60: approximations of the CAT model for ML.
    - Complex mixture models are often hard to compute and fail to converge (by multiple chains). **PMSF approximation** can be useful (available in IQtree).
    - Heterotachy: changing rates of evolution at sites in different parts of the tree .
      - Covarion models
      - Rate-shift models
      - Mixture of branch-length models (GHOST in IQtree)
    - Functional shifts (functional divergence)
      - FD sites violate homogeneity assumption and artefactually increase branch-length (LBA).
      - Try the FunDi mixture model.
- Reconstructing ‘deep’ phylogenies (large-scale species trees)
  - Single gene trees are not enough to resolve ‘ancient relationships’
    - “Ancient” signal erased by more recent substitutions
  - Improving phylogenetic signal, one way is to use multiple genes.
    - Supermatrices: combining genes together
    - Supertrees
    - Reconciliation methods
  - Minimazing potential artefacts
    - Cross validation was used to test two different topologies within Obazoa are supported by different phylogenetic models: The fitted parameter values from traning set are then used to compute the likelihood of the test set: how well the test set is 'predicted' by the model?
    - Try to eliminate ‘noisiest’ data
      - Fast-evolving site removal: Check *Brown et al. 2013 PRSB*, they gradually **remove a proportion of the fastest evolving sites** (determined by the $\Gamma$ model), then they observe the topology changes, suggesting misspecified simple model (e.g. LG) gave problematic topology.
      - Fast-evolving gene removal
      - Fast-evolving taxon removal
      - Recoding
    - GFmix model: tackle compositional bias in a protein model.
    - Eme is an expert on deep evolution (a LOT of Nature papers). How does LECA looks like? How do Eukaryotes relate to Asgards? 
    - Recoding: instead of studying all 20 aa, recode them to e.g. 4 category.
    - Testing for long branch attraction: you can test different models for whether they yield even propotion of differnt topologies under simulation.
    - TODO: Check the reserach context on viruses evolution, viruses tree of life, the narrow down to flu related or coronaviruses.

## The Coalescent: Inference using trees of ‘individuals’ - Peter Beerli

- Linking population genetics (population) and phylogenetics (trees)
  - Wright-Fisher model
    - The number of generations for two individuals to coalesce it a Geometric distribution with expected value $2N$.
  - Canning mdoel
  - Moran model
  - Kingman's coalescent
    - When the population size (N) is large, the discrete-generation Wright-Fisher process can be approximated by a continuous-time process. 
    - **Scaled Coalescence Rate ($\lambda_k$) for $k$ lineages:** When time is scaled appropriately (e.g., in units of $2N$ generations for diploids, or by $\Theta=4N\mu$), the rate at which *any* pair of $k$ lineages coalesces is:
    $\lambda_k = \binom{k}{2} \frac{1}{2N} = \frac{k(k-1)}{4N}$ (the other $k−2$ lineages continue into the past without coalescing in that same infinitesimal time step or generation where the first coalescence occurred.)
    - Exponential waiting time with rate $\lambda_k$ for the next coalescent event.
    - **Probability of a Specific Genealogy ($G$) given population size $N$:** Assuming each coalescence event is independent, the probability of a given genealogy (a specific tree topology and set of coalescent times $u_j$ for each interval where there were $k_j$ lineages) is the product of the probabilities of each interval:
    $$
    P(G\vert N) = \prod_{j \text{ (intervals)}} e^{-u_j \frac{k_j(k_j-1)}{4N}} \frac{k_j(k_j-1)}{4N} \times \frac{2}{k_j(k_j-1)}
    $$
    This simplifies to:
    $$
    P(G\vert N, \text{sample size } n) = \prod_{k=2}^{n} \exp\left(-u_k \frac{k(k-1)}{4N}\right) \frac{2}{4N}
    $$
    where $u_k$ is the duration of the interval when there were $k$ lineages.
  - The time to the most recent common ancestor (TMRCA) has a large variance (He demonstrated this with a simulation, even under a same population size, tree shapes can be very different).
  - The sample size should be much smaller than the population size
- A simulator: https://phyleauxsim.github.io/coalescent/
- Genetic data and the coalescent
  - Mutation introduces new alleles into a population at rate $µ$.
  - $4N\mu$ can be estimated genetic variability $S$ (Summary statistics).
  - Using genetic variability alone therefore does not allow to disentangle $N$ and $µ$. With multiple dated samples and known generation time we can estimate N and $µ$ independently.
  - **Watterson's Estimator ($\theta_W$):** Uses the number of variable sites ($S$) in a sample of $n$ individuals from a single locus: $\theta_W = \frac{S}{\sum_{i=1}^{n-1} \frac{1}{i}}$ This estimator uses a mutation rate *per locus*
- Bayesian Inference using the Coalescent
  * Goal: Calculate $p(\text{Model Parameters } \vert  \text{Data } D)$, e.g., $p(\Theta \vert  D)$.
  * Uses Bayes' rule: $p(\Theta \vert  D) = \frac{p(\Theta) p(D \vert  \Theta)}{p(D)}$.
  * **Felsenstein-like Equation for Likelihood (integrating over genealogies):** The likelihood of the parameters $\Theta$ given the data $D$ involves integrating over all possible genealogies $G$:
      $p(D \vert  \Theta) = \int_G p(G \vert  \Theta) p(D \vert  G) dG$
      where:
    * $p(G \vert  \Theta)$: Probability density of a genealogy $G$ given parameters $\Theta$ (from the coalescent model).
    * $p(D \vert  G)$: Probability density of the data $D$ given genealogy $G$ (from the mutation model, this is the standard phylogenetic tree likelihood).

## Extensions of the basic coalescent - Peter Beerli

### Recap

* The probability of a specific genealogy $G$ (topology and coalescent times $u_j$ for intervals with $k_j$ lineages) given the mutation-scaled effective population size $\Theta = 4N_e\mu$ (for diploids) is:
    $P(G\vert \Theta) = \prod_{j \text{ (intervals)}} e^{-u_j \frac{k_j(k_j-1)}{\Theta}} \frac{2}{\Theta}$
  * This formula involves:
    * Calculating the probability of waiting time $u_j$ until a coalescence: $e^{-u_j \frac{k_j(k_j-1)}{\Theta}}$ (survival probability).
    * Calculating the probability density of the specific coalescence event happening: $\frac{k_j(k_j-1)}{\Theta}$ (rate of coalescence for $k_j$ lineages) multiplied by the probability of a specific pair coalescing (which is $2/(k_j(k_j-1))$, simplifying the rate term for the interval to $2/\Theta$).
  * This allows calculating the probability density of a genealogy given $\Theta$.

### Extensions of the Coalescent

- The basic coalescent assumes a single, constant-sized, randomly mating population. Extensions address more realistic scenarios:
* **Exponential Growth Model:** If population size changes exponentially, $N(t) = N_0 e^{-gt}$ (where $N_0$ is current size, $t$ is time into the past, and $g$ is growth rate towards the present). The probability of a genealogy becomes:
$P(G\vert \Theta_0, g) = \prod_{j \text{ (intervals)}} e^{-(t_j - t_{j-1}) \frac{k(k-1)}{\Theta_0 e^{-gt_j}}} \frac{2}{\Theta_0 e^{-gt_j}}$ (Here, $t_j$ is the time at the end of the interval with $k$ lineages, and $\Theta_0$ is the current mutation-scaled population size).
* **Skyline Plots (Random Fluctuations):** Methods like Bayesian Skyline (BEAST), Skyride, Skyfish (BEAST, RevBayes) can estimate population size changes over time.
* **Bottlenecks:** Estimating bottlenecks depends on their severity, duration, and the amount of data (sample size, number of loci), it is HARD.
- **Migration Among Populations (Structured Coalescent):**
  * For multiple populations, the overall rate of events (coalescence or migration) changes. For two populations (1 and 2) with $k_1$ lineages in pop 1 and $k_2$ in pop 2, the total rate of any event is: 
  $$
  \text{Total Rate} = \underbrace{\frac{k_1(k_1-1)}{\Theta_1}}_{\text{coalescence in pop1}} + \underbrace{\frac{k_2(k_2-1)}{\Theta_2}}_{\text{coalescence in pop2}} + \underbrace{k_1 M_{21}}_{\text{migration 1 } \leftarrow \text{ 2}} + \underbrace{k_2 M_{12}}_{\text{migration 2 } \leftarrow \text{ 1}}
  $$
  where $M_{ij}$ is the scaled migration rate from population $j$ to $i$ (e.g., $M_{21} = 4N_1m_{21}$ if $\Theta_1=4N_1\mu$).

- **Population Splitting (Divergence Models):**
  * Used to estimate divergence times ($\tau$), ancestral population sizes, and migration rates between diverging populations (e.g., Isolation with Migration - IM models).
  * Tracing lineages backward: a lineage in population A today had an ancestor in an ancestral population B. The timing of this "population label switch" can be modeled using hazard functions (e.g., based on a Normal distribution for the divergence time).
  * The resulting genealogies incorporate coalescence, migration, and population splitting events.
  * More loci generally improve the precision of divergence time estimates.

### Robustness and Assumptions of the Coalescent

* **Sample Size ($n \ll N_e$):** Kingman's n-coalescent assumes at most two lineages merge per generation (no multiple mergers). This is a good approximation if $n \ll N_e$ (e.g., $n < \sqrt{4N_e}$ for diploids). It's fairly robust even if this is moderately violated, as multiple mergers become very rare with large $N_e$.
* **TMRCA Estimation:** The Time to Most Recent Common Ancestor (TMRCA) is often robust to sample size; even small samples can yield similar TMRCA estimates to large samples. Adding more independent loci is often more beneficial than adding more individuals per locus beyond a certain point (e.g., >8 individuals ).
* **Long-Term Averages:** Coalescent parameter estimates represent averages over long evolutionary timescales.
* **Recombination:** Standard coalescent typically assumes no intra-locus recombination. Recombination means different segments of a locus can have different genealogical histories. Ignoring recombination when it's present can bias estimates of $\Theta$ (often upwards) and migration rates (often downwards).

### Mutation Models and Genetic Data in Coalescent Inference

* **Confounding $N_e$ and $\mu$:** Genetic diversity (e.g., number of segregating sites $S$) is primarily a function of the product $N_e\mu$ (scaled as $\Theta$). It's hard to estimate $N_e$ and $\mu$ separately from genetic data alone without external information (like dated samples or known mutation rates per generation).
* **Methods of Inference:**
  * **Watterson's Estimator ($\theta_W$):** $\theta_W = \frac{S}{\sum_{i=1}^{n-1} (1/i)}$ (uses mutation rate per locus).
  * **Bayesian Inference:** Calculates $p(\Theta \vert  D) \propto p(\Theta) \int_G p(G\vert \Theta)p(D\vert G)dG$. The integral sums/averages over all possible genealogies ($G$) and is usually computed via MCMC.
* **Types of Mutation Models for $p(D\vert G)$:**
  * **Infinite Sites Model:** Assumes every new mutation occurs at a brand new site (no multiple hits). Leads to SNP data (bi-allelic markers). Often used with Site Frequency Spectra (SFS).
  * **Finite Sites Models (e.g., JC69, HKY, GTR):** Allow multiple hits, back mutations. Used for aligned DNA sequences.
* **Site Frequency Spectrum (SFS):**
  * The distribution of allele frequencies in a sample. Many recent population genomic methods use the SFS, often assuming an infinite sites model.
  * **Challenges with SFS:**
    * Accommodating real data to the infinite sites model (defining ancestral alleles, handling multi-allelic sites, errors).
    * SNP ascertainment bias: How SNPs are discovered can bias the SFS if not corrected.
    * May be problematic for species with high diversity / large $N_e$ where the infinite sites assumption is often violated (e.g., many tri-allelic sites observed in *Anopheles*).

- [Population divergence time estimation using individual lineage label switching](https://academic.oup.com/g3journal/article/12/4/jkac040/6528849?login=true)
- A potential mistake in [The Anopheles gambiae 1000 Genomes Consortium: Genetic diversity of the African malaria vector Anopheles gambiae. Nature, 552(7683):96–100, Dec 2017](https://pubmed.ncbi.nlm.nih.gov/29186111/), they report very high rate for positions with $>2$ mutations.

## Genomic data for evolutionary inference - Emily Jane McTavish

The talk emphasizes that while the quantity of sequence data is rapidly increasing, outstripping analytical capabilities (a point made by Jeff Thorne as early as 1991), many choices and potential pitfalls exist:

### Orthology vs. Paralogy

* Distinguishing orthologs (genes diverged by speciation) from paralogs (genes diverged by duplication) is critical.
* Including unrecognized paralogs can lead to incorrect phylogenetic inferences, as demonstrated by an example of turtle phylogeny where a small number of paralogous alignments had an extraordinary influence.
* Newer "orthology-free" methods like ROADIES aim to infer species trees directly from raw genome assemblies by sampling genes, performing pairwise alignments, and iteratively estimating gene and species trees (dubious).

### Speed vs. Accuracy of Phylogenetic Inference Methods
* For very large datasets (1000+ sequences), different ML tree inference software offer trade-offs:
  * **RAxML/ExaML:** Very efficient, especially with multiple runs.
  * **IQ-TREE:** Also fast and relatively accurate.
  * **FastTree:** Very fast but may have trade-offs with accuracy.
  - Fasttree joke: It is fast, and it is a tree.
* The presentation notes that "quick and dirty or black box methods" used for large datasets might lead to worse answers if not carefully considered.
* Newer methods like CASTER (a site-based quartet method) are very fast but their performance on complex, real-world problems needs further evaluation.
- Comments on [CASTER: Direct species tree inference from whole-genome alignments](https://www.science.org/doi/10.1126/science.adk9688): If you have to use “quick and dirty” or black box methods in order to be able to analyze large data sets - more data may result in WORSE answers.

### Is the Species Tree Always What You Want?
* Different genes can have different evolutionary histories (gene trees) due to processes like incomplete lineage sorting or introgression.
* If interested in a trait controlled by one or a few genes, the species tree may not accurately describe the evolutionary history of those specific genes.
* Holistic genome approaches, like considering ancient gene linkages, can offer insights into deep evolutionary questions, such as the sister group to all other animals.

### Data Processing Choices and Ascertainment Bias
* **Ascertainment bias** is a bias in parameter estimation or testing caused by non-random sampling of data. It is ubiquitous and can arise from how data is collected or filtered (e.g., sampling across the tree of life, volunteer surveys, studying undergraduates).
* **Missing Data in RADseq:** Factors like mutations at restriction sites, clustering parameters, or low coverage can cause allele drop-out. While random missing data might not be highly problematic, phylogenetically-biased missing data can mislead inference, affecting topology, branch lengths, and support values. Simply excluding sites with high missing data can bias rate estimation downwards by preferentially removing high-rate loci. There are no universal "rules-of-thumb" for handling this due to complex interactions. Investigating a range of filtering parameters is advised. The Penstemon RADseq case study shows that missing data can be phylogenetically biased, with many loci found only in one of the major clades, suggesting that analyzing clades **separately** or using different filtering parameters might be necessary.
* **Sequencing Error:** Can be problematic when true variation is rare, as errors (often singletons) can overestimate tip branch lengths. While error correction methods exist and genotype likelihoods could help, these are not always implemented in standard phylogenetic likelihood models. High coverage likely reduces the impact of sequencing error.
  - TODO: Can sequencing quality data used and implemented in phylogenetic likelihood models?
* **Reference Genome Choice:** Mapping reads to a reference can speed up consensus sequence generation but can also introduce bias. Variant calling can be biased towards the reference base in polymorphic regions, and branch lengths can change based on reference choice. Error rates can be correlated with distance to the reference, with errors biased towards the reference base. Reference choice can even affect topology. While sequence calls may change based on the reference, overall phylogenetic conclusions might sometimes remain unaffected.
  - Base call errors match the reference base 97% of the time, so the choice of reference genome can have a large impact on the phylogeny.
  - A useful tutorial on Reference Bias: https://github.com/snacktavish/TreeUpdatingComparison/blob/master/TreeUpdating.md
- [Free textbook: Phylogenetics in the Genomic Era](https://inria.hal.science/PGE/page/table-of-contents)

## Open Tree of Life project

### The Need for a Comprehensive Tree of Life

* New and improved evolutionary trees are constantly published, but even large-scale efforts often miss a significant fraction of known biodiversity (e.g., a recent plant phylogeny covering 8,000 species still missed 40% of plants).
* Taxonomy is often used as a proxy for evolutionary history, but it can be a coarse or even misleading representation.
* Researchers use taxonomy because comprehensive phylogenies are often not available for all species of interest, keep changing, or are hard to access.

### Features and Functionality

* **Taxonomic Integration:** Users can view the lineage of any taxon within the Open Tree Taxonomy (OTT). New taxa from uploaded trees can be added and will be incorporated into future synthetic trees, with opportunities for feedback to source taxonomies.
* **Synthetic Tree:** A continuously updated tree that synthesizes information from the curated phylogenies and the taxonomic backbone. It visualizes phylogenetic information and areas of conflict.
* **Date Estimates (DATELife):**
  * The main synthetic tree currently does not have inherent branch lengths because combining diverse data types (DNA, morphology, taxonomy) makes direct branch length synthesis non-obvious.
  * However, the DATELife project (Sanchez-Reyes, McTavish, O'Meara, 2024) allows for the translation of date estimates from input chronograms (dated trees) onto the Open Tree synthetic topology or a user-provided tree.
  * It works by matching taxa, finding congruent nodes between source chronograms and the target topology, and using median pairwise node ages to date the target tree.

### Why Use Open Tree?

* **For common community phylogenetic analyses:** Studies suggest that using synthesis phylogenies like the Open Tree of Life is justified and often sufficient.
* **Large-scale diversity assessment:** Facilitates projects like PhyloNext for analyzing phylogenetic diversity of GBIF-mediated data.
* **Conservation:** Can be used to measure potential loss of evolutionary distinct history due to extinctions by identifying species at risk that represent significant unique evolutionary heritage.
* **Convenience:** Easily get accurate relationships and citations for arbitrary sets of species (e.g., finding the closest relative with a reference genome).
* **Custom Synthesis:** Users can generate custom synthetic trees for their specific taxa of interest, potentially with personalized phylogeny rankings and choice of root.
* **Bird Tree Example:** A synthesis phylogeny of all birds (McTavish et al., 2025) covering 87% of species, built from 321 published trees, is available [A complete and dynamic tree of birds](https://www.pnas.org/doi/abs/10.1073/pnas.2409658122).

# Day 5
