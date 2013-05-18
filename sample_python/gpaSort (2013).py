#-------------------------------------------------------------------------------
# Name:        gpaSort.py
# Purpose:  A program to sort student information into GPA order
#
# Authors:      John Zelle, Adrienne Sands
# as - amended to allow for greater sort control, use graphical interface
#
# Created:     17/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#Test data - D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\gpaTest.txt

from book.gpa import Student, makeStudent
from book.button import *
from graphics import *

#Author: John Zelle
def readStudents(filename):
    infile = open(filename,'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

#Author: John Zelle
def writeStudents(students,filename):
    outfile = open(filename,'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(),s.getHours(),s.getQPoints()),
            file = outfile)
    outfile.close()

#Author: Adrienne Sands
class GUI:
    """Builds gpa file read widget"""
    def __init__(self,win):
        #create gui attributes
        self.win = win
        self.prompt = Text(Point(0,15),"Enter the name of the input file: ")
        self.entry = Entry(Point(0,10),10)
        self.gpaButton = Button(win,Point (-12,-5),10,4,"GPA")
        self.nameButton = Button(win,Point (0,-5),10,4,"Name")
        self.creditsButton = Button(win,Point(12,-5),10,4,"Credits")
        self.submitButton = Button(win,Point(0,5),10,4,"Submit")
        self.quitButton = Button(win,Point(0,-15),10,4,"Quit")
        self.ascButton = Button(win,Point(-12,-15),10,4,"Asc")
        self.descButton = Button(win,Point(12,-15),10,4,"Desc")

        #customize gui attributes
        self.prompt.setSize(8)
        self.entry.setFill('white')

        #draw attributes:
        self.prompt.draw(win)
        self.entry.draw(win)

        #activate submit and quit buttons to begin
        for button in [self.submitButton,self.quitButton]:
            button.activate()

    #set prompt text
    def setText(self,string):
        return self.prompt.setText(string)

    #set entry text
    def getText(self):
        return self.entry.getText()

    #checks if quit button has been clicked
    def quitCheck(self,p):
        return self.quitButton.clicked(p)

    def dataRead(self):
        """Reads input filename, creates list of student objects"""

        self.submitButton.deactivate()
        filename = self.getText()
        return readStudents(filename)

    def dataSort(self,data):
        """Sorts data by gpa,name, or credits"""
        self.setText("How would you like to sort?: ")
        for button in [self.gpaButton,self.nameButton,self.creditsButton]:
                button.activate()

        #only continue if one of the sort buttons has been clicked
        while True:
            p = self.win.getMouse()
            if (self.gpaButton.clicked(p) or self.nameButton.clicked(p) or self.creditsButton.clicked(p)):
                break

        if self.gpaButton.clicked(p):
            data.sort(key = Student.getGPA)
        elif self.nameButton.clicked(p):
            data.sort(key = Student.getName)
        else:
            data.sort(key = Student.getQPoints)

        #deactivate buttons for next steps
        for button in [self.gpaButton,self.nameButton,self.creditsButton]:
            button.deactivate()

        return data

    def dataOrder(self,data):
        """Orders data in descending or ascending order"""
        self.setText("Ascending or decending order?")
        for button in [self.ascButton,self.descButton]:
                button.activate()

        #only continue if one of the order buttons has been clicked
        while True:
            p=self.win.getMouse()
            if (self.ascButton.clicked(p) or self.descButton.clicked(p)):
                break

        if self.descButton.clicked(p):
            data.reverse()

        #deactivate buttons for next steps
        for button in [self.ascButton,self.descButton]:
            button.deactivate()

        self.submitButton.activate()

        return data

    def dataOutput(self,data):
        """Outputs data in an outfile"""
        self.setText("Enter a name for the output file: ")
        filename = self.getText()

        #only continue if submit has been clicked
        while True:
            p = self.win.getMouse()
            if self.submitButton.clicked(p):
                break

        filename = self.getText()
        writeStudents(data,filename)
        print("The data has been written to",filename)

#Author: Adrienne Sands
#Test data - D:\From Adrienne's Computer\Programming\Python\Chapter 11\sample data sets\gpaTest.txt
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
        gui.quitButton.deactivate()

        if gui.submitButton.clicked(p):
            data = gui.dataRead()
            gui.dataOutput(gui.dataOrder(gui.dataSort(data)))
            gui.quitButton.activate()
            p = win.getMouse()

    win.close()

if __name__ == '__main__':
    main()
