#-------------------------------------------------------------------------------
# Name:        arrayChallenge.py
# Purpose:  test python array functions
#
# Author:      Adrienne Sands
#
# Created:     18/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#like myList.count(x) - counts the number of times x is in the list
def count(myList,x):
    num = 0
    for i in myList:
        if i == x:
            num = num + 1
    return num

#like x in myList - returns true if x in list
def isin(myList,x):
    for i in myList:
        if i == x:
            return True
    return False

#like myList.index(x) - finds the first instance of x in myList
def index(myList,x):
    pos = 0
    for i in myList:
        if i == x:
            return pos
        pos = pos + 1
    return False

#like myList.reverse() - reverses myList
def reverse(myList):
    newList = []
    for i in range(len(myList)):
        newList.append(myList[-i-1])
    return newList

#like myList.sort() - sorts myList
def sort(myList):
    #insert sort algorithm
    #for each list position excluding the first one
    for i in range(1,len(myList)):
        #pick the value
        curVal = myList[i]
        #save that value's original position
        temp = i
        #while there are items to the left of this item
        #and the items to the left are greater than this item
        while (temp>0 and myList[temp-1]>curVal):
            #move this item left
            myList[temp]=myList[temp-1]
            #move your pointer left
            temp = temp - 1
        myList[temp] = curVal

    return myList

#tests reverse function
def reverseTest(myList):
    reversedList = reverse(myList)
    myList.reverse()
    reversePass = ((reversedList) == myList)
    if reversePass: print("Reversed List: ",reversedList)
    else:
        print("Reverse test fails.")

#tests reverse function
def sortTest(myList):
    sortedList = sort(myList)
    myList.sort()
    sortPass = (sortedList == myList)
    if sortPass: print("Sorted List: ",sortedList)
    else:
        print("Sort test fails.")

#tests testNum functions
def numTest(testNum,myList):
    totalCount = count(myList,testNum)
    isIn = isin(myList,testNum)
    place = index(myList,testNum)

    countPass = (totalCount == myList.count(testNum))
    isinPass = (isIn == (testNum in myList))
    indexPass = ((not isIn) or (place == myList.index(testNum)))

    if not countPass: print("Count test fails.")
    elif not isinPass: print("IsIn test fails.")
    elif not indexPass: print("Index test fails.")

    else:
        if isIn:
            print("Index: ",place)
            print("Count: ",totalCount)
        else: print(testNum,"is not in myList")

#receives entry from user, tests list
def main():
    print("This program creates functions like Python's built in array operations")
    myList = []

    while True:
        entry = input("Enter a number (<Enter> to Quit)")
        if entry == "":
            break
        myList.append(eval(entry))

    print("Original List: ",myList)

    reverseTest(myList)
    sortTest(myList)

    testNum = eval(input("Enter a test number: "))
    numTest(testNum,myList)

if __name__ == '__main__':
    main()
