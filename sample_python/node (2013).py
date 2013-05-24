#-------------------------------------------------------------------------------
# Name:        node.py
# Purpose:  linkedList
#
# Author:      Adrienne Sands
#
# Created:     23/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next

def main():
    #test initialization
    test = Node(99)
    print(test.getData())

if __name__ == '__main__':
    main()
