#Step 4

import random, hangman_art, hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

logo = hangman_art.logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):          # or for _ in range(len(chosen_word)):
    display += "_"            #or display += "_"

while not end_of_game:       #or while end_of_game is == to False
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True

    if guess not in chosen_word:
        print(f"Your guess is: '{guess}', and it is not in the word")


    #join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")

    stages = hangman_art.stages
    print(f"You have {lives} lives remaining")
    print(stages[lives])
    if lives == 0:
        print("You Lose")

