#-------------------------------------------------------------------------------
# Name:        monte hall game.py
# Purpose:	simulates the monte hall game
#
# Author:      Adrienne Sands
#
# Created:     05/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import randrange

class Button:
    """A button is a labeled rectangle in a window.  It is activated or
    deactivated with the activate() and deactivate() methods.  The clicked(p)
    method returns True if the button is active an p is inside it."""

    def __init__(self,win,center,width,height,label):
        """Creates a rectangular button, eg:
            qb = Button(myWin,centerPoint,width,height,'Quit')"""
        w,h = width/2.0, height/2.0
        x,y= center.getX(),center.getY()
        self.xmax, self.xmin = x+w,x-w
        self.ymax, self.ymin = y+h,y-h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self,p):
        "Returns true if button active and p inside"
        return(self.active and
                self.xmin <=p.getX()<=self.xmax and
                self.ymin <=p.getY()<=self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'"
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

def main():
    print("Let's play Three Button Monte!")
    win = GraphWin("Three Button Monte")
    door1,door2,door3=createDoors(win)
    winner=randomSelect()
    print("Click on one of the buttons...")
    choice=win.getMouse()

    if (winner==1) and door1.clicked(choice):
        print("Correct! You win!")
    elif (winner==2) and door2.clicked(choice):
        print("Correct! You win!")
    elif (winner==3) and door3.clicked(choice):
        print("You win!")
    else: print("Sorry :(")
    win.close()

#creates and draws doors as buttons
def createDoors(win):
    win.setCoords(0,0,100,100)
    door1 = Button(win,Point(20,70),20,20,"1")
    door2 = Button(win,Point(50,70),20,20,"2")
    door3 = Button(win,Point(80,70),20,20,"3")

    door1.activate()
    door2.activate()
    door3.activate()

    return door1,door2,door3

def randomSelect():
    return randrange(1,4)

if __name__ == '__main__':
    main()
