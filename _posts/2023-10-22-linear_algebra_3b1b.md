---
title: "Course notes: Essence of linear algebra (3b1b)"
date: 2023-10-22
permalink: /posts/2022-10-22/2023-10-22-linear_algebra_3b1b
categories:
  - Course notes
tags:
  - Mathematics
toc: true
# last_modified_at: 2023-09-01
---

The Youtube playlist [Essence of linear algebra](https://www.youtube.com/playlist?list%253DPLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) is a famous short course for linear algebra. It was super helpful for my previous interview for admission of the master of data science programme in HKU (which I got a offer on 2019 but forfeited eventually). Now I wanted to revisit this course again to solidly my understand on these concepts, in preparation of future study on deep learning models. I will take notes of the course here.

## Vectors | Chapter 1

Imagine vector addition and scalar multiplication in a visual way (in a coordinate system).

## Linear combinations, span, and basis vectors | Chapter 2

- Linear combination: a vector that can be expressed as a linear combination of other vectors.
- Span: the set of all possible linear combinations of a set of vectors.
- Basis: a set of vectors that are *linearly independent* and span the vector space.

## Linear transformations and matrices | Chapter 3

- Linear transformation: a function that maps vectors to vectors and preserves the linear combination (lines remain lines, origin remains fixed).
- Linear transformation on a given vector can be represented by a matrix multiplication, e.g. a 2D linear transformation can be represented by a 2x2 matrix multiplication on the vector (x, y), the original basis vectors (1, 0) and (0, 1) are transformed to the new basis vectors (a, c) and (b, d) :
$$
\begin{bmatrix}
    a & b \\
    c & d \\
\end{bmatrix}
\begin{bmatrix}
    x \\
    y \\
\end{bmatrix}
$$
- Every time you see a matrix, you can interpret it as a certain transformation of the space.

## Matrix multiplication as composition | Chapter 4

- Matrix multiplication is a composition of linear transformations, e.g., a 2x2 matrix multiplication can be interpreted as a composition of two linear transformations (e.g., rotation and shear), each of which is a 2D linear transformation represented by a 2x2 matrix multiplication.
- Matrix multiplication does not have the commutative property. This means that for matrices A and B: $A * B ≠ B * A$
- Matrix multiplication does have associativity, i.e., for matrices A, B, and C: $(A * B) * C = A * (B * C)$

