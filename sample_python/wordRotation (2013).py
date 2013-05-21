#-------------------------------------------------------------------------------
# Name:        wordRotation.py
# Purpose:  checks if one string is a rotation of another using one call to
#           isSubstring
#
# Author:      Adrienne Sands
#
# Created:     20/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
def isSubstring(s1,s2):
    return s1 in s2

def main():
    print("This program checks if one string is a rotation of another")
    print("i.e. 'erbottlewat' is a rotation of 'waterbottle'")
    sOriginal,sRotated= input("Enter two strings (original, rotated) separated by a comma").split(",")
    sConcat = sRotated*2
    result = "is not"

    if isSubstring(sOriginal,sConcat): result = "is"

    print("{0} {1} a rotation of {2}.".format(sRotated,result,sOriginal))

if __name__ == '__main__':
    main()
