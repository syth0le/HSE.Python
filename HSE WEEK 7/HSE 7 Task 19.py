inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
string = inFile.readlines()
candidates = []
for candidate in string:
    canSp = candidate.strip()
    candidates.append(canSp)
votes = len(candidates)
candidatesDict = {}
for can in candidates:
    candidatesDict[can] = candidatesDict.get(can, 0) + 1
candidatesDict = [(vot, cn) for cn, vot in candidatesDict.items()]
candidatesDict.sort(key=lambda x: x[0], reverse=True)
if candidatesDict[0][0] > (votes // 2):
    print(candidatesDict[0][1], file=outFile)
else:
    print(candidatesDict[0][1], candidatesDict[1][1], sep="\n", file=outFile)
inFile.close()
outFile.close()
