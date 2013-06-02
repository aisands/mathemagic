#__author__ = 'Adrienne'
# On CodeEval, test cases are read in from a file which is the first argument to your program
# Open the file and read in line by line. Each line represents a different test case
# (unless given different instructions in the challenge description)
#test input: C:\\Users\\Adrienne\\Documents\\Programming\\Python\\codeEval\\data\\fizzbuzzInput.txt

#input list of A,B,N

def fizzbuzz(A,B,N):
    final = []
    for i in range(1,N+1):
        temp = ""
        if i%A == 0:
            temp += 'F'

        if i%B == 0:
            temp += 'B'

        if i%A!=0 and i%B!=0:
            temp = str(i)

        final.append(temp)

    return ' '.join(final)

def test():
    input = 'C:\\Users\\Adrienne\\Documents\\Programming\\Python\\codeEval\\data\\fizzbuzzInput.txt'
    file = open(input)
    list = file.read().split('\n')
    for i in list:
        test = fizzbuzz(i)
        print("Test"+test+"Test")

def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases.readlines():
        a,b,n = map(int,(test.split(' ')))
        print(fizzbuzz(a,b,n))

    test_cases.close()

if __name__ == '__main__':
    import sys

    try:
        main()

    except Exception as e:
        print(e)
