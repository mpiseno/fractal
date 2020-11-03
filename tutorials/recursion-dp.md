---
layout: module
---

# Recursion and Dynamic Programming

---

This lesson will cover the basics of recursion and dynamic programming, two very power programming concepts. Recursion allows us to call functions from within themselves, while dynamic programming relies on storing results from intermediate computation (i.e. subproblems) to solve a larger problem, and often speeds up recursion.

## What is Recursion?

You may have see the idea of recursion or recursive formulas in math class before. For example, a sequence of numbers $(a_{n})\_{n=1}^{\infty}$ may be defined recursively by $a_{1} = 1$ and every subsequent term follows the recursive formula

$$a_{n} = 2a_{n-1} + 1 \quad n = 2, 3, ...$$

The first few terms of this recursively defined sequence would be $(1, 3, 7, 15, 31, ...)$. Here's a question: How would you write a program to compute the $N$th term in this sequence? You might just use a for loop and iterate n times to generate the term like this:

```py
def compute_nth_term(N):
    a = 1
    for i in range(1, N):
        a = 2 * a + 1

    return a
```

This is completely correct, and this method is called determining the $N$th term "iteratively", because we iterate to find the answer. Notice how we calculated the answer in a "bottom-up" way, starting from the first term and gradually computing later terms in the sequnce until we reached the $N$th one. Another approach is to start from the $N$th term, which we have an equation for and work backwards. We will prsent the code and then explain it:

```py
def compute_nth_term_recursive(n):
    if n == 1:
        return 1

    return 2 * compute_nth_term_recursive(n - 1) + 1
```

Notice how the recursive function above calls itself in order to determine the $(n-1)$st term, and once it has that, it can construct the $n$th term using the formula. But we can't keep calling the function inside itself forever; we need a stopping point. That's where the if statement above comes in. If we get to the case where $n = 1$, then we return the 1st term. In this way, we construct the answer from the "top down" and this is called determining the $N$th term "recursively".

A recursive function has two parts, a base case and a recursive call to itself. In the above example, the base case is when $n=1$ and the recursive call to itself determines the answer to a subproblem (the answer of the $(n-1)$st term) and uses the answer to that subproblem to get the answer of the current problem (the $n$th term). Notice that each time the function is recursively called, the function parameter $n$ is different.

The computation forms a "chain" where we keep asking for the answers to subproblems before solving the answers to the current problem. For example, the case where $N=5$:

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/recursion-dp/sequence-rec.png">

## Fibonacci

The Fibonacci sequence is a famous recursive sequence defined as $a_{1} = a_{2} = 1$ and 

$$a_{n} = a_{n-1} + a_{n-2} \quad n = 3, 4, 5, ...$$

Again, we can iteratively find the $N$th term of the Fibannaci sequence as follows:

```py
def fib(N):
    a = b = n = 1
    for i in range(2, N):
        n = a + b # Add the previous 2 terms
        b = a # update what is considered "previous terms"
        a = n

    return n
```

And as you might have guessed, we could just as easily use recursion to take a "top-down" approach to computing the $N$th Fibonacci number:

```py
def fib_rec(n):
    # Base case
    if n in [1, 2]:
        return 1

    # Recursive step
    return fib_rec(n - 1) + fib_rec(n - 2)
```

Again, we start with a problem that we want to solve, the $n$th Fibonacci number, and we use recursion to get the answers to the subproblems (i.e. the $(n-1)$st and $(n-2)nd$ Fibonacci numbers). Then we use the answers to those subproblems to construct the answer to the current problem using the formula. Of course we still need the base case, which here is the case when $n=1$ or $n = 2$.

Notice that for each recursive step there are two branches of computation that we have to get answers to (i.e. two subproblems), so instead of a chain, we will actually have a tree of subproblems. For example, to recursively compute the $5$th Fibonacci number:

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/recursion-dp/fib-tree.png">

The above computation tree can get extremely large when $N$ is large. For each problem, we have to solve 2 subproblems, meaning the number of function calls is roughly $2^{N}$. You can test this phenominon out yourself; try to compute a large Fibonacci number recursively and observe that as you increase $N$ the time it takes to get the answer exponentially increases.


## Dynamic Programming

In the last section we ended with a discussion about how computing the $N$th Fibonacci number takes a long time when $N$ is large. The first question you might ask is, can we do better? Observing the computation tree, we can see that many of the subtrees are repeated.

For example, the subtree Fib(3) is repeated twice in the full computation tree. There's no need to repeat this computation twice. Fib(3) is always Fib(3) no matter how many different times we compute it, so if we store the answer to Fib(3) the first time we compute it, the next time we need that number we can just immediately return it. That's the whole idea behind dynamic programming - storing the answer to repeated subproblems so that we don't have to recompute those answers.

To store the answers to repeated subproblems, we can use a dictionary that maps an int (the Fibonacci number corresponding to the subproblem we are currently on) to the answer for that subproblem.

```py
def fib_dp(n, dp):
    # Base case
    if n in [1, 2]:
        return 1

    # Check if we already have the answer to the subproblem
    if n in dp:
        return dp[n]

    # The answer was not in the dp table, so we need to compute it
    answer = fib_dp(n - 1, dp) + fib_dp(n - 2, dp)

    # After we have computed the answer, store it in the dp table for later use
    dp[n] = answer
    return answer


N = 100
print(fib_dp(N, {}))
```

The computation tree using dynamic programming eliminates the second Fib(3) subtree, and looks like this:

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/recursion-dp/fib-tree-dp.png">

We can test how much time this saves for large values of $N$. Let's plot computation time versus $N$ for both straight up recursion and for dynamic programming. Here we are using a library that we did not cover previously called matplotlib, which is a third-party library and does not come with Python.

```py
import time
import matplotlib.pyplot as plt

max_N = 40
rec_times = []
for i in range(1, max_N):
    start = time.time()
    ans = fib_rec(i)
    time_taken = time.time() - start
    rec_times.append(time_taken)

dp_times = []
for i in range(1, max_N):
    start = time.time()
    ans = fib_dp(i, {})
    time_taken = time.time() - start
    dp_times.append(time_taken)

plt.plot(list(range(1, max_N)), rec_times, 'r', label='Recursion')
plt.plot(list(range(1, max_N)), dp_times, 'b', label='DP')
plt.xlabel('N')
plt.ylabel('Computation time (seconds)')
plt.legend()
plt.show()
```

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/recursion-dp/rec-vs-dp.png">

As we can see, the computation time for recursion is exponential in $N$, while the dyanmic programming time is linear. Storing the answers to repeated subproblems for later use dramatically decreases the computation time for large $N$. This is the motivation behind dynamic programming - using extra space (in this case a dictionary to store values) to save on time. This time-space tradeoff is an extremely common theme in computer science and one that you will see many times in your career.

We have discussed recursion and how to compute the answers to recursive problems by considering subproblems and using the answers to those subproblems to construct the answer to the current problem. We have also seen how to use extra storage space to save on computation time using dynamic programming. See you all next time!

---

<div class="next-prev-btn-wrapper">
    <button class="next-prev-btn"><a href="{% link tutorials/word_guess.md %}">Previous Lesson</a></button>
    <div></div>
</div>