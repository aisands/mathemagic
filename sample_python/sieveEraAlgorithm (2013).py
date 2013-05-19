#-------------------------------------------------------------------------------
# Name:        sieveEraAlgorithm.py
# Purpose:  finds all prime numbers up to some limit n (Sieve of Eratosthenes)
#
# Author:      Adrienne Sands
#
# Created:     19/05/2013
# Copyright:   (c) Adrienne Sands 2013
#-------------------------------------------------------------------------------
#to do: implement Sieve of Atkin (http://en.wikipedia.org/wiki/Sieve_of_Atkin)
#produces a list of all primes up to n using a Sieve algorithm
def sieveEra(n):
    if n == 1:
        return 0

    sieveList = [x for x in range(2,n+1)]
    primeList = []

    while True:
        i = sieveList[0]
        primeList.append(i)
        sieveList = [x for x in sieveList if x%i!=0]
        if len(sieveList)==0:
            break

    return primeList

def test():
    #test1: primes <= 1
    if sieveEra(1)!=0:
        print("Test 1 failed.")
    #test2: primes <= 2
    elif sieveEra(2)!=[2]:
        print("Test 2 failed.")
    #test3: sievelist test
    elif sieveEra(38)!=sieveEra(40):
        print("Test 3 failed.")
    else:
        print("Success!")

#prompts the user for a number and prints out a list of primes <= that number
def main():
    print("This program uses the Sieve algorithm to print all primes up to n")
    print("Note: This program will take a while for n larger than 100,000.")
    n = int(input("Enter a number: "))
    print("Here are prime numbers up to (and including) n:\n",sieveEra(n))

if __name__ == '__main__':
    main()
