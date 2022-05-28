from tkinter import *
root = Tk()
#==========================================================================================
def red():
    q['text'] = "#ff0000"
    n['text'] = "Красный"
def orange():
    q['text'] = "#ff7d00"
    n['text'] = "Оранжевый"
def yellow():
    q['text'] = "#ffff00"
    n['text'] = "Желтый"
def green():
    q['text'] = "#00ff00"
    n['text'] = "Зеленый"
def lblue():
    q['text'] = "#007dff"
    n['text'] = "Голубой"
def blue():
    q['text'] = "#0000ff"
    n['text'] = "Синий"
def purple():
    q['text'] = "#7d00f"
    n['text'] = "Фиолетовый"
#=========================================================================================
n = Label(text="",font=("Comic Sans MS", 10, "bold"),width=30)
q = Label(text="",font=("Comic Sans MS", 10, "bold"),width=30,bg ="#ffffff")
w = Button(text="Красный",font=("Comic Sans MS", 10, "bold"),width=30)
e = Button(text="Оранжевый",font=("Comic Sans MS", 10, "bold"),width=30)
r = Button(text="Желтый",font=("Comic Sans MS", 10, "bold"),width=30)
t = Button(text="Зеленый",font=("Comic Sans MS", 10, "bold"),width=30)
y = Button(text="Голубой",font=("Comic Sans MS", 10, "bold"),width=30)
u = Button(text="Синий",font=("Comic Sans MS", 10, "bold"),width=30)
i = Button(text="Фиолетовый",font=("Comic Sans MS", 10, "bold"),width=30)
#==========================================================================================
w.config(bg='#ff0000',activebackground='#ff0000',command=red)
e.config(bg='#ff7d00',activebackground='#ff7d00',command=orange)
r.config(bg='#ffff00',activebackground='#ffff00',command=yellow)
t.config(bg='#00ff00',activebackground='#00ff00',command=green)
y.config(bg='#007dff',activebackground='#007dff',command=lblue)
u.config(bg='#0000ff',activebackground='#0000ff',command=blue)
i.config(bg='#7d00ff',activebackground='#7d00ff',command=purple)
#==========================================================================================

#==========================================================================================
n.pack()
q.pack()
w.pack()
e.pack()
r.pack()
t.pack()
y.pack()
u.pack()
i.pack()
root.mainloop()
#==========================================================================================