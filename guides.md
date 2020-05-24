---
layout: page
title: Guides
permalink: /guides/
---

### Computer Science Guides

<p align="justify">These guides are intended for students with little or no programming experience and are intended to provide the necessary information to get started with simple programming tasks and projects. We will be primarily programming in the Python programming language; specifically python3.</p>
---

#### Getting Started
<ul>
  <li>
    <a href="{{site.url}}/cs/2020/05/03/getting-started-with-python.html">Getting Started with Python</a>
  </li>
  <li>
    <a href="{{site.url}}/cs/2020/05/22/python-basics.html">Python Basics</a>
  </li>
</ul>

---
---

### Artificial Intelligence Guides

<p align="justify">These guides are for advanced students interested in learning theoretical concepts about artificial intellgence. Foundations of Machine Learning is intended to provide a solid understanding of the mathematics and ideas from which more advanced topics are built. This section is based off content from a first-year PhD course. Machine learning covers topics typically seen in an undergraduate or masters level machine learning course such as models and algorithms for supervised learning, clustering, and dimensionality reduction. Deep learning covers topics typically seen in a masters or first-year PhD course that form the building blocks of many advanced models used in current research.</p>
---

#### Supplementary Material

<ul>
  <li>
    <a href="{{site.url}}/supp/2020/01/15/what-is-ml.html">What is Machine Learning?</a>
  </li>
</ul>

<!-- <ul>
{% assign supp_posts = site.posts | where:"categories", "supp" %}
{% for page in supp_posts %}
  <li>
    <a href="{{site.url}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul> -->

#### Foundations of Machine Learning

<ul>
  <li>
    <a href="{{site.url}}/mfml/2020/01/23/vector-spaces-norms-and-inner-products.html">Vector Spaces, Norms, and Inner Products</a>
  </li>
  <li>
    <a href="{{site.url}}/mfml/2020/02/21/linear-approximation.html">Linear Approximation</a>
  </li>
</ul>

<!-- <ul>
{% assign mfml_posts = site.posts | where:"categories", "mfml" %}
{% for page in mfml_posts %}
  <li>
    <a href="{{site.url}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul> -->

#### Machine Learning

<ul>
  <li>
    <a href="{{site.url}}/ml/2020/04/12/neural-networks.html">Neural Networks</a>
  </li>
</ul>

<!-- <ul>
{% assign ml_posts = site.posts | where:"categories", "ml" %}
{% for page in ml_posts %}
  <li>
    <a href="{{site.url}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul> -->

#### Deep Learning

<ul>
  <li>
    <a href="{{site.url}}/dl/2020/02/29/cnns.html">Convolutional Neural Networks</a>
  </li>
  <li>
    <a href="{{site.url}}/dl/2020/02/02/reinforcement-learning.html">Reinforcement Learning Intro</a>
  </li>
  <li>
    <a href="{{site.url}}/dl/2020/02/05/deep-q-learning.html">Deep Q-Learning</a>
  </li>
  <li>
    <a href="{{site.url}}/dl/2020/02/10/policy-gradient-actor-critic.html">Policy Gradients and Actor Critic</a>
  </li>
</ul>

<!-- <ul>
{% assign dl_posts = site.posts | where:"categories", "dl" %}
{% for page in dl_posts %}
  <li>
    <a href="{{site.url}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul> -->

<!-- #### Advanced Topics

<ul>
  <li>
    <a href="{{site.url}}/adv/2020/04/12/a2c-ppo.html">A2C and PPO</a>
  </li>
</ul> -->

<!-- <ul>
{% assign adv_posts = site.posts | where:"categories", "adv" %}
{% for page in adv_posts %}
  <li>
    <a href="{{site.url}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul> -->
