#-------------------------------------------------------------------------------
# Name:        set.py
# Purpose:  represents a classical set
#                set(x) - creates a set (elements is the initial list of items)
#               addElement(x) - adds x to the set
#               deleteElement(x) - removes x from the set if present
#               member(x) - returns true if x is in the set, false otherwise
#               intersection(set2) -returns a new set containing elements in
#                   common to set1 and set2
#               union(set2) - returns a new set containing just those elements
#                   in common to this set and set2
#               subtract(set2) - returns a new set containing all the elements
#                   of this set that are not in set2
#
# Author:      Adrienne Sands
#
# Created:     21/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------

class Set:
    #elements is the initial list of items in the set
    def __init__(self,elements):
        self.elements = elements

    #gets the elements in the set
    def getElements(self):
        return self.elements

    #adds an element to the set
    def addElement(self,x):
        self.elements.append(x)

    #removes an element from the set if it exists
    def deleteElement(self,x):
        if self.member(x):
            self.elements.remove(x)

    #checks if x in the set
    def member(self,x):
        return (x in self.elements)

    #new set containing all elements in common with self and set2
    def intersection(self,set2):
        set1El = self.elements
        set2El = set2.elements
        intersection = []
        for i in set1El:
            if i in set2El:
                intersection.append(i)

        return Set(intersection)

    #new set containing all elements in self, set2, or both
    #currently set to remove duplicate elements
    def union(self,set2):
        set2El = set2.elements
        union = self.elements
        for i in set2El:
            if i not in union:
                union.append(i)
        return Set(union)

    #new set containing all elements of the set that are not in set2
    def subtract(self,set2):
        subtraction = self.elements
        set2El = set2.elements
        for i in set2El:
            if i in subtraction:
                subtraction.remove(i)
        return Set(subtraction)

def test():
    #test initialization and getelements method
    test1 = Set([1,2,3])
    print("Original set: ",test1.getElements())

    #test addElement method
    test1.addElement(5)
    print("After adding 5: ",test1.getElements())

    #test deleteElement method
    test1.deleteElement(5)
    test1.deleteElement(7)
    print("After deleting 5,7: ",test1.getElements())

    #test member method
    print("Three is in the set: ",test1.member(3))
    print("Four is in the set: ",test1.member(4))

    #test intersection, union, subtract methods
    test2 = Set([2,3,4,5])
    print("\nOriginal set: ",test1.getElements())
    print("New set: ",test2.getElements())
    print("Intersection: ",(test1.intersection(test2)).getElements())
    print("Union: ",(test1.union(test2)).getElements())
    print("Subtraction: ",(test1.subtract(test2)).getElements())

def main():
    pass

if __name__ == '__main__':
    test()
