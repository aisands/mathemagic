#Author: 'Adrienne'
#Challenge Description: Print out the sum of integers read from a file.
#Input sample: The first argument to the program will be a text file containing a positive integer, one per line. e.g.
#5
#12
#Output sample: Print out the sum of all the integers read from the file. e.g.
#17

def main():
    total = 0
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        total += int(test)
    print(total)

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
