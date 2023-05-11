import sys
import os
import random

# Import whatever other libraries you need

# G and Y represent text formatting codes for green and
# yellow text output. Variable names are brief so as to
# be unobtrusive when interspersed with text
G = '\x1b[0;30;42m'  # green text
Y = '\x1b[0;30;43m'  # yellow text
N = '\x1b[0m'        # normal text/no highlighting
os.system("")
ALLOWED_GUESSES = 6
WORD_LENGTH = 5


def main(args):
    # TODO: If there is an argument, set that argument to be the word.
    # Otherwise, the word should be randomly selected from valid
    # letters of WORD_LENGTH in the Scrabble words file. (Use a
    # separate function to get the valid words from the
    # Scrabble words files)

    lineList = get_valid_words(WORD_LENGTH)

    if len(args) > 1:
        secretWord = args[1].upper()
    else:
        secretWord = random.choice(lineList)

    # TODO: Study the following string to underestand how G, Y and N
    # behave for colored text highlights
    print(f"Welcome to {Y}PY{G}WOR{Y}D{G}LE{N}!")

    # TODO: You'll want a list to collect failed guesses. You can use
    # this list to print the guesses each time, and also use
    # the list's length to keep track of how many guesses have
    # been made
    preGuesses = []
    guessWord = ""
    tryCount = len(preGuesses)

    # TODO: You'll probably want a while loop to continue as long
    # as the user's answer is not correct and the guesses are
    # fewer than the allowed number of guesses.
    while guessWord != secretWord and tryCount < ALLOWED_GUESSES:
        tryCount += 1
        guessWord = input('Enter your guess (5 letters):\n').upper()

    # TODO: You may want yet another while loop to repeat the prompt
    # in case of invalid guesses
        while guessWord not in lineList or len(guessWord) != WORD_LENGTH:
            guessWord = input('Enter your guess (5 letters):\n').upper()
        preGuesses.append(guessWord)

    # TODO: Use a separate function, format_guess, to format
    # the guess with green and yellow highlighting for printing out.
    # That's where you'll compare it to the correct word.
    # TODO: Print out the list of guesses so far with each new guess
        for i in preGuesses:
            print('\t'*2, format_guess(secretWord, i))

    # TODO: Print an appropriate message when the game ends
    if guessWord == secretWord:
        print(f"Congrats You got it in {len(preGuesses)} tries")
    else:
        print(f"Sorry the word was {secretWord}")


def format_guess(x, y):  # TODO: Add necessary parameters

    # TODO: Implement this function so that it returns
    # the guess string highlighted with green and yellow based
    # on comparing letters with the original word.

    # See assignment instructions for specifics about how
    # letters should be highlighted
    secret_word = list(x.upper())
    guess = list(y.upper())

    for i in range(len(secret_word)):
        if secret_word[i] == guess[i]:
            guess[i] = G + guess[i] + N
            secret_word[i] = '_'
        elif guess[i] in secret_word:
            char = guess[i]
            guess[i] = Y + guess[i] + N
            secret_word["".join(secret_word).find(char)] = "_"

    return "".join(guess)


def get_valid_words(LENGTH):  # TODO: Add necessary parameters

    # TODO: Implement this function so that it returns
    # a list of words consisting of only words of the
    # correct length from the Scrabble word list
    res = []

    with open('Collins Scrabble Words (2019).txt') as w:
        for word in w.read().split():
            if (len(word) == LENGTH):
                res.append(word)
    return res


main(sys.argv)
