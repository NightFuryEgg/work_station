import tkinter as tk
window= tk.Tk()

class TNode:
    pass

def newNode(d):
    node=TNode
    node.data=d
    node.left=None
    node.right=None
    return node

def makeTree(s):
    k=lastOp(s)
    if k<0:
        Tree = newNode(s)
    else:
        Tree=newNode(s[k])
        Tree.left=makeTree(s[:k])
        Tree.right=makeTree(s[k+1:])
    return Tree

def lastOp(s):
    minP=50
    k=-1
    for i in range(len(s)):
        if prior(s[i])<=minP:
            minP=prior(s[i])
            k=i
    return k

def prior(ch):
    if ch in '+-':
        return 1
    if ch in '/*':
        return 2
    return 100

def calcTree(Tree):
    if Tree.left==None:
        return int(Tree.data)
    else:
        n1 = calcTree(Tree.left)
        n2 = calcTree(Tree.right)
        if Tree.data=='+':
            res =n1+n2
        elif Tree.data == '-':
            res =n1-n2
        elif Tree.data == '*':
            res =n1*n2
        else:
            res=n1//n2

def calc():
    s=ent.get()
    tree=makeTree(s)
    res=calcTree(tree)
    s=s+' = ' + str(res)+'\n'
    ent.delete(0,"end")
    text.insert(0.1, s)

def clrscr():
    text.delete(0.1, 'end')

fr1=tk.LabelFrame(text='Пример')
fr1.pack(padx=5,pady=5)
fr2=tk.LabelFrame(text='Решение')
fr2.pack(padx=5,pady=5)

ent=tk.Entry(fr1,width=35, font=("Times",20))
but_1=tk.Button(fr1, text='Вычислить', font=("Times",15), command=calc)
but_2=tk.Button(text='Очистить',font=("Times",15), command=clrscr)
text=tk.Text(fr2, height=10, width=35,font=("Times",20),wrap='none')

scroll=tk.Scrollbar(fr2, command=text.yview)
text.config(yscrollcommand=scroll.set)

scroll_1=tk.Scrollbar(fr2, command=text.xview, orient='horizontal')
text.config(xscrollcommand=scroll_1.set)



ent.pack(padx=5)
but_1.pack(pady=3)
scroll_1.pack(side='bottom', fill="x",anchor='w')
text.pack(padx=5, side='left')
scroll.pack(side='left',fill="y")
but_2.pack(pady=3)
window.mainloop()