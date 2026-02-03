def prime(untilnumber):
    for i in range(2, untilnumber):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

x = input("please enter a number: ")
x = int(x)
prime(x)