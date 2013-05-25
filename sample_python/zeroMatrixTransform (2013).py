#-------------------------------------------------------------------------------
# Name:        matrixZeroTransform.py
# Purpose:  Write an algorithm s.t. if an element in an MxN matrixx is 0,
#           its entire row and column is 0
#
# Caveats: Only works for multidimensional arrays
#
# Author:      Adrienne Sands
#
# Created:     19/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#to do: amend for single dimensional array (list)
#import numpy for array manipulation
from numpy import *

#if an element is 0, transforms that element's row/column = 0
def zeroTransform(array):
    x,y= array.shape
    #boolean to store whether row/column contains 0. False if row/col contains 0, True else.
    boolArray = ones((x,y),bool)
    transformedArray = zeros((x,y),bool)

    for row in range(x):
        if 0 in array[row]:
            for col in range(y):
                if array[row][col]==0:
                    boolArray[row,:]= False #returns the rowth row
                    boolArray[:,col]=False #returns the colth column

    transformedArray = array*boolArray

    return transformedArray

def test():
    #test1: 3x3 square matrix
    test1= arange(9).reshape(3,3)
    aprint(1,test1)

    #test2: 2x5 matrix w/ one zero
    test2= array([[1,2,3,0,5],[2,8,3,4,5]])
    aprint(2,test2)

    #test3: 3x4 matrix w/ no zeros
    test3 = array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    aprint(3,test3)

    #test4: 3x4 matrix w/ two zeros
    test4 = array([[1,2,0,4],[5,6,7,8],[0,10,11,12]])
    aprint(4,test4)

    #test5: 1x6 matrix w/ zero
    test5 = array([[1,2,3,4,0,6]])
    aprint(5,test5)


def aprint(num,array):
    print("Test {0}:".format(num))
    print(array,zeroTransform(array),sep="\n\n",end="\n\n")

def main():
    pass

if __name__ == '__main__':
    test()
