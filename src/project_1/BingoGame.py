# BingoGame
#
# author: Adam spice
# date: 28.08.19

from random import randint


class Bingo:
    def __init__(self):
        self.bingo_card = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
        self.guesses = []
        self.number_of_hits = 0

    def test(self):
        """Generates random numbers for testing"""
        while self.number_of_hits < 10:
            called_number = randint(0, 100)
            self.handle_choice(called_number)

    def play_game(self):
        """Prompts the user for their choice via input and checks to see if it's valid"""
        while self.number_of_hits < 10:
            # get players choice
            called_number = input("Please enter a number between 1 and 80 ")

            # check to see if called_number is a digit.
            # If it is int it else print invalid choice
            if called_number.isdigit():
                called_number = int(called_number)
                self.handle_choice(called_number)
            else:
                print("invalid choice " + str(10 - self.number_of_hits) + " left to guess")

    def handle_choice(self, called_number):
        """Handles the users or test number to see if it passes the game logic"""

        # check to see if called_number is between 1 and 80
        if called_number not in range(1, 80):
            print("invalid choice " + str(10 - self.number_of_hits) + " left to guess")
        else:
            # look to see if that number has been guessed before
            if called_number not in self.guesses:
                self.guesses.append(called_number)

                # handle if number is in the bingo card
                if called_number in self.bingo_card:
                    self.number_of_hits += 1
                    if self.number_of_hits == 10:
                        print("BINGO!!")
                    else:
                        print("Hit, " + str(10 - self.number_of_hits) + " left to guess")
                else:
                    print("Miss, " + str(10 - self.number_of_hits) + " left to guess")
            else:
                print("You have already tried that number")


x = Bingo()
# This will play the game by generating random numbers between 0 and 100
# it does this so that it will test invalid entries
x.test()

# This will play the game normally
x.play_game()
