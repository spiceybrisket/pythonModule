# RockPaperScissors.py
#
# author: Adam spice
# date: 28.08.19


from random import randint

# create a dictionary of play options
available_chices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors",
    "e": "Exit"
}

# assign a random play to the computer
random_number = randint(0, len(available_chices) - 2)
computer = available_chices[list(available_chices)[random_number]]

# set player to False
player = False

while not player:
    # get players choice
    player_input = raw_input("""
    Please enter a choice from the following:
    
    Press r for Rock,
    Press p for Paper
    Press s for Scissors
    Press e to Exit
    
    """)
    # lookup players input in dictionary
    player = available_chices[player_input]

    if player == "Exit":
        print("Bye bye")
        break
    else:
        print "Player chooses %s, computer chooses %s " % (player, computer)

        if player == computer:
            print("Tie!")

        elif player == "Rock":
            if computer == "Paper":
                print "You lose! %s covers %s" % (computer, player)
            else:
                print "You win! %s smashes %s" % (player, computer)

        elif player == "Paper":
            if computer == "Scissors":
                print "You lose! %s cut %s" % (computer, player)
            else:
                print "You win! %s covers %s" % (player, computer)

        elif player == "Scissors":
            if computer == "Rock":
                print "You lose... %s smashes %s" % (computer, player)
            else:
                print "You win! %s cut %s" % (player, computer)
        else:
            print("That's not a valid play. Check your spelling!")

    # set player to False so the loop continues
    player = False
