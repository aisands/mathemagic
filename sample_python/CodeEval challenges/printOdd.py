#Author: 'Adrienne'
#Challenge Description: Print the odd numbers from 1 to 99.
#Input sample: None
#Output sample: Print the odd numbers from 1 to 99, one number per line.

def printOdd(num):
    for i in range (1,num+1):
        if i%2 !=0:
            print(i)
def main():
    printOdd(99)

if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e)
