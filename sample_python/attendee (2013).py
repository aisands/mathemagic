#-------------------------------------------------------------------------------
# Name:        attendee.py
# Purpose:  keeps track of name, company, state, and email address
#
# Author:      Adrienne Sands
#
# Created:     22/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
class Attendee:
    def __init__(self,name,company,state,emailAddress):
        self.name = name
        self.company = company
        self.state = state
        self.emailAddress = emailAddress

    def getInfo(self,string):
        output = []
        if ("name" in string) or string=="all":
            output.append(self.name)
        if ("email" in string) or string=="all":
            output.append(self.emailAddress)
        if ("company" in string) or string=="all":
            output.append(self.company)
        if ("state" in string) or string=="all":
            output.append(self.state)

        return output

    def getState(self):
        return self.state

    def getNameEmail(self):
        return self.name,self.emailAddress

def main():
    pass

if __name__ == '__main__':
    main()
