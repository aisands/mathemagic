#Author: 'Adrienne'
#Challenge Description: You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't'(case matters) in 'S' or -1 if there is none. The position to be printed out is zero based.

#Input sample: The first argument is a file, containing a string and a character, comma delimited, one per line. Ignore all empty lines in the input file.e.g.

#Hello World,r
#Hello CodeEval,E
#Output sample:  Print out the zero based position of the character 't' in string 'S', one per line. Do NOT print out empty lines between your output. e.g.

#8
#10

def rightmostChar(line):
    str,let = line.split(',')
    indices = list(range(len(str)))
    indices.reverse()
    for i in indices:
        if str[i] == let:
            return i
    return -1

def main():
    test_cases = open(sys.argv[1], 'r').read().splitlines()
    for test in test_cases:
        print(rightmostChar(test))
    test_cases.close()

def test():
    print(rightmostChar('Hello World,r'))
    print(rightmostChar('Hello CodeEval,E'))

if __name__ == '__main__':
    import sys
    try:
        main()

    except Exception as e:
        print(e)
