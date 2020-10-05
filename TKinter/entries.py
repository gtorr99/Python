from tkinter import *
from functools import partial

def bt_click():
    lb["text"] = de.get()

screen = Tk()

# Data Entry (de)
de = Entry(screen)
de.place(x=100, y=100)

bt = Button(screen, width=20, text="Ok", command=bt_click)
bt.place(x=100, y=150)

lb = Label(screen, text="Label")
lb.place(x=100, y=50)


screen.geometry("300x300+200+200")
screen.mainloop()
