import turtle as ts
n=3
a=200 #длина квадрата
x=200 #длина полоски древа
t.speed(7)
t.left(90)
t.up()
t.backward(300)
t.down()
def side_line(a):
    return side_kv(a)+(side_kv(a)//2)
def side_kv(a):
    return a//(2**0.5)
def kv(a):
    n=3
    t.left(90)
    t.forward(a//2)
    while n!=0:
        t.left(90)
        t.forward(a)
        n-=1
    t.left(90)
    t.forward(a // 2)
    t.right(90)
def tree(n,a,x):
    t.up()
    t.forward(x)
    t.down()
    kv(a)
    if n!=0:
        t.left(45)
        tree(n-1,side_kv(a),side_line(a))
        t.right(90)
        tree(n-1,side_kv(a),side_line(a))
        t.left(45)
    t.up()
    t.backward(a+a//2)
    t.down()

tree(n,a,x)
t.done()