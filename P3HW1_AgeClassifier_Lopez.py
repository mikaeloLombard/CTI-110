# CTI-110 
# P3HW1 - Age Classifier 
# Miguel Lopez 
# 3/10/2018
#

def main():
    print("Welcome to Age Classifier")
    print(" ")
    # Get input from user
    age=int(input("Enter the person's age: "))
    print(" ")

    # Calculate what age range is the person

    if age ==1 or age < 1:
        print("This person is an infant!")

    else:
        if age > 1 and age < 13:
            print("This person is a child!")

        else:
            if age >=13 and age < 20:
                print("This person is a teenager!")
                
            else:
                if age >= 20:
                    print("This person is an adult!")

main()

                
                
