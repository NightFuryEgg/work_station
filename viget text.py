import tkinter as tk
window= tk.Tk()
def ins_t():
    string = 'Привет, Мир \n line 2\n line 3'
    text.insert(1.0, string)
    text.tag_add('title', 1.0, '1.end')
    text.tag_add('line2', 2.0, '2.end')
    text.tag_add('line3', 3.0, '3.end')
    text.tag_config('title', justify='center', font=('Arial', 20, 'bold'))
    text.tag_config('line2', justify='left', font=('Verdana', 15, 'bold'))
    text.tag_config('line3', justify='left', font=('Verdana', 15, 'bold'))


def del_t():
    text.delete(1.0, 'end')

def get_t():
    string=text.get(1.0, 'end')
    lab['text']=string
def sml():
    lab_sml=tk.Label(text=':-o', bg='yellow', font=(15))
    text.window_create('insert', window=lab_sml)

fr1=tk.Frame()
fr2=tk.Frame()


text= tk.Text(fr1,bg='green', height=20, width=40, fg='#FFFFFF', wrap='word')
scroll=tk.Scrollbar(command=text.yview)
text.config(yscrollcommand=scroll.set)
lab=tk.Label()


tk.Button(fr2, text='Del', command=del_t).pack(side='left')
tk.Button(fr2, text='get', command=get_t).pack(side='left')
tk.Button(fr2, text='insert', command=ins_t).pack(side='left')
tk.Button(fr2, text='Smile', command=sml).pack(side='left')

text.pack(side='left')
scroll.pack(side='right', fill="y")
fr1.pack()
fr2.pack()

lab.pack()
print(text['height'],text['width'])

window.mainloop()