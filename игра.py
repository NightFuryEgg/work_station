class TRoad:
    def __init__(self, lendth_user, width_user):
        if lendth_user>0:
            self.lendth=lendth_user
        else:
            self.lendth=0
        if width_user>0:
            self.width=width_user
        else:
            self.width=0
class TCar:
    def __init__(self, road_user, p_user, v_user):
        self.road=road_user
        self.p=p_user
        self.v=v_user
        self.x=0
    def move(self):
        self.x+=self.v
        if self.x>self.road.lendth:
            self.x=0
class TLight:
    red=0
    redyellow=1
    green=2
    yellow=3
    def __init__(self, x_user,road_user):
        self.road=road_user
        if self.road.lendth>x_user and x_user>=0:
            self.x=x_user
        else:
            self.x=0
        self.stage=self.red
    def timer(self):
        pass

n=3
road=TRoad(120,n)

cars=[]
for i in range(n):
    cars.append(TCar(road,i+1,(i+1)*2 ))
print(f'Дорога: длинна={road.lendth}, ширина={road.width} полос')
print('Свойства машин:{}')
for i in range(n):
    print(f'{i}: Полоса ={cars[i].p}, скорость ={cars[i].v} x={cars[i].x}')
time=10
for i in range(time):
    for car in cars:
        car.move()
print('Свойства машин:{}')
for i in range(n):
    print(f'{i}: Полоса ={cars[i].p}, скорость ={cars[i].v} x={cars[i].x}')

light=TLight(road, 50)
print(light.x)
