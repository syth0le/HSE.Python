p = int(input())
x = int(input())
y = int(input())
money_before = 100 * x + y
money_after = int(money_before * (100 + p) / 100)
print(money_after // 100, money_after % 100)
