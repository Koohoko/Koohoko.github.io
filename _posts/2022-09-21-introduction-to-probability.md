---
title: "Book notes: Introduction to Probability (Dimitri P. Bertsekas and John N. Tsitsiklis, 2008)"
date: 2022-09-21
permalink: /posts/2022-09-21/introduction-to-probability
categories:
  - Book notes
tags:
  - Mathematics
  - Probability
toc: true
last_modified_at: 2022-12-13
---

This post records the notes when I read [*Introduction to Probability*](https://www.amazon.com/Introduction-Probability-2nd-Dimitri-Bertsekas/dp/188652923X) by Dimitri P. Bertsekas and John N. Tsitsiklis. 

## Sample Space and Probability
### Probabilistic models
- Sample space must be *collectively exhaustive*, i.e., different elements of the sample space should be distinct and mutually exclusive. The sample space is usually denoted Ω.

### Conditional probability
- The Monty Hall Problem, Switch to the other unopened door will result in 2/3 probability of winning.

### Total probability theorem and Bayes' rule
- Total Probability Theorem
<img src="/files/2022-09-21-introduction-to-probability/Screenshot%202022-09-27%20at%2015.54.42.png" width="500"/>
- Bayes' Rule
<img src="/files/2022-09-21-introduction-to-probability/Screenshot%202022-09-28%20at%2016.55.07.png" width="500"/>
  - Posteriro and prior probability: Given that the effect $B$ has been observed, we wish to evaluate the probability $P(A_i|B)$ that the cause $A_i$ is present. We refer to $P(A_i|B)$ as the **posterior probability** of event $A_i$ given the information, to be distinguished from $P(A_i)$, which we call the **prior probability**.

### Independence and counting
- A very important point here is that we usually test the independence **numerically**, rather than logically, see below:
<img src="/files/2022-09-21-introduction-to-probability/Screenshot%202022-12-13%20at%2015.09.32.png" width="500"/>

- Independent Bernoulli trials form Binomial model. Note that the binomial probabilities add to 1, thus showing the binomial formula: $\sum_{k=0}^n{n \choose k}p^k(1-p)^{n-k}=1$. In the special case where $p=0.5$, this formula becomes $\sum_{k=0}^n{n \choose k}=2^n$. This equal to the number of all subsets of an n-element set. which is $2^n$ (全子集问题：针对每一个元素，都有取或不取两个选择，因此总共的不同的子集数量为$2^n$).
s
- If the order of selection matters, the selection is called a permutation, and otherwise, it is called a combination.

- **Partitions**: 
- <img src="/files/2022-09-21-introduction-to-probability/Screenshot%202022-12-13%20at%2015.37.03.png" width="500"/>

- A very useful example: How many different words (letter sequences) can be obtained by rearranging the letters in the word TATTOO? 
<img src="/files/2022-09-21-introduction-to-probability/Screenshot%202022-12-13%20at%2015.44.41.png" width="500"/>

- The above question have a similar application in genomic study, how many different synonymous genomes can be obtained by swapping the synonymous codons in the genome?

## Discrete random variables
### Basic concepts
- Mathematically, a random variable is a real-valued function of the experimental outcome (Random variables must have explicit numerical values). Thus, a function of a random variable defines another random variable (e.g. one can constrcut Binomial random variable with Bernoulli random variable).
- A random variable is called **discrete** if its range (the set of values taht it can take) is either finite or countably infinite.
- A discrete random variable has an associated probability mass function (PMF). which gives the probability of each numerical value that the random variable can take.

### Probability mass functions
- The **binomial random variable** is the number of heads X in the n-toss sequence : $P(X=k)={n \choose k}p_k(1-p)^{n-k},k=0,1,...,n.$
- The **geometric random variable** is the number X of tosses needed for a head to come up for the first time: $P(X=k)=(1-p)^{k-1}p, k=1,2,...$. Also note that the *sum of geometric sequence* $S_n=\sum_{k=0}^{\infty}p^k=\frac{1-p^{n+1}}{1-p}$ (using $pS_n - S_n$ to derive this), so when $n \to \infty$ it becomes $\frac{1}{1-p}$. Thus, sum of the PMF: $\sum_{k=1}^{\infty}(1-p)^{k-1}p=p\sum_{k=0}^{\infty}(1-p)^k=p\frac{1}{1-(1-p)}=1.$
- The **Poisson random variable** is the number X of success (small $p$) in (large $n$) total events. The PMF: $P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}, k=0,1,2,...$ where $\lambda$ is a positive parameter, I tend to think $\lambda$ as the expected number of success for each individual ($np$). The Poisson PMF can approximate the binomial PMF when $n$ is large and $p$ is small. Using Poisson PMF may result in simpler model and calculation.

### Expectance and variance
Expectance: $E[g(X)] = \sum_xg(x)p_X(x)$ 
Variance: $var(X) = \sum_x(E[X]-x)^2p_X(x)$
A convenient alternative formula: $var(X) = -(E[X])^2 + E[X^2]$

### Mean and variance of some common random variables
- Bernoulli: 
  $E[X] = p$,
  $E[X^2] = 1^2*p+0^2*(1-p)=p$,
  $var(X) = (1-p)^2p+p^2(1-p)=p(1-p)(1-p+p)=p(1-p)$.
