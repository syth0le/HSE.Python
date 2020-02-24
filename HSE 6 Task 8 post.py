marks = map(int, input().split())
cntMarks = [0] * 11
for mark in marks:
    cntMarks[mark] += 1
for nowMark in range(11):
    print((str(nowMark) + ' ') * cntMarks[nowMark], end='')


