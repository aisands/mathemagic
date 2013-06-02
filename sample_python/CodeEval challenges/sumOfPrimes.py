#__author__ = 'Adrienne'
#Challenge Description:
#Write a program to determine the sum of the first 1000 prime numbers.
#Input sample:
#   None
#
#Output sample:
#Your program should print the sum on stdout, i.e. 3682913

def sumOfPrimes(n=1000):
    primes = []
    num = 2

    while len(primes)< n:
        if checkIfPrime(num):
            primes.append(num)
        num += 1
    return sum(primes)

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
    print(sumOfPrimes())

if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e)
