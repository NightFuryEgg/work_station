def s(a):
    aux=0
    for i in a:
        aux+=i
    return aux
def enter():
    flag=True
    while flag:
        N= int(input('введите натуральное число'))
        if N>0:
            flag=False
    return N

def fib(k):
    a=[1,1]
    i=0
    while a[i]+a[i+1] < k:
        a.append(a[i]+a[i+1])
        i+=1
    return a if k!=1 else [0]
N=enter()
k=s(fib(N))
print(fib(N))
print(k)