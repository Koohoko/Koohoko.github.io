---
title: 激励回归树模型回顾
date: 2016-01-18 20:35:16
tags: [BRT,Machine learning,激励回归树]
categories: Methodology
description: A Review of Boosted Regression Trees
---

根据~~基本法~~本人之前的承诺，本来技术性文章是要用英文写的。但是现在我后悔了。。还是决定先用中文好了。

### What is BRT? 什么是激励回归树？
#### 回归
我们探索多变量之间的关系的时候，经常会用到回归。从最简单的最小二乘回归，到对因变量作变换的广义线性回归（Generalized Linear Models），再到用样条函数（natrual splines）来拟合非线性关系的广义相加模型（Generalized Addictive Models），每个模型都有它自己的特点。

#### 树模型
对于树模型，大家容易会想到决策树（Decision Trees）和随机森林（Random Forests）。决策树的想法很朴素，就像二叉树一样，一直作分类，它的优势就是简单快捷。随机森林可以理解为很多棵决策树的集合，大家来共同预测，最后选出大家投票最多的作为结果。在随机森林的基础上，还有Gradient Boost Decision Tree，这些方法在很多Data Mining的Tutorial都会提到，都是传统的分类方法。

#### 激励回归树
对于BRT简要的历史，以下引用几段我觉得写得很清晰的:

> [Elith J, Leathwick J R, Hastie T. A working guide to boosted regression trees[J]. Journal of Animal Ecology, 2008, 77(4): 802-813.](http://soilslab.cfr.washington.edu/Publications/Elith-etal-2008.pdf)

> The past 20 years have seen a growing sophistication in the types of statistical model applied in ecology, with impetus from substantial advances in both statistics and computing. Early linear regression models were attractively straightforward, but too simplistic for many real-life situations. In the 1980s and 1990s, generalized linear models (GLM; McCullagh & Nelder 1989) and generalized additive models (GAM; Hastie & Tibshirani 1990) increased our capacity to analyse data with non-normally distributed errors (presence–absence and count data), and to model nonlinear relationships. These models are now widely used in ecology, for example for analysis of morphological relationships (Clarke & Johnston 1999) and population trends (Fewster et al. 2000), and for predicting the distributions of species (Buckland & Elston 1993).  
> Over the same period, computer scientists developed a wide variety of algorithms particularly suited to prediction, including neural nets, ensembles of trees and support vector machines. These machine learning (ML) methods are used less frequently than regression methods in ecology, perhapspartly because they are considered less interpretable and therefore less open to scrutiny. It may also be that ecologists are less familiar with the modelling paradigm of ML, which differs from that of statistics. Statistical approaches to model fitting start by assuming an appropriate data model, and parameters for this model are then estimated from the data. By contrast, ML avoids starting with a data model and rather uses an algorithm to learn the relationship between the response and its predictors (Breiman 2001). The statistical approach focuses on questions such as what model will be postulated (e.g. are the effects additive, or are there interactions?), how the response is distributed, and whether observations are independent. By contrast, the ML approach assumes that the data-generating process (in the case of ecology, nature) is complex and unknown, and tries to learn the response by observing inputs and responses and finding dominant patterns. This places the emphasis on a model’s ability to predict well, and focuses on what is being predicted and how prediction success should be measured.  
> In this paper we discuss a relatively new technique, boosted regression trees (BRT), which draws on insights and techniques from both statistical and ML traditions. The BRT approach differs fundamentally from traditional regression methods that produce a single ‘best’ model, instead using the technique of boosting to combine large numbers of relatively simple tree models adaptively, to optimize predictive performance (e.g. Elith et al. 2006; Leathwick et al. 2006, 2008). The boosting approach used in BRT places its origins within ML (Schapire 2003), but subsequent developments in the statistical community reinterpret it as an advanced form of regression (Friedman, Hastie & Tibshirani 2000).

### Why we choose this model? 为什么要用BRT？
回归树有很多吸引人的*优势*，包括：
1. 不管是因变量还是自变量，都可以是连续变量或者分类变量，非常普适；
2. 对拟合的单调变换很稳定；
3. 可以用简单的形式拟合复杂的变量间相互作用；
4. 对缺失值和outlier不敏感。

同时回归树的两个*弱点*：
1. 预测形式过于简单；
2. 树模型太多就难以集中解释。

**都被Boosting的方法解决了。**

正因如此，BRT开始在生态学和传染病学领域被广泛应用。

### How to build a BRT model? 如何建模？
推荐一份Tutorial，基于R，非常简单直观，跟着走一遍就会了。
[Boosted Regression Trees for ecological modeling](http://w.download.idg.pl/CRAN/web/packages/dismo/vignettes/brt.pdf)

### What the results mean? 该如何解读结果？
结果的解读是BRT的重头戏，可以说的非常多。写文章的时候，先要把结果的意义都理解了，才能结合自己的专业知识给出建议和进行更深的讨论。基于以上的tutorial，他们有一篇发表了的[paper：A working guide to boosted regression trees](http://soilslab.cfr.washington.edu/Publications/Elith-etal-2008.pdf)结合着来看效果超好。

同时给大家介绍一些~~人生~~经验：
- 在建模之前不要太着急，要~~闷声发大财~~先对变量进行处理，如果因变量明显偏态，而且不易转换分布，可以考虑转为二分类变量。 
1. 为了实验的完整性，应该对tree complexity, learning rate等参数作sensitivity test；
2. Relative importance可以导出，可以讨论；
3. interaction effects 可以导出，可以讨论；
4. Partial dependency plots 非常值得讨论，它们代表的是relationships between predictors and response variable；
5. 如果predictors很多，有function可以simplify model。

### End 尾言
到这里，BRT的应用层面，有以上的应该差不多了。Plos One上面有个海洋生态学的研究，做得非常完整全面，重点部分也是用BRT的，也可以参考一下。[Environmental factors affecting large-bodied coral reef fish assemblages in the Mariana Archipelago](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0031374)

今天就到这里。
~~只是一些微小的工作，谢谢大家~~
  

