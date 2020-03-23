n = int(input())
f1 = 0
f2 = 1
k = 0
f = 0
if n == 0:
    f = f1
elif n == 1:
    f = f2
elif n >= 2:
    while k <= n - 2:
        f = f1 + f2
        f1 = f2
        f2 = f
        k += 1
print(f)
