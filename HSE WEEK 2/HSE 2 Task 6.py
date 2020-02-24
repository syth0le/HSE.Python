x = int(input())
y = int(input())
if (y // (y - x + 1)) == (y / (y - x + 1)):
    print("YES")
else:
    print("NO")
