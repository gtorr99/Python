from tkinter import *

screen = Tk()


lb1 = Label(screen, text="Label 1")
lb2 = Label(screen, text="Label 2")
lb1.grid(row=10, column=10)


screen.geometry("500x200+200+200")
screen.mainloop()