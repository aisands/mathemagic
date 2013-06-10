#Author: 'Adrienne'
#Challenge Description:  You are given two sorted list of numbers(ascending order). The lists themselves are comma delimited and the two lists are semicolon delimited. Print out the intersection of these two sets.
#
#Input sample: File containing two lists of ascending order sorted integers, comma delimited, one per line. e.g.
#1,2,3,4;4,5,6
#7,8,9;8,9,10,11,12
#
#Output sample: Print out the ascending order sorted intersection of the two lists, one per line, e.g.
#4
#8,9

def setIntersection(line):
    out = []
    lists = line.split(";")
    for i in lists[0].split(','):
        if i in lists[1].split(','):
            out.append(i)
    return ','.join(out)

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(setIntersection(test))
    test_cases.close()

def test():
    print(setIntersection('1,2,3,4;4,5,6'))
    print(setIntersection('7,8,9;8,9,10,11,12'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
