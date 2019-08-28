# GradeCalculator
#
# author: Adam spice
# date: 28.08.19


def test():
    """Uses the below test assertions to test the Grade Calculator"""
    print("Test assertions starting\n")
    calculate_total_score(78, 65)
    calculate_total_score(22, 15)
    calculate_total_score(99, 99)
    print("\n")
    print("Test assertions complete\n")


def get_grade():
    """Prompts the user for their results"""
    project = int(input("Please enter you project result: ").strip(" %"))
    exam = int(input("Please enter you exam result: ").strip(" %"))
    calculate_total_score(project, exam)


def calculate_total_score(project, exam):
    """Calculates the users final score"""
    final_score = (project + exam) * 0.5
    display_grade(final_score)


def display_grade(final_score):
    """determines the uses final grade and displays it"""
    if final_score <= 49:
        grade = "Fail"
    elif final_score in range(50, 59):
        grade = "D"
    elif final_score in range(60, 69):
        grade = "C"
    elif final_score in range(70, 79):
        grade = "B"
    else:
        grade = "A"

    print("Your total score is " + str(final_score) + "% and your grade is a " + grade)


# To run the below test assertions run test() else run get_grade()
test()
get_grade()

'''
test assertion 1
project = 78
exam = 65
final score should = 71.5
grade should = B
'''

'''
test assertion 2
project = 21
exam = 15
final score should = 18.5
grade should = Fail
'''

'''
test assertion 3
project = 99
exam = 99
final score should = 99
grade should = A
'''
