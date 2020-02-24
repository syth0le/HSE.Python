import math


def distance(x1, x2, y1, y2):
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    sqrtDist = math.sqrt(dist)
    return sqrtDist


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
perimetr1 = distance(x1, x2, y1, y2) + distance(x2, x3, y2, y3)
perimetr2 = perimetr1 + distance(x1, x3, y1, y3)
print('{0:.6}'.format(perimetr2))
