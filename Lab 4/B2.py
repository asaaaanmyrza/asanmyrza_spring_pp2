def evens(n):
    for i in range (n + 1):
        if (i%2==0):
            print(i)

n = int(input("Enter the number: "))
evens(n)