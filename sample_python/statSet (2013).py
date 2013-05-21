#-------------------------------------------------------------------------------
# Name:        statSet.py
# Purpose:  statSet class used to do simple statistical calculations (w/o numpy)
#
# Author:      Adrienne Sands
#
# Created:     21/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from copy import copy
from math import sqrt

class StatSet:
    def __init__(self):
        self.data = []

    def getData(self):
        return self.data

    def addNumber(self,x):
        if isinstance(x,(int,float)):
            data = self.data
            data.append(x)
            self.data = data

        return self #return self to allow for multiple adds

    def mean(self):
        nums = self.data
        if len(nums)>0:
            return sum(nums)/len(nums)
        else:
            return 0

    def median(self):
        nums = copy(self.data)
        nums.sort()

        length = len(nums)
        remainder = length%2
        med = 0

        if length == 0:
            return Non
        elif remainder == 0:
            med = (nums[length//2] + nums[length//2 - 1])/2
        else:
            med = nums[length//2]
        return med

    def stdDev(self):
        data = self.data
        N = self.count()
        mean = self.mean()
        devSum = 0

        for i in range(N):
            devSum = devSum + (data[i]-mean)**2

        return sqrt(devSum)

    def count(self):
        count = len(self.data)
        return count

    def min(self):
        nums = copy(self.data)
        nums.sort()
        minNum = nums[0]
        return minNum

    def max(self):
        nums = copy(self.data)
        nums.sort()
        maxNum = nums[-1]
        return maxNum

def test():
    #test class constructor and addNumber method
    test = StatSet()
    test.addNumber(3).addNumber(6).addNumber(2).addNumber(4).addNumber(11)
    print("StatSet instance: ",test.getData())

    #test mean, median, stdDev, count, min, max
    print("Mean: ",test.mean())
    print("Median: ",test.median())
    print("Standard Deviation: ",test.stdDev())
    print("Min: ",test.min())
    print("Max: ",test.max())
    print("Min: ",test.min())
    print("Count: ",test.count())

    test.addNumber(13).addNumber(16).addNumber(12).addNumber(41).addNumber(11)
    print("\nAfter second addition")
    print("Mean: ",test.mean())
    print("Median: ",test.median())
    print("Standard Deviation: ",test.stdDev())
    print("Min: ",test.min())
    print("Max: ",test.max())
    print("Min: ",test.min())
    print("Count: ",test.count())

def main():
    print("This program tests the StatSet class")
    statSet = StatSet()
    while True:
        n = input("Enter a number (<Enter> to quit): ")
        if n == "":
            break
        statSet.addNumber(int(n))

    print("Data: ", statSet.getData())
    print("Mean: ",statSet.mean())
    print("Median: ",statSet.median())
    print("Standard Deviation: ",statSet.stdDev())
    print("Min: ",statSet.min())
    print("Max: ",statSet.max())
    print("Min: ",statSet.min())
    print("Count: ",statSet.count())

if __name__ == '__main__':
    main()
