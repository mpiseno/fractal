---
layout: module
---

# Algorithms

---

## What is an Algorithm?

An algorithm is, very simply put, an explanation of how to accomplish a certain task. The algorithm itself is an abstract concept, and is separate from a program, although programming is how we implement the algorithm. You use algorithms every day and may not even realize it. For example, an algorithm for doing the dishes would look something like:

```
while there are still dishes in the sink:
    Use a sponge to apply soap to the dish and scrub
    Place the dish in the dishwasher

Turn on the dishwasher and select the correct settings
Press start on the dishwasher
```

Notice how we did not explicitly write code, but rather we listed out specific instructions that represent an idea - an algorithm! Writing out our logic in this way is typically called pseudocode. It is a fact that every positive integer can be factored as the product of prime numbers, known as a prime factorization. Here's an algorithm to find the prime factorization of an integer n.

```
let p = 2
let factors = 1
while n does not equal 1:
    while p divides n:
        factors = factors * p
        n = n / p

    set p to be the next prime number greater than the current p

return factors
```

Using the above algorithm, we get that the prime factorization of 60 is $2^{2}3^{1}5^{1}$. Algorithms allow us to write down solutions to some really useful tasks. In this lesson, we will explore algorithms for sorting items in a list, searching for items in a list, and of course, finding the closest path between you and your fridge!

## Sorting

Sorting is a problem that comes up everywhere from organizing your socks to trading stocks, so learning how to program a sorting algorithm will be invaluable in writing future programs. We will learn an algorithm known as Bubble Sort, which is a simple way to sort a list of items, which in our case will be a list of ints.

### Bubble Sort

Imagine we have an unsorted list of ints. In bubble sort, we put one element of the list in the correct place at a time. The idea is to start at the front of the list and "slide" the element as far to the right as possible, swapping it with the element to its right if the element to its right is less than it. Once we can't slide the first element to the right any more, we pick up where we left off and continue sliding that element to the right, and so on, until we reach the end of the list.

```py
nums = [5, 4, 3, 1, 2]

[4, 5, 3, 1, 2] # swap the 5 and 4

[4, 3, 5, 1, 2] # swap the 5 and 3

[4, 3, 1, 5, 2] # swap the 5 and 1

[4, 3, 1, 2, 5] # swap the 5 and 2

# Now the last position contains the correct number (5)
```

The we go back to the end of the list and repeat to put the correct number in the second-to-last position! Then the third-to-last, and so on. If we repeat this process N times, where N in the length of the list, then the whole list will be sorted.

<div class="lesson-img">
    <img src="{{site.baseurl}}/imgs/lesson_imgs/algorithms/bubble_sort.gif">
    <p class="text-center">Source: <a href="https://commons.wikimedia.org/wiki/Category:Bubble_sort#/media/File:Bubble_sort_with_flag.gif">Wikimedia</a></p>
</div>

The algorithm for this is quite simple:

```
let nums be the list we are sorting
let n = length of nums
Repeat n times:
    i = 0
    Repeat n times:
        if nums[i + 1] < nums[1]:
            swap nums[i + 1] and nums[i]

        i = i + 1
```

We of course need to do some extra checking to make sure we don't index out of bounds, but that is an implementation detail. The code for this algorithm looks quite similar:

```py
nums = [5, 4, 3, 1, 2]

n = len(nums)
for _ in range(n):
    for j in range(n):
        # Make sure we don't index out of bounds
        if j < n - 1 and nums[j + 1] < nums[j]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1] # swap

print(nums)
```

The _ in the code above it a little Python trick that just signifies that we don't need a variable for the iterator so we can just throw it away. For the remainder of the topics we discuss, we will not write down the pseudocode, but we will give the code and a detailed explanation.


## Searching

The task now is to search for a given integer in a sorted list of ints. If the interger we are looking for exists in the list, we output true, otherwise we output false. If the list was not sorted, we would simply iterate through the list until we found the int we were looking for, which is called sequantial search or linear search. However, knowing that the list is sorted lets us use a clever algorithm called Binary Search to find the item faster.

### Binary Search

The idea behind binary search is to cut the area we are searching in half at each step. We keep variables for the index of the left end of our search area and the right end. Then we compute the index of the middle point of our search area, by simply taking the average, and looking at the number at that index. If that number is less than our target number, then our taget number has to be in the right half of the list (since the list is sorted in increasing order), meaning we have just cut our search area in half! We keep cutting our search area in half until either we have found what we are looking for or the search area becomes empty, in which case we have not found the element.

```py
target = 5
nums = [1, 2, 3, 5, 6, 8, 10, 14, 19, 21, 30]

# L               M                   R
  [1, 2, 3, 5, 6, 8, 10, 14, 19, 21, 30]

# The item at the midpoint index M is greater than our target,
# so the target is in the left half of our search area.


# L      M     R                      
  [1, 2, 3, 5, 6, _, _, _, _, _, _]

# The item at the midpoint index M is less than our target,
# so the target is in the right half of our search area.


#           L  M  R                   
  [_, _, _, 5, 6, 8, _, _, _, _, _]

# The item at the midpoint index M is greater than our target,
# so the target is in the left half of our search area.


#           L
#           R
#           M                     
  [_, _, _, 5, _, _, _, _, _, _, _]

# The item at the midpoint index M is equal to the target - we found it!
```

In the gif below, the target is 37:

<div class="lesson-img">
    <img src="{{site.baseurl}}/imgs/lesson_imgs/algorithms/binary_search.gif">
    <p class="text-center">Source: <a href="https://medium.com/@jeffrey.allen.lewis/javascript-algorithms-explained-binary-search-25064b896470">Jeff Lewis, Medium</a></p>
</div>

Here is the code implementation for the algorithm:

```py
nums = [1, 2, 3, 5, 6, 8, 10, 14, 19, 21, 30]

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False

print(binary_search(nums, 5))
```

## Fastest Path to Fridge

Here's a fun example. Say you're in your room and want to find the fastest path to your fridge. The floor layout looks like the layout below, where arrows represent doorways and the different color arrows represent two possible paths to the fridge.

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/algorithms/floorplan.png">

We need to represent the concepts of "rooms" and "paths" in a form that we can do computation on and we also need to define what it means to be the "fastest" path.

We can do the first task by using a data structure called a graph, which has vertices (or nodes) connected by edges. In our case, the rooms will be the vertices and if two rooms have a doorway (i.e. a path) connecting them, then they will have an edge between them.

For the second task, we can simply define a cost for going from one room to another. The cost will be 1 each time you switch from one room (i.e. one vertex) to another. Thus, the fastest path to the fridge will be the path that incurs the smallest cost along the way. For our purposes, we will say that as soon as the path reaches the kitchen vertex, we have found the fridge. Now putting it all together, the graph looks like this:

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/algorithms/graph.png">

where S is your room (the start), Br is the bathroom, Bd is the bedroom, L is the living room, D in the dining room, and K is the kitchen (the goal location). In code, we can just use a dictionary to map the rooms to a list of other rooms that it leads to.

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

Now that we have all the modeling out of the way, we need to think of an algorithm that can take our graph input and compute the shortest path to K. For this we will use an extremely useful algorithm called breadth first search or BFS.

### Breadth First Search

The idea behind BFS is that we start at a starting vertex (S in our case) and then search one "layer" out. In this case, the layer is the group of vertices that are 1 step away from the start, namely 'Br' and 'L'. Then we search another layer out by considering the vertices that are 1 step away from each of 'Br' and 'L'. We keep doing this - searching one more layer out - until we reach the goal location, at which point we are guaranteed that it is the shortest path.

In order to implement this in code, we need another data structure, called a queue. This is just a list except we can also pop from the left side of the list (the beginning) instead of just the right side (the end). At first, just 'S' will be in the queue. We pop from the queue and then see all the neighbor vertices of the vertex that we popped and ad them to the back of the queue, which holds the vertices to be processed in the next layer.

One last caveat: In order to keep track of the actual path, we don't just store the vertices in the queue, but rather we store lists of the path so far ending at the current vertex we are examining. For example, if we are at the vertex 'Bh' and we just came from 'Br', which came from 'S', then our tuple would look like ['S', 'Bh', 'Br']. Finally, here is the code.

```py
# We will learn about import in the next lesson, but this is a useful class
# that implements a queue
from collections import deque

graph = {
    'S': ['Br', 'L'],
    'Br': ['Bd'],
    'Bd': ['L'],
    'L': ['D, K'],
    'D': ['K'],
    'K': []
}

def find_shortest_path(start, target):
    q = deque([[start]]) # create a queue with just the start in it at first
    while q: # loop until the queue is empty
        path = q.popleft()
        cur_vertex = path[-1] # -1 is shorthand for the last thing in the list
        if cur_vertex == target:
            return path
        
        # If we aren't at the target yet, add all the neighbors to the end of
        # the queue to be searched in the next layer
        for neighbor in graph[cur_vertex]:
            new_path = path.copy()
            new_path.append(neighbor)
            q.append(new_path)

    # Return nothing of the path isn't found
    return None

shortest_path = find_shortest_path('S', 'K')
print(shortest_path)
```

Running the above code yields, the shortest path, which you probably already visualized from the graph: ['S', 'L', 'K'] with a cost of 2.

Sorting and searching are two fundamental tasks in programming, and learning different algorithms for doing them will pay dividends in the future. In the next lesson, we will explore some useful code libraries that will also come in handy in every day programming, and that will be useful in the future lesson where you will create your first project!


---

<div class="next-prev-btn-wrapper">
    <button class="next-prev-btn"><a href="{% link tutorials/data_structures.md %}">Previous Lesson</a></button>
    <button class="next-prev-btn"><a href="{% link tutorials/libraries.md %}">Next Lesson</a></button>
</div>