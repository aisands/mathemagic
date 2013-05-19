#-------------------------------------------------------------------------------
# Name:        automatedCensor.py
# Purpose:  prompts user for input/output file and wordlength,n; reads in text from a file
# and creates a new file where all n-length words are replaced by n *'s
#
# Assumptions: 1. ignores punctuation, 2. words printed on a single line
#
# Author:      Adrienne Sands
#
# Created:     19/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#to do: allow for punctuation
#D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\censorTest.txt
def censor(stringList,censorNum):
    censoredList = []
    temp = ""
    censorChar = "*"*censorNum

    for i in stringList: #for each line in the file
        temp=i.split() #split the line into words
        for j in range(len(temp)): #for each word
            if len(temp[j])==censorNum: #if the length of the word == censorNum
                temp[j]=censorChar #replace it with the censor
        censoredList.append(" ".join(temp)) #add the new line to censoredList

    return censoredList

#prompts the user for an input/output file name and a word length to censor
def main():
    filename = input("Enter an input filename: ")
    infile = open(filename,'r')
    stringList=infile.readlines()
    infile.close()

    censorNum = int(input("What size words do you want to censor? "))
    output = censor(stringList,censorNum)

    filename = input("Enter an output filename: ")
    outfile = open(filename,'w')

    for i in output:
        print(i,file=outfile)
    outfile.close()

    print("File printed to",filename)

if __name__ == '__main__':
    main()
