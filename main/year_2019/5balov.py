import tkinter
from tkinter import *
root = Tk()
#===============================================================================================
e1 = Entry(width=40,text = "Введите число")
e1.config(bg = "aqua")
e2 = Button(width=40,text = "Преобразовать")
e2.config(bg = "white")
e3 = Listbox(width=40)
e3.config(bg = "purple")
#===============================================================================================

def chikibamboni(event):
    a = int(e1.get())
    m = 1
    aa = []
    while m*m <= a:
        if a%m==0:
            aa.append(m)
            if m!=a//m:
                aa.append(a//m)
        m+=1
    aa.sort()
    e3.insert(0,aa)

e2.bind('<Button>', chikibamboni)
e1.pack()
e2.pack()
e3.pack()
root.mainloop()