from tkinter import *

def sum():
    if (str(dteNum1.get()).isnumeric() and str(dteNum2.get()).isnumeric()):
        lbResult["text"] = "Result: " + str(float(dteNum1.get()) + float(dteNum2.get()))
    else:
        lbResult["text"] = "Enter only numeric values!"

screen = Tk()

xAxis = 90

lbTitle = Label(screen, text="Sum of Values")
lbTitle.place(x=xAxis + 15, y=50)

dteNum1 = Entry(screen)
dteNum1.place(x=xAxis, y=80)

dteNum2 = Entry(screen)
dteNum2.place(x=xAxis, y=100)

lbResult = Label(screen, text="Result: ")
lbResult.place(x=xAxis, y=130)

btnSum = Button(screen, width=20, text="Sum", command=sum)
btnSum.place(x=xAxis, y=160)


screen.geometry("300x300+200+200")
screen.mainloop()