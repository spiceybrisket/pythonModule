# GradeCalculator
#
# author: Adam spice
# date: 28.08.19


def test():
    print("Test assertions starting\n")
    print('''
    test assertion 1
    project = 78
    exam = 65
    final score should = 71.5
    grade should = B
    ''')
    print("Test 1 result:")
    calculate_total_score(78, 65)

    print('''
    test assertion 2
    project = 21
    exam = 15
    final score should = 18.5
    grade should = Fail
    ''')
    print("Test 2 result:")
    calculate_total_score(22, 15)

    print('''
    test assertion 3
    project = 99
    exam = 99
    final score should = 99
    grade should = A
        ''')
    print("Test 3 result:")
    calculate_total_score(99, 99)
    print("\n")
    print("Test assertions complete\n")


def get_grade():
    project = int(input("Please enter you project result: ").strip(" %"))
    exam = int(input("Please enter you exam result: ").strip(" %"))
    calculate_total_score(project, exam)


def calculate_total_score(project, exam):
    final_score = (project + exam) * 0.5
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


# test case assertion 3
'''
project = 99
exam = 99
final score should = 99
grade should = A
'''

# To run the above test assertions run test() else run get_grade()
test()
get_grade()
