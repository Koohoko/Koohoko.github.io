---
title: "Paper digest: More structured coalescent papers: on Erik M. Volz's work"
date: 2025-01-12
permalink: /posts/2025-01-10-Structured_coalescent4
categories:
  - Paper digest
tags:
  - Coalescent theory
  - Structured coalescent
  - Phylogenetics
toc: true
# last_modified_at: 2025-01-05
---

Back on 2012, [Eric M. Volz](https://scholar.google.com/citations?user=cp2B1yUAAAAJ&hl=en) had


## [Complex Population Dynamics and the Coalescent Under Neutrality](https://academic.oup.com/genetics/article/190/1/187/6063310) by *Eric M. Volz* on Genetics, 2012.

## Summary

- In this paper, Erik showed how to derive the rate of coalescence, as well as the likelihood of a gene genealogy with heterochronous sampling and labeled taxa, and how to simulate a coalescent tree conditional on a complex demographic history.

1. **A New Coalescent Framework:** The paper develops a coalescent model for populations with complex, non-linear dynamics described by deterministic systems of arbitrary dimensions. It handles:
   *   **Varying Birth and Death Rates:** Unlike standard coalescent models, it doesn't assume constant rates. Birth and death rates can be any differentiable function of time and the state of the system.
   *   **Structured Populations:** It accounts for population structure (multiple "demes") where gene copies can reproduce within and across demes, and migration can occur.
   *   **Large Sample Fractions:** The model can handle scenarios where a significant portion of the population is sampled, which is often the case in epidemiological studies.
2. **Derivation of Coalescent Rate Under Birth-death Process:** 
   - The rate of coalescence (λ<sub>2</sub>) for two lineages is $\frac{1}{Y({s})}$ under Kingman coalescent.
   - Under a birth–death process with varying rates. It shows that λ<sub>2</sub> is not simply the inverse of the population size (1/Y), but rather a function of both population size and the time-varying birth rate: $λ_2(s) = 2f(s)/Y^2(s)$.
   - The birth rate $f(t)=\beta X(t)Y(t)$ correspond to $\beta SI$ in the SIR model.
   - In traditional Birth-Death model, $f(t)=cY(t)$, where $c$ is a constant, such as exponential growth.
   - The birth rate of a singe copy is $f(t, Y)/Y(t)$, it is both time ($f(t, Y)$) and state ($Y(t)$) dependent.
   - Classical solutions, such as $\lambda_2(s) \propto 1/Y(s)$, appear as special cases when births are strictly proportional to population size. 
   - The coalescent rate is under BD model, in Moran's style:
    
    $$  
    F(s) = \int_0^s f(\tau) \, d\tau,\\
    \Lambda_2(s) = \sum_{j=1}^{\lfloor F(s) \rfloor} \frac{\sigma^2_M(j)}{\overline{Y}(j)}.
    $$
   - After some steps we reached:
    
    $$
    \lambda_A(s) = \left( \frac{A(s)}{2} \right) \frac{2f(s)}{Y^2(s)}.
    $$

3. **Bias in Skyline Estimators:** It demonstrates that non-parametric estimators of N<sub>e</sub>, such as the skyline plot, can be biased when birth rates are not proportional to population size. This is particularly relevant in scenarios like "Faster Than Exponential" (FTE) or "Slower Than Exponential" (STE) growth, which can occur during epidemics.
4. **Number of Lineages Through Time (NLFT):** The paper explores the relationship between the NLFT and population dynamics. It shows that the NLFT is sensitive to the history of birth rates, not just population size, leading to potentially counterintuitive interpretations of tree shapes.
5. **Structured Populations:** It extends the coalescent to structured populations with concurrent birth, death, and migration processes. It derives a master equation for the rate of coalescence in such scenarios.
   - Note that in the structured coalescent model in this paper, Gene copies may reproduce both **within and across** demes. Consequently, two gene copies in different demes may coalesce without being preceded by a migration event (which may be too simplistic for some scenarios).
   - TOO many formulas, I will skip them here.
6. **Simulation and Likelihood:** The paper presents methods for simulating coalescent trees and calculating the likelihood of a gene genealogy conditional on a complex demographic history, including structured populations.

