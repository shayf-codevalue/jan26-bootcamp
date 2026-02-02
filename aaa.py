def primenumber(N):
{
    for i in range(2, N + 1):
        Flag=True
        for j in range(2, i):
          if i % j == 0:
           Flag = False	
        if Flag : print(i) 
}