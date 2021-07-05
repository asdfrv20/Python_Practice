from tkinter import *

class App: 
    def __init__(self):
        self.hello_check = False
        self.quit_check = False

        window = Tk()
        self.helloB = Button(window, text="Hello", command=self.Hello, fg="red", font=('돋움체', 15))
        self.helloB.pack(side=LEFT,padx=10)
        # helloB.place(x=0, y=0, width=100, height=20)
        self.quitB = Button(window, text="Quit", command=self.Quit, fg='green', font=('돋움체', 15))
        self.quitB.pack(side=LEFT,padx=10)
        # quitB.place(x=110, y=0, width=100, height=20)
        window.mainloop()

    def Hello(self):
        self.hello_check = not self.hello_check
        if self.hello_check:
            self.helloB['text'] = 'Welcome to the world!'
        else:
            self.helloB['text'] = 'Hello'

    def Quit(self):
        self.quit_check = not self.quit_check
        if self.quit_check:
            self.quitB['text'] = 'Quit button Pressed'
        else:
            self.quitB['text'] = 'Quit'

App()


        
