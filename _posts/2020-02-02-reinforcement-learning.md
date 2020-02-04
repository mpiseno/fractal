---
layout: post
title:  "Reinforcement Learning Introduction"
date:   2020-02-02 00:06:43 -0800
categories: ["dl"]
---

### Reinforcement Learning

Reinforcement learning (RL) is difference from supervised and unsupervised learning. In supervised learning, we have truth data (labels) for our problem that we use to check the output of our model against, correcting for mistakes accordingly. In unsupervised learning, we are learning some structure to the data. In RL we don't have data necessarily, but instead we have an environment and a set of rules. There exists an agent that lives in this environment and its objective is to take actions that will eventually lead to reward. Whereas supervised learning tries to match data to its corresponding label, in RL we try to maximize reward. In other words, we are learning how to make the agent make a good sequence of actions.


<center>
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/RL_Intro/rl-schema.png"/>  
  </div>
</center>

### Framing an RL Problem

We well frame an RL problem as a Markov Decision Process (MDP), which is a fancy-sounding way of formulating decision making under uncertainty. We will define the following ideas that will guide us in formulating the problem:

* $\mathbf{S}$: The set of possible states
* $\mathbf{A}$: The set of possible actions the agent can take
* $R(s, a, s')$: A probability distribution of the reward given for being in state $s$, taking action $a$ and ending up in a new state $s'$
* $\mathbb{T}(s, a, s')$: A probability distribution of state transitions
* $\gamma \in [0, 1)$: A scalar discount factor (will come in handy later)

Some literature will also use $\mathbf{O}$ which is the set of possible observations given to the agent by the environment. This is sometimes the same as $\mathbf{S}$ and sometimes not. In a fully observable MDP, the agent has has all information about the state of the environment, so when the agent receives an observation $o_{i} \in \mathbf{O}$, it contains the same information as the state of the environment $s_{i} \in \mathbf{S}$. An example of this is chess - each player (agent) knows exactly what the state of the game is at any time. In a partially observable MDP this is not the case. The agent does not have access to the full state of the environment, so when it received an observation, it does not contain the same information as the state of the environment, hence these are two difference concepts. An example of this is poker - each player does not know the cards of the other players and therefore does not have access to the full state of the game.

The last concept is a policy, which is a function $\pi(s) : \mathbf{S} \Rightarrow \mathbf{A}$ that tells us which action to take given a state. The whole idea of RL is to learn a good policy; one that will tell us good actions to take in each state of the environment. A policy can interpreted deterministically $\pi(s)$ (The action taken when we are in state $s$), or stochastically $\pi(a\|s)$ (the probability of taking action $a$ in state $s$).

Most of the time in RL, we do not have access to the true distributions $R(s, a, s')$ and $\mathbb{T}(s, a, s')$. If we had these distributions, we could easily calculate the optimal policy, however without this information we have to estimate them by trying out actions in our environment and seeing if we get reward or not.

### Grid World

For now, we will assume we have access to the distributions $R(s, a, s')$ and $\mathbb{T}(s, a, s')$ so that we can really drive home the point that if we have the true distributions at hand, we can calculate the optimal policy. Image we have the following problem.

* The agent lives in a grid, where each square is a state. This is the state space.
* The agent can move North, South, East, or West (N, S, E, W). This is the action space.
* 80% of the time, the action the agent takes does as it is intended. 10% of the time the agent slips and moves to one side, and 10% of the time the agent slips to the other side. For example if the agent chooses to move north, there is a 80% chance it will do so, a 10% chance it will move west, and a 10% chance it will move east. This is the transition probability distribution.
* There is a destination state that deterministically gives the agent a reward of +1 for reaching it and a terminal state that deterministically gives the agent a reward of -1 for reaching it.


<center>
  <div class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/RL_Intro/gridworld-example.png"/>  
  </div>
</center>

### Finding Optimal Policies

So now that we have a concrete example of a problem, we can discuss what it means to find an optimal policy for it. Some questions that come when determining what a "good" policy is are "does it maximize the reward right now?" and "does is maximize the future reward?". Typically, we maximize the discounted future reward; the idea being that we want policies that take future state into consideration, but we also don't want the policy to focus so much on optimizing for future rewards that it doesn't take actions that would put the agent in a good state now. Therefore we define the optimal policy $\pi^{\ast}$ in the following way.

$$\pi^{\ast} = \arg \max_{\pi} \mathbb{E}\bigg[\sum_{t \geq 0} \gamma^{t}r_{t}|\pi\bigg]$$

Here, time is indexed by $t$. This means we want to maximize the expectation of the discounted reward given some policy. Notice since $\gamma$ is between 0 and 1, we will optimize for states closer in time more than ones further.

#### Value Function and Q-Function

We have a notion of what a "good" policy is, but how do we actually find it? This is where the Value function and Q function come in. The value function is a prediction of future reward and basically answers the question "how good is the current state $s$ that I'm in?". We denote $V^{\pi}(s)$ as the expected cumulative reward of being in state $s$ and then following policy $\pi$ thereafter.

$$V^{\pi}(s) = \mathbb{E}\bigg[\sum_{t \geq 0} \gamma^{t}r_{t}|s_{0}=s, \pi\bigg]$$

We also have the notion of an optimal value function $V^{\ast}(s)$, which is the expected cumulative reward of being in state $s$ and then following the optimal policy $\pi^{\ast}$ thereafter. The Q function represents a similar idea - $Q^{\pi}(s, a)$ is the expected cumulative reward for taking action $a$ in state $s$ and then following policy $\pi$ thereafter. Similarly $Q^{\ast}(s, a)$ is the expected cumulative reward of taking action $a$ in state $s$ and following the optimal policy thereafter.

$$Q^{\pi}(s, a) = \mathbb{E}\bigg[\sum_{t \geq 0} \gamma^{t}r_{t}|s_{0}=s, a_{0}=a, \pi\bigg]$$

Remember, the value function only deals with states, and the Q function deals with state-action pairs! Now we can go about defining the optimal value and policy from the Q function values. It is clear that the optimal value and policy for a state can be defined in terms of the Q function as follows.

$$V^{\ast}(s) = \max_{a}Q^{\ast}(s, a)$$

$$\pi^{\ast}(s) = \arg \max_{a}Q^{\ast}(s, a)$$

These optimal values can be calculated recursively using what are called the Bellman equations, defined below. Notice how the calculation of these values requires we have access to the true distributions $\mathbb{T}(s', a, s)$ (denoted with $p(\cdot)$ below) and $R(s', a, s)$ (denoted with $r(\cdot)$ below).

$$V^{\ast}(s) = \max_{a}\sum_{s'}p(s'|s, a)[r(s, a) + \gamma V^{\ast}(s')]$$

$$Q^{\ast}(s, a) = \sum_{s'}p(s'|s, a)[r(s, a) + \gamma V^{\ast}(s')]$$

The summation over all possible next-states $s'$ of $p(s'\|s, a)$ comes from the definition of expectation in probability $\mathbb{E}[f(\cdot)] = \sum_{x}p(x) \cdot f(x)$. We are summing over all subsequent states the probability of being in that state, given the current state and action, then multiplying by the reward we get for being in that next state. It should be clear that the expected reward of being in state $s$, taking action $a$ and ending up in state $s'$ is exactly $r(s, a) + \gamma V^{\ast}(s')$.

To reiterate, if we know the distributions $\mathbb{T}$ and $R$, we have a recursive way of calculating the optimal Q value of any state-action pair, and hence we can extract the optimal policy. Now we will go over two algorithms for doing so.

### Value Iteration

The idea of value iteration pretty much exactly follows the logic we described above. The algorithm is as follows.

<center>
  <div class="col-lg-10 col-md-10 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/RL_Intro/VI-algorithm.png"/>  
  </div>
</center>

Each iteration of Value Iteration costs $O(\|\mathbf{S}\|^{2}\|\mathbf{A}\|)$ time and is very expensive for large state spaces. Recall our grid world game with values for each state initialized to 0.

<center>
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <img src="{{site.baseurl}}/assets/RL_Intro/gridworld-VI-step1.png"/>  
  </div>
</center>

Let's do an example calculation of one iteration of Value Iteration on the state (3, 3) (where the agent is pictured).

$$
\begin{align*}
V^{2}((3, 3)) &= \max_{a}\sum_{s'}p(s'|(3, 3), a)[r(s, (3, 3)) + \gamma V^{1}(s')] \\
&= \sum_{s'\in \{(4, 3), (3, 2)\}} p(s'|(3, 3), \text{right})[r((3, 3), \text{right}) + \gamma V^{1}(s')] \\
&= (0.8 * (0 + \gamma * 1)) + (0.1 (0 + \gamma * 0)) + (0.1 (0 + \gamma * 0)) \\
&= 0.8\gamma
\end{align*}$$

Note that the above calculation did not include other actions for brevity since we already knew the max operation would give us right as the optimal action. Now state (3, 3) has value $0.8\gamma$ and we can keep recursing to calculate the values of all the other states. After doing so, this would be 1 iteration of Value Iteration. We would repeat this process until the values converge.

### Policy Iteration
