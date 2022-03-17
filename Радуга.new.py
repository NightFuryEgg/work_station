import tkinter as tk

window=tk.Tk()
f_top = tk.Frame(window)
def func_r():
    function(but_1['bg'],but_1['text'])
def func_o():
    function(but_2['bg'],but_2['text'])
def func_y():
    function(but_3['bg'],but_3['text'])
def func_g():
    function(but_4['bg'],but_4['text'])
def func_b():
    function(but_5['bg'],but_5['text'])
def func_d():
    function(but_6['bg'],but_6['text'])
def func_p():
    function(but_7['bg'],but_7['text'])

def function(a,b):
    a=a[1:]
    ent.delete(0,len(but_1['text']))
    ent.insert(0,a)
    lab['text']=b

lab=tk.Label(font=("Comic",10, 'bold'), height=2)
ent=tk.Entry(width=20, justify='center')

but_1=tk.Button(text='красный', width=4, height=2, command = func_r, bg='#ff0000', fg='#ff0000',activebackground='#ff0000', activeforeground='#ff0000')
but_2=tk.Button(text='оранжевый', width=4, height=2, command = func_o, bg='#ff7d00', fg='#ff7d00',activebackground='#ff7d00', activeforeground='#ff7d00')
but_3=tk.Button(text='жёлтый', width=4, height=2, command = func_y, bg='#ffff00', fg='#ffff00',activebackground='#ffff00', activeforeground='#ffff00')
but_4=tk.Button(text='зелёный', width=4, height=2, command = func_g, bg='#00ff00', fg='#00ff00',activebackground='#00ff00', activeforeground='#00ff00')
but_5=tk.Button(text='голубой', width=4, height=2, command = func_b, bg='#007dff', fg='#007dff',activebackground='#007dff', activeforeground='#007dff')
but_6=tk.Button(text='синий', width=4, height=2, command = func_d, bg='#0000ff', fg='#0000ff',activebackground='#0000ff', activeforeground='#0000ff')
but_7=tk.Button(text='фиолетовый', width=4, height=2, command = func_p, bg='#7d00ff', fg='#7d00ff',activebackground='#7d00ff', activeforeground='#7d00ff')


def ending():
    lab.pack()
    ent.pack()
    f_top.pack(ipady=5)
    but_1.pack(side='left',padx=1,pady=2, ipadx=1)
    but_2.pack(side='left',padx=1,pady=2)
    but_3.pack(side='left',padx=1,pady=2)
    but_4.pack(side='left',padx=1,pady=2)
    but_5.pack(side='left',padx=1,pady=2)
    but_6.pack(side='left',padx=1,pady=2)
    but_7.pack(side='left',padx=1,pady=2)
    window.mainloop()

ending()