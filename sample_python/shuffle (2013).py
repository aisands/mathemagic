#-------------------------------------------------------------------------------
# Name:        shuffle.py
# Purpose:  scrambles a list into a random order
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randrange

#scrambles a list into a random order
def shuffle(myList):
    newList = []
    length = len(myList)

    for i in myList:
        pos = randrange(0,length)
        newList.insert(pos,i)

    return newList

#takes in user entered streak
def main():
    print("This program takes a list and shuffles it into a random order")
    myList = []

    while True:
        entry = input("Enter a list element (<Enter> to Quit)")
        if entry == "":
            break
        myList.append(entry)

    print(shuffle(myList))

if __name__ == '__main__':
    main()
