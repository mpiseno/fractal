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

Where the third line follows from the fact that $\nabla_{x}f(x) = f(x)\nabla_{x}\log(f(x))$. The fact that we have turned the gradient of our cost function $J$ into an expectation is good because that means we can estimate it by sampling data. The last piece of the puzzle is to figure out how to calculate $\nabla_{\theta}\log(\pi_{\theta}(\tau))$. Note that we can rewrite $\pi_{\theta}(\tau)$ as

$$\begin{align*}
\pi_{\theta}(\tau) = \pi_{\theta}(a_{1}, s_{1}, a_{2}, s_{2}, ..., s_{T}) &= p(s_{1}) \prod_{t=1}^{T} p(a_{t}|s_{t})p(s_{t+1}|a_{t}, s_{t}) \\
&= p(s_{1}) \prod_{t=1}^{T} \pi_{\theta}(a_{t}|s_{t})p(s_{t+1}|a_{t}, s_{t})
\end{align*}$$

Convince yourself that the above relation is true. $\pi_{\theta}(\tau)$ is the probability of trajectory $\tau$ happening. It is the probability of starting in $s_{1}$, then taking action $a_{1}$ given $s_{1}$, then transitioning to state $s_{2}$ given $a_{1}$ in $s_{1}$, and so on. This joint probability can be factored out. The last step is to realize $p(a_{t}\|s_{t})$ is the definition of $\pi_{\theta}(a_{t}\|s_{t})$. Now

$$\begin{align*}
\nabla_{\theta} \log(\pi_{\theta}(\tau)) &= \nabla_{\theta}\log\bigg[p(s_{1}) \prod_{t=1}^{T} \pi_{\theta}(a_{t}|s_{t})p(s_{t+1}|a_{t}, s_{t})\bigg] \\
&= \nabla_{\theta}\bigg[\log(p(s_{1})) + \sum_{t=1}^{T}\log(\pi_{\theta}(a_{t}|s_{t})) + \sum_{t=1}^{T}\log(p(s_{t+1}|a_{t}, s_{t}))\bigg] \\
&= 0 + \nabla_{\theta}\sum_{t=1}^{T}\log(\pi_{\theta}(a_{t}|s_{t})) + 0
\end{align*}$$

This simplication is enough for us to completed our estimate of the policy gradient $\nabla_{\theta}J(\theta)$.

$$
\nabla_{\theta}J(\theta) \approx \frac{1}{N}\sum_{n=1}^{N}\Bigg[\bigg(\sum_{t=1}^{T} \nabla_{\theta}\log(\pi_{\theta}(a_{n,t}|s_{n,t}))\bigg)\bigg(\sum_{t=1}^{T}r(s_{n,t},a_{n,t})\bigg)\Bigg]
$$

Where $N$ is just the number of episodes (analogous to epochs) we do. Having a set of $N$ trajectories and then averaging the policy gradient estimate over each of them makes this estimate more robust. Now that we can estimate the policy gradient, we simply would update our parameters in the familiar way

$$\theta \leftarrow \theta - \alpha\nabla_{\theta}J(\theta)$$

One interpretation of this result is that we are trying to maximize the log likelihood of trajectories that give good rewards and minimize the log likelihood of those that don't. This is the idea behind the REINFORCE algorithm which is

1. sample $N$ trajectories by running the policy
2. estimate the policy gradient like above
3. update the parameters $\theta$
4. Repeat until converged

### Actor Critic

One issue with vanilla policy gradients is that its very hard to assign credit to state-action pairs that resulted in good reward because we only consider the total reward $\sum_{t=1}^{T}R(a_{t}, s_{t})$. The trajectories are noisy. But if we had the $Q$ function, we would know what state-action pairs were good. In other words, we would estimate the gradient of $J$ as

$$\nabla_{\theta}J(\theta) = \mathbb{E}[\nabla_{\theta}\log(\pi_{\theta}(\tau))Q_{\pi_{\theta}}(\tau)]$$

The idea of actor-critic is that we have an actor that samples trajectories using the policy, and a critic that critiques the policy using the $Q$ function. Since we don't have the optimal $Q$ functions, we can estimate it like we did in deep Q learning. So we could have a policy network that takes in a state and returns a probability distribution over the action space (i.e. $\pi_{\theta}(a\|s))$ and a $Q$ network that takes in a state-action pair and returns its Q value estimate. Let's say this network is parameterized by a generic variable $\beta$. Note that these don't have to be neural networks, but for the sake of this guide I'll just say "network". So we have networks $\pi_{\theta}$ and $Q_{\beta}$. The general actor-critic algorithm then goes like

1. Initialize $s, \theta, \beta$
2. Repeat until converged:
  * Sample action $a$ from $\pi_{\theta}(\cdot\|s)$
  * Receive reward $r$ and sample next state $s' \sim p(s'\|s, a)$
  * Use the critic to evaluate the actor and update the policy similar to like we did in policy gradients:
      $$\theta \leftarrow \theta - \alpha\nabla_{\theta}\log(\pi_{\theta}(a|s))Q_{\beta}(s, a)$$
  * Update the critic according to some loss metric: $\text{MSE Loss} = (Q_{t+1}(s, a) - (r + \max_{a'}Q_{t}(s', a')))^{2}$
  * Update $\beta$ using backprop or whatever update rule

Of course you can sample whole trajectories instead of one state-action pair at a time. Different types of actor-critic result from changing the "critic". In REINFORCE, the critic was simply the reward we got from the trajectory. In actor-critic, the critic is the Q function. Another popular choice is called advantage actor-critic, in which the critic is the advantage functions

$$A_{\pi_{\theta}}(s, a) = Q_{\pi_{\theta}}(s, a) - V_{\pi_{\theta}}(s)$$

Where V is the value function (recall value iteration). The advantage function A tells us how much better is taking action $a$ in state $s$ than the expected cumulative reward of being in state $s$.

This concludes our discussion of RL for the Deep Learning section. In the future I will make more RL-related guides that focus on more advanced topics and current research. Feel free to reach out with any questions or if you notice something you think is inaccurate and I'll do my best to respond!
