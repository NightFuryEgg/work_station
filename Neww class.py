import random as r
import pickle
class car:
    mark=""
    vehicle=0

n=5
garage=[]
for i in range(n):
    garage.append(car())
    garage[i].mark='M'+str(i+1)
    garage[i].vehicle=r.randint(10,100)


'''for i in range(0,len(garage)-1):
    for j in range(len(garage)-2,i-1,-1):
        if garage[j].vehicle > garage[j+1].vehicle:
            garage[j],garage[j+1]=garage[j+1],garage[j]

for i in range(len(garage)):
    print(garage[i].mark, garage[i].vehicle, sep=' | ')'''

garage.sort(key=lambda x: (x.vehicle)%10)

file=open('garage.dat','wb')
pickle.dump(garage,file)
file.close()

for i in range(len(garage)):
    print(garage[i].mark, garage[i].vehicle, sep=' | ')

file=open('garage.dat','rb')
garage_1=[]

while True:
    try:
        aux=pickle.load(file):
        garage_1.append(aux)
    except:
        break