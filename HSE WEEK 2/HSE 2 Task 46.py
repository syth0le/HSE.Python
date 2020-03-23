n = int(input())
max = 0
k = 0
pred1 = 0
pred2 = 0
while n != 0:
    if n > pred1:
        k += 1
        if pred1 < pred2:
            k = 2
        if k >= max:
            max = k
    elif n < pred1:
        k += 1
        if pred1 > pred2:
            k = 2
        if k >= max:
            max = k
    elif n == pred1:
        k = 1
    pred2 = pred1
    pred1 = n
    n = int(input())
print(max)
