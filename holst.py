import  tkinter as tk
window= tk.Tk()

'''canv.create_line(10,10,190,60)'''
'''canv.create_line(100,180,100,60, fill='red', dash=(10,2), width=7, activefill='blue', arrow='last', arrowshape= '20 40 20')'''

'''canv.create_rectangle(10,10,190,60)'''
'''canv.create_rectangle(60,80,140,190, fill='red', width=4, outline='blue', activedash=(10,2))'''
'''cor=[(100,30),(20,90),(180,90)]
canv.create_polygon(cor)'''
'''cor_1=[(50,50),(20,170),(180,170),(150,50)]
canv.create_polygon(cor_1, fill='orange', outline="blue", width=3, activefill=('yellow'))'''
'''canv.create_rectangle(150,80,190,120)'''
'''canv.create_arc(50,10,150,110, start=0, extent=45, fill='red')
canv.create_arc(50,10,150,110, start=240, extent=120, style='chord', fill='green')
canv.create_arc(50,10,150,110, start=160, extent=-70, style='arc', fill='blue', width=5)'''


'''canv.focus_set()
canv.bind('<Down>', lambda event:canv.move(ball, 0,2))
canv.bind('<Up>', lambda event:canv.move(ball, 0,-2))
canv.bind('<Left>', lambda event:canv.move(ball, -2,0))
canv.bind('<Right>', lambda event:canv.move(ball, 2,0))
print(canv.coords(ball))'''

def motion():
    global xi
    global yi
    global v

    if (x-r)<=canv.coords(ball)[0]+v<(x-r)+v:
        xi=-v+0.3
    if -v <= canv.coords(ball)[0] -v <=0:
        xi=v-0.3
    if (y - r) <= canv.coords(ball)[1] + v < (y - r) + v:
        yi=-v
    if -v <= canv.coords(ball)[1] -v <=0:
        yi=v
    window.after(10,motion)
    canv.move(ball,xi,yi)

def motion1():
    global sxi
    global syi
    global sv

    if (x - r) <= canv.coords(ball_1)[0] + sv < (x - r) + sv:
        sxi = -sv + 0.3
    if -v <= canv.coords(ball_1)[0] - sv <= 0:
        sxi = sv - 0.3
    if (y - r) <= canv.coords(ball_1)[1] + sv < (y - r) + sv:
        syi = -sv
    if -sv <= canv.coords(ball_1)[1] - sv <= 0:
        syi = sv
    if canv.coords(ball)[0]>=canv.coords(ball_1)[0]<=x-canv.coords(ball_1)[0] + sv:
        sxi=sv-0.3
    window.after(10, motion1)
    canv.move(ball_1, sxi, syi)

x=800
y=300
r=50
v=2

sv=3

xi=-v
yi=v

sxi=sv
syi=sv

canv=tk.Canvas(window, width=x, height=y, bg='yellow')
canv.pack()
ball=canv.create_oval(60,40,60+r,40+r, fill='lightgray')
motion()
ball_1=canv.create_oval(700,120,700+r,120+r, fill='lightgray')
motion1()

window.mainloop()