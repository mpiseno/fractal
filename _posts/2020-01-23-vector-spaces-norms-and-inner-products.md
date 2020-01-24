---
layout: post
title:  "Vector Spaces, Norms, and Inner Products"
date:   2020-01-23 00:06:43 -0800
categories: ["mfml"]
---

### Vector Spaces

We will begin our study of the mathematical foundations of machine learning by considering the idea of a vector space. A vector space $\mathbf{S}$ is a set of elements called vectors that obey the following
* For $\mathbf{x, y, z} \in \mathbf{S}$:
  * $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$ (commutative)
  * $\mathbf{x} + (\mathbf{y} + \mathbf{z}) = (\mathbf{x} + \mathbf{y}) + \mathbf{z}$ (associative)
  * $\mathbf{x} + 0 = \mathbf{x}$

* Scalar multiplication is distributive and associative
* $\mathbf{S}$ is closed under scalar multiplication and vector addition. i.e.
$\mathbf{x}, \mathbf{y} \in \mathbf{S} \implies a\mathbf{x} + b\mathbf{y} \in S \quad \forall a, b \in \mathbb{R}$

The last bullet is arguably the most important and describes the more descriptive "linear vector space".

A couple examples of linear vectors spaces are:
1. $\mathbb{R}^{N}$

    $$\mathbf{x} = \begin{bmatrix}x_{1} \\ \vdots \\ x_{N}\end{bmatrix}$$

    Note that the addition of any two vectors in $\mathbb{R}^{N}$ is also a vector in $\mathbb{R}^{N}$.

2. Polynomials of degree $N$

    Note that for polynomials $p(x) = \alpha_{N}x^{N} + ... + \alpha_{1}x + \alpha_{0}$ and $t(x) = \beta_{N}x^{N} + ... + \beta_{1}x + \beta_{0}$, $ap(x) + bt(x)$ is still a polynomial of degree $N$ for any choice of $a$ and $b$, therefore the space of all degree $N$ polynomials is a linear vector space.

Thinking of functions as elements of a vector space might seem strange, but we will soon see that functions can be represented as discrete sets of numbers (i.e. vectors) and manipulated the same way that we normally think about manipulating vectors in $\mathbb{R}^{N}$.

#### Linear Subspaces
