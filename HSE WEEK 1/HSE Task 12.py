A = int(input())
B = int(input())
N = int(input())
print(((A * 100 + B) // 100 * N) + (B * N // 100), B * N % 100)
