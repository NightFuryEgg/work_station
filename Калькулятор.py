import tkinter as tk
import ast

def chek():# наличие символов
    if ent_2.get()=='' and ent_1.get()=='':
        lab.config(fg='red')
        lab['text'] = 'Error: Введи хоть что-нибудь'
        help = 'No'
    elif ent_1.get()=='':
        lab.config(fg='red')
        lab['text']='Error: Введи число в первую строку'
        help='No'
    elif ent_2.get()=='':
        lab.config(fg='red')
        lab['text']='Error: Введи число во вторую строку'
        help = 'No'
    else:
        help='Yes'
    return help

def chek_num(a,b):# отсутствие иных символов, кроме цифр
    if ',' in a or ',' in b:
        lab.config(fg='red')
        lab['text'] = 'Error: Запиши дробь через точку'
        help = 'No'
        return help
    else:
        try:
            ast.literal_eval(a), ast.literal_eval(b)
        except ValueError:
            lab.config(fg='red')
            lab['text']='Error: Как я тебе выполню это действие?'
            help='No'
            return help
        except SyntaxError:
            lab.config(fg='red')
            lab['text'] = 'Error: Как я тебе выполню это действие?'
            help = 'No'
            return help
        else:
            return ast.literal_eval(a), ast.literal_eval(b)

def function_1():
    if chek()=='Yes':
        if chek_num(ent_1.get(),ent_2.get())=='No':
            pass
        else:
            s_1,s_2 = chek_num(ent_1.get(),ent_2.get())
            lab.config(fg='black', font=("Comic", 10))
            rez=s_1+s_2
            lab['text']=f'{rez:.2f}'
def function_2():
    if chek() == 'Yes':
        if chek_num(ent_1.get(), ent_2.get()) == 'No':
            pass
        else:
            lab.config(fg='black', font=("Comic", 10))
            s_1,s_2 = chek_num(ent_1.get(),ent_2.get())
            rez = s_1 - s_2
            lab['text'] = f'{rez:.2f}'
def function_3():
    if chek() == 'Yes':
        if chek_num(ent_1.get(), ent_2.get()) == 'No':
            pass
        else:
            lab.config(fg='black', font=("Comic", 10))
            s_1,s_2 = chek_num(ent_1.get(),ent_2.get())
            rez = s_1 * s_2
            lab['text'] = f'{rez:.2f}'
def function_4():
    if chek() == 'Yes':
        if chek_num(ent_1.get(), ent_2.get()) == 'No':
            pass
        else:
            lab.config(fg='black', font=("Comic", 10))
            s_1,s_2 = chek_num(ent_1.get(),ent_2.get())
            try:
                rez = s_1 / s_2
            except ZeroDivisionError:
                lab.config(fg='red')
                lab['text'] = 'Error: На ноль не дели'
            else:
                lab.config(fg='black', font=("Comic", 10))
                lab['text'] = f'{rez:.2f}'

window=tk.Tk()

ent_1=tk.Entry(width=15)
ent_2=tk.Entry(width=15)

but_1=tk.Button(text='+', width=20, height=1, command = function_1)
but_2=tk.Button(text='-', width=20, height=1, command = function_2)
but_3=tk.Button(text='*', width=20, height=1, command = function_3)
but_4=tk.Button(text='/', width=20, height=1, command = function_4)

lab=tk.Label(font=("Comic",10, 'bold'))

def ending():
    ent_1.pack()
    ent_2.pack()
    but_1.pack()
    but_2.pack()
    but_3.pack()
    but_4.pack()
    lab.pack()
    window.mainloop()

ending()