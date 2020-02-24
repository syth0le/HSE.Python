string = input()
a = string.find('h')
b = string.rfind('h')
print(string[0:a], string[b+1:], sep='')
