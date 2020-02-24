numList = input().split()
long = len(numList)
number = 1000
for i in range(0, long):
    if 0 < int(numList[i]) < number:
        number = int(numList[i])
print(number)
