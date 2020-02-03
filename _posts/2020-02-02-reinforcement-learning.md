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

Here, time is indexed by $t$. This means we want to maximize the expected value of the discounted reward given some policy. Notice since $\gamma$ is between 0 and 1, we will optimize for states closer in time more than ones further.
