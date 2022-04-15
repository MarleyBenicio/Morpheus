from tkinter import *

def cloner():
    intfcclnr = Tk()
    intfcclnr.title('Clonar site')
    intfcclnr.geometry('250x85')
    intfcclnr.configure(background = 'black')
    intfcclnr.resizable(width=False, height=False)

    titulo = Label(intfcclnr,text = "Site", fg = "yellow", bg = "black")
    titulo.place(x = 5, y = 5)

    site = Entry(intfcclnr, width = 34)
    site.place(x = 1, y = 25)

    botaoclonar = Button(intfcclnr, text = "Clonar", fg = "blue", bg = "black", bd = 0)
    botaoclonar.place(x = 90, y = 55)
