import math
a = float(input())
b = float(input())
c = float(input())
if b ** 2 - 4 * a * c < 0:
    print('')
elif b ** 2 - 4 * a * c == 0:
    x1 = - b / (2 * a)
    print('{0:.6}'.format(x1))
elif b ** 2 - 4 * a * c > 0:
    x1 = (- b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x2 > x1:
        print('{0:.6}'.format(x1), '{0:.6}'.format(x2))
    elif x2 < x1:
        print('{0:.6}'.format(x2), '{0:.6}'.format(x1))
    else:
        print('{0:.6}'.format(x1), '{0:.6}'.format(x2))
