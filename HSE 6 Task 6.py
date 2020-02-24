town = int(input())
distTown = list(map(int, input().split()))
shelter = int(input())
distShelter = list(map(int, input().split()))
rez_distTown = distTown[:town]
rez_distShelter = distShelter[: shelter]
i = 0
k = 0
result = []
rez_distTown.sort()
rez_distShelter.sort()
zhopa = int(rez_distTown[i])
while i <= len(rez_distTown):
    if rez_distShelter[k] == rez_distTown[i]:
        result.append(distShelter.index(rez_distShelter[k])) 
        k += 1
        i += 1
    elif rez_distShelter[k] != rez_distTown[i]:
        if len(distShelter[:k + 1]) <= shelter:  # abs(переменная)
            l = min(distShelter[k - 1] - distTown[i], distShelter[k] - distTown[i])
            if l < 0:
                m = min(-l, distShelter[k + 1] - distTown[i])
            else:
                m = min(l, distShelter[k + 1] - distTown[i])
            if m < 0:
                result.append(distShelter.index(-m + zhopa))
            else:
                result.append(distShelter.index(m + zhopa))
            i += 1
            k += 1
        else:
            l = min(distShelter[k - 1] - distTown[i], distShelter[k] - distTown[i])
            if l < 0:
                result.append(distShelter.index(-l + zhopa))
            else:
                result.append(distShelter.index(l + zhopa))
            i += 1
            k += 1
print(*result)
