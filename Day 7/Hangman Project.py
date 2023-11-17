#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
world_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(world_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):          # or for _ in range(len(chosen_word)):
    display += "_"            #or display += "_"

while not end_of_game:       #or while end_of_game is == to False
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #then reduce 'lives' by 1.
    #if lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    #join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(f" You have {lives} lives remaining")
    print(stages[lives])
    if lives == 0:
        print("You Lose")

