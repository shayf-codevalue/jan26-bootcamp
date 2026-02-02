def primeNums(N):
	for i in range (N):
		flag = 0
		for j in range i:
			if (j != 1 and j != i):
				if ( i % j == 0):
					flag = 1
		if (flag = 0):
			print(i)