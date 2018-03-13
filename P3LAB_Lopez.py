# CTI-110 
# P3LAB- Debug
# Miguel Lopez 
# 3/11/2018
#


def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 0
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score and score < A_score:
             print('Your grade is: B')
        else:
            if score >= C_score and score < B_score:
                print('Your grade is: C')
            else:
                if score >= D_score and score < C_score:
                    print('Your grade is: D')
                
                else:
                    if score >= F_score and score < D_score:
                        print('Your grade is: F')
                    
                    else:
                        print("Your entry is not valid!")







# program start
main()
