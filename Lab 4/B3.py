def divisible(n):
    for i in range (n + 1):
        if(i%3==0 or i%4==0):
            print(i)

n = int(input("Enter the number: "))
divisible(n)