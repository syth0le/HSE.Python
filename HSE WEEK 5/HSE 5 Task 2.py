a = int(input())
b = int(input())
c = b + 1
d = b - 1
if a < b:
    for i in range(a, c):
        print(i)
elif a > b:
    for i in range(a, d, -1):
        print(i)
else:
    print(a)
