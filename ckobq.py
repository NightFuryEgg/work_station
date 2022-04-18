def cer(r):
    s=r
    rez=int(s[0])+int(s[2])
    print(rez)
    return rez
def scob(s):
    n_s=''
    while len(s)>0:
        char = s[0]
        s = s[1:]
        if char=='(':
            temp,s=scob(s)
            n_s+=str(cer(temp))
        elif char==')':
            print(n_s)
            return n_s,s
        else:
            n_s+=char

    return n_s


s='(1+1)*2'
print(scob(s))
