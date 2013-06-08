#Author: 'Adrienne'
'''
Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

Input sample: The first argument will be a text file containing a comma separated list of two integers, one list per line. e.g.
13,8
17,16

Output sample: Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line.
16
32
'''

#finds the smallest multiple of n which is greater than or equal to x
def findMultiple(x,n):
    num = n
    while num < x:
        num *= 2

    return num

def test():
    print(findMultiple(13,8))
    print(findMultiple(17,16))

def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases.readlines():
        x,n = map(int,test.split(','))
        print(findMultiple(x,n))

    test_cases.close()

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
