import turtle as t
t.speed(0)
n=4
a=300
def tre(n,a):
    if n==0:
        for i in range(3):
            t.forward(a)
            t.left(120)
    else:
        tre(n-1,a/2)
        t.forward(a/2)
        tre(n - 1, a / 2)
        t.forward(a/2)
        t.left(120)
        t.forward(a / 2)
        tre(n - 1, a / 2)
        t.left(60)
        t.forward(a/2)
        t.left(60)
        t.forward(a/2)
        t.left(120)
tre(n,a)
t.done()