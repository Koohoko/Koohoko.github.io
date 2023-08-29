---
title: "Paper digest: Informing policy via dynamic models: cholera in Haiti (Jesse Wheeler)"
date: 2023-08-11
permalink: /posts/2023-08-11/2023-08-11-modelling_cholera_haiti
categories:
  - Paper digest
tags:
  - Infectious Disease Modelling
toc: true
# last_modified_at: 2022-09-01
---

[This paper](https://doi.org/10.48550/arXiv.2301.08979) is from Edward L. Ionides et al. It considers the 2010-2019 cholera epidemic in Haiti, and studies three dynamic models developed by expert teams to advise on vaccination policies. Importantly, the paper demonstrates the basic usage of the SpatPOMP model. The [code](https://github.com/jeswheel/haiti_article) and [software](https://github.com/jeswheel/haitipkg) are also provided.

## Introduction
Population dynamics may be nonlinear and stochastic, with the resulting complexities compounded by incomplete understanding of the underlying biological mechanisms and by partial observability of the system variables. Quantitative models for these dynamic systems offer potential for designing effective control measures.

Questions of interest include:
- What indications should we look for in the data to assess whether the model-based inferences are trustworthy?
- What diagnostic tests and model variations can and should be considered in the course of the data analysis? 
- What are the possible trade-offs of increasing model complexity, such as the inclusion of interactions across spatial units?

Three models from different expert groups were considered:
- **Model 1** is stochastic and describes cholera at the national level; 
- **Model 2** is deterministic with spatial structure, and includes transmission via contaminated water;
- **Model 3** is stochastic with spatial structure, and accounts for measured rainfall. 

The groups largely adhered to existing guidelines on creating models to inform policy ([Behrend et al., 2020](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0008033); [Saltelli et al., 2020](https://www.nature.com/articles/d41586-020-01812-9))

## Mechanistic models for cholera in Haiti
- Models that focus on learning relationships between variables in a dataset are called associative, whereas models that incorporate a known scientific property of the system are called causal or mechanistic.
- Lucas critique: Lucas et al. (1976) pointed out that it is naive to predict the effects of an intervention on a given system based entirely on historical associations.
- **Model 1**: The model was implemented by a team at Johns Hopkins Bloomberg School of Public Health (here- after referred to as the Model 1 authors) in the R programming language using the pomp package (King et al., 2016). Original source code is publicly available with DOI: 10.5281/zenodo.3360991.
  - SEIAR model: describes susceptible, latent (exposed), infected (and symptomatic), asymptomatic, and recovered individuals in vaccine cohort $z$. Here, $z = 0$ corresponds to unvaccinated individuals, and $z ∈ 1:Z$ describes hypothetical vaccination programs.
  - Reported cholera cases at time point $n$ ($Y_n$) are assumed to come from a negative binomial measurement model, where only a fraction ($ρ$) of new weekly cases are reported.
- **Model 2**: Model 2 was developed by a team that consisted of members from the Fred Hutchinson Cancer Research Center and the University of Florida (hereafter referred to as the Model 2 authors). While Model 2 is the only deterministic model we considered in our analysis, it contains perhaps the most complex descriptions of cholera in Haiti: Model 2 accounts for movement between spatial units; human-to-human and environment-to-human cholera infections; and transfer of water between spatial units based on elevation charts and river flows.
The source code that the Model 2 authors used to generate their results was written in the Python programming language, and is publicly available at 10.5281/zenodo.3360857 and its accompanying GitHub repository https://github.com/lulelita/HaitiCholeraMultiModelingProject. 
  - Susceptible individuals are in compartments $S_{uz}(t)$, where $u ∈ 1:U$ corresponds to the $U = 10$ departments, and $z ∈ 0:4$ describes vaccination status:
    - z = 0: Unvaccinated or waned vaccination protection. 
    - z = 1: One dose at age under five years.
    - z = 2: Two doses at age under five years.
    - z = 3: One dose at age over five years.
    - z = 4: Two doses at age over five years.
  - Individuals can progress to a latent infection $E_{uz}$ followed by symptomatic infection $I_{uz}$ with recovery to $R_{uz}$ or asymptomatic infection $A_{uz}$ with recovery to $R^A_{uz}$. The force of infection depends on both direct transmission and an aquatic reservoir, $W_u(t)$.
  - Reported cases are assumed to come from a log-normal distribution, with the log-scale mean equal to the reporting rate $ρ$ times the number of newly infected individuals.
- **Model 3**: Model 3 was developed by a team of researchers at the Laboratory of the Swiss Federal Institute of Technology in Lausanne, hereafter referred to as the Model 3 authors. The code that was originally used to implement Model 3 is archived with the DOI: 10.5281/zenodo.3360723, and also available in the public GitHub repository: jcblemai/haiti-mass-ocv-campaign. 
  - The latent state is described as $X(t)=(S_{uz}(t), I_{uz}(t), A_{uz}(t), R_{uzk}(t), W_{u}(t), u \in 0:U, z \in 0:4, k \in 1:3)$. $k ∈ 1:3$ models non-exponential duration in the recovered class before waning of immunity.