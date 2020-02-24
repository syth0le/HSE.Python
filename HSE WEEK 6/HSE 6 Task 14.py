def marksUp(var, ex_marks):
    if len(ex_marks) <= var:
        return 0
    elif ex_marks[0] == ex_marks[var]:
        return 1
    for i in range(var, 0, -1):
        if ex_marks[i] < ex_marks[i - 1]:
            return ex_marks[i - 1]


inFile = open('input.txt', 'r', encoding='UTF8')
ex_marks = []
var = int(inFile.readline())
for line in inFile:
    a = int(line.split()[-3])
    b = int(line.split()[-2])
    c = int(line.split()[-1])
    if a > 39 and b > 39 and c > 39:
        ex_marks.append(a + c + b)
ex_marks.sort(reverse=True)
inFile.close()
print(marksUp(var, ex_marks))
