---
layout: module
---

# Data Structures

---

## What is a data structure?

Very simply, a data structure is an object that hold various types of data to be used in our program. A very simple example is if we had a program that prints out the name of each person in a class. To do this, we could save a string variable for each person in the class, but that would be quite tedious, and not scalable if there are hundreds of students in the class. A data structure that would be useful for this task would be a list, which is just a collection of items, in this case strings, that we can index in to, add names to, remove names from, etc..

Data structures come in all shapes and sizes. Some data structures are very complicated and are made up of smaller data structurs to access data faster or in smart ways, depending on the application. The types of data structures we will be discussing in this lesson are fundamental to our study of programming. We will study lists (also called arrays in other programming languages), sets (also called hashsets), and dictionaries (also called hashmaps).

Recall from our last lesson, classes are objects that contain variables and methods that are specific for that class's use. The data structures we are studying are just classes under the hood, so they will have some useful methods that we can access.

## Lists

A list in Python, is an ordered collection of objects. The objects we store in a list could be anything, strings, ints, bools, different instances of the Cat class, or even other lists. You can create a list using square brackets and assigning it to a variable. You can index into a list to retrieve a value using the square brackets [i] on the list where i is the index you want to retrieve from. Valid indices are 0 to the length of the list - 1.

```py
# Create a list using the square brackets
names = ['Alice', 'Bob', 'Charlie']

# Index into a list by using square brackets on the list
name = names[1]

# Make sure to only use valid indices!
name = names[3] # errors!
```

Lists indices start at 0 (NOT 1!) so the last index is the length of the list - 1. That's why trying to access index 3 above will error. We can also assign elements to certain indices, which overrides the value that is currently at that index.

```py
names[0] = 'Alex'
print(names)
```

A couple of useful operators and functions: The built-in len function will give us the length of the list. The "in" keyword can be used to test whether or not an item is in a list.

```py
fruits = ['Apple', 'Orange', 'Watermelon', 'Cherry']

length = len(fruits)
print(length)

# Check if something is in the list
if 'Apple' in fruits:
    print('We have apples')
```

One thing you might want to do is iterate through a list and calculate some information about the list. For example, if we wanted to compute the maximum of a list of numbers, we could simply iterate through the list and do a couple checks.

```py
nums = [1, 5, 9, 2, 6, 13, 24, 32, 13, 5]

max_so_far = 0
for i in range(len(nums)):
    current_num = nums[i]
    if current_num > max_so_far:
        max_so_far = current_num

print(max_so_far)
```

Lists actually support something called a for-each loop, which directly gives you access to the elements in the list without having to index into the list. Furthermore, a cleaner way to calculate the maximum of two numbers, as we do in the code inside the for loop, is to just use Python's built-in max function.

```py
nums = [1, 5, 9, 2, 6, 13, 24, 32, 13, 5]

max_so_far = 0
for num in nums: # This is a for-each loop. No indexing required!
    max_so_far = max(max_so_far, num)

print(max_so_far)
```

The max function actually works directly on lists as well, but under the hood it is doing exactly what we coded above.

#### Useful methods

Since lists are just instantiations of the list class, there are some helpful methods we can use. We want to be able to both add and remove items from our list, and thankfully Python provides methods for these. The append method adds an items to the end of the list. The pop method removes the last item in the list and returns it to the user. Finally, the remove method removes the first instance of the item we want to remove from the list.

```py
students = ['Michael', 'Sally', 'John', 'Camila', 'Emily', 'Jose']

# Append a string to the end of the list
students.append('Lee')
print(students)

# Remove the last element from the list
last_student = students.pop()
print(last_student)

# Remove a student from the list
students.remove('John')
print(students)
```

Here's an example of how we might use these. Say we wanted to find all the odd numbers from a list and return them. To do this, we could iterate over the list and check if each number is odd. If it is, we add it to another list.

```py
nums = [0, 2, 3, 9, 1, 5, 7, 8, 6, 4]
odds = []
for num in nums:
    # The % operator is modulus. Every odd number is 1 mod 2
    if num % 2 == 1:
        odds.append(num)

print(odds)
```

## Dictionaries and Sets

Lists are great if we want an ordered collection of items. Lists essentially map integers, which are the indices, to items. But sometimes we want to map arbitrary items to other items. For example if we wanted to store a person's name and their associated age, lists only complicate things.

Dictionaries, also called hashmaps in other languages, are a way to define this type of mapping. They are instantiated using curly braces {}. Entries in the dictionary take the form key : value, where key is the thing we want to map from, and value is the thing we want to map to. To access the value at a particular key, you use the square brackets [] on the dictionary.

```py
# Define a dictionary
name_to_age = {'Michael': 22, 'Amy': 30, 'Jose': 25}

age = name_to_age['Michael']
print(age)
```

You can also modify the dictionary to replace or add new key/value pairs.

```py
name_to_age = {'Michael': 22, 'Amy': 30, 'Jose': 25}

name_to_age['Cindy'] = 23
```

Sets, also called hashsets, are another key data structure in Python. Sets are an unordered collection of elements, but unlike dictionaries they are not a mapping from one key to a value, but rather they are just a collection of keys. Sets are instantiated with the set() built-in class.

```py
names = set('Cindy', 'Jose', 'Michelle')
```

You can add and remove from sets using the add and remove methods respectively.

```py
names = set('Cindy', 'Jose', 'Michelle')

names.add('Lee')
names.remove('Lee')
```

For both dictionaries and sets, the "in" keyword works just as it does for lists.

```py
names = set('Cindy', 'Jose', 'Michelle')
if 'Jose' in names:
    print('Jose is in the set.')
else:
    print('Jose is not in the set.')
```

You might be wondering what is the use of a set versus a list, since they are both a collection of items. The requirement of an ordering of the elements in a list actually makes certain operations on lists slower than sets. For example, if you remove an item from the middle of a list, every other item to the right of the item you removed must be shifted left by one space. In a set, we can remove an item without messing with the other items.

Here's an example that uses both lists and dictionaries: Write a function that takes in a list of ints and outputs a dictionary that contains counts for each of the unique elements in the list. Before looking at the solution below, try it on your own!

```py
nums = [1, 2, 2, 2, 9, 15, 15, 3, 3, 6,
        20, 20, 20, 15, 14, 13, 14, 2, 1]

def counter(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

    return counts

counts = counter(nums)
print(counts)
```

As we will see in later lessons, the data structures we covered will be crucial in writing more interesting programs. These data structures are the foundations of more complex data structures like linked lists, binary trees, and heaps. They are also crucial in writing algorithms that are efficient, which we will cover in the next lesson.

Remember to write the code in your text editors and run it for yourself, as well as try out different tasks. See you in the next lesson!

---

<div class="next-prev-btn-wrapper">
    <button class="next-prev-btn"><a href="{% link tutorials/hello_world.md %}">Previous Lesson</a></button>
    <button class="next-prev-btn"><a href="{% link tutorials/algorithms.md %}">Next Lesson</a></button>
</div>