import math
def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

a = int(input("Base1: "))
b = int(input("Base2: "))
h = int(input("Height: "))

print(trapezoid_area(a, b, h))