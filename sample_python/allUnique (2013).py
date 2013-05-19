#-------------------------------------------------------------------------------
# Name:        allUnique
# Purpose:  algorithm determines if a string has all unique characters
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#to redo using dictionary/ hashes

#using count function (no hashes/dictionary)
def allUnique(string):
    for i in string:
        if string.count(i)>1:
            return False
    return True

def test():
    print("This program tests the allUnique function.")
    #test1: string with all unique characters
    print("This should return true: ",allUnique("abcdefg"))

    #test2: string with all repeated characters
    print("This should return false: ",allUnique("aaaaaa"))

    #test3: string with some unique, some repeated characters
    print("This should return false: ",allUnique("bcdeaaa"))

def main():
    print("This function determines if a string has all unique characters.")
    entry = input("Enter a string")

    if allUnique(entry): print("'",entry,"' contains all unique characters.")
    else: print("'",entry,"' contains repeated characters.")

if __name__ == '__main__':
    main()
