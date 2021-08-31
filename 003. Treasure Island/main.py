from images import chest, dragon

print(dragon)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("")

first = input("You look around the beach and found an opening to a forest.\nYou walk there, curious as to where it may lead.\nAs you come closer to the opening, you found two pathways.\nShould you go to the left one or the right one? Left or Right?\n")

lowerfirst = first.lower()

if lowerfirst == "left":
  second = input("You picked the left route. Everything seems okay so far.\nAs you walk further, you found a narrow river, cutting you off from a cave.\nShould you swim across the narrow river or wait for a bit? Swim or Wait?\n")

  lowersecond = second.lower()

  if lowersecond == "wait":
    third = input("As you wait and look around for a bit, you see a plank, hidden behind a tree.\nYou take the plank and use it as a bridge to get to the cave.\nAs you walk closer to the cave, you see three doors, red and blue and yellow.\nWhich door will you open? Red, Blue, or Yellow?\n")

    lowerthird = third.lower()
    
    if lowerthird == "blue":
      print(chest)
      print("You open the blue door. There it is, a chest. You open it and found a scroll.\nYou read the scroll. 'It is not about the treasure, but it is about the friends we make along the way'.\nPissed, you throw the scroll away and go back to the ship.\nYou win! Thank you for playing!")

    elif lowerthird == "red":
      print("You open the red door. All of a sudden, fire shoot out of the door, burning you and your beautiful face.\nYou died. Game over.")

    elif lowerthird == "yellow":
      print("You open the yellow door. A beast pounced at you, ripping half of your beautiful face.\nYou died from blood loss. Game over.")

    else:
      print("Instructions unclear. You don't know what you're doing. You died from starvation.\nGame over.")

  elif lowersecond == "swim":
    print("You try swimming across the narrow river. Unbeknownst to you, the trouts in the river likes human flesh.\nYou died from being eaten. Game over.")

  else:
    print("Instructions unclear. You don't know what you're doing.\nYou died from starvation. Game over.")

elif lowerfirst == "right":
  print("The pathway to the right is very dark. Nevertheless, you are a brave adventurer, aiming for fame and fortune. You walk several steps ahead, fell into a hole, broke several bones, and cannot escape.\nYou died. Game over.")

else:
  print("Instructions unclear. You don't know what you're doing.\nYou died from starvation. Game over.")

