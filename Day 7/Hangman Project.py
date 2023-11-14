

#Step 1

world_list = ["ardvark","baboon","camel"]

#TODO-1 - randomly choose a word from the world_list and assign it to the variable called chosen word.
import random
chosen_word = random.choice(world_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guesses lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen word.
guesses = []
for letter in chosen_word :
    if letter == guess:
        print("Right")
    else:
        print("Wrong")