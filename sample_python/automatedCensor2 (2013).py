#-------------------------------------------------------------------------------
# Name:        automatedCensor2.py
# Purpose: Extension of automatedCensor; accepts an input file and file of
#           censored words.  Replaces words in the original file by *'s
#
#
# Author:      Adrienne Sands
#
# Created:     20/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#test original file: D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\censorOriginal.txt
#test censor file: D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\censorList.txt

import automatedCensor

def censor(stringList,censoredString):

    for j in censoredString.split(): #for each word in the censoredString
        for i in range(len(stringList)): #for each line
            censorChar = "*"*len(j) #create the censorString
            stringList[i] = stringList[i].replace(j,censorChar)

    return stringList

def main():
    while True:
        method = input("Censor by number of characters (num) or censor file (file): ")
        if method == "num":
            automatedCensor.main()
            break
        elif method == "file":
            censorByFile()
            break

def censorByFile():
    filename = input("Enter an input/output filename: ")
    infile1 = open(filename,'r') #open the file for read/write
    originalStringList=infile1.readlines()
    infile1.close()

    filename = input("Enter the file of censored words: ")
    infile2 = open(filename,'r')
    censoredString = infile2.read() #returns a string of the censored words
    infile2.close() #close file of censored words

    newStringList = censor(originalStringList,censoredString)

    filename = input("Enter an output filename: ")
    outfile = open(filename,'w')
    outfile.writelines(newStringList)
    infile1.close()

    print("File printed to",filename)

if __name__ == '__main__':
    main()
