import tkinter as tk

# A new instance of tk
window = tk.Tk()

# Changes window title
window.title("Main Window")

# Changes background to black
window["bg"]         = "black" 
window["background"] = "black"

# Width x Height + Left + Top (distance)
# WxH+L+T
# 300x300+100+100 pixels
window.geometry("300x300+100+100")

window.mainloop()