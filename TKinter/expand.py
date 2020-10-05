from tkinter import *

screen = Tk()

lb1 = Label(screen, text="Linha 1", bg="white")
lb2 = Label(screen, text="Linha 2", bg="yellow")
lb3 = Label(screen, text="Linha 3", bg="blue")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=0)
lb3.pack(side=TOP, fill=BOTH, expand=1)

screen.geometry("500x200+200+200")
screen.mainloop()