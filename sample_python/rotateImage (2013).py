#-------------------------------------------------------------------------------
# Name:        rotateImage
#
# Purpose:  Given an image represented by an NxN matrix where each pixel in the
#           image is 4 bytes. Write a method to rotate the image by 90'.
#
# Caveats:  If original image is not square, will crop to the smaller dimension
#
# Author:      Adrienne Sands
#
# Created:     19/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from numpy import *
import scipy.misc

#takes in an array and rotates it 90' clockwise
def rotateImage(array):
    x,z = min(array.shape[0],array.shape[1]),array.shape[2]
    #changed to use ints for simplicity/ cleaner readout
    newArray = zeros((x,x,z),array.dtype)

    for row in range(x):
        newArray[:,(x-1-row)]=array[row]

    return newArray

#test 3x3 matrix
# [[0 1 2],      [[6 3 0],
# [ 3 4 5],   >   [7 6 1],
# [ 6 7 8],       [8 5 2],

#test 4x4 matrix
# [[0 1  2   3],      [[12  8  4  0],
# [ 4 5  6   7],   >   [13  5  6  1],
# [ 8 9  10 11],       [14  9 10  2],
# [12 13 14 15]]       [15 11  7  3]]

#tests with numeric matrices
def test():
    test3Array = arange(9).reshape(3,3)
    test4Array = arange(16).reshape(4,4)

    print(test3Array,"\n",rotateImage(test3Array),sep="\n")
    print()
    print(test4Array,"\n",rotateImage(test4Array),sep="\n")

#test file: C:\Users\FruityLoops\Pictures\adrienne-sands.jpg
#prompts user for an image filename, reads image, rotates, and saves rotated
#image to a new filename
def main():
    print("This program rotates an image by 90 degrees")
    filename = input("Enter a filename: ")
    inimage = scipy.misc.imread(filename)

    rotatedImage = rotateImage(inimage)

    filename = input("Enter an output filename: ")
    scipy.misc.imsave(filename,rotatedImage)

    print("Image written to",filename)

if __name__ == '__main__':
    main()
