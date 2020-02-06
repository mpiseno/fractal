---
layout: post
title:  "Deep Q-Learning"
date:   2020-02-05 00:06:43 -0800
categories: ["dl"]
---

### Learning-Based Methods

Policy and Value Iteration gave us a solid way to find the optimal policy when we have perfect information about the environment (i.e. we know the distributions of state transitions and rewards), but when this information is not know, we have to get clever with how we determine good policies. One way is to learn by trial and error - taking actions in the environment and observing what states we transition to under different actions and what rewards we obtain for doing so. Doing this gives us data in the form $(s, a, r, s')$. If we take action $a$ in state $s$ we receive reward $r$ and transition to state $s'$. From this data we can try to approximate the unknown distributions.

Another issue we face is large state spaces. Policy and Value iteration worked fine for Gridworld (small state space), but when the total number of states becomes large, these algorithms become intractable - they contain a $\|\mathbf{S}\|^{3}$ and a $\|\mathbf{S}\|^{2}$ term respectively in their time complexities! Our solution to this issue is to learn a lower-dimensional representation of the state using neural networks. This is known as deep reinforcement learning, and the type we will be exploring in this guide is called deep Q-Learning.

### Deep Q-Learning

Essentially what we are trying to do is approximate $Q^{\ast}(s, a)$ using a neural network. If we can get a good approximation of $Q^{\ast}$, we can extract a good policy. This neural network will be parameterized by a generic term $\theta$, will take as input the state $s$ and output value for each possible action, which we can perform a max operation over to get the best action to take.
