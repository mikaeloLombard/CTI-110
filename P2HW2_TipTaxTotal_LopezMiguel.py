# CTI-110 
# P2HW2 - Tip Tax Total 
# Miguel Lopez
# 2/18/2018
#


# Welcome
print(" Welcome to Total Cost of Your Meal Calculator")

# Get input from user

foodCost = float(input("What is the cost of the meal? "))

# Display tip amount
tipAmount = float(foodCost * .18)
print("The tip amount is: $", format(tipAmount , ',.2f'))

# Display sales tax

salesTax = float(foodCost * .07)
print("The sales tax is: $", format(salesTax, ',.2f'))

# Display the total cost of the meal
totalCost = float(foodCost + tipAmount + salesTax)
print("The total cost of the meal is: $", format(totalCost, ',.2f'))





