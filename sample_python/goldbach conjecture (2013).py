#-------------------------------------------------------------------------------
# Name:   goldbach conjecture.py
# Purpose:	Tests GoldBach's Conjecture
#
# Author:      Adrienne Sands
#
# Created:     05/05/2013
# Copyright:   (c) Adrienne Sands 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("this program checks to make sure a number is even"
        "then finds two prime numbers that add to that number.")
    n=eval(input("enter a number: "))

    if n%2 != 0:
        print(n,"isn't even. ")

    else:
        decFactor = n//2
        incFactor = n//2
        factorSum = 0
        goldbach = False

        while (decFactor > 1) and (goldbach == False):
            if (isPrime(decFactor) and isPrime(incFactor)):
                goldbach = True
                break
            decFactor = decFactor - 1
            incFactor = incFactor + 1

        if goldbach == True: print("{0} and {1} sum to {2} and are both prime."
            .format(decFactor,incFactor,n))
        else: print("Maybe Goldbach wasn't such a smart guy after all.")

def isPrime(n):
    import math
    divisor = 2
    isPrime = True

    while (divisor <= math.sqrt(n)) and (isPrime):
        if n % divisor == 0:
            isPrime = False
            break
        divisor = divisor + 1

    if isPrime: return True
    else: return False

if __name__ == '__main__':
    main()
