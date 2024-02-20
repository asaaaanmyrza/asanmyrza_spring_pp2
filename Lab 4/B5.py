def tozero(n):
    while n >=0:
        yield (n)
        n-=1

n = int(input("Enter the number: "))

for num in tozero(n):
    print(num)