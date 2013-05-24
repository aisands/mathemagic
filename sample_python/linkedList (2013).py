#-------------------------------------------------------------------------------
# Name:        linkedList
# Purpose:
#
# Author:      Adrienne Sands
#
# Created:     23/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from node import *

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,data):
        newNode = Node(data)
        if self.head == None:   #if the list is empty make it the head
            self.head = newNode

        if self.tail != None: #else append it after the tail
            self.tail.setNext(newNode)

        self.tail = newNode #then make this node the tail
        return self

    def removeNode(self,index):
        previousNode = None
        currentNode = self.head
        i = 0
        if index<len(self.getData()):
            while (currentNode!=None) and (i<index):
                previousNode = currentNode
                currentNode = currentNode.getNext()
                i += 1

            if previousNode == None:    #previous node none if at the head
                self.head = currentNode.getNext() #change the head to the next node

            else:   #else set the next
                previousNode.setNext(currentNode.getNext())
        return self

    def getData(self):
        output = []
        node = self.head

        while node!=None:
            output.append(node.getData())
            node = node.getNext()
        return output

    def removeDuplicates(self):
        dataList = self.getData() #returns a list of elements in the linkedList
        i = 0
        toRemove = []
        for element in dataList:    #go through each element in the
            if dataList[i:].count(element)>1:
                toRemove.append(i)
            i += 1
        toRemove.reverse()
        for j in toRemove:
            self.removeNode(j)

    def findNtoLast(self,n):

        return nToLastNode


def main():
    #test initialization and getData functions
    test = LinkedList()
    print("After initialization: ",test.getData())

    #test addNode functions
    test.addNode(3).addNode(4).addNode(5).addNode(4).addNode(3).addNode(4)
    print("After adding nodes 3-5: ",test.getData())

    #test removeNode function
    #test.removeNode(7).removeNode(2)
    #print("After removing nodes at indices 7,2: ",test.getData())

    #remove duplicates
    test.removeDuplicates()
    print("After removing duplicates: ",test.getData())

if __name__ == '__main__':
    main()
