num = int(input())
if num % 400 == 0:
    print("YES")
elif num % 100 == 0:
    print("NO")
elif num % 4 == 0:
    print("YES")
else:
    print("NO")
