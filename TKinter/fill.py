from tkinter import *

screen = Tk()

lb1 = Label(screen, text="horizontal", bg="red")
lb2 = Label(screen, text="", bg="black")
lb3 = Label(screen, text="", bg="black")

lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)





screen.geometry("400x300+200+200")
screen.mainloop()