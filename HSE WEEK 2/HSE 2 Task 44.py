n = int(input())
k = 1
a = ''
l = 0
h = 0
while k <= n:
    h = k
    while h != 0:
        a += str(h % 10)
        h = h // 10
    if int(a) == k:
        l += 1
    a = ''
    k += 1
print(l)
