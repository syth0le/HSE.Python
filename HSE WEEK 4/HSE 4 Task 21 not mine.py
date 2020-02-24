def Hanoi(n, x, y):
    if n > 0:
        Hanoi(n - 1, x, y)
        print(n, x, 2)
        Hanoi(n - 1, y, x)
        print(n, 2, y)
        Hanoi(n - 1, y, x)
        Hanoi(n - 1, x, y)
    return (n, x, y)


n = input()
print(Hanoi(n, 1, 3))
