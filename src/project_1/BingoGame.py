# BingoGame
#
# author: Adam spice
# date: 28.08.19


def play_game():
    bingo_card = [7, 26, 40, 58, 73, 14, 22, 34, 55, 68]
    guesses = []
    number_of_hits = 0

    # while the number of hits is less than 10 loop
    while number_of_hits < 10:

        # get players guess
        called_number = int(input("Please enter a number between 1 and 80 "))

        # look to see if that number has been guessed before
        if called_number not in guesses:
            guesses.append(called_number)

            # handle if number is in the bingo card
            if called_number in bingo_card:
                number_of_hits += 1
                print("Hit, " + str(10 - number_of_hits) + " left to guess")
            else:
                print("Miss, " + str(10 - number_of_hits) + " left to guess")
        else:
            print("You have already tried that number")

    # print bingo and end once 10 hits
    print("BINGO!!")

#te7st
play_game()
