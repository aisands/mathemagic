#Author: 'Adrienne'
#Challenge Description:  Print out the grade school multiplication table up to 12*12.
#Input sample: None
#Output sample: Print out the table in a matrix like fashion, each number formatted to a width of 4 (The numbers are right-aligned and strip out leading/trailing spaces on each line). The first 3 line will look like:
#1   2   3   4   5   6   7   8   9  10  11  12
#2   4   6   8  10  12  14  16  18  20  22  24
#3   6   9  12  15  18  21  24  27  30  33  36

def printMultiples(num):
    print(num,end="")
    for i in range(2,13):
        print('%4s' % str(num*i),end="")
    print("")

def main():
    for i in range(1,13):
        printMultiples(i)

if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e)
