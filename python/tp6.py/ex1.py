T1=[]
T2=[]
T3=[]
for i in range(1,11):
    T1.append(i)
for j in range(11,21):
    T2.append(j)
for k in range(len(T1)):
    T3.append(T1[k]+T2[k])
print(T3) 
