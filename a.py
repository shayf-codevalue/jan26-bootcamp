def primeNumbers(N):
    for i in range (2,N+1):
        flag=True
        for j in range(2,N):
            if i%j==0:
                flag=False
        if flag:
            print (i)