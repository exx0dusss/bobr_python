from tkinter import * 
import random
import time
import pygame
from pygame import mixer
pygame.init()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

#===========================================================================================================================================          
def tadaa():
    tada = mixer.Sound("tadaa.wav")
    tada.play()
def endead():
    pygame.mixer.music.load("lose.wav")
    pygame.mixer.music.play()
def pause():
    pygame.mixer.music.load("pause.wav")
    pygame.mixer.music.play()
def mainmenu():
    pygame.mixer.music.load("mainmenu.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(3)
def fly():
    pygame.mixer.music.load("fly.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
def endead():
    alien_hit = mixer.Sound("alien_hit.wav")
    alien_hit.play()
def mute(event):
    pygame.mixer.music.pause()
def unmute(event):
    pygame.mixer.music.unpause()
def game():
    pygame.mixer.music.load("8-bit.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(3)
def shoot():
    alien_shoot = mixer.Sound("alien_shoot.wav")
    alien_shoot.play()
def playbut():
    pressb = mixer.Sound("button-30.wav")
    pressb.play()
def sound(event):
    rootset = Tk()
    rootset.geometry('200x100')
    rootset.title('sound')
    rootset.resizable(False, False)      
    def back(event):
        rootset.destroy()
    b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b12 = Button(rootset ,width=30,height=1,text = "+",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b13 = Button(rootset ,width=30,height=1,text = "-",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11.bind('<Button-1>',back)
    b12.bind('<Button-1>',unmute)
    b13.bind('<Button-1>',mute)
    b12.pack()
    b13.pack()
    b11.pack()
def controls(event):
    rootset = Tk()
    rootset.geometry('300x340')
    rootset.title('info')
    rootset.resizable(False, False)
    def back(event):
        rootset.destroy()
    b11 = Button(rootset ,width=60,height=2,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b12 = Label(rootset ,width=60,height=2,text = "Move left ---   ⇐",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b13 = Label(rootset ,width=60,height=2,text = "Move right ---  ⇒",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b122 = Label(rootset ,width=60,height=2,text = "Move up ------  ⇑",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b133 = Label(rootset ,width=60,height=2,text = "Move down ---   ⇓",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b14 = Label(rootset ,width=60,height=2,text = "Shoot --------- Space",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b15 = Label(rootset ,width=60,height=2,text = "Pause --------  Escape",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white') 
    b16 = Label(rootset ,width=60,height=2,text = "2019-2020 PYTHON ALL RIGHTS RESERVED",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b11.bind('<Button-1>',back)
    b12.pack()
    b13.pack()
    b122.pack()
    b133.pack()
    b14.pack()
    b15.pack()
    b16.pack()
    b11.pack()
def settings1(event):
    rootset = Tk()
    rootset.geometry('300x200')
    rootset.title('settings')
    rootset.resizable(False, False)
    def back(event):
        rootset.destroy()
    b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11.bind('<Button-1>',back)
    b11.pack()
    
def lvl(event):
    rootset = Tk()
    rootset.geometry('300x170')
    rootset.title('settings')
    rootset.resizable(False, False)
    rootset.configure(background='#211036')
    def back(event):
        rootset.destroy()
    b111 = Button(rootset ,width=30,height=1,text = "Лёгкий",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b112 = Button(rootset ,width=30,height=1,text = "Средний",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b113 = Button(rootset ,width=30,height=1,text = "Сложный",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11.bind('<Button-1>',back)
    l4 = Label(rootset, width=30,height=1,bg='#211036',activebackground='#211036')
    b111.bind('<Button-1>', space)
    b112.bind('<Button-1>', space1)
    b113.bind('<Button-1>', space2)
    b111.pack()
    b112.pack()
    b113.pack()
    l4.pack()
    b11.pack()

def settings(event):
    rootset = Tk()
    rootset.geometry('200x100')
    rootset.title('settings')
    rootset.resizable(False, False)
    def back(event):
        rootset.destroy()
    b13 = Button(rootset ,width=30,height=1,text = "Звук",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b12 = Button(rootset ,width=30,height=1,text = "Управление",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11.bind('<Button-1>',back)
    b12.bind('<Button-1>',controls)
    b13.bind('<Button-1>',sound)
    b12.pack()
    b13.pack()
    b11.pack()
    
def info(event):
    rootset = Tk()
    rootset.geometry('530x130')
    rootset.title('settings')
    rootset.resizable(False, False)
    rootset.configure(background = "#211036")
    def back(event):
        rootset.destroy()
    b13 = Label(rootset ,width=60,height=2,text = "COPYRIGHT (c)2019-2020 PYTHON ALL RIGHTS RESERVED",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b12 = Label(rootset ,width=60,height=2,text = "Python(c),Copyright 2019-2020, tkinter Inc, All rights reserved",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
    b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
    b11.bind('<Button-1>',back)
    b13.pack()
    b12.pack()
    b11.pack()

def leave(event):
    root1.destroy()
#=====================================================================================================================================
    
def space(event):
    root = Tk()
    root.geometry('500x600')
    root.title("project.space.exe")
    root.resizable(False, False)
    c = Canvas(root, width=500, height=600, bg='#330033')
    c.focus_set()
    game()
    img = PhotoImage(master = c,file="sp3.png")
    img1 = PhotoImage(master = c,file="enemy1.png")
    imgb = PhotoImage(master = c,file = "space.png")
    c.create_image(105,300,anchor = CENTER,image=imgb)
    imgh = PhotoImage(master = c,file = "heart.png")
    imgm = PhotoImage(master = c,file = "meteorit.png")
    imgbs = PhotoImage(master = c,file = "boss.png")
    imgbl = PhotoImage(master = c,file = "bulletl.png")
    hl = 3
    sc = 0
    bosshp = 10
    c.create_image(487,19,image=imgh)
    c.create_text(450,20,text = ('HP=',hl),fill='GREY',font=("Comic Sans MS", 13, "bold"), tag = 'health')
    c.create_text(450,586,text = ('Score=',sc),fill='GREY',font=("Comic Sans MS", 13, "bold"),tag = 'score')
    def restart():
        root3 = Tk()
        root3.geometry('250x100')
        root3.title("gg")
        root3.resizable(False, False)
        root3.configure(background='#211036')
        def back1(event):
            pygame.mixer.music.stop()
            root.destroy()
            root3.destroy()           
        b46 = Button(root3,width=30,height=4,text = "Выйти",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
        b46.bind('<Button-1>',back1)
        b46.pack()
        root3.mainloop()
    def bossk():
        nonlocal bosshp
        bosshp = bosshp - 1
        if bosshp == 0:
            c.delete(boss)
        
    def gg():
        pygame.mixer.music.load("win.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(3)
        c.itemconfigure(rocket, state = HIDDEN)
        c.itemconfigure(enemyy, state = HIDDEN)
        c.create_text(240,290,text = ('You win!!!'),fill='red',font=("Comic Sans MS", 32, "bold"),tag = 'score')
        
    def lose():
        pygame.mixer.music.load("gg.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(3)
        c.itemconfigure(rocket, state = HIDDEN)
        c.itemconfigure(enemyy, state = HIDDEN)
        c.create_text(240,290,text = ('You Lose!!!'),fill='red',font=("Comic Sans MS", 32, "bold"),tag = 'lose')
    def helthp():
        nonlocal hl
        hl = hl-1
        c.delete('health')
        c.create_text(450,20,text = ('HP=',hl),fill='GREY',font=("Comic Sans MS", 13, "bold"),tag = 'health')
        if hl == 0:
            nonlocal sc
            if sc < 20 or sc == 20:
                c.create_text(240,330,text = ('Your place is 3'),fill='red',font=("Comic Sans MS", 32, "bold"),tag = 'score')
                lose()
                restart()
            elif sc == 80 or sc < 80:
                c.create_text(240,330,text = ('Your place is 2'),fill='red',font=("Comic Sans MS", 32, "bold"),tag = 'score')
                lose()
                restart()
            elif sc > 160 or sc == 160:
                c.create_text(240,330,text = ('Your place is 1'),fill='red',font=("Comic Sans MS", 32, "bold"),tag = 'score')
                gg()
                restart()
    def escape(event):
        rootset = Tk()
        rootset.geometry('230x130')
        rootset.title('settings')
        rootset.resizable(False, False)
        rootset.configure(background='#211036')
        def back1(event):
            rootset.destroy()
            root.destroy()
            mainmenu()
        b13 = Button(rootset ,width=30,height=1,text = "Звук",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
        b11 = Button(rootset ,width=30,height=1,text = "Назад",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
        b3 = Button(rootset,width=30,height=1,text = "Выйти",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
        l4 = Label(rootset, width=30,height=1,bg='#211036',activebackground='#211036')
        def back(event):
            rootset.destroy()
        b13.bind('<Button-1>',sound)
        b13.pack()
        b11.bind('<Button-1>',back)
        b3.bind('<Button-1>',back1)
        b3.pack()
        l4.pack()
        b11.pack()
    c.bind('<Escape>',escape)
    
#============================================================================================================================================
    rocket = c.create_image(300, 400, anchor=NE, image=img)   
    c.bind('<Left>', lambda event: c.move(rocket, -5, 0))
    c.bind('<Right>', lambda event: c.move(rocket, 5, 0))

    def met():
        x = random.randint(5,500)
        ml = c.create_image(x,18,image=imgm,tag = "meter")
    met()
    def motionl():
        c.move("meter", 0, 5)
        if c.coords("meter")[1] < 590:
            root.after(7, motionl)
        else:
            c.delete("meter")
            met()
            motionl()
    motionl()

#============================================================================================================================================    
    def enemy21():
        for i in range(1):
            x = random.randint(50,550)
            y = random.randint(40,80)
            global enemyy
            enemyy = c.create_image(x,y,image=img1)
    enemy21()
            
    def score():
        nonlocal sc
        sc = sc+20
        c.delete("score")
        c.create_text(450,586,text = ('Score=',sc),fill='GREY',font=("Comic Sans MS", 13, "bold"),tag = 'score')
        if sc == 20:
            tadaa()
        elif sc == 40:
            tadaa()
        elif sc == 60:
            tadaa()
        elif sc == 120:
            tadaa()
        elif sc == 140:
            tadaa()
        elif sc == 160:
            tadaa()
        elif sc == 180:
            tadaa()
        elif sc == 200:
            tadaa()
        elif sc == 220:
            tadaa()
        elif sc == 240:
            tadaa()
        elif sc == 260:
            tadaa()
        elif sc == 280:
            tadaa()
        
    def motionen():
        c.move(enemyy, 0, 0.5)
        if c.coords(enemyy)[1] < 590:
            if ((c.coords(rocket)[0]) > (c.coords(enemyy)[0])):
                if ((c.coords(rocket)[0])-50 < (c.coords(enemyy)[0])):
                    if ((c.coords(rocket)[1]) < (c.coords(enemyy)[1])):
                        helthp()
                        c.delete(enemyy)
                        enemy21()
                        motionen()
            root.after(7, motionen)
        else:
            c.delete(enemyy)
            enemy21()
            motionen()
    motionen()
    def bullet(event):
        c1 = c.coords(rocket)[0]-23
        c2 = c.coords(rocket)[1]+5
        shoot()
        bullet2 = c.create_image(c1,c2,image=imgbl)
        a = c.coords(bullet2)[0]
        b = c.coords(bullet2)[1]
        def motion1():
            c.move(bullet2, 0, -2)
            if c.coords(bullet2)[1] > 15:
                if ((c.coords(bullet2)[0]+80) > (c.coords(enemyy)[0])):
                    if ((c.coords(bullet2)[0]) < (c.coords(enemyy)[0])):
                        if ((c.coords(bullet2)[1]) < (c.coords(enemyy)[1])):
                            endead()
                            score()
                            #c.delete(bullet2)# hide
                            c.itemconfigure(bullet2, state = HIDDEN)
                            c.delete(enemyy)
                            enemy21()
                root.after(7, motion1)
            else:
                c.delete(bullet2)
            

        motion1()
    
    c.bind('<space>', bullet)
    c.pack()
#============================================================================================================================================        
    
    root.mainloop()
    
#============================================================================================================================================
mainmenu()
root1 = Tk()
root1.geometry('300x500')
root1.title("project.space.exe")
root1.resizable(False, False)
root1.configure(background='#211036')
f_bot = Frame(root1)
f_top = Frame(root1)
name = Label(width=25)
name.configure(background='#211036')
b= Button(width=30,height=3,text = "Начать игру",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
b1 = Button(width=30,height=3,text = "Настройки",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
b2 = Button(width=30,height=3,text = "Об игре",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=playbut)
b3 = Button(width=30,height=3,text = "Выйти",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white',command=mute)
l = Label(width=35,height=2,bg='#211036',activebackground='#211036')
l1 = Label(width=35,height=2,bg='#211036',activebackground='#211036')
l2 = Label(width=35,height=2,bg='#211036',activebackground='#211036')
l3 = Label(width=35,height=1,bg='#211036',activebackground='#211036')
l5 = Label(width=35,height=1,bg='#211036',activebackground='#211036')
l7 = Label(width=35,height=1,bg='#211036',activebackground='#211036')
b16 = Label(width=30,height=2,text = "PYTHON ALL RIGHTS RESERVED",font=("Comic Sans MS", 10, "bold"),bg='aqua',activebackground='white')
b.bind('<Button-1>', lvl)
b1.bind('<Button-1>', settings)
b2.bind('<Button-1>', info)
b3.bind('<Button-1>', leave)
name.pack()
b.pack()
l.pack()
b1.pack()
l1.pack()
b2.pack()
l2.pack()
b3.pack()
l7.pack()
b16.pack()

root1.mainloop()
