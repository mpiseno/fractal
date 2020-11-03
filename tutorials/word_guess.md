---
layout: module
---

# Project: Word Guessing Game

---

This is the first time we will combine many of the previously learned skills to produce a fully functional program that does something non-trivial. We will be making a word guessing game! You are engouraged to try to implement the game on your own before looking at the solution that we provide - this is the best way for you to learn! You can download a sample csv of words from <a href="{{ site.baseurl }}/tutorials/assets/words.csv">here</a>, but feel free to add your own words.

### The Rules

The program should read in words from a csv file and then randomly choose one of the words for the player to guess. The player should get a maximum of 6 incorrect guesses to complete the word, where each guess consists of a single character. The program will display blanks representing the length of the word. At any point in the game the player should be able to guess the full word (not just a single character). Guessing the full word incorrectly should also decrement the number of guesses remaining.

If the character guesses a character correctly, the number of guesses does not decrement. Upon guessing correctly, the blanks corresponding to that letter should be filled in for the player to view.

If the player guesses incorrectly, the number of guesses remaining gets decremented and the program should display the incorrect characters previously guessed at each step.

When the game ends the program should print out whether the player won or lost. The complete program should look something like the following.

<img class="lesson-img" src="{{site.baseurl}}/imgs/lesson_imgs/word_game/word_game.png">

Hints:

1. Use a data structure to keep track of which characters were guessed already
2. The "break" keyword can be used to immediately exit a loop
3. Break up the logic into different functions to write more manageable code

### Input

In order to take user input you need to know about an additional built-in function in Python called input, which takes input from the terminal and saves it to a string variable.

```py
# After the below line executes and the users types in something and presses enter,
# the variable x will be a string of the user's input.
x = input()
```

### Solution

First, we need to import the necessary libraries and read in the words from the csv.

```py
import csv
import random
import time

# Create a list of all the possible words for the game
words = []
with open('words.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        word = row[0]
        words.append(word)
```

Next we will set up the game by asking for the user's name and selecting a word at random to choose. We will also represent the guessed word as a list of characters, which initially is just a bunch of blank '\_' characters.

```py
# Game setup
print('Hi! What is your name?')
name = input() # Grab the user's name
print(f'Hello {name}. Let\'s play a guessing game...')
print('Thinking of a word...')
word = random.choice(words)
time.sleep(5) # This just pauses the program for 5 seconds
print('Got it!\n')

# Create a blank slate for the user to start with that looks something like
# ['_', '_', '_', '_', '_', '_']
guessed_word = []
for character in word:
    if character == ' ':
        guessed_word.append(' ')
    else:
        guessed_word.append('_')
```

We want to keep track of how many guesses the user has so far, the max guesses allowed, and the set of characters that the users has already guessed. Additionally, we define a helper function to handle the logic of finding matching characters in the target word for the guess that the user made.

```py
# Start the game
num_guesses = 0
MAX_GUESSES_ALLOWED = 6
letters_guessed = set()

# Helper function to handle guesses
def handle_guess(correct_word, guess):
    '''
    Returns false if the user guessed an incorrect word, and true otherwise.
    '''

    # If the guess is already in the set of inocrrect characters, we return false
    # immediately
    if guess in letters_guessed:
        return False

    # Find the indices that match the guess
    indices = []
    for i in range(len(correct_word)):
        if correct_word[i] == guess:
            indices.append(i)

    # Replace the '_' characters with the correct guess character
    for correct_idx in indices:
        guessed_word[correct_idx] = guess

    return len(indices) > 0
```

Finally, the actual game loop. We want to loop for user input until either we run out of guesses or the user has guessed the correct word. At the beginning of each step, we print out the current state of the game and some useful information as well as ask for the user input.

```py
current_state = ''.join(guessed_word)
while current_state != word and num_guesses < MAX_GUESSES_ALLOWED:
    print('\n' + current_state +
        f'\tIncorrect guesses: {list(letters_guessed)}' +
        f'\tRemaining guesses: {MAX_GUESSES_ALLOWED - num_guesses}')
    print('What is your guess?')
    guess = input()

    # If the player guessed the whole word
    if len(guess) > 1:
        if guess == word:
            current_state = guess
            break

        num_guesses += 1
    else:
        correct = handle_guess(word, guess)

        if not correct:
            letters_guessed.add(guess)
            num_guesses += 1

    current_state = ''.join(guessed_word)


if current_state == word:
    print('You won!')
else:
    print('You lost...')
```

That's it! To recap, we used a set data structure to keep track of the currently guessed characters, we used a helper function to handle the logic of updating the current game state, and we used our knowledge of libraries and logical statements to encode the game logic. The full code can be downloaded <a href="{{ site.baseurl }}/tutorials/assets/word_game.py">here</a>.

Congratulations! You've just written your first game that utilized many of the skills we have learned. In future lessons we will explore concepts like those in the previous lesson but in more detail and with newer material. Until then keep practicing and try to make even more interesting programs!

---

<div class="next-prev-btn-wrapper">
    <button class="next-prev-btn"><a href="{% link tutorials/libraries.md %}">Previous Lesson</a></button>
    <button class="next-prev-btn"><a href="{% link tutorials/recursion-dp.md %}">Next Lesson</a></button>
</div>