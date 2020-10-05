from tkinter import *

screen = Tk()

# Instance - Pattern Container
lb = Label(screen, text="It's not a bug")
lb.place(x=100, y=100)

screen.geometry("300x300+200+200")

screen.mainloop()