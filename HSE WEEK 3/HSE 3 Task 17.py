string = input()
a = string.find('h')
b = string.rfind('h')
print(string[0:b], string[a+1:], sep='')
