inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
lines = sorted(lines)
for line in lines:
    print(*line.split()[:2] + line.split()[3:], file=outFile)
inFile.close()
outFile.close()
