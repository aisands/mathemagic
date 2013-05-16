#-------------------------------------------------------------------------------
# Name:        valid date.py
# Purpose:     accepts a date, determines whether its invalid
#
# Author:      Adrienne Sands
#
# Created:     29/04/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#To do: fix february so don't need another statement in the passing condition.
#use case select?

def main():
    print("this program determines whether a date is valid.")
    m = input("enter a date in the form M/DD/YYYY")
    [month,day,year] = [int(x) for x in m.split("/")]

    #check if year valid
    if year < 1: print("year invalid.")

    #check if month between 1 and 12
    elif (month < 1) or (month > 12): print("month invalid.")

    #check if day valid..
    #30 days have september, april, june, and november
    elif (month in [4,6,9,11]) & (day>30): print("invalid day. This month only has 30 days.")

    #february
    #leap year if year divisible by 4 unless a century year
    elif (month == 2):
        if (year%4==0) & (year%100>0): febDays = 29 #non-century years divisible by 4
        if(year%400==0): febDays=29
        else: febDays =28

        if day>febDays: print("invalid day. february only had {0} days this year.".format(febDays))
        else: print(m,"is a valid date!")

    #all the rest have 31
    elif (day<0) or (day>31): print("invalid day.")

    else: print(m,"is a valid date!")

if __name__ == '__main__':
    main()
