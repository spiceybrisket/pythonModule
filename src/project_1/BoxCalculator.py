# GradeCalculator
#
# author: Adam spice
# date: 27.08.19


class BoxCalculator:
    def __init__(self):
        self.big = 5
        self.medium = 3
        self.small = 1

    def test(self):
        """Tests the functionality of the box calculator"""
        print("starting test assertions")
        number_to_test1 = 48
        number_to_test2 = 4
        number_to_test3 = 195487945116
        self.calculate_boxes(number_to_test1)
        self.calculate_boxes(number_to_test2)
        self.calculate_boxes(number_to_test3)
        print("test assertions complete\n")

    def calculate_boxes(self, number_of_items=0):
        """Calculates the number of boxes required to pack the number of items supplied"""
        # determine the number of big boxes will be needed and any remainder
        big_used = int(number_of_items / self.big)
        remainder = number_of_items % self.big

        # determine the number of medium boxes needed and any remainder
        if remainder < 3:
            med_used = 0
        else:
            med_used = int(remainder / self.medium)
            remainder = remainder % self.medium

        # determine the number of small boxes needed and any remainder
        if remainder < 1:
            sml_used = 0
        else:
            sml_used = int(remainder / self.small)

        self.print_output(sml_used, med_used, big_used, number_of_items)

    def print_output(self, sml_used, med_used, big_used, number_of_items):
        """Formats and outputs the results"""
        # handle plural of box correctly
        if sml_used == 1:
            box_text = "box"
        else:
            box_text = "boxes"

        # cast to string for better outputting
        total_used = str(big_used + med_used + sml_used)
        sml_used = str(sml_used)
        med_used = str(med_used)
        big_used = str(big_used)

        print("\r")
        # show the number of each box type
        print(
            "To pack " + str(number_of_items) + " items you need to use " +
            big_used + " big, " + med_used + " medium and "
            + sml_used + " small " + box_text)
        print("\r")
        # show the total number of boxes needed
        print("Total number of boxes needed is:" + total_used)


x = BoxCalculator()

# This will test the calculator using the below assertions
x.test()

# This will run the calculator normally. Must include number of items
x.calculate_boxes()

'''
test assertion 1
number_of_items = 48
big = 9
med = 1
small = 0
total_used = 10
'''

'''
test assertion 2
number_of_items = 4
big = 0
med = 1
small = 1
total_used = 2
'''
'''
test assertion 3
number_of_items = 195487945116
big = 39097589023
med = 0
small = 1
total_used = 39097589024
'''
