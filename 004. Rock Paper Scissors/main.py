import random
from choice import rock, paper, scissors

#turn the ASCII images into a list
rpsChoice = [rock, paper, scissors]
#input player choice of rps
playerChoice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#randomize the computer choice
computerChoice = random.randint(0, 2)

if playerChoice >= 3 or playerChoice < 0:
  print("You input an invalid number. You lose!")
else:
  #print result
  print(rpsChoice[playerChoice])
  print("Computer chose:")
  print(rpsChoice[computerChoice])
  #result ifs
  if playerChoice == 0 and computerChoice == 1:
    print("You lose!")
  elif playerChoice == 0 and computerChoice == 2:
    print("You win!")
  elif playerChoice == 1 and computerChoice == 0:
    print("You win!")
  elif playerChoice == 1 and computerChoice == 2:
    print("You lose!")
  elif playerChoice == 2 and computerChoice == 0:
    print("You lose!")
  elif playerChoice == 2 and computerChoice == 1:
    print("You win!")
  elif playerChoice == computerChoice:
    print("You drew!")
    
