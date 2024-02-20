import math
def regular_polygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


s = int(input)
l = int(input())

area = regular_polygon_area(s, l)
print( int(area))
