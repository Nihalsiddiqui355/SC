

x = [0.2, 0.3, 0.4]
w = [0.1, 0.2, 0.3]

yin = 0
theta=0.5
for i in range(3):
    yin = yin + x[i]*w[i]
print("Net input Yin=", yin)

if (yin < theta):
    output = 0
elif (yin > theta):
    output = 1
    print("Output:-", output)
