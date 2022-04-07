import tkinter as tk
def nam():
    lab['text']=str(var.get())
    if int(var.get())==1:
        lab.config(bg='red')
    elif int(var.get())==2:
        lab.config(bg='aqua')

window= tk.Tk()
fr1=tk.Frame()
fr2=tk.Frame()

var=tk.IntVar()
var.set(0)
lab_2=tk.Label(fr1,text='Голосование')
r1=tk.Radiobutton(fr1,text='First',variable=var,value=1, command=nam, indicatoron=0)
r2=tk.Radiobutton(fr1,text='Second',variable=var,value=2, command=nam, indicatoron=0)

lab=tk.Label(fr2,text='0', bg='yellow', font=30)
lab.pack(fill='x')

lab_2.pack()
r1.pack(anchor="w")
r2.pack(anchor="w")
fr1.pack(side='left')
fr2.pack(side='left')
window.mainloop()