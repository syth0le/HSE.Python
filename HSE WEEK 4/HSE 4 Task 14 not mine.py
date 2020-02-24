def multiplication(a, n):
    if 0 == a == n:
        return 1
    if 0 == a:
        return 0
    if 0 == n:
        return 1
    if n % 2 == 0:
        return multiplication(a, n / 2) ** 2
    return a * multiplication(a, n - 1)


a = float(input())
n = float(input())
print(multiplication(a, n))
