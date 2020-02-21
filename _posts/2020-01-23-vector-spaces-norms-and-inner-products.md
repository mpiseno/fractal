---
layout: post
title:  "Vector Spaces, Norms, and Inner Products"
date:   2020-01-23 00:06:43 -0800
categories: ["mfml"]
---

$\newcommand{\norm}[1]{\left\lVert#1\right\rVert}$

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

2. The set of all polynomials of degree $N$

    Note that for polynomials $p(x) = \alpha_{N}x^{N} + ... + \alpha_{1}x + \alpha_{0}$ and $t(x) = \beta_{N}x^{N} + ... + \beta_{1}x + \beta_{0}$, $ap(x) + bt(x)$ is still a polynomial of degree $N$ for any choice of $a$ and $b$, therefore the space of all degree $N$ polynomials is a linear vector space.

Thinking of functions as elements of a vector space might seem strange, but we will soon see that functions can be represented as discrete sets of numbers (i.e. vectors) and manipulated the same way that we normally think about manipulating vectors in $\mathbb{R}^{N}$.

#### Linear Subspaces

Now that we have the notion of a vector space, we can introduce the idea of a linear subspace, which is a mathematical tool that will soon become useful. A linear subspace is a subset $\mathbf{T}$ of a vector space $\mathbf{S}$ that contains the zero vector (i.e. $\mathbf{0} \in \mathbf{T}$) and is closed under vector addition and scalar multiplication.

$$\mathbf{x}, \mathbf{y} \in \mathbf{T} \implies a\mathbf{x} + b\mathbf{y} \in T \quad \forall a, b \in \mathbb{R}$$

<div class="container">
  <div class="row">
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <figure class="figure">
        <img src="{{site.baseurl}}/assets/Vector_Spaces/subspace_counterexample.png"/>
        <figcaption class="figure-caption text-center">T is not a linear subspace</figcaption>
      </figure>   
    </div>
    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <figure class="figure">
        <img src="{{site.baseurl}}/assets/Vector_Spaces/subspace_example.png"/>
        <figcaption class="figure-caption text-center">T is a linear subspace</figcaption>
      </figure>   
    </div>
  </div>
</div>

In the figure above we see on the left a counter example of a linear subspace. It is a counter example because it does not contain the zero vector and also because it is easy to see we could take a linear combination of two vectors in $\mathbf{T}$ to get a vector outside $\mathbf{T}$, so both conditions are violated. This is not the case for the subspace on the right, and it is in fact a linear subspace of $\mathbf{S} = \mathbb{R}^{2}$.

### Norms

A Vector space is a set of elements that obey certain properties. By introducing a norm to a particular vector space, we are giving it a sense of distance. A norm $\norm{\cdot}$ is a mapping from a vector space $\mathbf{S}$ to $\mathbb{R}$ such that for all $\mathbf{x, y} \in \mathbf{S}$,

1. $\norm{\mathbf{x}} \geq 0$ and $\norm{\mathbf{x}} = 0 \iff \mathbf{x} = \mathbf{0}$
2. $\norm{\mathbf{x} + \mathbf{y}} \leq \norm{\mathbf{x}} + \norm{\mathbf{y}}$ (triangle inequality)
3. $\norm{a\mathbf{x}} = \|a\|\norm{\mathbf{x}}$ (homogeneity)

This definition should feel familiar. The norm of a vector $\norm{\mathbf{x}}$ is its distance from the origin and the norm of the difference of two vectors $\norm{\mathbf{x - y}}$ is the distance between the two vectors. Here are some examples of norms that we will be using later on.

1. The standard euclidean norm (aka the $\ell_{2}$ norm): $\mathbf{S} = \mathbb{R}^{N}$

    $$\norm{\mathbf{x}}_{2} = \sqrt{\sum_{n=1}^{N}|x_{n}|^{2}}$$

2. $\mathbf{S} = $ the set of continuous functions on $\mathbb{R}$ ($\mathbf{x}$ is a function)

    $$\norm{\mathbf{x}}_{2} = \sqrt{\int_{-\infty}^{\infty}|x(t)|^{2}dt}$$

### Inner Products

By now we have introduced vector spaces and normed vector spaces, the latter being a subset of the former. Now we will introduce the inner product. The inner product $\langle\cdot, \cdot\rangle$ is a function that takes two vectors in a vector space and produces a real number (or complex number, but we will ignore this for now).

$$\langle\cdot,\cdot\rangle: \mathbf{S}\times\mathbf{S}\rightarrow \mathbb{R}$$

A valid inner product obeys three rules for $\mathbf{x, y, z}\in\mathbf{S}$:

1. $\langle\mathbf{x},\mathbf{y}\rangle = \langle\mathbf{y},\mathbf{x}\rangle$ (symmetry)

2. For $a, b \in \mathbb{R}$

    $$\langle a\mathbf{x} + b\mathbf{y}, \mathbf{z}\rangle = a\langle\mathbf{x}, \mathbf{z}\rangle + b\langle\mathbf{y}, \mathbf{z}\rangle$$ (linearity)

3. $\langle\mathbf{x}, \mathbf{x}\rangle \geq 0$ and $\langle\mathbf{x}, \mathbf{x}\rangle = 0 \iff \mathbf{x} = \mathbf{0}$

Two important examples of inner products are

1. The standard inner product (aka the dot product): $\mathbf{S} = \mathbb{R}^{N}$

    $$\langle\mathbf{x},\mathbf{y}\rangle = \sum_{n=1}^{N}x_{n}y_{n} = \mathbf{y}^{T}\mathbf{x}$$

2. The standard inner product for continuous functions on $\mathbb{R}^{N}$. If $\mathbf{x, y}$ are two such functions

    $$\langle\mathbf{x}, \mathbf{y}\rangle = \int_{-\infty}^{\infty}x(t)y(t)dt$$

The last concept I want to introduce is the idea of an induced norm. It is a fact that every valid inner product induces a valid norm (but not the other way around). This induces norm has very useful properties that not all other norms have. For some inner product $\langle\cdot,\cdot\rangle_{\mathbf{S}}$ on a vector space $\mathbf{S}$, the induced norm is defined as

$$\norm{\mathbf{x}}_{\mathbf{S}} = \sqrt{\langle\mathbf{x},\mathbf{x}\rangle_{\mathbf{S}}}$$

The standard inner product induces the standard euclidean norm. Two important properties of induced norms (not all norms!) are

1. The Cauchy-Schwartz Inequality:

    $$|\langle\mathbf{x},\mathbf{y}\rangle| \leq \norm{\mathbf{x}}\norm{\mathbf{y}}$$

2. Pythagorean Theorem:

    If $\langle\mathbf{x},\mathbf{y}\rangle = 0$ then $\mathbf{x}$ and $\mathbf{y}$ are orthogonal and $\norm{\mathbf{x} + \mathbf{y}} = \norm{\mathbf{x}} + \norm{\mathbf{y}}$


A Hilbert space is an inner product space that is also complete, which means that for every infinite sequence of elements $\mathbf{x_{1}}, \mathbf{x_{2}}, ... $ that gets closer and closer to one another, these elements also approach some precise element in the space. In more rigorous terms, it means that every Cauchy sequence is convergent, but the spaces we discuss in these guides will have this completeness property unless otherwise stated, so I will use Hilbert space and inner product space more or less interchangeably. Just keep the completeness requirement in the back of your mind.

All the ideas presented in these notes are important foundational mathematical concepts that we will make use of in later notes. You should become very familiar with them and know how to determine if an inner product or a norm is valid or not. Now that we have some mathematical tools, next time we will discuss a foundational problem is machine learning - linear approximation.
