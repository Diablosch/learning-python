import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

#Choose a word from the list and determine its length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Beginning state of the game
end_of_game = False
lives = 6

#Import logo from hangman_words.py
print(logo)

#Create blanks and print for clue
display = []
for _ in range(word_length):
    display += "_"
print("")
print(display)
print("")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win! Good job!")

    #Import the stages from hangman_art.py
    print(stages[lives])