d=1000000
A=[1]

for k in range(2,101):
    r=0
    for i in range(len(A)):
        s=A[i]*k+r
        A[i]=s%d
        r=s//d
    if r>0:
        A.append(r)
print(A)
New=str(A.pop(-1))

for i in range(len(A)-2,-1,-1):
    New+='0'* (6-len(str(A[i])))+ str(A[i])
print(New)
