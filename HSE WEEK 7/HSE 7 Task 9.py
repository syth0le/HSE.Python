man = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_every1, known_by_some1 = set.intersection(*man), set.union(*man)
print(len(known_by_every1), *sorted(known_by_every1), sep='\n')
print(len(known_by_some1), *sorted(known_by_some1), sep='\n')
