N = int(input())
a = ((N // 100) // 10)
b = ((N // 100) % 10)
c = ((N % 100) // 10)
d = ((N % 100) % 10)
t = (a - d) * (a - d) + (c - b) * (c - b) + 1
print(t)
