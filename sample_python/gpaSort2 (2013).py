#-------------------------------------------------------------------------------
# Name:        gpaSort2
# Purpose: creates a decorated list that will sort students by GPA
#
# Author:      Adrienne Sands
#
# Created:     19/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#Test data - D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\gpaTest.txt
from gpaSort import *

def dataSort2(gui,gpaList):
    """Sorts data by gpa,name, or credits"""
    tempList = []
    decoratedList = []
    data = []

    gui.setText("How would you like to sort?: ")
    for button in [gui.gpaButton,gui.nameButton,gui.creditsButton]:
            button.activate()

    #only continue if one of the sort buttons has been clicked
    while True:
        p = gui.win.getMouse()
        if (gui.gpaButton.clicked(p) or gui.nameButton.clicked(p) or gui.creditsButton.clicked(p)):
            break

    if gui.gpaButton.clicked(p):
        for i in gpaList:
            tempList.append(i.getGPA())
    elif gui.nameButton.clicked(p):
        for i in gpaList:
            tempList.append(i.getName())
    else:
        for i in gpaList:
            tempList.append(i.getQPoints())

    decoratedList = list(zip(tempList,gpaList))

    #deactivate buttons for next steps
    for button in [gui.gpaButton,gui.nameButton,gui.creditsButton]:
        button.deactivate()

    #sort by the first element in the decoratedList
    decoratedList.sort(key=lambda tup:tup[0])

    for (i,j) in decoratedList:
        data.append(j)

    return data

def main():
    print("This program sorts student grade information by GPA, name, or credits.")
    #create graphics window
    win = GraphWin()
    win.setCoords(-20,-20,20,20)

    #create graphical interface
    gui = GUI(win)

    p = win.getMouse()

    #runs through program until user clicks quitButton
    while not gui.quitCheck(p):
        if gui.quitCheck(p):
            break
        elif gui.submitButton.clicked(p):
            gui.quitButton.deactivate()
            data = gui.dataRead()
            gui.dataOutput(gui.dataOrder(dataSort2(gui,data)))
            gui.quitButton.activate()
            p = win.getMouse()

    win.close()

if __name__ == '__main__':
    main()
