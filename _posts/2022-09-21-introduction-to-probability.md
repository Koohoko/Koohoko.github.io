---
title: "Book notes: Introduction to Probability"
date: 2022-09-21
permalink: /posts/2022-09-21/introduction-to-probability
categories:
  - Book notes
tags:
  - Mathematics
  - Probability
toc: true
# last_modified_at: 2022-09-01
---

This post records the notes when I read [*Introduction to Probability*](https://www.amazon.com/Introduction-Probability-2nd-Dimitri-Bertsekas/dp/188652923X) by Dimitri P. Bertsekas and John N. Tsitsiklis. 

## Sample Space and Probability
### Sets
- **De Morgan's laws**
![](/files/2022-09-21-introduction-to-probability/IMG_6FB930A919BE-1.jpeg)

### Probabilistic models
- **Sample space** must be *collectively exhaustive*, i.e., different elements of the sample space should be distinct and mutually exclusive. The sample space is usually denoted Ω.

### Conditional probability
- **The Monty Hall Problem**, Switch to the other unopened door will result in 2/3 probability of winning.

### Total probability theorem and Bayes' rule
- Total Probability Theorem
![](/files/2022-09-21-introduction-to-probability/Screenshot%202022-09-27%20at%2015.54.42.png)
- Bayes' Rule
![](/files/2022-09-21-introduction-to-probability/Screenshot%202022-09-28%20at%2016.55.07.png)
  - Posteriro and prior probability: Given that the effect $B$ has been observed, we wish to evaluate the probability $P(A_i|B)$ that the cause $A_i$ is present. We refer to $P(A_i|B)$ as the **posterior probability** of event $A_i$ given the information, to be distinguished from $P(A_i)$, which we call the **prior probability**.

### Independence
