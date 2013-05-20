#-------------------------------------------------------------------------------
# Name:        cardSort.py
# Purpose: creates a list of card objects and prints out the cards grouped by
#           suit and in rank order within each suit. Reads the list of cards
#           from a file where each line represents a single card with the rank
#           and suit separated by a space
#
# Author:      Adrienne Sands
#
# Created:     20/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#to do: create script that generates test case files

from card import *
from numpy import *

#test file - C:\Users\FruityLoops\Desktop\to move to harddrive\cardTest.txt
#creates poker dictionary (#max number of same card, flush?, straight? RF?) : handName
def pokerDictionary():
    pokerDictionary = {
    (1, True,  True,   True): "Royal Flush", #working
    (1, True,  True,   False):  "Straight Flush", #working
    (4, False,  False,  False):  "Four of a Kind", #working
    (5, False,  False,  False):  "Full House", #working
    (1, True,  False,  False):  "Flush", #working
    (1, False,  True,   False):  "Straight", #working
    (3, False,  False, False):  "Three of a Kind", #working
    (2.1, False,  False,  False):  "Two pair", #working
    (2, False,  False,  False):  "Pair", #working
    }

    return pokerDictionary

#creates and sorts list of card tuples from a stringList of card elements
#[('rank1 suit1'),('rank2 suit2')...] > [(rank1,suit1),(rank2,suit2)...]

def orderCardStringList(cardStringList):
    newCardStringList = []

    for i in cardStringList: #for each line
        i = i.split()
        rank = i[0]
        suit = i[1]
        newCardStringList.append((rank,suit))

    newCardStringList.sort(key = lambda tup: (tup[1],int(tup[0])))

    return newCardStringList

#create card objects from list of card tuples
#[(rank1,suit1),(rank2,suit2)...] > [card1,card2,...]
def createCardList(cardStringList):
    cardList = []
    for i in cardStringList:
        cardList.append(str(Card(i[0],i[1])))
    return cardList

#compare a cardStringList with a poker dictionary to determine the hand
def pokerRead(cardStringList):
    #initialize variables
    pokerDict = pokerDictionary()
    rankDict = {}
    suitDict = {}
    straight = False
    flush = False
    RF = False

    # i = (rank,suit)
    for i in cardStringList:
        rank = int(i[0]) #parse rank
        suit = i[1] #parse suit
        #create rank: count in rankDict
        if rank in rankDict:
            rankDict[rank] = rankDict[rank]+1
        else: rankDict[rank]=1

        #create suit: count in suitDict
        if suit in suitDict:
            suitDict[suit] = suitDict[suit]+1
        else: suitDict[suit]=1

    #save off counts for each rank/suit
    rankKeys = rankDict.keys()
    rankValues = rankDict.values()

    #find the smallest, largest rank and the range (spread) between them
    maxRank = max(rankKeys, key=int)
    minRank = min(rankKeys, key=int)
    spread = maxRank - minRank

    #find the maximum number of cards of the same rank
    numSameCard = max(rankValues,key=int)

    #edge handling for straights: compare rankDictionary
    #with incrementing sequence starting with min value
    if spread == 4:
        straight = (list(rankDict)==list(range(minRank,minRank+5)))

    #handling for flush
    if max(suitDict.values())==5:
        flush = True  #highest number of same suit

    if (straight and flush and (minRank == 10)):
            RF = True

    #handle edge cases:

    #full house vs. three of a kind
    #    (5, 0,  False,  0):  "Full House"
    #    (3, 0,  False,  0):  "Three of a Kind
    elif numSameCard == 3:
        tempList = dict((k,v) for k,v in rankDict.items() if v>1)
        if len(tempList) ==2: #if two ranks have counts more than 1, full house
            numSameCard = 5 #representation for full house in dict

    #two pair vs pair
    #   (2, 0,  False,  0):  "Pair"
    #   (4, 0,  False,  0):  "Two pair"
    elif numSameCard == 2:
        tempList = dict((k,v) for k,v in rankDict.items() if v>1)
        if len(tempList) ==2: #if two ranks have counts more than 1, two pair
            numSameCard = 2.1   #representation for full house in dict

    dictTup = (numSameCard,flush,straight,RF)

    if dictTup in pokerDict:
        handName = pokerDict[dictTup]
    else:
        handName = str(max(rankDict.keys()))+" high"

    return handName

#test data file - D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\cardTest.txt (revised as needed)
def main():
    print("This program reads a list of cards from a file and prints the list")
    print("grouped by suit and in rank order within each suit")
    filename = input("Which file? ")
    infile = open(filename,'r')
    cardStringList = infile.readlines()
    infile.close()

    orderedCardStringList = orderCardStringList(cardStringList)

    cardList = createCardList(orderedCardStringList)

    while True:
        printMethod = input("Print to file or screen? ")
        if printMethod == "screen":
            print("Sorted card list: ",cardList)
            print(pokerRead(orderedCardStringList))
            break

        elif printMethod == "file":
            filename = input("Print to which file? ")
            outfile = open(filename,'w')
            outfile.writelines(sortedCardList,pokerRead(orderedCardStringList))
            print("Results printed to",filename)
            break

if __name__ == '__main__':
    main()
