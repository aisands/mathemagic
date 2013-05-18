#-------------------------------------------------------------------------------
# Name:        innerProd.py
# Purpose:  computes the inner product of two (same length) lists
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------

def innerProd(x,y):
    if len(x) != len(y):
        return False

    total = 0
    for i in range(len(x)):
        total = total + int(x[i])*int(y[i])

    return(total)

def main():
    print("This program computes the inner product of two lists")
    list1 = input("Enter a list of numbers separated by commas").split(',')
    list2 = input("Enter a second list of numbers separated by commas").split(',')
    print("Inner product: ",innerProd(list1,list2))

if __name__ == '__main__':
    main()
