a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    print(c)
elif a >= b >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a >= c >= b:
    print(a)
elif c >= a >= b:
    print(c)
