#-------------------------------------------------------------------------------
# Name:        card.py
# Purpose: playing card class
#
# Author:      FruityLoops
#
# Created:     05/05/2013
# Copyright:   (c) FruityLoops 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randrange
class Card:
    def __init__(self,rank,suit):
        """creates a playing card.  inputs:
            rank: int 1-13 indicating the ranks Ace - King
            suit: single character 'd','c','h','s' indicating the suit"""
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        """returns the blackjack value of a card. ace counts as 1,
            face cards as 10"""
        if self.rank > 10:
            return 10
        else: return self.rank

    def __str__(self):
        """converts an Card to a string"""
        face = int(self.rank)
        if face == 1: face = "Ace"
        elif face == 11: face = "Jack"
        elif face == 12: face = "Queen"
        elif face == 13: face = "King"
        else: face = str(face)

        suit = self.suit
        if suit == "d": suit = "Diamonds"
        elif suit == "s": suit = "Spades"
        elif suit == "h": suit = "Hearts"
        else: suit = "Clubs"

        return (face+" of "+suit)

def main():
    print("Generates n randomly generated cards and prints BlackJack Value")
    n = eval(input("How many cards would you like to generate? "))
    for i in range(n):
        rank = randrange(1,14)
        suit = randrange(1,5)
        if suit == 1: suit = "d"
        elif suit == 2: suit = "s"
        elif suit == 3: suit = "h"
        else: suit == "c"
        currentCard = Card(rank,suit)

        print(currentCard," = BJ Value",currentCard.BJValue())

if __name__ == '__main__':
    main()
