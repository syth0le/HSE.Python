num = int(input())
saveMin = 0
saveMax = 0
while num != 0:
    if saveMax >= saveMin >= num:
        saveMax = saveMax
        saveMin = saveMin
    elif saveMax >= num >= saveMin:
        saveMax = saveMax
        saveMin = num
    elif num >= saveMax >= saveMin:
        saveMin = saveMax
        saveMax = num
    num = int(input())
print(saveMin)
