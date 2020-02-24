def minOfFour(a, b, c, d):
    e = min(a, b)
    f = min(c, d)
    g = min(e, f)
    return g


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(minOfFour(a, b, c, d))
