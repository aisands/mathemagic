#Author: 'Adrienne'
#Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

#Input sample: Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. e.g.

#20,6
#2,3
#You may assume M will never be zero.
#Output sample: Print out the value of N Mod M

def mod(line):
    N,M = [int(i) for i in line.split(",")]
    intdiv = N//M
    return N-(M*intdiv)

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(mod(test))
    test_cases.close()

def test():
    print(mod('20,6'))
    print(mod('2,3'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
