def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("First number: "))
b = int(input("Secod number: "))

for square in squares(a, b):
    print(square)