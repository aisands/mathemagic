#Author: 'Adrienne'
#Challenge Description: You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.
#Input sample: File containing a list of sorted integers, comma delimited, one per line. e.g.
#1,1,1,2,2,3,3,4,4
#2,3,4,5,5
#Output sample: Print out the sorted list with duplicates removed, one per line, e.g.
#1,2,3,4
#2,3,4,5

def removeDups(line):
    line = line.split(',')
    temp = line[0]

    for i in line[1:]:
        if i == temp:
            line.remove(i)
        temp = i

    return toString(line)

def toString(list):
    return ",".join(list)

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(removeDups(test))
    test_cases.close()

def test():
    print(removeDups('1,1,1,2,2,3,3,4,4'))
    print(removeDups('2,3,4,5,5'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
