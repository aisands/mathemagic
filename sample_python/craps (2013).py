#-------------------------------------------------------------------------------
# Name:        craps.py
# Purpose:	simulates multiple games of craps
#
# Author:      Adrienne Sands
#
# Created:     05/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randrange
def main():
    print("This program simulates multiple games of craps and estimates win probability.")
    numGames = eval(input("How many games do you want to simulate? "))
    wins=simulateNCraps(numGames)
    printSummary(wins,numGames)

def simulateNCraps(numGames):
    wins = 0
    for i in range(numGames):
        if simulateOneCraps(): wins = wins + 1
    return wins

def simulateOneCraps():
    #simulates one game of craps
    #returns false if player loses
    #returns true if player wins

    roll = randrange(1,13)
    if roll in [2,3,12]: return False
    elif roll in [7,11]: return True
    else:
        reroll = 0
        while reroll not in [7,11]:
            reroll = randrange(1,13)
            if reroll == 7: return False
            elif reroll == roll: return True

def printSummary(wins,numGames):
    print("You won {0} games ({1:0.1%})".format(wins,wins/numGames))

if __name__ == '__main__':
    main()
