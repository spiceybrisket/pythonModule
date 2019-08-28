# GradeCalculator
#
# author: Adam spice
# date: 28.08.19


def test():
    calculate_total_score(78, 65)
    calculate_total_score(22, 15)
    calculate_total_score(99, 99)


def get_grade():
    project = int(input("Please enter you project result: "))
    exam = int(input("Please enter you exam result: "))
    calculate_total_score(project, exam)


def calculate_total_score(project, exam):
    final_score = (project + exam)*0.5
    display_grade(final_score)


def display_grade(final_score):
    if final_score <= 49:
        grade = "Fail"
    elif (final_score >= 50) and (final_score <= 59):
        grade = "D"
    elif (final_score >= 60) and (final_score <= 69):
        grade = "C"
    elif (final_score >= 70) and (final_score <= 79):
        grade = "B"
    else:
        grade = "A"

    print("Your total score is " + str(final_score) + "% and your grade is a " + grade)


# test case assertion 1
'''
project = 78
exam = 65
final_score = 71.5
grade = B
'''

# test case assertion 2
'''
project = 21
exam = 15
final_score = 18.5
grade = Fail
'''

# test case assertion 3
'''
project = 99
exam = 99
final_score = 99
grade = A
'''


# To run the above test assertions run test() else run get_grade()
test()
