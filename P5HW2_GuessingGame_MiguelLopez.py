# Is a guess the number game that guides you unyil you get right number
# 4/22/18
# CTI-110 P5HW2 - Random Number Guessing Game
# Miguel Lopez
#

# Imports random module
import random

def main():
    n = random.randint(1, 100)
    guess = int(input("Enter a number from 1 to 100: "))
    while n != "guess":
        print
        if guess < n:
            print ("guess is low")
            guess = int(input("Enter an integer from 1 to 100: "))
        elif guess > n:
            print ("guess is high")
            guess = int(input("Enter an integer from 1 to 100: "))
        else:
            print ("Congratulations! You guessed it!")
        
            restart = input("Would you like to restart the game? ")
            if restart == "yes" or restart == "y":
                 main()
            if restart == "n" or restart == "no":
                print ("See you soon. Goodbye!")
                break

         
main()




