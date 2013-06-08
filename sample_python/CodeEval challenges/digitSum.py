#Author: 'Adrienne'
#Challenge Description:
#Given a positive integer, find the sum of its constituent digits.
#
#Input sample: The first argument will be a text file containing positive integers, one per line. e.g.
#23
#496
#Output sample: Print to stdout, the sum of the numbers that make up the integer, one per line. e.g.
#5
#19

def digitSum(x):
    total = 0
    for dig in x:
        total += int(dig)
    return total

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(digitSum(test))
    test_cases.close()

def test():
    print(digitSum('23'))
    print(digitSum('496'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
