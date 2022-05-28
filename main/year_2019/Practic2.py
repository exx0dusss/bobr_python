from tkinter import *
root = Tk()
f_top = Frame(root) # root можно не указывать
f_bot = Frame(root)
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
#==========================================================================================
n = Label(text="",font=("Comic Sans MS", 10, "bold"),width=30)
q = Label(text="",font=("Comic Sans MS", 10, "bold"),width=10,bg ="#ffffff")
w = Button(font=("Comic Sans MS", 10, "bold"),width=3)
e = Button(font=("Comic Sans MS", 10, "bold"),width=3)
r = Button(font=("Comic Sans MS", 10, "bold"),width=3)
t = Button(font=("Comic Sans MS", 10, "bold"),width=3)
y = Button(font=("Comic Sans MS", 10, "bold"),width=3)
u = Button(font=("Comic Sans MS", 10, "bold"),width=3)
i = Button(font=("Comic Sans MS", 10, "bold"),width=3)
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

#==========================================================================================
f_top.pack()
f_bot.pack()
n.pack(side=TOP)
q.pack(side=TOP)
w.pack(side=LEFT,padx=2,pady=2)
e.pack(side=LEFT,padx=2,pady=2)
r.pack(side=LEFT,padx=2,pady=2)
t.pack(side=LEFT,padx=2,pady=2)
y.pack(side=LEFT,padx=2,pady=2)
u.pack(side=LEFT,padx=2,pady=2)
i.pack(side=LEFT,padx=2,pady=2)
root.mainloop()