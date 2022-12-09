
x=[0.2, 0.3, 0.4]
w=[0.1 , 0.2 , 0.3 ]
yin=0
for i in range(3):
    yin=yin + x[i]*w[i]

print("net input Yin = ", yin)

if(yin<0):
    output=0
elif (yin>1):
    output=1
else :
    output=yin

print (" Output : " , output)
