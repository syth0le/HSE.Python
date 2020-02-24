A = int(input())
B = int(input())
print("YES" * (0 ** (A % B)), "NO" * (1 - 0 ** (A % B)), sep="")
