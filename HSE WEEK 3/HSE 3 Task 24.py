s = input()
sN1 = s[:1]
sN2 = s[-1]
sNew = s[1:-1]
s3 = sN1 + sNew.replace('', '*') + sN2
if len(s) == 1:
    print(s)
else:
    print(s3)
print(sN2)

неправильно(переделать):
stringInput = input()
a = len(stringInput)
i = 0
while i < a:
    string1 = (stringInput[:i+1])[i:]
    stringTemporary = string1 + '*'
    i += 2
return string1
    print(stringTemporary)
