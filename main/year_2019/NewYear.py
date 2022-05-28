from tkinter import * 
root = Tk()

#=====================================================================================================================================
month = Entry(width=20,text = "Введите месяц",font=("Comic Sans MS", 10, "bold"),)
chislo = Entry(width=20,text = "Введите число",font=("Comic Sans MS", 10, "bold"))
month.config(bg='aqua')
chislo.config(bg='aqua')
l = Label(width=20)
l.config(font=("Comic Sans MS", 10, "bold"))
b = Button(text = "Подсчитать",font=("Comic Sans MS", 10, "bold"))
b.config(bg='#7d00ff',activebackground='#7d00ff')
d = 365
a = 31
ab = 30
abc = 28
er = -1
#=====================================================================================================================================
def newyear(event):
    month1 = int(month.get())
    chislo1 = int(chislo.get())
    if month1 == 1:
        l['text']=(d-chislo1)
    elif month1 == 2: 
        l['text'] = (d-30-chislo1)
    elif month1 == 3:
        l['text']= (d-58-chislo1)
    elif month1 == 4:
        l['text'] = (d-89-chislo1)
    elif month1 == 5:
        l['text'] = (d-119-chislo1)
    elif month1 == 6:
        l['text'] = (d-150-chislo1)
    elif month1 == 7:
        l['text'] = (d-181-chislo1)
    elif month1 == 8:
        l['text'] = (d-212-chislo1)
    elif month1 == 9:
        l['text'] = (d-242-chislo1)
    elif month1 == 10:
        l['text'] = (d-272-chislo1)
    elif month1 == 11:
        l['text'] = (d-303-chislo1)
    elif month1 == 12 :
        l['text'] = (d-334-chislo1)
    else:
        l['text'] = -1
#=====================================================================================================================================
b.bind('<Button>', newyear)
month.pack()
chislo.pack()
b.pack()
l.pack()
root.mainloop()
#=====================================================================================================================================