---
layout: post
title:  "Python Basics"
date:   2020-05-22 00:06:43 -0800
categories: ["cs"]
---

### Introduction

<p align="justify">Python is a versatile programming language used in many different applications from simple scripting to entire applications. It was created in the late 80s by Guido van Rossum, and has seen increased adoption particularly in the data science and machine learning communities in recent years. We are using python because it is syntactically easy to read compared to other languages, beginner friendly, as has many packages that we can use for anything we want to build.</p>

<p align="justify">Python files have the ".py" file extension and can be run in the terminal (command prompt for windows users) by running, </p>

```
python filename.py
```

<p align="justify">where "filename" is replaced with the name of your python file, while in the directory (folder) that the file is in. You can interactively test python code by simply running</p>

```
python
```
<p align="justify">in the terminal. This will open a python shell where you can type and run code line by line.</p>

### Primitive Types

<p align="justify">The most basic data in python are primitive data types, which include:</p>

* int (integers, example: 1)
* float (floating point numbers, example: 0.25)
* str (words and characters, example: 'a')
* bool (true and false, example: True)

<p align="justify">We can assign values that have these types to variable in our program using the = operator (the assignment operator). Anything following "#" in a python program is a code comment, meaning it will not be considered code in the program. Comments help the programmer and others who are reading the code understand what the code does.</p>

```python
x = 1 # the variable x is of type int
y = 1.0 # the variable y is of type float

word = 'this is a string' # the variable word is of type str
word = "this is a string" # we can use either '' or "" to define a string
program_running = True # the variable program_running is of type bool

# We can perform math on floats and ints
z = x + y
z = (z + 45) / y - (171.4256 * 0.5)

# We cannot combine ints and float with strings
bad_code = x + word # this will error
```

<p align="justify">The above code defines some variables or different types and manipulates them. Note how some types cannot be combined. However, we can append strings together, and we can covert an int to a string add it to another string</p>

```python
num_apples = 5
sentence_begin = 'I have '
sentence_end = ' apples'

# The str() function converts primitives of other types into a string
sentence = sentence_begin + str(num_apples) + sentence_end
print(sentence)
```

```
output:
I have 5 apples
```

<p align="justify">Just like the str() function converts other types to string, there is an int() function and float() function that converts to int and float respectively. They don't work with every input though; float('hello') will give you an error.</p>

### Data Structures

<p align="justify">Data structures are more advanced ways to store data that prove very useful in a variety of scenarios. We will cover two commonly used data structures, lists and dictionaries, but there are many more. Just like we have primitive types, list and dictionaries are their own types in python, but they are not primitives.</p>

#### Lists

<p align="justify">A list in python is a way to store sequential elements of information. They are created using square brackets. You can retrieve a particular element from a list by doing something called indexing, which means you pass in the position of the element you want in the list (see code below).</p>

```python
mylist = [4, 2, 7, 6, 10, 245] # a list of ints

element = mylist[3] # use brackets to index into the list
another_element = mylist[0] # indices begin at 0 in python!!! <-- IMPORTANT

# Accessing the last element in a list
last_element = mylist[len(mylist) - 1]

# Lists can hold elements of differing types
another_list = [1, 24.6, "an element", True]

# You can also add elements to an existing list later on
mylist.append(27)
```

<p align="justify">Note that indices begin at 0 in python. There is a very good theoretical reason for this that I won't go into here, but just remember the first element of a list is always at index 0. This means the final index of a list is the length of the list minus 1. The length of a python list can be accessed using the len() function. To add elements to the end of an existing list, use the append() method.</p>

#### Dictionaries

<p align="justify">A dictionary in python is a data structure that acts as a mapping from keys to values. A dictionary is created using curly braces. Values can be accessed using the name of the key insides square brackets.</p>

```python
# Define the dictionary
fruits = {}

# Add some key-value pairs
fruits['apples'] = 10
fruits['oranges'] = 6
fruits['bananas'] = 2400

num_bananas = fruits['bananas']
print(num_bananas)
print(fruits['oranges'] < 7)
```

```
output:
2400
True
```

<p align="justify">One important property of dictionaries is that keys must be unique, which values do not have to be unique. This means we cannot define two entries in the dictionary whose keys are both 'apple'. Some useful methods (functions that are specific to a particular type) that can be called on dictionaries are keys() and values().</p>

```python
keys = fruits.keys() # the keys method returns a list of the keys in the dictionary
print(keys)

vals = fruits.values() # the values method returns a list of the values in the dictionary
print(vals)
```

```
output:
['apples', 'oranges', 'bananas']
[10, 6, 2400]
```

### Logical Statements

<p align="justify">Just like any programming language, python has some basic logical statements that can be used to encode logic into your program. The main ones we will use are if statements, for loops, and while loops.</p>

#### If

<p align="justify">If statements can be used to separate code that executes based on a condition. If blocks are broken up into if, elif, and else, which checks a condition, checks a condition if the previous condition was false, and provides some code to default to if all the previous conditions were false, respectively.</p>

```python
x = 5

if x == 4:
  print("x is 4!")
elif: x == 5:
  print("x is 5!")
else:
  print("x is neither 4 nor 5")
```

```
output:
x is 5 !
```

<p align="justify">In the if statement above, the condition is x == 4. Note the difference between the assignment operator "=", which assigns a value to a variable, and the equality operator "==" which checks if two values are equal. X is not 4, so the code will not execute the print statement in that if block. The program moves on to the next statement, the elif statement which checks if x is equal to 5. Since x is 5, the output of this program is "x is 5!". The program then moves past this entire block; there is no need to look at the else statement because we already know x is 5 at this point. You have to include an elif or an else statement.</p>

```python
if True == True:
  print("This is a tautology!")

if True == False:
  print("This is a fallacy!")
```

```
output:
This is a tautology!
```

#### For and While Loops

<p align="justify">For loops are a way to loop over the same block of code a predefined number of times. The canonical way to construct a for loop in python is to use the range() function which executes code a certain number of times.</p>

```python
for i in range(3):
  print(i)

mylist = [10, 12, 14]

for i in range(len(mylist)):
  print(mylist[i])
```

```
output:
0
1
2
10
12
14
```
<p align="justify">While loops on the other hand execute a block of code until the condition is false.</p>

```python
i = 0
while i < 4:
  print(i)
  i = i + 1
```

```
output:
0
1
2
3
```
<p align="justify">In the above code, the code inside the while loop executed until i was no longer less than 4. If we never reassigned x to increment at event iteration of the while loop, this loop would have continued forever!</p>

### Functions

<p align="justify">We have already seen some built-in functions that come with python, namely len(), range(), print(). But we can also define our own functions that take input parameters and do some computation. This is useful for situations when we might need to reuse the same code several times so we don't have to keep rewriting it. To do this, we use the "def" keyword. To return a value from a function, use the "return" keyword.</p>

```python
def add(x, y):
  return x + y

result = add(5, 7)
```
<p align="justify">The above function is very simple, but we can do all sorts of crazy computation using functions, and we can also compose functions together.</p>

```python
def get_max_if_below_x(list_, x):
  maximum = max(list_)
  if maximum < x:
    return maximum
  else
    return 0

mylist = [1, 3, 5, 7, 9]
print(get_max_if_below_x(mylist, 10))
print(get_max_if_below_x(mylist, 9))
```

```
output:
9
0
```

<hr>

<p align="justify">This guide introduced some basic types in python, a couple useful data structures, logical statements, and custom functions. These are the basic steps needed to create more complex programs using python. I encourage you to get creative with writing custom programs and if you get stuck, be proactive about searching for answers online. I'll leave you with some resources that helped me when I was learning python - good luck!</p>

* [A great online python textbook](https://automatetheboringstuff.com/)
* [StackOverflow](https://stackoverflow.com/questions/tagged/python-3.x)
