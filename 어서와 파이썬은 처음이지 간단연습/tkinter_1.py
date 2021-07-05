# tkinter 간단한 이벤트 처리
from tkinter import *

callback_check = False

def callback():
    global callback_check
    callback_check = not callback_check
    if callback_check==True:
        button["text"] = "버튼이클릭되었음!"
    else:
        button["text"] = "클릭"

window = Tk()
button = Button(window, text="클릭", command=callback)
button.pack()

window.mainloop()