# CTI-110 
# P2T1 - Sales Prediction 
# Miguel Lopez
# 2/18/2018
#

print("Welcome to Sales Predictiton Calculator")
# Get the projected total sales from user
totalSales = float(input("Enter the projected amount of total sales number:  "))

# Calculate the profit as 23 percent of the total sales
annualProfit = (totalSales * .23)

# Display the profit to user
print("The annual profit is: $ ", format(annualProfit, ',.2f'))






