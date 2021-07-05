from tkinter import *

window = Tk()

def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=500, height=500)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()