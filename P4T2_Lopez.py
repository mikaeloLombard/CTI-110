# CTI-110 
# P4T2
# Miguel Lopez 
# 3/25/2018
#


def main():
    print("Welcome to Bug Collector Calculator")
    print(" ")

    # Initialize the accumulator

    total=0

    # Get the number of dogs for each day

    for day in range(1,8):
        # Prompt the user
        print("Enter the bugs collected on day", day)

        # Get input from user
        bugs = int(input())

        # Add number of bugs to total
        total = total + bugs

    # Display total of bugs.

    print("You collected a total of", total, "bugs.")
    


    
    
    
    













main()


