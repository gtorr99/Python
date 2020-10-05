from tkinter import * 

screen = Tk()

# lb1 = Label(screen, text="Label 1", bg="green")
# lb2 = Label(screen, text="Label 2", bg="red")
# lb3 = Label(screen, text="Label 3", bg="yellow")
# lb4 = Label(screen, text="Label 4", bg="blue")

# # This order defines objects position with pack
# lb1.pack(side=RIGHT)
# lb2.pack() # Top is the default
# lb3.pack(side=LEFT)
# lb4.pack(side=BOTTOM)

lb1 = Label(screen, text="RIGHT", bg="white")
lb2 = Label(screen, text="BOTTOM", bg="white")
lb3 = Label(screen, text="LEFT", bg="white")
lb4 = Label(screen, text="TOP", bg="white")

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM) 
lb3.pack(side=LEFT)
lb4.pack(side=TOP)

screen["bg"] = "black"

screen.geometry("400x300+200+200")
screen.mainloop()