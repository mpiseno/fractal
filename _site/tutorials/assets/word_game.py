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




