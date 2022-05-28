from tkinter import *
import random
root = Tk()
root.geometry('700x500+200+100')
root.title("Crazy_Button.exe")
#==========================================================================================================================================
b1 = Button(text="(◑‿◐) ", width=15, height=3)
b1.config(background = "aqua",activebackground = "aqua")
 
def change(e):
    b1['text'] = "( ͡ᵔ ͜ʖ ͡ᵔ ) "
    b1.place(x = random.randint(1,400),y = random.randint(1,400))
    b1['activebackground'] = 'grey'
def dy(e):
    b1.place(x = 280,y = 200)
    b1['text'] = "О май гад,ты что,крейзи?"
    b1.bind("<Enter>", dy)
    b1.config(width=20, height=3,background = "aqua",activebackground = "aqua")
#============================================================================================================================================
b1.bind("<Enter>", change)
b1.bind("<Button-1>", dy)
 
b1.pack()
root.mainloop()
#============================================================================================================================================