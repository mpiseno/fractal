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

Now consider a trajectory $\tau = (s_{1}, a_{1}, s_{2}, a_{2}, ..., s_{T})$ which is a sequence of state-action pairs until the terminal state. We are trying to learn $\theta$ that maximizes the reward of some trajectory. So in the spirit of gradient descent, we are going to take actions within our environment to sample a trajectory and then use the rewards gained from that trajectory to adjust our parameters. We can write our loss function as

$$J(\theta) = \mathbb{E}_{\tau \sim \pi_{\theta}(\tau)}[R(\tau)]$$

where $R(\tau)$ is the cumulative reward gained by our trajectory. Our objective is to take the gradient of this function with respect to $\theta$ so that we can use the gradient descent update rule to adjust our parameters, but the reward function is not known and may not even be differentiable, but with a few clever tricks we can estimate the gradient. Recall that for any continuous function $f(x)$, $\mathbb{E}[f(x)] = \int_{-\infty}^{\infty}p(x)f(x)dx$ where $p(x)$ is the probability of event $x$ occurring. So we have

$$\begin{align*}
J(\theta) &= \mathbb{E}_{\tau \sim \pi_{\theta}(\tau)}[R(\tau)] \\
&= \int p(\tau)R(\tau)d\tau \\
&= \int \pi_{\theta}(\tau)R(\tau)d\tau
\end{align*}$$

and

$$\begin{align*}
\nabla_{\theta}J(\theta) &= \nabla_{\theta} \int \pi_{\theta}(\tau)R(\tau)d\tau \\
&= \int \nabla_{\theta}\pi_{\theta}(\tau)R(\tau)d\tau \\
&= \int \pi_{\theta}(\tau)\nabla_{\theta}\log(\pi_{\theta}(\tau))R(\tau)d\tau \\
&= \mathbb{E}_{\tau \sim \pi_{\theta}(\tau)}[\nabla_{\theta}\log(\pi_{\theta}(\tau))R(\tau)]
\end{align*}$$

Where the third line follows from the fact that $\nabla_{x}f(x) = f(x)\nabla_{x}\log(f(x))$. The fact that we have turned the gradient of our cost function $J$ into an expectation is good because that means we can estimate it by sampling data. The last piece of the puzzle is to figure out how to calculate $\nabla_{\theta}\log(\pi_{\theta}(\tau))$.
