import  tkinter as tk
window= tk.Tk()
canv=tk.Canvas(window, width=200, height=200, bg='yellow')
canv.pack()
'''canv.create_line(10,10,190,60)'''
'''canv.create_line(100,180,100,60, fill='red', dash=(10,2), width=7, activefill='blue', arrow='last', arrowshape= '20 40 20')'''

'''canv.create_rectangle(10,10,190,60)'''
'''canv.create_rectangle(60,80,140,190, fill='red', width=4, outline='blue', activedash=(10,2))'''
'''cor=[(100,30),(20,90),(180,90)]
canv.create_polygon(cor)'''
'''cor_1=[(50,50),(20,170),(180,170),(150,50)]
canv.create_polygon(cor_1, fill='orange', outline="blue", width=3, activefill=('yellow'))'''
'''canv.create_rectangle(150,80,190,120)'''
o=[canv.create_oval(50,10,150,110, fill='lightgray'),
canv.create_arc(50,10,150,110, start=0, extent=45, fill='red'),
canv.create_arc(50,10,150,110, start=240, extent=120, style='chord', fill='green'),
canv.create_arc(50,10,150,110, start=160, extent=-70, style='arc', fill='blue', width=5)]


canv.focus_set()
canv.bind('<Down>', lambda event:canv.move(o, 0,2))
canv.bind('<Up>', lambda event:canv.move(o, 0,-2))
canv.bind('<Left>', lambda event:canv.move(o, -2,0))
canv.bind('<Right>', lambda event:canv.move(o, 2,0))

print(canv.coords(o))
window.mainloop()