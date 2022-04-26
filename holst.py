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
canv.create_rectangle(150,100,170,120)
canv.create_oval(150,100,170,120)

window.mainloop()