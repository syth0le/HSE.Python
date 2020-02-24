A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
if A2 == A1 and B2 == B1 and C2 == C1:
    print('Boxes are equal')
elif A2 == A1 and B2 == C1 and C2 == B1:
    print('Boxes are equal')
elif A2 == B1 and B2 == A1 and C2 == C1:
    print('Boxes are equal')
elif A2 == B1 and B2 == C1 and C2 == A1:
    print('Boxes are equal')
elif A2 == C1 and B2 == A1 and C2 == C1:
    print('Boxes are equal')
elif A2 == C1 and B2 == C1 and C2 == A1:
    print('Boxes are equal')

elif A2 > A1 and B2 == B1 and C2 == C1:
    print('The first box is larger than the second one')
elif A2 == A1 and B2 > B1 and C2 == C1:
    print('The first box is larger than the second one')
elif A2 == A1 and B2 == B1 and C2 > C1:
    print('The first box is larger than the second one')
elif A2 > A1 and B2 > C1 and C2 == B1:
    print('The first box is larger than the second one')
elif A2 > A1 and B2 == C1 and C2 > B1:
    print('The first box is larger than the second one')
elif A2 == A1 and B2 > C1 and C2 > B1:
    print('The first box is larger than the second one')
elif A2 > A1 and B2 > C1 and C2 > B1:
    print('The first box is larger than the second one')

elif A2 == B1 and B2 == A1 and C2 == C1:
    print('The first box is larger than the second one')
elif A2 == B1 and B2 == C1 and C2 == A1:
    print('The first box is larger than the second one')
elif A2 == C1 and B2 == A1 and C2 == C1:
    print('The first box is larger than the second one')
elif A2 == C1 and B2 == C1 and C2 == A1:
    print('The first box is larger than the second one')

elif A2 == A1 and B2 == B1 and C2 == C1:
    print('Boxes are equal')
elif A2 == A1 and B2 == B1 and C2 == C1:
    print('Boxes are equal')
elif A2 == A1 and B2 == C1 and C2 == B1:
    print('Boxes are equal')
elif A2 == B1 and B2 == A1 and C2 == C1:
    print('Boxes are equal')
elif A2 == B1 and B2 == C1 and C2 == A1:
    print('Boxes are equal')
elif A2 == C1 and B2 == A1 and C2 == C1:
    print('Boxes are equal')
elif A2 == C1 and B2 == C1 and C2 == A1:
    print('Boxes are equal')

elif A1 * B1 * C1 > A2 * B2 * C2:
    print('he first box is larger than the second one')
elif A1 * B1 * C1 < A2 * B2 * C2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')



Boxes are equal, если коробки одинаковые,

The first box is smaller than the second one, если первая коробка может быть положена во вторую,

The first box is larger than the second one, если вторая коробка может быть положена в первую,

Boxes are incomparable, во всех остальных случаях