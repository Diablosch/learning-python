# Welcome message
print("Welcome to the tip calculator!")

# Asking for input from users
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? (without %) ")
split = input("How many people to split the bill? ")

# Calculations for the tip
# Float is used due to possibility of the tip being decimal numbers
bill_with_tip = float(bill) * (1 + float(tip) / 100)
split_bill = round(bill_with_tip / int(split), 2)
split_bill_format = "{:.2f}".format(split_bill)

# Output meesage 
print(f"Each person should pay: ${split_bill_format}")