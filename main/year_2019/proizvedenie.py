from tkinter import *
root = Tk()
e1 = Entry(width=20)
e1.config(bg = "aqua")
e11 = Entry(width=20)
e11.config(bg = "aqua")
e2 = Button(width=20,text = "Chikibambox")
e2.config(bg = "purple")
e3 = Label(width=20,text = "Otvet")
e3.config(bg = "purple")
def umn(event):
    a = int(e1.get())
    b = int(e11.get())
    c = 0
    for i in range(a,b+1):
        c = c + (i**2)
        e3['text'] = (i,c)
e2.bind('<Button>', umn)
e1.pack()
e11.pack()
e2.pack()
e3.pack()
