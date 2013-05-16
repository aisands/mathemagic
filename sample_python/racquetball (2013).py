#-------------------------------------------------------------------------------
# Name:        racquetball.py
# Purpose:	simulates several matches of racquetball
#
# Author:      Adrienne Sands
#
# Created:     05/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import random

def main():
    printIntro()
    probA,probB,m,n = getInputs()
    winsA,winsB = simNMatches(m,n,probA,probB)
    printSummary(winsA,winsB)

def printIntro():
    print("This program simulates several matches of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A serves first")
    print("in even games.")

def getInputs():
    #returns the four simulation parameters
    probA = eval(input("What is the prob. player A wins a serve? "))
    probB = eval(input("What is the prob. player B wins a serve? "))
    m = eval(input("How many matches to simulate? "))
    n = eval(input("How many games per match? "))

    return probA,probB,m,n

def simNMatches(numMatches,numGames,probA,probB):
    #Simulates n matches of racquetball between players whose abilities
    #are represented by the probability of winning a serve. Returns number of wins.
    winsA = winsB = 0
    for i in range(numMatches):
        winner = simOneMatch(numGames,probA,probB)
        if winner=="A":
            winsA = winsA +1
        else:
            winsB = winsB +1
    return winsA,winsB

def simOneMatch(numGames,probA,probB):
        gameWinsA = gameWinsB = counter = 0
        server = ""

        for i in range(numGames):
            counter = counter + 1
            if counter % 2 != 0: server ="A"
            else: server = "B"
            scoreA,scoreB=simOneGame(server,probA,probB)
            if scoreA > scoreB: gameWinsA = gameWinsA + 1
            else: gameWinsB = gameWinsB +1

        if gameWinsA > gameWinsB: return "A"
        else: return "B"

def simOneGame(server,probA,probB):
    #simulates a racquetball game between players  whose abilities are
    #represented by the probability of winning a serve. Returns the final score
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA,scoreB):
        if server =="A":
            if random() < probA:
                scoreA = scoreA+1
            else: server = "B"
        else:
            if random() < probB:
                scoreB = scoreB+1
            else: server = "A"
    return scoreA,scoreB

def gameOver(a,b):
    #a and b represent scores for a racquetball game
    #Returns True if the game is over, False otherwise
    return a==15 or b==15

def printSummary(winsA,winsB):
    n = winsA + winsB  #games played
    print("\nMatches simulated:",n)
    print("Match wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Match wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__':
    main()
