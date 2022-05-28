import tkinter
from tkinter import *
root = Tk()
#===============================================================================================
e1 = Entry(width=20,text = "Введите число")
e1.config(bg = "aqua")
e2 = Button(width=20,text = "Преобразовать")
e2.config(bg = "white")
e3 = Listbox(width=20,height=4)
e3.config(bg = "purple")
#===============================================================================================

def chikibamboni(event):
    a = str(e1.get())
    for i in(a):
        e3.insert(0,i)

e2.bind('<Button>', chikibamboni)
e1.pack()
e2.pack()
e3.pack()
root.mainloop()