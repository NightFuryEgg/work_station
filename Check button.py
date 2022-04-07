import tkinter as tk
def nam():
    if var1.get()== 2:
        lab['bg']='yellow'
    else:
        lab['bg']='aqua'
    lab.config(font='Arial '+str(var2.get()))
    lab['fg'] = var3.get()

window= tk.Tk()
fr1=tk.Frame()
fr2=tk.Frame()

var1=tk.IntVar()
var1.set(2)
var2=tk.IntVar()
var2.set(10)
var3=tk.StringVar()
var3.set('black')


lab_2=tk.Label(fr1,text='Голосование')

ch1=tk.Checkbutton(fr1,text='Синий',variable=var1,onvalue=1, offvalue=2, command=nam)
ch2=tk.Checkbutton(fr1,text='Большой размер',variable=var2,onvalue=50, offvalue=30, command=nam)
ch3=tk.Checkbutton(fr1,text='Красный цвет',variable=var3,onvalue="red", offvalue="black", command=nam)

lab=tk.Label(fr2,text='0', bg='yellow', font=30)
lab.pack(fill='x')

lab_2.pack()
ch1.pack(anchor="w")
ch2.pack(anchor="w")
ch3.pack(anchor="w")
fr1.pack(side='left')
fr2.pack(side='left')
window.mainloop()