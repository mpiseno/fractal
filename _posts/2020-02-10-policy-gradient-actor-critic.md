---
layout: post
title:  "Policy Gradient and Actor Critic"
date:   2020-02-10 00:06:43 -0800
categories: ["dl"]
---

### Policy Gradient

What if we could learn the policy parameters directly? We can approach this problem by thinking of policies abstractly - Let's consider a class of policies defined by $\theta$ and refer to such a policy as $\pi_{\theta}(a\|s)$ which is a probability distribution over the action space conditioned on the state $s$. These parameters $\theta$ could be the parameters of a neural network or a simple polynomial or anything really.

Let's note define a metric $J$ which can be used to evaluate the quality of a policy $\pi_{\theta}$. What we really want to do is maximize the expected future reward, so naturally we can write

$$J(\pi_{\theta}) = \mathbb{E}\bigg[\sum_{t=1}^{T}R(s_{t}, a_{t})\bigg]$$

where $R(s_{t}, a_{t})$ is the reward given by taking action $a$ in state $s$ and time $t$. The optimal set of parameters for the policy can then be written as

$$\theta^{\ast} = \arg\max_{\theta}\mathbb{E}\bigg[\sum_{t=1}^{T}R(s_{t}, a_{t})\bigg]$$
