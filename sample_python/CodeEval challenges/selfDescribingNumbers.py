#Author: 'Adrienne'
#Challenge Description: A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.

#Input sample: The first argument is the pathname to a file which contains test data, one test case per line. Each line contains a positive integer. Each line is in the format: N i.e. a positive integer eg.
#2020
#22
#1210
#Output sample:If the number is a self-describing number, print out a 1. If not, print out a 0 eg.
#1
#0
#1
#For the curious, here's how 2020 is a self-describing number: Position '0' has value 2 and there is two 0 in the number. Position '1' has value 0 because there are not 1's in the number. Position '2' has value 2 and there is two 2. And the position '3' has value 0 and there are zero 3's.

def selfDescribe(numString):
    for i in range(len(numString)):
        if int(numString[i])!=list(numString).count(str(i)):
            return 0
    return 1

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(selfDescribe(test))
    test_cases.close()

def test():
    print(selfDescribe('2020'))
    print(selfDescribe('22'))
    print(selfDescribe('1210'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
