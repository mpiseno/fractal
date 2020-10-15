---
layout: module
---

# Libraries

---

## What is a Library?

Just like at a normal library, where you might check out books and gain knowledge, code libraries are where you checkout useful functions and classes and gain functionality for your program. In the previous lesson, we saw an example of a class that was imported into our program from a library, namely the deque class imported from the collections library. In this lesson, we will introduce some libraries that we can use to build up more complex programs. For all of the libraries discussed in this lesson, we have linked the official documentation below, which details all the functionality available:

* [Math](https://docs.python.org/3/library/math.html)
* [Random](https://docs.python.org/3/library/random.html)
* [Collections](https://docs.python.org/3/library/collections.html)
* [CSV](https://docs.python.org/3/library/csv.html)

### Using Libraries

There are many built-in libraries (ones that come with Python) that can be imported into your program, but two particularly versatile ones are math and random. You may be wondering, "if they come with Python why do we have to explicitly import them?", and the answer is somewhat beyond the scope of this lesson, but in short, we have to store those functions somewhere to be able to use them, which increases the size of our program. If we can get away with having a smaller program by not using functions that we do not need, then that's always better.

To import a library, you use the import keyword

```py
import math

x = 5.5
print(math.ceil(x))
```

You can choose to just import a single funtion, class, or variable from a library using the from keyword

```py
from math import ceil

x = 5.5
print(ceil(x))
```

## Math and Random

Here we will discuss a few of the useful functions in the math and random libraries. The math library, as you might guess, provides useful mathematical capabilites so you don't have to implement these functions yourself. Here are a few examples of some useful functions and how to use them. For the compete list of functions, refer to the documentation in the first section.

```py
import math

# Square root
x = 25
sqrt_x = math.sqrt(x)

# Generic power
x = 2
second = math.pow(x, 2)
fifth = math.pow(x, 5)
eighth = math.pow(x, 8)

# Exp and Log
x = 4
expx = math.exp(x)
logx = math.log(x)
log8x = math.log(x, 8) # optionally specify a base

# Ceiling and Floor
x = 5.5
ceiling = math.ceil(x)
floor = math.floor(x)

# Counting (combination and permutation)
num_ways = math.comb(10, 4)
num_ordered_ways = math.perm(10, 4)
```

The random library provides various functionality to sample from random distributions, or choose random objects.

```py
import random

# Choose a unformly distributed random number between a and b (inclusive)
a, b = 1, 100
r = random.randint(a, b)

# Sample a uniform random element from a list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = random.choice(x)

# Randomly shuffle the elements of a list
print(f'Before: {x}')
random.shuffle(x)
print(f'After: {x}')
```

## Collections

We used the collections library in the last lesson to import the deque class, which is an implementation of a queue data structure. The collections library is full of really useful data structures!

### Deque

A deque (pronounced like "deck") is an implementation of a queue, meaning we can pop elements from the front of the queue and push elements to the back of the queue. The key property of a queue is that elements pass through it in a First-In-First-Out (FIFO) manner, meaning the first element push to the back of the queue is the first element popped from the front (Although the deque class provides extra functionality that breaks this rule like allowing you to push elements into the front).

```py
import collections

q = collections.deque()

# Push elements into the back
for i in range(10):
    q.append(i)
    print(q)


# Pop elements fron the front
while q: # loop until the queue is empty
    popped_value = q.popleft()
    print(f'{q}\tpopped value: {popped_value}')
```

### Default Dict

In the data structure section, we introduced the dictionary class, which is an implementation of a hash map. It allowed us to map keys to certain values. In the algorithms lesson, we used a dictionary to map vertices to the list of vertices they were connected to. Recall:

```py
graph = {
    'S': ['Br', 'L'],
    'Br': ['Bd'],
    'Bd': ['L'],
    'L': ['D, K'],
    'D': ['K'],
    'K': []
}
```

One limitation of dictionaries is that we have to check if a key exists in the dictionary before operating on it. For example, if you had a dictionary that mapped letters to a list of numbers like this

```py
d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
}
```

then you would not be able to do something like

```py
d['d'].append(25)
```

because accessing d['d'] would error. That's where default dicts come in. When you instantiate a default dict, you specify what the type of the value will be. In the above example, we would specify a list type. Then, when you try to query the default dict at a key, if they key does not exist in the dictionary, it will just return the default value, in this case an empty list.

```py
import collections

d = collections.defaultdict(list)
d['d'].append(1)
print(d)

# Another example with ints
d = collections.defaultdict(int)
d['a'] += 1
```

## CSV

In this section we will learn about the csv library, which allows you to read from and write to csv files. But first, we need to go over something called a file object.

### File Objects

File objects are returned by the "open" built-in Python function and they are a special type of variable that references a file to be read or written to. The most common way to use file objects are inside a with statement. Assume we have a csv file called "info.csv" with peoples' name and age.

```py
with open('info.csv', 'r') as f:
    line = f.readline()
```

In the above code, f is the file object and it has certain methods like readline that allow us to read from the file. The second argument to the open function specifies that we are opening the file in read mode.

### Reading a CSV

Now we can proceed with learning about the reading and writing functionality of the csv library. To read a file, the library offers a reader class which has methods for reading lines from the csv. To instantiate it, you must provide the file object for the csv file. The reader object returned is an iterator over the rows of the csv.

```py
import csv

with open('info.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

In the above example, each row is actually a list of the fields in that row, so we can index directly into the list.

```py
with open('info.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Since reader is an iterator, the next function works to get the next row
    first_row = next(reader)
    name, age = first_row[0], first_row[1]
```

### Writing to a CSV

This is just analogous to the reader: You use the writer class and the corresponding method to write rows to the csv file. The rows that you write are lists in your program. The only difference is now we open the file with 'w' which stands for write mode.

```py
import random

with open('new_info.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)

    # Create 4 rows of 10 random numbers
    for _ in range(4):
        row = []
        for _ in range(10):
            row.append(random.randint(1, 100))

        # Use the writerow method to write to the csv file
        writer.writerow(row)
```

We now have all the tools we need to start the first project - creating a word guessing game! In the next lesson we will introduce the first project (which we encourage you to try on your own before looking at the solution). You will need to use various data structures, libraries, and write correct code for the game to work. See you there!

---

<div class="next-prev-btn-wrapper">
    <button class="next-prev-btn"><a href="{% link tutorials/algorithms.md %}">Previous Lesson</a></button>
    <button class="next-prev-btn"><a href="{% link tutorials/word_guess.md %}">Next Lesson</a></button>
</div>