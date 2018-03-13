# CTI-110 
# P3T1 - Calculate the area of a rectangle and will tell which has a
# greater area or if they are equal
# Miguel Lopez 
# 3-4-18
#

def main():
    print("Welcome to Area of two Rectangles Calculator")
    print(" ")
    print("Enter the measures of two rectangles "+\
          "and the calculator compare the data.")
    print(" ")
    
    # Get input from user for rectangle 1
    print("First rectangle:")
    width=float(input("Enter the width: "))
    height=float(input("Enter the height: "))
    area = width * height

    # Show the area of the first rectangle

    print("The are of the first triangle is: ", format(area, ',.2f'))


    # Get input from user for rectangle 1
    print("  ")
    print("Second rectangle:")
    width2=float(input("Enter the width: "))
    height2=float(input("Enter the height: "))
    area2 = width2 * height2

    # Show the area of the first rectangle

    print("The are of the second triangle is: ", format(area2, ',.2f'))

    # Calculate which has a higher area or if they are equal

    if area > area2:
        print("The first rectangle has the larger area!")

    else:
        if area < area2:
            print("The second rectangle has the larger area!")
        else:
            print("Both rectangles have equal area!")

    

    

        


    

main()

    
