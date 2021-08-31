from replit import clear
from art import logo

print(logo)
bidders = {}

def find_highest_bidder(bidding_players):
  highest_bid = 0
  winner = ""
  for bidder in bidding_players:
    bid_amount = bidding_players[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

con_bool = True
while con_bool:
  name = str(input("What is your name?: "))
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  con_input = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if con_input == "yes":
    con_bool = True
    clear()
  elif con_input == "no":
    con_bool = False
    clear()
    find_highest_bidder(bidders)
