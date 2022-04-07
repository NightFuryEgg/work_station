import tkinter as tk
window= tk.Tk()

fr1=tk.LabelFrame(text='Пример')
fr1.pack(padx=5,pady=5)
fr2=tk.LabelFrame(text='Решение')
fr2.pack(padx=5,pady=5)

ent=tk.Entry(fr1,width=35, font=("Times",20))
but_1=tk.Button(fr1, text='Вычислить', font=("Times",15))

text=tk.Text(fr2, height=10, width=35,font=("Times",20),wrap='none')

scroll=tk.Scrollbar(fr2, command=text.yview)
text.config(yscrollcommand=scroll.set)

scroll_1=tk.Scrollbar(fr2, command=text.xview, orient='horizontal')
text.config(xscrollcommand=scroll_1.set)

but_2=tk.Button(text='Очистить',font=("Times",15))





ent.pack(padx=5)
but_1.pack(pady=3)
scroll_1.pack(side='bottom', fill="x",anchor='w')
text.pack(padx=5, side='left')
scroll.pack(side='left',fill="y")
but_2.pack(pady=3)
window.mainloop()