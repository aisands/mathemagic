#-------------------------------------------------------------------------------
# Name:        sumOfSquares
# Purpose: computes the sum of squares of numbers read from a file
#
# Author:      Adrienne Sands
#
# Created:     22/04/2013
# Copyright:   (c) AdrienneSands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#test file: C:/Users/FruityLoops/Desktop/testData3.txt
def main():
    print("this program computes the sum of squares of numbers read from a file.")
    fileName=input("which file would you like to read? ")
    infile=open(fileName,"r")
    data=infile.readlines()
    total = 0
    for i in data:
        total = total + sumList(squareEach(toNumbers(i)))

    print("the sum of squares of the numbers in this file is, ",total)

#modifies a list of numbers by squaring each entry
#input: nums - a list of numbers
def squareEach(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]**2
    print("nums is ",nums)
    return nums

#returns the sum of the numbers in a list
#input: nums - a list of numbers
def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total = total+nums[i]
    print("total is ",total)
    return total

#modifies each entry in a list by converting it to a number
#input: strList - a list of strings representing numbers
def toNumbers(strList):
    index=0
    newList=list(strList[:-1])
    print("new list before processing ",newList)
    for i in range(len(newList)):
        val=int(strList[i])
        newList[i]= val
    print("newList after processing ",newList)
    return newList

if __name__ == '__main__':
    main()
