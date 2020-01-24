---
layout: page
title: Guides
permalink: /guides/
---

<p>These guides build upon one another. Mathematical foundations is intended to provide a solid understanding of the mathematics from which more advanced topics are built. This section is based off content from a first-year PhD course. Traditional machine learning covers topics typically seen in an undergraduate or masters level machine learning course such as models and algorithms for supervised learning, clustering, and introductory reinforcement learning. Deep learning covers topics typically seen in a masters or first-year PhD course that form the building blocks of many advanced models used in current research.</p>
---
### Supplementary Material
<ul>
{% assign supp_posts = site.posts | where:"categories", "supp" %}
{% for page in supp_posts %}
  <li>
    <a href="{{site.baseurl}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul>

### Mathematical Foundations

<ul>
{% assign mfml_posts = site.posts | where:"categories", "mfml" %}
{% for page in mfml_posts %}
  <li>
    <a href="{{site.baseurl}}/{{ page.url }}" title="{{ page.title }}">{{ page.title }}</a>
  </li>
{% endfor %}
</ul>

### Traditional Machine Learning

### Deep Learning
