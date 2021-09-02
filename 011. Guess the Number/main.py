from art import logo
from replit import clear
import random

def play_game():
  # Include an ASCII art logo.
  print(logo)

  # Welcome message to the user
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  # Establish the number to guess by the player and game condition
  number = random.randint(1, 100)
  is_game_over = False

  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    num_of_guess = 10
  else:
    num_of_guess = 5

  # Allow the player to submit a guess for a number between 1 and 100.
  while not is_game_over:

    # Track the number of turns remaining.
    if num_of_guess > 0:
      print(f"You have {num_of_guess} attempts remaining to guess the number")
      guess = int(input("Make a guess: "))

      # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
      if guess > number:
        print("Too high.")
        num_of_guess -= 1
      elif guess < number:
        print("Too low.")
        num_of_guess -= 1
      
      # If they got the answer correct, show the actual answer to the player.
      elif guess == number:
        print(f"You got it! The answer was {number}.")
        is_game_over = True
      else:
        is_game_over = True
    
    # If they run out of turns, provide feedback to the player. 
    else:
      print(f"You've run out of guesses, you lose.")
      is_game_over = True

  if input("Would you like to play the game again? Enter 'y' or 'n': ") == "y":
    clear()
    play_game()

play_game()