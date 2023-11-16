#Step 3

import random
world_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(world_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):          # or for _ in range(len(chosen_word)):
    display += "_"            #or display += "_"
print(display)

#TODO-1: - Use a while loop to let the user guess again
# The loop should only stop once the user has guessed
# all the letters in the chosen_word and 'display'
# has no more blanks ("_"). Then you can tell the user they've won

guess = input("Guess a letter: ").lower()

#Check guessed letter
for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter} \n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

print(display)