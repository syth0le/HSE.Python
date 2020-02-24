N = int(input())
a = (N % 1440) // 60
b = (N % 60)
print(a, b)
