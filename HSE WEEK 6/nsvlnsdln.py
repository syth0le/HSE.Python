def pizdec(k, list):
    if len(list) <= k:
        return 0
    elif list[0] == list[k]:
        return 1
    for i in range(k, 0, -1):
        if list[i] < list[i - 1]:
            return list[i - 1]


inFile = open('input.txt', 'r', encoding='utf8')
k = int(inFile.readline())
list = []
for line in inFile:
    a, b, c = [int(i) for i in line.split()[-3:]]
    if a >= 40 and b >= 40 and c >= 40:
        list.append(a + b + c)
inFile.close()
list.sort(reverse=True)
print(pizdec(k, list))
