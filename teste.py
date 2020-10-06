from tkinter import *
dict_l = {}
def read_file():
    f = open('{}.txt'.format(dteModel.get()))

    for line in f:
        if line.find('[') != -1:
            first=int(line.find('['))
            last=int(line.find(']'))
            dict_l['name']=line[first+1:last]
            continue
        if line.find('X') != -1:
            dict_l["xPos"] = line[6:line.find('\n')]
            continue
        if line.find('Y') != -1:
            dict_l['yPos'] = line[6:line.find('\n')]
            continue
        if line.find('W') != -1:
            dict_l['width'] = line[6:line.find('\n')]
            continue
        if line.find('H') != -1:
            dict_l['height'] = line[7:]

    f.close()
    generateWidgets()

def generateWidgets():
    bt1 = Button(screen, text=dict_l['name'], width=dict_l['width'])
    bt1.place(x=dict_l['xPos'], y=dict_l['yPos'])

screen = Tk()

dteModel = Entry(screen, text="xTeste")
dteModel.place(x=70, y=70)

texto="Ok"
bt = Button(screen, text=texto, command=read_file)
bt.place(x=100, y=100)


screen.geometry("500x300+200+200")
screen.mainloop()