#-------------------------------------------------------------------------------
# Name:        conference.py
# Purpose:  keeps track of conference attendees
#
# Author:      Adrienne Sands
#
# Created:     22/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
from attendee import *

class Conference:
    def __init__(self):
        self.attendees = []
	#remove attendee from conference
    def deleteAttendee(self,attendee):
        if attendee in self.attendees:
            self.attendees.remove(attendee)
        return self

	#register an attendee
    def addAttendee(self,attendee):
        self.attendees.append(attendee)
        return self
	
	#get info on all attendees
    def getAllInfo(self,string):
        output = []
        for i in self.attendees:
            output.append(i.getInfo(string))
        return output
	
	#get info on all attendees from a certain state
    def roster(self,state):
        return [i.getInfo("all") for i in self.attendees if i.getState()==state]

def main():
    #test class initializations
    test = Conference()
    marissa = Attendee('marissa','world wide','tn','marissa@mail.com')
    jen = Attendee('jen','world wide tech','tn','jen@mail.com')
    dan = Attendee('dan','epic','mi','dan@mail.com')

    #test addAttendee,getInfo,roster methods
    test.addAttendee(marissa).addAttendee(jen).addAttendee(dan)
    print("Info on Marissa: ",marissa.getInfo("all"))
    print("All attendees: ",test.getAllInfo("all"))

    #test deleteAttendee method
    test.deleteAttendee(dan)
    print("Attendees after removal: ",test.getAllInfo("all"))

    #test roster method
    print("Attendees from TN: ",test.roster('tn'))


if __name__ == '__main__':
    main()
