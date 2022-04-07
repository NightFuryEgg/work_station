import tkinter as tk

window = tk.Tk()
ent=tk.Entry(window, width=20)
lab=tk.Label(window, text="Привет Мир!")
but=tk.Button(window, text="Преобразовать")

ent.pack()
lab.pack()
but.pack()
window.mainloop()