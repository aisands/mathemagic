#-------------------------------------------------------------------------------
# Name:        stringReverse
# Purpose:  reverses a string
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
def reverse(string):
    newString = []
    for i in range(len(string)):
        newString.append(string[-i-1])

    return ''.join(newString)

def test():
    if ("gfedcba"==reverse("abcdefg")): print("Test successful!")
    else: print("Test failed.")

def main():
    print("This program returns the reverse of a string.")
    entry = input("Enter a string: ")
    print("Reversed string: ",reverse(entry))

if __name__ == '__main__':
    main()
