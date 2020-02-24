data = list(map(int, input().split()))
sum = 0
rezult = 0
i = 0
numList = []
while data[1] > 0:
    user = int(input())
    data[1] -= 1
    numList.append(user)
numList.sort()
for i in range(0, len(numList)):
    sum += numList[i]
    rezult += 1
while data[0] < sum:
    sum -= numList[rezult-1]
    rezult -= 1
print(rezult)
