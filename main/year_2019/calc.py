from tkinter import * 
root = Tk()
#==================================================================================================== 
e1 = Entry(width=20)#Поле
e2 = Entry(width=20)#Поле
a = Button(text="+")
b = Button(text="-")
e = Button(text="/")
k = Button(text="*")
#====================================================================================================
l = Label(bg='white', fg='black', width=20)
#==============================================Функции================================================ 
def plus(event):
    s1 = int(e1.get())
    s2 = int(e2.get())
    l['text'] = (s1+s2)
def minus(event):
    s1 = int(e1.get())
    s2 = int(e2.get())
    l['text'] = (s1-s2)
def umnozhenie(event):
    s1 = int(e1.get())
    s2 = int(e2.get())
    l['text'] = (s1*s2)
def delenie(event):
    s1 = float(e1.get())
    s2 = float(e2.get())
    l['text'] = (s1/s2)
#===============================================Назначения============================================ 
a.bind('<Button-1>', plus)
b.bind('<Button-1>', minus)
e.bind('<Button-1>', delenie)
k.bind('<Button-1>', umnozhenie)
#===============================================Обработка========================================== 
e1.pack()
e2.pack()
a.pack()
b.pack()
e.pack()
k.pack()
l.pack()
root.mainloop()
#================================================Конец===============================================