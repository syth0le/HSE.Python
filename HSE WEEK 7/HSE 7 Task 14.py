emDict = {}
inFile = open("7_week_input.txt", 'r', encoding="UTF8")
lines = inFile.read()
words = lines.split()
numMassive = []
for word in words:
    if word in emDict:
        emDict[word] += 1
        numMassive.append(emDict[word])
    else:
        emDict[word] = 0
        numMassive.append(emDict[word])
print(*numMassive)
inFile.close()
