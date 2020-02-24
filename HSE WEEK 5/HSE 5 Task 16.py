numList = input().split()
k = 0
l = 0
long = len(numList)
for i in range(0, long):
    if int(numList[i]) >= k:
        k = int(numList[i])
        l = i
print(k, l)
