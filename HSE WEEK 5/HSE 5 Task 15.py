numList = input().split()
k = 0
long = len(numList)
for i in range(0, long):
    if int(numList[i]) > 0:
        k += 1
print(k)
