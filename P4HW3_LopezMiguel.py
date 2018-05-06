# CTI-110 
# P4HW3 - Factorial
# Miguel Lopez 
# 3/25/2018
#

def main():

    # Get integer from user

    userInt= int(input("Enter a nonnegative integer? "))
    
    
    # while loop

    while userInt < 1:
        userInt= int(input("Enter a nonnegative integer? "))

    factorial = 1

    for numb in range(1, userInt + 1):
        factorial = factorial * numb

    print("The factorial of ", userInt, "is ", format(factorial , ',.1f'))
    
        
        
    
    
    
    
                    
                    


main()
        
        


