# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    if(number==0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        return 'invalid input'

    
def name_to_number(name):
    if(name=='rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        return 'invalid input'

def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    if(player_number == comp_number):
        rpsls(name)
        return 0;
    elif(player_number == 0):
        if(comp_number == 3 or comp_number == 4):
            temp = 'Player'
        elif(comp_number == 1 or comp_number == 2):
            temp = 'Computer'
    elif(player_number == 1):
        if(comp_number == 4 or comp_number == 0):
            temp = 'Player'
        elif(comp_number == 3 or comp_number == 2):
            temp = 'Computer'
    elif(player_number == 2):
        if(comp_number == 0 or comp_number == 1):
            temp = 'Player'
        elif(comp_number == 3 or comp_number == 4):
            temp = 'Computer'
    elif(player_number == 3):
        if(comp_number == 1 or comp_number == 2):
            temp = 'Player'
        elif(comp_number == 4 or comp_number == 0):
            temp = 'Computer'
    elif(player_number == 4):
        if(comp_number == 2 or comp_number == 3):
            temp = 'Player'
        elif(comp_number == 0 or comp_number == 1):
            temp = 'Computer'
        
    print 'Player chooses ',number_to_name(player_number),player_number
    print 'Computer chooses ',number_to_name(comp_number) ,comp_number
    print temp,' wins!\n'
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


