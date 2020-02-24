num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 - num3 == 1 and num2 - num4 == 1:
    print("YES")
elif num3-num1 == 1 and num4 - num2 == 1:
    print("YES")
elif num1 - num3 == 1 and num4 - num1 == 1:
    print("YES")
elif num3 - num1 == 1 and num2 - num4 == 1:
    print("YES")
elif num1 - num3 == 0 and num2 - num4 == 1:
    print("YES")
elif num1 - num3 == 0 and num4 - num2 == 1:
    print("YES")
elif num1 - num3 == 1 and num2 - num4 == 0:
    print("YES")
elif num3 - num1 == 1 and num2 - num4 == 0:
    print("YES")
else:
    print("NO")
