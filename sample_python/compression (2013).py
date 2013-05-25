#-------------------------------------------------------------------------------
# Name:        compression.py
# Purpose:  does basic string compression
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#does basic string compressions (using the counts of characters)
# aabbbcddddaa = a2b3c1d4a2
#returns the original string if the compressed string is longer

def compression(string):
    stringList = list(string)
    compressedList = []
    count = 1
    i = 0

    while i < len(string):
        val = stringList[i] #take the ith element for comparison
        compressedList.append(val) #append the value
        i = i+1 #look at the next item
        while (i<len(string)) and (stringList[i]==val):
            count = count+1
            i = i+1
        compressedList.append(str(count)) #append the count
        count = 1 #reset your count

    compressedString = "".join(compressedList)

    if len(compressedString)< len(string):
        return compressedString
    else: return string

def test():
    #test case 1: no repeats (compressed string longer)
    if compression("abcdefghijk")!="abcdefghijk":
        print("Test 1 failed.")

    #test case 2: all repeats (compressed string shorter)
    elif compression("aaaa")!="a4":
        print("Test 2 failed.")

    #general test: some repeats (compressed string shorter)
    elif compression("aabbbbbccdde")!="a2b5c2d2e1":
        print("Test 3 failed.")

    else: print("Success!")

def main():
    print("This program does a basic string compression.")
    print("If the compressed version of the string is longer than the original,")
    print("it will print the original.\n")
    string = input("Enter a string for compression: ")
    print("Original string: {0}\nCompressed string: {1}".format(string,compression(string)))

if __name__ == '__main__':
    main()
