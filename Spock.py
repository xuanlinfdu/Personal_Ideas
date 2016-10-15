# This program can only work with codesulptor

import random


def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = "name error!"
    return number


def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "number error!"
    return name

def exam_result(player_number, comp_number):
    if comp_number == ((player_number + 1) % 5) or comp_number == ((player_number + 2) % 5):
        result = 0
    elif comp_number == ((player_number + 3) % 5) or comp_number == ((player_number + 4) % 5):
        result = 1
    elif comp_number == player_number:
        result = 2
    else:
        result = 3
    return result



def rpsls(player_choice):
    # introduce names and numbers and exam result
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    result = exam_result(player_number, comp_number)
    
    # print the result
    print "\n"
    print "Player chooses", player_choice
    print "Computer chooses", comp_choice
    if result == 0:
        print "Computer wins!"
    elif result == 1:
        print "Player wins!"
    elif result == 2:
        print "Deuce!"
    else:
        print "Error!"
        

rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")
rpsls("rock")


rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")
rpsls("paper")


rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")
rpsls("Spock")

rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")
rpsls("lizard")

rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")
rpsls("scissors")

    
            
