from tkinter import *
import pygame
import operator
from pygame import mixer
pygame.init()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
root = Tk()
root.geometry('269x330')
root.title("TEST.EXE")
root.resizable(False, False)
root.configure(background='black')
#################FUNCTIONS############################
def playbut():
    pressb = mixer.Sound("button-30.wav")
    pressb.play()
############################
def ab1():
    l.delete(0, 'end')
    playbut()
    l.insert(END,7)
############################
def ab2():
    l.delete(0, 'end')
    playbut()
    l.insert(END,4)
############################
def ab3():
    l.delete(0, 'end')
    playbut()
    l.insert(END,1)
############################
def ab4():
    l.delete(0, 'end')
    playbut()
    l.insert(END,0)
############################
def ab5():
    l.delete(0, 'end')
    playbut()
    l.insert(END,8)
############################
def ab6():
    l.delete(0, 'end')
    playbut()
    l.insert(END,5)
############################
def ab7():
    l.delete(0, 'end')
    playbut()
    l.insert(END,2)
############################
def ab8():
    l.delete(0, 'end')
    playbut()
    l.insert(END, chr(44))
############################
def ab9():
    l.delete(0, 'end')
    playbut()
    l.insert(END,9)
############################
def ab10():
    l.delete(0, 'end')
    playbut()
    l.insert(END,6)
############################
def ab11():
    l.delete(0, 'end')
    playbut()
    l.insert(END,3)
############################
def ab12():
    playbut()
    answ = (l.get())
    a = list(answ)
    digit_one = int(a[0])
    digit_two = int(a[2])
    l.delete(0, 'end')
    if sign == "+":
        result = operator.add(digit_one, digit_two)
        l.insert(END,result)
    elif sign == "-":
        result = operator.sub(digit_one, digit_two)
        l.insert(END,result)
    elif sign == "/":
        result = operator.truediv(digit_one, digit_two)
        l.insert(END,result)
    elif sign == "*":
        result = operator.mul(digit_one, digit_two)
        l.insert(END,result)
############################
def ab13():
    l.delete(0, 'end')
    playbut()
    l.delete(0,END)
############################
def ab14():
    l.delete(0, 'end')
    playbut()
    global sign
    sign = '/'
    l.insert(END,chr(47))
    return sign
############################
def ab15():
    l.delete(0, 'end')
    playbut()
    global sign
    sign = '-'
    l.insert(END,chr(45))
    return sign
############################
def ab16():
    l.delete(0, 'end')
    playbut()
    global sign
    sign = '+'
    l.insert(END,chr(43))
    return sign
############################
def ab17():
    l.delete(0, 'end')
    playbut()
    global sign
    sign = '*'
    l.insert(END,chr(42))
    return sign
#################FUNCTIONS############################
l = Entry(text = 'Entry',background = 'pink', width = 44)
l2 = Label(background = 'pink', width = 300, height=3)
b1 = Button(text="7", width=8, height=3,background = 'lightblue', command=ab1)
b2 = Button(text="4 ", width=8, height=3,background = 'lightblue', command=ab2)
b3 = Button(text="1 ", width=8, height=3,background = 'lightblue', command=ab3)
b4 = Button(text="0 ", width=8, height=3,background = 'lightblue', command=ab4)
b5 = Button(text="8 ", width=8, height=3,background = 'lightblue', command=ab5)
b6 = Button(text="5 ", width=8, height=3,background = 'lightblue', command=ab6)
b7 = Button(text="2 ", width=8, height=3,background = 'lightblue', command=ab7)
b8 = Button(text=",", width=8, height=3,background = 'lightblue', command=ab8)
b9 = Button(text="9", width=8, height=3,background = 'lightblue', command=ab9)
b10 = Button(text="6", width=8, height=3,background = 'lightblue', command=ab10)
b11 = Button(text="3", width=8, height=3,background = 'lightblue', command=ab11)
b12 = Button(text="=", width=8, height=3,background = 'lightblue', command=ab12)
b13 = Button(text="<-", width=8, height=2,background = 'lightblue', command=ab13)
b14 = Button(text="÷", width=8, height=2,background = 'lightblue', command=ab14)
b14_2 = Button(text="×", width=8, height=2,background = 'lightblue', command=ab17)
b15 = Button(text="–", width=8, height=3,background = 'lightblue', command=ab15)
b16 = Button(text="+", width=8, height=3,background = 'lightblue', command=ab16)

'''
cancelImageData = 
    R0lGODlhEAAQAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr
    /wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
    mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMA
    MzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV
    /zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPV
    mTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYr
    M2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA
    /2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/
    mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlV
    M5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq
    /5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswA
    mcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyA
    M8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV
    /8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8r
    mf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+q
    M/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP//
    /wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAQABAAAAiWAPcJHEiwYEFpCBMiNLhP
    WjZz4CB+A5dN2sGH2TJm+7ax4kCHEOlx3EgPHEeLDc1loydwokB6G1EJlEYRHMt6
    +1hW/IaSpreN+/ThzIYq5kyKGffV07ePpzSeMzl+UypU6aunMhtSdCcwI0t606A2
    3PjN3VVXK2NO+/iKIzZp0xB+Q4Xt4re7te4WZSgNVV+EfhkKLhgQADs=

l.image = PhotoImage(data=cancelImageData)
imageLabel = Label(root, image=l.image)
imageLabel.place(x = 250, y = 15)
'''
#################COORDS####################################
l.place(x = 1, y = 1, height = 50)
b1.place(x = 2, y = 55)
b2.place(x = 2, y = 112)
b3.place(x = 2, y = 169)
b4.place(x = 2, y = 226)
b5.place(x = 69, y = 55)
b6.place(x = 69, y = 112)
b7.place(x = 69, y = 169)
b8.place(x = 69, y = 226)
b9.place(x = 136, y = 55)
b10.place(x = 136, y = 112)
b11.place(x = 136, y = 169)
b12.place(x = 136, y = 226)
b13.place(x = 203, y = 55)
b14.place(x = 203, y = 97)
b14_2.place(x = 203, y = 136)
b15.place(x = 203, y = 175)
b16.place(x = 203, y = 226)
l2.place(x = 1, y = 281)
#################COORDS####################################


root.mainloop()