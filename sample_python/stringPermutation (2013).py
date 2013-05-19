#-------------------------------------------------------------------------------
# Name:         stringPermutation.py
# Purpose:  determines if a string is a permuation of another
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#returns true if string1 is a permutation of string2. compares sorted lists
def isPermutation(string1,string2):
    list1,list2 = list(string1),list(string2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True

    else: return False

#tests the isPermutation function
def test():
    #test1: permutation, all elements in common (abc vs bac)
    if not isPermutation("abc","bac"):
        print("Test 1 failed")

    #test2: non-permutation, no elements in common (abc vs def)
    elif isPermutation("abc","def"):
        print("Test 2 failed")

    #test3: non-permutation, some elements in common (abc vs bacd)
    elif isPermutation("abc","bacd"):
        print("Test 3 failed")

    else: print("Tests successful!")

#accepts user input of 2 strings; tests whether string1 is a permutation of string2
def main():
    print("This program determines if one string is a permutation of another.")
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")

    if isPermutation(string1,string2): fill = "is"
    else: fill = "is not"

    print("'{0}' {1} a permutation of '{2}'.".format(string1,fill,string2))

if __name__ == '__main__':
    main()
