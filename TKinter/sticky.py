from tkinter import *

screen = Tk()


lblSpace        = Label(screen, text="SPACE", width="15", height=3, bg="blue")
lblHorizontal   = Label(screen, text="HORIZONTAL", bg="yellow")
lblVertical     = Label(screen, text="VERTICAL", bg="red")

# Sticky - determines the position by the directions of the wind rose
lblSpace.grid(row=0, column=0)
lblHorizontal.grid(row=1, column=0, sticky=E)
lblVertical.grid(row=0, column=1, sticky=S)

screen.geometry("200x100+100+100")
screen.mainloop()