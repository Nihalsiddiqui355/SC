
s1 = [[1], [0], [0], [0]]
t1 = [0, 1]
s2 = [[1], [1], [0], [0]]
t2 = [0, 1]
s3 = [[0], [0], [0], [1]]
t3 = [1, 0]
s4 = [[0], [0], [1], [1]]
t4 = [1, 0]
w1new = []
w2new = []
for i in range(0, 4):
    w1 = s1[i][0]*t1[0]
    w2 = s1[i][0]*t1[1]
    w1new.append(w1)
    w2new.append(w2)
print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w1new[i], w2new[i])

w3new = []
w4new = []
for i in range(0, 4):
    w3 = s2[i][0]*t2[0]
    w4 = s2[i][0]*t2[1]
    w3new.append(w3)
    w4new.append(w4)
print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w3new[i], w4new[i])

w5new = []
w6new = []
for i in range(0, 4):
    w5 = s3[i][0]*t3[0]
    w6 = s3[i][0]*t3[1]
    w5new.append(w5)
    w6new.append(w6)
print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w5new[i], w6new[i])


w7new = []
w8new = []
for i in range(0, 4):
    w7 = s4[i][0]*t4[0]
    w8 = s4[i][0]*t4[1]
    w7new.append(w7)
    w8new.append(w8)
print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w7new[i], w8new[i])
w9 = []
w10 = []
for i in range(0, 4):
    w9new = w1new[i]+w3new[i]+w5new[i]+w7new[i]
    w9.append(w9new)
    w10new = w2new[i]+w4new[i]+w6new[i]+w8new[i]
    w10.append(w10new)
print("The final weight matrix is : ")
print("W = ")
for i in range(0, 4):
    print(w9[i], w10[i])
