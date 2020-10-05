from tkinter import *

def bt_click():
    print("bt_click")
    lb["text"] = "Funcionou!"

screen = Tk()

# Instance - Pattern Container
lb = Label(screen, text="It's not a bug")
lb.place(x=100, y=150)

bt = Button(screen, width=20, text="Ok", command=bt_click)
bt.place(x=100, y=100)


screen.geometry("300x300+200+200")
screen.mainloop()