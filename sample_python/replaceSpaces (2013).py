#-------------------------------------------------------------------------------
# Name:        replaceSpaces.py
# Purpose:  replaces spaces with '%20'
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#replaces spaces in a string with %20
def replaceSpaces(string):
    stringList = string.split(" ")
    for i in range(len(stringList)-1):
        stringList[i] = "{0}%20".format(stringList[i])

    return "".join(stringList)

def test():
    #test1 - "This_is_a_test."
    print("Original String:This is a test.")
    print("New String: {0}".format(replaceSpaces("This is a test.")))

    #test2 - "This_ _is_a_ _test."
    print("Original String:This  is a  test.")
    print("New String: {0}".format(replaceSpaces("This  is a  test.")))

    #test3 - "_This_is_a_ _test. "
    print("Original String: This is a  test. ")
    print("New String: {0}".format(replaceSpaces(" This is a  test. ")))

    #test4 - "_"
    print("Original String: ")
    print("New String: {0}".format(replaceSpaces(" ")))

    #test5 - ""
    print("Original String:")
    print("New String: {0}".format(replaceSpaces("")))

def main():
    print("This program takes in a string and replaces spaces with '%20'")
    string = input("Enter a string")
    print("New string: ",replaceSpaces(string))

if __name__ == '__main__':
    main()
