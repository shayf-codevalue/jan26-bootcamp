def primenumber(N):
{
    for i in range(2, N + 1):
        Prime=True
        for j in range(2, i):
          if i % j == 0:
           Prime = False
	   break
        if Prime : print(i) 
}// test commit
