---
layout: post
title:  "Machine Learning Introduction"
date:   2020-01-15 00:06:43 -0800
categories: ["supp"]
---

### What is Machine Learning?

Machine Learning (ML) is, as Tom Mitchell stated, "The study of algorithms that improve their performance P at some task T with experience E". Another way of looking at it is that we are learning an algorithm that solves an inference problem or a model that describes some data set. We will discuss these two concepts at a basic level below and then introduce some cool things machine learning and deep learning have accomplished to hopefully incite some interest.

#### Inference

Inference means making a decision or prediction about some sort of data, perhaps in a probabilistic sense. For example, I might give you an image and say "is there a cat in this image?" or "what is the probability that there is a cat in this image?"

<img src="{{site.baseurl}}/assets/MLIntro/kit.jpg" alt="cat" width="200" height="150"/><img src="{{site.baseurl}}/assets/MLIntro/cat.jpg" alt="cat" width="200" height="150"/><img src="{{site.baseurl}}/assets/MLIntro/catinbox.jpg" alt="cat" width="150" height="150"/><img src="{{site.baseurl}}/assets/MLIntro/catbowl.jpg" alt="cat" width="150" height="150"/>

As you might imagine, it gets more complex and ambiguous when the thing you're trying to predict is secluded in some way or only represents the idea of the thing you're trying to predict instead of being the thing itself (e.g. the cat-faced bowl above).

There are perhaps more interesting inference problems where you don't have complete information, but you know some related information. For example, if I give you the temperature in San Francisco, San Jose, and Fremont, can you predict (infer) the temperature in Palo Alto? Or If I give you the position and velocity of a car at time $t_{1}$, can you tell me the probability the car will be 5 meters north at time $t_{2}$? The output of an inference algorithm can either be a concrete decision (e.g. the image does have a cat in it) or a probability distribution over the set of possible outcomes (e.g. there is a 60% chance that the temperate in Palo Alto is between 50 and 65 degrees Fahrenheit).

#### Modeling

Modeling allows us to describe data either qualitatively or numerically. There are typically geometric models, which are ones that try to find geometric structure in data and probabilistic models, which try to find a probability distribution given a bunch of samples of random variables.

An example of a geometric model might be: I have (square-footage, location, number of bedrooms) information for 1000 houses. How can I find some combination of these attributes that still comes close to fitting the data? This boils down to finding a lower-dimensional subspace that comes close to containing all the original data.

<figure>
  <center>
    <img src="{{site.baseurl}}/assets/MLIntro/subspace.png" alt="subspace" width="300" height="200"/>
    <figcaption>Data close to a lower dimensional subspace</figcaption>
  </center>
</figure>


### Why study ML?
