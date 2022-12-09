


def printSet(X):
    for i in range(0, 3):
        print(X[i], "/", elt[i], end=' + ')
    print(X[3], "/", elt[3], end='}')

elt = ['w', 'x', 'y', 'z']
A = [0.5, 0.4, 0.3, 0.2]
B = [0.2, 0.1, 0.2, 1]
U = []
print("elements=", elt)
print("set A=", A)
print("set B=", B)
for i in range(0, 4):
    if A[i] > B[i]:
        U.append(A[i])
    else:
        U.append(B[i])
print("Union={")
printSet(U)
print()
I = []
for i in range(0, 4):
    if A[i] < B[i]:
        I.append(A[i])
    else:
        I.append(B[i])
print()
print("Intersection")
printSet(I)
print()
AC = []
BC = []
print("Complement of A")
for i in range(0, 4):
    AC.append(1-A[i])
    output = round(AC[i], 2)
printSet(AC)
print()
print("Complement of B")
for i in range(0, 4):
    BC.append(1-B[i])
printSet(BC)
print()
AMB = []
BMA = []
print()
for i in range(0, 4):
    if A[i] < BC[i]:
        AMB.append(A[i])
    else:
        AMB.append(BC[i])
print()
print("Difference of A/B")
printSet(AMB)
print()
for i in range(0, 4):
    if B[i] < AC[i]:
        BMA.append(B[i])
    else:
        BMA.append(AC[i])
print()
print("Difference of B/A")
printSet(BMA)
print()
