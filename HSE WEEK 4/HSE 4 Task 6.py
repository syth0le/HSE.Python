import math


def IsPointInCircle(x, y, xc, yc, r):
    ex = ((x - xc) ** 2)
    ey = ((y - yc) ** 2)
    if math.sqrt(ex + ey) <= r:
        return True
    else:
        return False


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
