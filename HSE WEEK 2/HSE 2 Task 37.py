n = int(input())
pred = n
k = 0
while n != 0:
    if n > pred:
        k += 1
    pred = n
    n = int(input())
print(k)
