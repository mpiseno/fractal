---
layout: module
---

# Hello World

---

## What is Computer Science and Why Should We Care?

Computer Science is, broadly, the study of computing. It is an extremely large field that encompasses many subfields like algorithms, operating systems, web development, artificial intelligence, networking, and so much more. In many respects, computer science and comptuer scientists are responsble for much of the modern technology used every day and tons of exciting new technologies currently in development.

These lessons will largely focus on programming (or coding), a task that is necessary for much of the aforementioned technology. Much of the technology you see on a day to day basic is just code. Of course your phone apps and the screen display are code, but many of the other things in your daily life are too. The elevator buttons you press, your coffee machine settings, the light that turns on and off depending on the position of your refridgerator door - its all just code.

We should care about programming, and computer science more broadly, because it inundates our life and will only become more relevant in years to come. Learning programming opens so many doors, not only in the job market, but also as an stimulating academic interest. There is a plethora of impactful problems and work to be done in this vast field, and it all starts with coding "Hello World".

## Python

Python is the programming language we will use in our lessons. It is becomming one of the most popular programming languages because of its ease of use and it versatility. Python can be used for everything from creating websites to training the most state of the art AI models.

### Downloading Python and an Editor

To start programming in python, we must first download it, just like any other application you might download on your computer. You can download the latest version of python from [the official website](https://www.python.org/downloads/). Make sure you select the correct download for your operaitng system (Windows, Mac, or otherwise). Once it is downloaded, go through the installation instructions by continuing to click continue until Python is installed successfully.

Now open a the terminal if you are using a Mac by pressing (⌘ + Space) and searching for "terminal". If you are on windows, open the home menu and search for "command prompt". The terminal (command prompt) is how you interact with your computer and give it commands to run the programs that you write and many other useful commands. Type "python" in the terminal and press enter. If you see something like the output below, then you've downloaded Python correctly.

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/hello_world/terminal.png">

The python environment above is just an interactive environment inside the terminal where you can run and test python code, but it is not where we will be writing most of our code. You can type "quit()" and press enter to exit this interactive environment.

We will be writing most of our code inside a text editor. Think of it like a Word document, but for code. [Sublime](https://www.sublimetext.com/3) is a simple and easy to use editor. Once it is downloaded, you can open up Sublime and start writing code!

### Hello World

In this section, we will write and run our first Python program. Open up Sublime and create a new file called hello_world.py. Python files are designated with the ".py" file extension. Make sure to save this file in a folder (also called a directory) on your computer that you know. For example, "\~/Desktop/projects/hello_world.py". The "\~" charcter means the home directory on your computer.

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/hello_world/sublime.png">

Now that we created a file in which to write our code, let's write our first program - it will just be 1 line of code! Write the following in the editor and save it.


```py
print('Hello World!')
```

Now open a terminal (or command prompt) and nagivate to the directory where the python file is located. We can do this with the "cd" command, which stands for "change directory". To make sure the file is actually in this directory, we can type "ls" to show the contents of the current directory.


<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/hello_world/terminal_cd.png">

Finally, to run the program we just wrote, type

```
python hello_world.py
```

in the terminal. The first item tells the terminal that we are running a python program, while the second item tells the terminal which python file to actually run. This is how we will run all our programs. You should see the words "Hello World!" print out in the terminal after running the program.


<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/hello_world/terminal_hello_world.png">

Congratulations! You have just written and run your first Python program!


## Python Concepts

In this section, we will explore some important concepts in python that will be the building blocks of your future python programs. In all the following examples, we run the python program in the same way as above in the Hello World section. Feel free to create a new python file to write all these examples in or just read along.

### Primitive Types

Coding deals with numbers, decimals, logic, and words. Every programming language has primitives, the basic building blocks of data. In Python, we can save each of these types of primitives into a variable to be referenced later in our program. The # character can be used to write comments in your code. Anything following the # symbol on the same line will not be treated as code, but as a comment about the code.

In Python, numbers are called ints, variables that hold the value true or false are called bools, word are called strings, and decimals are called floats. When declaring strings, you can either wrap the string in single quotes '' or double quotes "".

```py
# The variable x points to an int of value 5
x = 5

# The variable y points to a float of value 4.523
y = 4.523

# The variable my_string points to a string
my_string = 'hello'

# The variable is_program_running points to a bool of value True
is_program_running = True
```

You can perform certain operations on these primitives. For example the + operator adds ints or floats together. It can also be used to concatentate strings. However you cannot use the + operator to combine an int with a string because the program will error.

```py
# Add an int and a float
z = x + y
print(z)

# Concatenate two strings
hello_world = my_string + ' world'
print(hello_world)

# This errors (try it)!
z2 = x + ' world'
print(z2)
```

Several other operations are defined too. For ints and floats, you can substract -, multiply \*, divide /, integer divide (division with no remainder) //, and exponentiate \*\*. For strings you can use the multiplication operator to concatentate a string multiple times.

```py
# Multiple an int and a float
z = x * y 
print(z)

# Concatenate a string multiple times
greetings = my_string * 10
print(greetings) # prints hellohellohello ... hello
``` 


### Logical Statements

In many of our programs, we want to only execute a portion of code based on some condition. There are three main types of conditional logical statements that we will use.

An if statement executes a portion of code only if the condition of the if statement is met.

```py
x = 5
if x > 4:
    print('x is greater than 4')
```

An if statement can also be combined with an elif statement, which executes its block of code if the if statement condition was not met but the elif condition was met. Finally, you can also specify an else statement which executes if none of the above conditions have been met.

```py
y = 10
if y > 12:
    print('y is greater than 12')
elif y > 9:
    print('y is greater than 9')
else:
    print('y is less than or equal to 9')
```

The next type of conditonal statement is a for loop, which executes its block of code a predetermined number of times. The most simple form of this uses a built-in function of Python called range (we will discuss functions below). The range function returns an iterator over a collection of indices. The code below gives a clear example.

```py
num_iterations = 10
for i in range(num_iterations):
    print('This is iteration ' + str(i))
```

This above code will print out what iteration it is on 10 times. Each iteration, the variable i is set to whatever number iteration we are on, so i is an int. Because i is an int and not a string, we cannot directly concatenate it, which is why we use Python's built-in str function to convert the int i to string form.

The last type of conditonal statement is a while loop, which executes its block of code until its condition is false. While loops can run forever if the condition never becomes false.

```py
i = 0
while i < 10:
    print(i)
    i = i + 1
```

```py
# This while loop runs forever
while True:
    print('This will run forever')
```


### Functions

We have already seen some built-in functions that come with python, namely range and print, but we can also define our own functions that take input parameters and do some computation. This is useful for situations when we might need to reuse the same code several times so we don't have to keep rewriting it. To do this, we use the "def" keyword. To return a value from a function, use the "return" keyword. A function is not required to return a value.

```py
def say_hello(name):
    return 'hello ' + name + '!'

print(say_hello('Michael'))
```

```py
# The ReLU function is defined as 0 if x is negative or 0 and x if x is positive.
# ReLU is used a lot in machine learning.
def ReLU(x):
    if x <= 0:
        return 0
    else:
        return x

output = ReLU(-4) # output points to the value 0
output = ReLU(4) # output points to the value 4
```

Here's a fun example. Functions can actually be passed in as parameters to other functions just like variables. So we can define a function called integrate that approximates the definite integral of another function.

```py
# Computes the square of x
def f(x):
    return x ** 2

def integrate(func, lower_lim, upper_lim):
    num_rectangles = (upper_lim - lower_lim) / 0.05
    delta_x = (upper_lim - lower_lim) / num_rectangles
    area_under_curve = 0
    c = lower_lim
    for i in range(int(num_rectangles)):
        midpoint = (c + delta_x) / 2
        height = func(midpoint)
        area_under_curve = area_under_curve + delta_x * height
        c = c + 2 * delta_x

    return area_under_curve
    

result = integrate(f, 0, 4)
print(result)
```


### Classes

Now for the last topic of this lesson - classes! A class in Python is an object that has certain properties. A class can contain variables and functions that are specific to that class. Usually we create a class to represent some sort of concept or object in our code. We create a class using the "class" keyword. For example:

```py
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, string):
        print('meow!' + ' ' + string)

    def calculate_age_in_months(self):
        return self.age * 12

    def say_name(self):
        self.speak('my name is ' + self.name)

my_cat = Cat('Cloudy', 5)
```

A function within a class is called a method, and we usually refer to it by saying something like "The Cat class's speak method". Notice each method's first parameter must be the keyword "self", which indicates that the method belongs to this class. The \_\_init\_\_ method is an optional method that specifies the behavior when we make an instance of (or instantiate) the class. So in our example, when we instantiate the Cat class, we set class variables called self.name and self.age.

We can now use these methods with the instance of the class we created in the following way.

```py
my_cat = Cat('Violet', 3)

# prints "meow! you are in my spot."
my_cat.speak('you are in my spot.')

my_cat.say_name()
months_old = my_cat.calculate_age_in_months()
```

In the next lesson, we will explore data structures, which are implemented as different classes in python. For example, a list in python is a data structures that holds a collections of values. Because under the hood it is just a class, it has certain methods that we can call on it.

That's all for now. See you in the next lesson!

---

<div class="next-prev-btn-wrapper">
    <!-- <button class="next-prev-btn">Previous Lesson</button> -->
    <div></div>
    <button class="next-prev-btn"><a href="{% link tutorials/data_structures.md %}">Next Lesson</a></button>
</div>

