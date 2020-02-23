---
layout: post
title:  "Linear Approximation"
date:   2020-02-21 00:06:43 -0800
categories: ["mfml"]
---

$\newcommand{\norm}[1]{\left\lVert#1\right\rVert}$

### Linear Approximation

Linear approximation is a fundamental problem in machine learning, and one that has a surprising amount of mathematical structure built around it for such a seemingly simple problem. Consider the following problem: We have a Hilbert space $\mathbf{S}$ and a subspace $\mathbf{T} \subseteq \mathbf{S}$. We also have an element $\mathbf{x} \in \mathbf{S}$. What is the closest element $\mathbf{\hat{x}} \in \mathbf{T}$ to $\mathbf{x}$?

<center>
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/Linear_Approx/linear-approx-problem.png"/>  
  </div>
</center>

This Hilbert space $\mathbf{S}$ has an inner product $\langle\cdot, \cdot\rangle$ and induced norm $\norm{\cdot}$. So we can frame the problem as finding the point $\mathbf{\hat{x}} \in \mathbf{T}$ such that $\norm{\mathbf{\hat{x} - x}}$ is minimized.

$$\begin{equation} \tag{1}
\text{minimize}_{\mathbf{y\in T}} \norm{\mathbf{y - x}}
\end{equation}$$

We can find a unique minimizer by exploiting orthogonality. In fact, $\mathbf{\hat{x} \in T}$ is the closest point to $\mathbf{x \in S}$ if $\mathbf{\hat{x} - x}$ is orthogonal to all other points $\mathbf{y \in T}$. This means that $\langle \mathbf{\hat{x} - x}, y\rangle = 0$ for all $\mathbf{y \in T}$

Lets show that if $\langle\mathbf{\hat{x} - x}, \mathbf{y}\rangle = 0$ for all $\mathbf{y \neq \hat{x} \in T}$ then $\mathbf{\hat{x}}$ is minimizer of $(1)$.

$$\begin{align*}
\norm{\mathbf{x - y}}^{2} &= \norm{(\mathbf{x - \hat{x}}) - (y - \mathbf{\hat{x}})}^{2} \\
&= \norm{\mathbf{x - \hat{x}}}^{2} + \norm{\mathbf{y} - \mathbf{\hat{x}}}^{2}
\end{align*}$$

The last equality follows from the Pythagorean theorem. This is valid because we required that $\\mathbf{x - \hat{x}}$ was orthogonal to all points in $\mathbf{T}$, and $\mathbf{y} - \mathbf{\hat{x}}$ is certainly in $\mathbf{T}$!

<center>
  <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/Linear_Approx/closest-point.png"/>  
  </div>
</center>

Therefore, if $\norm{\mathbf{y} - \mathbf{\hat{x}}}^{2} \neq 0$ (i.e. $\mathbf{y} \neq \mathbf{\hat{x}}$), then

$$\norm{\mathbf{x} - \mathbf{y}}^{2} > \norm{\mathbf{x - \hat{x}}}^{2}$$

where equality is achievd only when $\mathbf{y} = \mathbf{\hat{x}}$. This implies that $\mathbf{\hat{x}}$ is a unique minimizer of $(1)$. This is a pretty intuitive result: If $\mathbf{x - y}$ is not orthogonal to $\mathbf{T}$, then there is some other point $\mathbf{\hat{x}}$ that comes closer to $\mathbf{x}$ while still remaining inside $\mathbf{T}$. This can be seen visually in the image above.

#### Computing the closest point

So we know that $\mathbf{\hat{x}}$ is a unique minimizer of $(1)$ if $\langle\mathbf{x - \hat{x}}, y\rangle = 0$ for all $\mathbf{y} \neq \mathbf{\hat{x}}$ in $\mathbf{T}$, but how do we actually compute $\mathbf{\hat{x}}$? If $\mathbf{T}$ is an $N$-dimensional subspace, that means we can represent any point in the space by a linear combination of $N$ basis vectors - call them $\mathbf{v_{1}}, \mathbf{v_{2}}, ..., \mathbf{v_{N}}$.

$$\mathbf{\hat{x}} = \alpha_{1}\mathbf{v_{1}} + \alpha_{2}\mathbf{v_{2}} + ... + \alpha_{N}\mathbf{v_{N}} = \sum_{n=1}^{N}\alpha_{n}\mathbf{v}_{N}$$

for some constants $\\{ \alpha \\}_{1}^{N}$. Orthogonality also tells us

$$\langle\mathbf{x - \hat{x}}, \mathbf{v_{k}}\rangle = 0$$

If we take the inner product of $\mathbf{x - \hat{x}}$ with one of the basis vectors we generate a linear equation.

$$\begin{align*}
\langle\mathbf{x - \hat{x}}, \mathbf{v_{k}}\rangle &= \big\langle\mathbf{x} - \sum_{n=1}^{N}\alpha_{n}\mathbf{v_{n}}, \mathbf{v_{k}}\big\rangle \\
&= \langle\mathbf{x}, \mathbf{v_{k}}\rangle - \alpha_{1}\langle\mathbf{v_{1}, \mathbf{v_{k}}}\rangle - ... - \alpha_{N}\langle\mathbf{v_{1}, \mathbf{v_{k}}}\rangle \\
\Rightarrow \langle\mathbf{x}, \mathbf{v_{k}}\rangle &= \alpha_{1}\langle\mathbf{v_{1}, \mathbf{v_{k}}}\rangle + ... + \alpha_{N}\langle\mathbf{v_{1}, \mathbf{v_{k}}}\rangle
\end{align*}$$

In fact, we can generate $N$ different linear equations by taking the inner product with each of the basis vector separately. That means we can solve this linear system of equations for $\mathbf{\alpha}$, the vector of coefficients!

$$\begin{align*}
\begin{bmatrix}\langle\mathbf{x}, \mathbf{v_{1}}\rangle \\ \vdots \\ \langle\mathbf{x}, \mathbf{v_{N}}\rangle\end{bmatrix} &=
\begin{bmatrix}
\langle\mathbf{v_{1}}, \mathbf{v_{1}}\rangle &  ... & \langle\mathbf{v_{N}}, \mathbf{v_{1}}\rangle \\
\vdots & \ddots & \vdots \\
\langle\mathbf{v_{1}}, \mathbf{v_{N}}\rangle & ... & \langle\mathbf{v_{N}}, \mathbf{v_{N}}\rangle
\end{bmatrix}\begin{bmatrix}\alpha_{1} \\ \vdots \\ \alpha_{N}\end{bmatrix} \\
\\
\mathbf{b} &= \mathbf{G\alpha} \\
\Rightarrow \mathbf{\alpha} &= \mathbf{G^{-1}b}
\end{align*}$$

Where $\mathbf{G}$ is the matrix if inner products and is called the Gram Matrix or Grammian of the basis $\\{\mathbf{v}\\}_{n=1}^{N}$. After we solve for our coeeficientls, we can easily reconstruct the closest point in $\mathbf{T}$ to $\mathbf{x}$ by

$$\mathbf{\hat{x}} = \alpha_{1}\mathbf{v_{1}} + ... + \alpha_{N}\mathbf{v_{N}}$$

Take a second to appreciate what we did. We took a minimization problem, converted it to a finite dimensional linear algebra problem by exploiting our basis to ask the question "what basis coefficients will create a $\mathbf{\hat{x}}$ that minimizes the objective?". This idea is central to many more topics we will cover.

$\mathbf{G}$ is invertible because the basis vectors are linearly independent. Also, since the inner product is a symmetric function, the Gram Matrix is also symmetric. Because the Gram matrix is square and invertible, $\mathbf{b} = \mathbf{G\alpha}$ always has a solution. Further, if we have an orthogonal basis, then the Gram Matrix is exactly the Identity transformation, and the coefficients can be calculated by simply taking inner products of $\mathbf{x}$ with each basis vector.


##### Example

We will close with an example to drive this idea home. Let our Hilbert space $\mathbf{S} = \mathbb{R}^{3}$ with the standard inner product and

$$\mathbf{T} = \text{Span}\Bigg(\begin{bmatrix}1 \\ 0 \\ 1\end{bmatrix}, \begin{bmatrix}-1 \\ 0 \\ 1\end{bmatrix}\Bigg), \mathbf{x} = \begin{bmatrix}2 \\ 1 \\ 0\end{bmatrix}$$

The vectors we defined $\mathbf{T}$ with form a basis for the subspace. What is the closest point in $\mathbf{T}$ to $\mathbf{x}$? We can write $\mathbf{\hat{x}}$ as

$$\mathbf{\hat{x}} = \alpha_{1}\mathbf{v_{1}} + \alpha_{2}\mathbf{v_{2}}$$

and our Gram Matrix and $\mathbf{b}$ are

$$\mathbf{G} = \begin{bmatrix}
2 & 0 \\
0 & 2
\end{bmatrix}, \mathbf{b} = \begin{bmatrix}2 \\ -2\end{bmatrix}$$

The inverse Gram Matrix is

$$\begin{bmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{2}
\end{bmatrix}$$

Finally, $\mathbf{\alpha} = \begin{bmatrix}1 & -1\end{bmatrix}^{T}$. We reconstruct our solution using the coefficients: $\mathbf{\hat{x}} = \mathbf{v_{1}} - \mathbf{v_{2}} = \begin{bmatrix}2 & 0 & 0\end{bmatrix}^{T}$
