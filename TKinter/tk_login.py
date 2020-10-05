from tkinter import *

screen = Tk()


lblLogin = Label(screen, text="Login: ")
lblPsswd = Label(screen, text="Password: ")

dteLogin = Entry(screen,)
dtePsswd = Entry(screen,)

btnConfirm = Button(screen, text="Confirm")

lblLogin.grid(row=0, column=0)
lblPsswd.grid(row=1, column=0)
dteLogin.grid(row=0, column=1)
dtePsswd.grid(row=1, column=1)
btnConfirm.grid(row=2, column=1)

screen.geometry("200x100+100+100")
screen.mainloop()