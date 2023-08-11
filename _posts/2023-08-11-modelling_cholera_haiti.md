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
- Model 1 is stochastic and describes cholera at the national level; 
- Model 2 is deterministic with spatial structure, and includes transmission via contaminated water;
- Model 3 is stochastic with spatial structure, and accounts for measured rainfall. 

The groups largely adhered to existing guidelines on creating models to inform policy ([Behrend et al., 2020](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0008033); [Saltelli et al., 2020](https://www.nature.com/articles/d41586-020-01812-9))