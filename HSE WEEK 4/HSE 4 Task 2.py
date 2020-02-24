import math


def distance(x1, y1, x2, y2):
    if x1 > x2 and y1 > y2:
        tempx = x1 - x2
        tempy = y1 - y2
        dist = (tempx ** 2) + (tempy ** 2)
        sqrDist = math.sqrt(dist)
        return sqrDist
    elif x1 < x2 and y1 < y2:
        tempx = x2 - x1
        tempy = y2 - y1
        dist = (tempx ** 2) + (tempy ** 2)
        sqrDist = math.sqrt(dist)
        return sqrDist
    elif x1 > x2 and y1 < y2:
        tempx = x1 - x2
        tempy = y2 - y1
        dist = (tempx ** 2) + (tempy ** 2)
        sqrDist = math.sqrt(dist)
        return sqrDist
    elif x1 < x2 and y1 > y2:
        tempx = x2 - x1
        tempy = y1 - y2
        dist = (tempx ** 2) + (tempy ** 2)
        sqrDist = math.sqrt(dist)
        return sqrDist
    elif x1 == x2 or y1 == y2:
        tempx = x2 - x1
        tempy = y1 - y2
        dist = (tempx ** 2) + (tempy ** 2)
        sqrDist = math.sqrt(dist)
        return sqrDist


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print('{0:.6}'.format(distance(x1, x2, y1, y2)))
