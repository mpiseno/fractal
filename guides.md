---
layout: page
title: Guides
permalink: /guides/
---
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
<p>This section contains tutorials related to mathematical concepts as they relate to traditional machine learning. The idea is that a strong understanding of the theory behind these algorithms will force a deeper understanding (and greater appreciation) for machine learning. If this section feels too theoretical and the reader prefers to just understand machine learning and deep learning at a higher level, this section can be skipped.</p>


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
