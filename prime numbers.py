def PrimeNumbersToN (N) :
    if N < 2:
        return

    for num in range(2, N + 1):
        x = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                x = False
                break
        if x:
            print(num)


N = int(input("הכנס מספר: "))

# שליחת המספר לפונקציה
PrimeNumbersToN(N)