string1 = input()
a = string1.find('f')
string2 = string1[a+1:]
b = string2.find('f')
if a == -1:
    print(-2)
elif b == -1:
    print(-1)
else:
    string3 = (string1[0:a] + string1[a+1:])
    c = string3.find('f')
    print(c + 1)
