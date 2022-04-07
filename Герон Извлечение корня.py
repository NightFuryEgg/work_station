import math
a=5/2
def isqrt(a):
    x_0 = a
    while True:
        x=(x_0**2+a)/(2*x_0)
        if x_0>x:
            x_0=x
        else:
            return x_0
print(isqrt(a))
print(math.sqrt(a))
print(a**0.5)