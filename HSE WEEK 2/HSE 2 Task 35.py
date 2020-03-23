n = int(input())
k = 0
sum = 0
while n != 0:
    sum += n
    k += 1
    n = int(input())
print(sum / k)
