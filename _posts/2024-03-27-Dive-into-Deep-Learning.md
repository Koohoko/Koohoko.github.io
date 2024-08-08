---
title: "Course notes: Dive into Deep Learning (D2L) / 动手学深度学习"
date: 2024-03-27
permalink: /posts/2024-03-27/Dive-into-Deep-Learning
categories:
  - Course notes
tags:
  - Deep Learning
toc: true
last_modified_at: 2024-03-27
---

I decide to take this course by myself. It will likely last for a few months. I hope I will finishing it by September 2024. I like it at the first glance because it is fully open-sourced and I heard that it is quite popular.

**Content and Structure**
![Content and Structure](https://d2l.ai/_images/book-org.svg)

## 1. Introduction

*Machine learning* is the study of algorithms that can learn from experience. In this book, we will teach you the fundamentals of machine learning, focusing in particular on deep learning, a powerful set of techniques driving innovations in areas as diverse as computer vision, natural language processing, healthcare, and genomics.

### Key components of machine learning

1. The *data* that we can learn from.
2. A *model* of how to transform the data.
3. An *objective function* (loss function) that quantifies how well (or badly) the model is doing.
4. An algorithm to adjust the model’s parameters to *optimize* the objective function.

### Kinds of Machine Learning Problems

1. *Supervised learning*: the model is trained on a labeled dataset.
     1. *Regression*: the model predicts a continuous value. (How much? How many?) (square error loss)
     2. *Classification*: the model predicts a discrete label. (Which one?) (cross-entropy loss)
     3. *Tagging*: multi-label classification.
     4. *Search*: Impose a ranking on a set of items.
     5. *Recommendation*: Predict the preference of a user for an item.
     6. *Sequence learning*: Predict the next element in a sequence (or sequence-to-sequence learning).

2. Unsupervised and self-supervised learning: the model is trained on an unlabeled dataset.
     1. *Clustering*: Group similar data points together.
     2. *Dimensionality reduction (subspace estimation)*: Simplify the data without losing too much information.
     3. *Symbolic reasoning*: Discover patterns in data.
     4. *Causal discovery (e.g., probabilistic graphical models)*: Infer cause-and-effect relationships.
     5. *Deep generative modeling*: Generate new data samples. These models estimate the density of the data, either explicitly or implicitly. Once trained, we can use a generative model either to score examples according to how likely they are, or to sample synthetic examples from the learned distribution. Early deep learning breakthroughs in generative modeling came with the invention of variational autoencoders (Kingma and Welling, 2014, Rezende et al., 2014) and continued with the development of generative adversarial networks (Goodfellow et al., 2014). More recent advances include normalizing flows (Dinh et al., 2014, Dinh et al., 2017) and diffusion models (Ho et al., 2020, Sohl-Dickstein et al., 2015, Song and Ermon, 2019, Song et al., 2021).

3. Interacting with an Environment
We want to think about intelligent agents, not just predictive models. This means that we need to think about choosing actions, not just making predictions. In contrast to mere predictions, actions actually impact the environment. If we want to train an intelligent agent, we must account for the way its actions might impact the future observations of the agent, and so offline learning is inappropriate. This is the realm of reinforcement learning.

4. Reinforcement Learning
In reinforcement learning, an agent interacts with an environment, learning how to behave by receiving feedback in the form of rewards or punishments. 

Reinforcement learning have to deal with many interesting challenges that do not arise in supervised learning. For instance, the agent must balance exploration (trying out new things) and exploitation (doing what has worked well in the past). It must also consider the fact that rewards might be delayed in time, and that actions might have long-lasting consequences. Also, reinforcement learners must deal with the credit assignment problem: determining which actions to credit or blame for an outcome. Reinforcement learners may also have to deal with the problem of partial observability. That is, the current observation might not tell you everything about your current state.

When the environment is fully observed, we call the reinforcement learning problem a *Markov decision process*. When the state does not depend on the previous actions, we call it a *contextual bandit problem*. When there is no state, just a set of available actions with initially unknown rewards, we have the classic *multi-armed bandit problem*.

## 2. Preliminaries

### Data Manipulation


