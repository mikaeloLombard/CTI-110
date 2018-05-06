# Gives average and grade
# 4/21/2018
# CTI-110 P5HW1 - Test Average and Grade
# Miguel Lopez
#


# This function takes input from the user, turns it into float with variable num
# Also divides the scores using split with a comma
def main():
    print("Welcome to average and grade calculator")
    scores = input("Enter five test scores separated by commas: ")
    return [float(num) for num in scores.split(",")]

# This function determines the letter grade using if, elif, or else
def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

# This function calculates the avarage of of the grades
# by adding all grades (sum(grades)) and dividing by
# the quantity of grades (len(grades))
# Also, uses the function determine_grade passing the avarage variable
# to calculate the overall grade. Finally it prints the result for the user
def calc_average(numGrades):
    average = sum(numGrades) / len(numGrades)
    letter_grade = determine_grade(average)
    print("The average is: {:.1f} which is {}".format(average, letter_grade))

# This Function shows the number and letter grade for each entry 
def show_num_letter(num, letter_grade):
    print("{:.1f} is {}\n".format(num, letter_grade))


lst = main()
for n in lst:
    show_num_letter(n, determine_grade(n))
calc_average(lst)
