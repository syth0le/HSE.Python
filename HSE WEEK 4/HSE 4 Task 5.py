import math


def IsPointInSquare(a, b):
    if a <= 0 and b <= 0:
        if -1 <= a + b <= 1:
            return True
        else:
            return False
    elif a >= 0 and b <= 0:
        if -1 <= a - b <= 1:
            return True
        else:
            return False
    elif a <= 0 and b >= 0:
        if -1 <= b - a <= 1:
            return True
        else:
            return False
    elif a >= 0 and b >= 0:
        if -1 <= a + b <= 1:
            return True
        else:
            return False
    elif a == 0 and b == 0:
        if -1 <= a + b <= 1:
            return True
        else:
            return False

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
