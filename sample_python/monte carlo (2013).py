#-------------------------------------------------------------------------------
# Name:        monte carlo.py
# Purpose: estimates the value of pi using monte carlo
#
# Author:      Adrienne Sands
#
# Created:     05/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    print("This program estimates the value of pi using Monte Carlo techniques.")
    numDarts = eval(input("Enter the number of darts: "))
    hits = simulateDarts(numDarts)
    printSummary(numDarts,hits)

def simulateDarts(numDarts):
    hits = 0
    for i in range(numDarts):
        if simulateDart(): hits = hits + 1
    return hits

from random import random
def simulateDart():
    x = 2*random() - 1
    y = 2*random() - 1

    if x**2 + y**2 <=1: return True
    else: return False

def printSummary(numDarts,hits):
    est = 4 * (hits/numDarts)
    print("After {0} darts, your estimate of pi is {1:0.5}.".format(numDarts,est))

if __name__ == '__main__':
    main()
