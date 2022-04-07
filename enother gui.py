import tkinter as tk

def function():
    but_1["text"]='Изменено'
    but_1['bg']='yellow'
    but_1['activebackground']='green'
    but_1['activeforeground']='red'
    ent.delete(0,20)
    ent.insert(0,'Красный+')
window = tk.Tk()

but_1=tk.Button(text = 'Изменить', width=10, height= 3, bg='white')

lab=tk.Label(text='Hello world', font=("Comic",25, 'bold'))
lab.config(bg='#FFAAAA', bd=20)
ent=tk.Entry(width=50)


but_1.config(command = function)
but_1.pack()
lab.pack()
ent.pack()
window.mainloop()