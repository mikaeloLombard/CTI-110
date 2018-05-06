# CTI-110 
# P4HW2 - Running total
# Miguel Lopez 
# 3/25/2018
#

def main():
    # Set variables
    total = 0
    
    numb = float(input("Enter a number? "))

    count = 0
    
    # Formula and loop
    
    while numb > -1 :
            
        total = total + numb
        numb = float(input("Enter a number? "))
        
    print(" Total: ", total)
    
                    
                    


main()
        
        


