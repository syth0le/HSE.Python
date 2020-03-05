maxNum = int(input())
allNums = set(range(1, maxNum+1))
possibleNums = allNums
while True:
    nums = input()
    if nums == "HELP":
        break
    nums = {int(x) for x in nums.split()}
    answer = input()
    if answer == "YES":
        possibleNums &= nums
    else:
        possibleNums -= nums
print(*sorted(possibleNums))
