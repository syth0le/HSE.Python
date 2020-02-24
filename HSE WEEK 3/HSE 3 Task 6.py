import math
p = int(input())
x = int(input())
y = int(input())
p1 = p / 100
if p / 100 != p // 100:
    sumKop = y + (y * p1) % 100
    sumRub = x + (p1 * x) + (y * p1) // 100
    valueKop = (sumRub - math.floor(sumRub)) * 100
    if valueKop + 0.5 >= math.ceil(valueKop):
        print(math.floor(sumRub), math.ceil(valueKop))
    elif valueKop + 0.5 < math.ceil(valueKop):
        print(math.floor(sumRub), math.floor(valueKop))
elif p / 100 == p // 100:
    sumKop1 = math.ceil((y + ((y * (p // 100)) % 100)) % 100)
    sumRub1 = math.ceil(x + (x * (p // 100)) + ((y * (p // 50)) // 100))
    print(sumRub1, sumKop1)
