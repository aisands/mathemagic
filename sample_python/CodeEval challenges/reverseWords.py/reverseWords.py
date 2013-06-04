#Author: 'Adrienne'
#Write a program to reverse the words of an input sentence.
#Input sample:
#The first argument will be a text file containing multiple sentences, one per line. Possibly empty lines too. e.g.
#
#Hello World
#Hello CodeEval
#Output sample:
#Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print.
#e.g. World Hello
# CodeEval Hello

def reverse(line):
    return " ".join(line.split()[::-1])

def main():
    test_cases = open(sys.argv[1], 'r')

    for line in test_cases.readlines():
        if line != "":
            print(reverse(line))

    test_cases.close()

def test():
    string = ["this is a test"]
    for i in string:
        print(reverse(i))

if __name__ == '__main__':
    import sys

    try:
        main()

    except Exception as e:
        print(e)
