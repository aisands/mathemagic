#__author__ = 'Adrienne'
#Challenge Description:
#Write a program to determine the biggest prime palindrome under 1000.
#Input sample:
#   None
#
#Output sample:
#Your program should print the largest palindrome on stdout. i.e. 929

def primePalindrome(n=1000):
    out = 1
    for i in range(1,n+1):
        if checkIfPalindrome(i) and checkIfPrime(i):
            out = max(out,i)

    return out

def checkIfPalindrome(num):
    num = str(num)
    return num == num[::-1]

def checkIfPrime(num):
    isPrime = True
    if num ==1 :
        return True

    else:
        for div in range(2,(num//2)+1):
            if num % div == 0:
                isPrime = False
                break

        return isPrime

def main():
    print(primePalindrome())


if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e)
