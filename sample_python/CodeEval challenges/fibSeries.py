#Author: 'Adrienne'
#Challenge Description:

#The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1;. Given a positive integer 'n', print out the F(n).

#Input sample: The first argument will be a text file containing a positive integer, one per line. e.g.
#5
#12
#Output sample: Print to stdout, the fibonacci number, F(n). e.g.
#5
#144

def findFib(num):
    if num > 1:
        return findFib(num-1) + findFib(num-2)
    elif num == 1:
        return 1
    else:
        return 0

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(findFib(int(test)))
    test_cases.close()

def test():
    print(findFib(5))
    print(findFib(12))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
