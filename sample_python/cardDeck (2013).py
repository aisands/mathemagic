#-------------------------------------------------------------------------------
# Name:        cardDeck.py
# Purpose:  class Deck representing a deck of cards
#               constructor - creates a new deck of 52 cards in standard order
#               getCardList - returns list of cards in deck
#               shuffle - randomizes the order of the cards
#               dealCard - returns a single card from the top of the deck,
#                           removes it from the deck
#               cardsLeft - returns the number of cards in the deck
#
# Author:      Adrienne Sands
#
# Created:     21/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from card import Card
from cardSort import orderCardStringList, createCardList
import random

class Deck:
    def __init__(self):
        deckStringList = []
        for i in ['s','h','c','d']:
            for j in range(1,14):
                deckStringList.append((j,i))

        #newDeckStringList = orderCardStringList(deckStringList)
        #print(newDeckStringList)
        self.deckStringList = deckStringList
        self.deckList = createCardList(deckStringList)

    def getCardStringList(self):
        return self.deckStringList

    def getCardList(self):
        return self.deckList

    def shuffle(self):
        deckStringList = self.deckStringList
        shuffledList = []
        randList = list(range(self.cardsLeft()))
        random.shuffle(randList)

        for i in randList:
            shuffledList.append(deckStringList[i])

        self.deckStringList = shuffledList
        self.deckList = createCardList(shuffledList)

    def dealCard(self):
        self.deckStringList = self.deckStringList[1:] #remove element from string list
        return self.deckList.pop(0)

    #uses deckStringList vs deckList for performance
    def cardsLeft(self):
        return len(self.deckStringList)

def test():
    #tests deck creation
    testDeck = Deck()
    print("Current cards in deck:\n",testDeck.getCardList())
    print("Cards left: ",testDeck.cardsLeft())

    #tests dealing
    print(testDeck.dealCard())
    print(testDeck.getCardList())
    print("Cards left: ",testDeck.cardsLeft())

    #tests shuffling
    testDeck.shuffle()
    print(testDeck.dealCard())
    print('Should be shuffled: ',testDeck.getCardList())

def main():
    print("This program deals out a sequence of n cards from a shuffled deck")
    n = int(input("How many cards do you want? "))
    deck = Deck()
    deck.shuffle()
    hand = []

    for i in range(n):
        hand.append(deck.dealCard())

    print("Here are your cards: ",hand)

if __name__ == '__main__':
    main()
