# CTI-110 
# P3HW2 - Software Sales
# Miguel Lopez 
# 3/11/2018
#

def main():
    price=float(99.0)
    print("Welcome to Software Sales Discount Calculator")
    print(" ")

    # Get input from user
    numItems=float(input("Enter the number of items: "))
    print(" ")

    # Calculate discount and display total

    if numItems ==0 or numItems < 10:
        print("Sorry, there is NO discount with this number of items !")
        print("Your total is: $ :",price * numItems)

    else:
        if numItems >= 10 and numItems <= 19:
            total=float(price * numItems)
            total2=(total * 0.10)
            total3=(total - total2)
            print(format(total, ',.2f'))
            print("Your discount is 10% or: $ ", format(total2, ',.2f'))
            print("Your total is: $ ", format(total3, ',.2f'))
            

        else:
            if numItems >=20 and numItems <= 49:
                total=float(price * numItems)
                total2=(total * 0.20)
                total3=(total - total2)
                print(format(total, ',.2f'))
                print("Your discount is 20% or: $ ", format(total2, ',.2f'))
                print("Your total is: $ ", format(total3, ',.2f'))
            
                
            else:
                if numItems >=50 and numItems <= 99:
                    total=float(price * numItems)
                    total2=(total * 0.30)
                    total3=(total - total2)
                    print(format(total, ',.2f'))
                    print("Your discount is 30% or: $ ", format(total2, ',.2f'))
                    print("Your total is: $ ", format(total3, ',.2f'))

                else:
                    if numItems >=100:
                        total=float(price * numItems)
                        total2=(total * 0.40)
                        total3=(total - total2)
                        print(format(total, ',.2f'))
                        print("Your discount is 40% or: $ ", format(total2, ',.2f'))
                        print("Your total is: $ ", format(total3, ',.2f'))

        
            
main()
