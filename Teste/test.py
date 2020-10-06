from collections import namedtuple
import tkinter as tk

Rect = namedtuple('Rect', 'x0, y0, x1, y1')

class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None

class Demo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.msg_text = tk.StringVar()
        self.msg = tk.Message(self, textvariable=self.msg_text, width=100)
        self.msg.grid(row=0, column=0)

        self.picture = tk.PhotoImage(file='C:/Users/GTorr/Documents/VSCode/Workspace/Python/Teste/archipelago2.png')
        img_rects = [Rect(0, 26, 80, 78),
                     Rect(89, 26, 183, 78),
                     Rect(119, 120, 168, 132),
                     Rect(126, 74, 219, 125),
                     Rect(134, 135, 219, 164),
                     Rect(0, 148, 21, 164)]
        self.imagemapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
        self.image = tk.Label(self, image=self.picture, borderwidth=0)
        self.image.bind('<Button-1>', self.image_click)
        self.image.grid(row=1, column=0)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=2, column=0)

    def image_click(self, event):
        hit = self.imagemapper.find_rect(event.x, event.y)
        self.msg_text.set('{} clicked'.format('nothing' if hit is None else
                                              'rect[{}]'.format(hit)))

app = Demo()
app.master.title('Image Mapper')
app.mainloop()