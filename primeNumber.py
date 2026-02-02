def isPrime(n):
    if n <= 1:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def printPrimeNumbers(number):
    n = 0
    while n<=number:
        if isPrime(n):
            print(n)
        n+=1
