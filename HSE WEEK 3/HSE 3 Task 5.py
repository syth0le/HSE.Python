import math
n = float(input())
if n + 0.5 >= math.floor(n) + 1:
    print(math.ceil(n))
elif n + 0.5 < math.floor(n) + 1:
    print(math.floor(n))
