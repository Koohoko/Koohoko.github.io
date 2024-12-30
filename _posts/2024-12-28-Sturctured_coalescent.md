---
title: "Notes: Structured coalescent"
date: 2024-12-28
permalink: /posts/2024-12-28/Structured_coalescent
categories:
  - Paper digest
tags:
  - Structured coalescent
  - Phylogenetics
toc: true
# last_modified_at: 2024-09-01
---

I wanted to get in more details about the structured coalescent model, here I record some notes when I read related papers/tutorials, and watch videos.

# Coalescent quick recap

It is a series of short [Youtube videos by Scott Roy](https://www.youtube.com/playlist?list=PLXbnX6Ihecnmngifb2E_L3nqwR2tiLcTu).

- Coalescent is about mathematically trace back in time to find a appropriate tree shape / genealogy that can explain the observed data.
- Geometric Series Summation: $\sum_{i=0}^{\infty}{r^i} = \frac{1}{1-r}$ (note that $0<r<1$, and r can be a probability of coalescence). So that $\sum_{i=0}^{\infty}{(1-p)^i} = \frac{1}{p}$. 
- Time for $n=2$ individuals to coalescence is a classic waiting problem:
$$
P(t)=(\frac{N-1}{N})^{t-1}\frac{1}{N}\\
E(t)=\frac{1}{\frac{1}{N}}=N
$$
- Expected waiting time for coalescence (discrete): 
$$
\begin{align*}
E[t] &= 1p+2p(1-p)+3p(1-p)^2+... \\
&=\sum_{i=0}^{\infty}{(i+1)p(1-p)^i} =\sum_{i=1}^{\infty}{ip(1-p)^i} =\sum_{i=0}^{\infty}{ip(1-p)^i}\\
&=\sum_{i=0}^{\infty}{ip(1-p)^i} + \sum_{i=0}^{\infty}{1p(1-p)^i}\\
&=(1-p)\sum_{i=0}^{\infty}{ip(1-p)^{i-1}}+p\sum_{i=0}^{\infty}{(1-p)^i}\\
&=(1-p)E[t]+p\frac{1}{p}\\
&=\frac{1}{p}
\end{align*}
$$
- Time for $n>2$ individuals to coalescence: 
  - First coalescence:
  $$
  E(t)=\frac{1}{\frac{n\choose2}{N}}=\frac{N}{n\choose2}
  $$
  - Second coalescence:
  $$
  E(t)=\frac{N}{n-1\choose2}
  $$
  - Third coalescence:
  $$
  E(t)=\frac{N}{n-2\choose2}
  $$
  - ...
  - Such that the coalescence time is getting longer for deep branches.
- To jointly model mutation process and coalescent process, we need to consider the mutation rate $\mu$ and coalescent rate $\lambda$. The expected number of mutations before the first coalescence is: 
  $$
  \begin{align*}
  E(mut)&=\frac{\mu}{\lambda}\\
  &=\frac{n\mu}{n\frac{n\choose2}{N}}\\
  &=\frac{2N\mu}{n-1}.
  \end{align*}
  $$
  As a result, the expected number of mutations increases backwards in time (as $n$ is decreasing).