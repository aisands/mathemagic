#-------------------------------------------------------------------------------
# Name:        graphicsGroup.py
# Purpose:  class that groups separate pieces of a drawing together to be
#           positioned together; class manages a list of graphics objects
#
# Author:      Adrienne Sands
#
# Created:     21/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from graphics import *
class GraphicsGroup:

    #anchor is a Point. Creates an empty group with the given anchor point
    def __init__(self,anchor):
        if isinstance(anchor,Point):
            self.data = [anchor]
            self.anchor = anchor

    #returns a clone of the anchor point
    def getAnchor(self):
        return self.anchor.clone()

    def getData(self):
        return self.data

    #gObject a graphics object. Adds gObject to the group
    def addObject(self,gObject):
        self.data.append(gObject)

    #moves all objects in the group (including anchor point)
    def move(self,dx,dy):
        data = self.getData()
        for i in data:
            i.move(dx,dy)

        self.data = data
        self.anchor = data[0]

    #draws all objects into win. Doesn't draw the anchor point
    def draw(self,win):
        for i in self.data[1:]:
            i.draw(win)

    #undraws all objects in the group
    def undraw(self):
        for i in self.data[1:]:
            i.undraw()

def test():
    #tests initialization of GraphicsGroup class and getAnchor
    win = GraphWin()
    win.setCoords(-10,-10,10,10)
    anchor = Point(0,0)
    test = GraphicsGroup(anchor)
    print("Number of objects after initialization: ",len(test.data))
    print("Anchor: ({0},{1}) "
        .format(test.getAnchor().getX(),test.getAnchor().getY()))

    #tests addObject method (adds 4 objects to Graphics Group)
    for i in range(1,5):
        test.addObject(Circle(anchor,i))
    print("Number of objects after add method: ",len(test.data))

    #tests draw method
    test.draw(win)
    win.getMouse()

    #tests undraw method
    test.undraw()

    #tests move method
    test.move(3,3)
    test.draw(win)
    win.getMouse()

    win.close()

#draws a bullseye using a GraphicsGroup then moves the group to user's mouse location
def main():
    print("This program draws/moves a bulls-eye using your mouse location.")
    win = GraphWin()
    win.setCoords(-10,-10,10,10)
    anchor = win.getMouse()
    test = GraphicsGroup(anchor)

    for i in range(1,5):
        test.addObject(Circle(anchor,i))

    test.draw(win)
    print("Where do you want to redraw the bulls-eye?")
    anchorNew = win.getMouse()
    test.move(anchorNew.getX(),anchorNew.getY())

    print("Click to close.")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
