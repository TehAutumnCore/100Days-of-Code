#Step 2

import random
world_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(world_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1 - Create an empty List called display.
#for each letter in the chosen_word, add a "-" to 'display'.
#So if the chosen_word was "apple", display should be ["_","_","_","_","_",] with 5 "_" representing each
#letter to guess.

guess = input("Guess a letter: ").lower()

#TODO-2 - Loop through each position in the chosen_word;
#If the letter at that position matches 'guesses' then reveal that letter in thh display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_",]

guesses = []
for letter in chosen_word :
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#TODO-3 - Print 'display' and you should see the guessed
#letter in the correct position and every other letter replace "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

