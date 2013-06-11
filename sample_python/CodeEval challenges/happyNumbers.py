#Author: 'Adrienne'

#A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

#Input sample: The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. Each line is in the format: N i.e. a positive integer eg.
#1
#7
#22
#Output sample: If the number is a happy number, print out a 1. If not, print out a 0 eg.
#1
#1
#0
#For the curious, here's why 7 is a happy number: 7->49->97->130->10->1. Here's why 22 is NOT a happy number: 22->8->64->52->29->85->89->145->42->20->4->16->37->58->89 ...

def happyNumber(numString):
    temp = [int(i) for i in list(numString)]
    hold = [int(numString)]

    while True:
        newNum = sum([int(i)**2 for i in temp])
        if newNum == 1:
            return newNum
        elif newNum in hold:
            return 0
        else:
            hold.append(newNum)
            temp = list(str(newNum))

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(happyNumber(test))
    test_cases.close()

def test():
    print(happyNumber('1'))
    print(happyNumber('7'))
    print(happyNumber('22'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
