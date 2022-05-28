import time, os, pygame
from tkinter import *
time.sleep(2)

programmrun = (1)

root1 = Tk()
root1.geometry('600x300')
root1.title("test.exe")
root1.resizable(False, False)
root1.configure(background='#D3D3D3')
f_bot = Frame(root1)
f_top = Frame(root1)
b= Label(width=150,height=2,text = "Welcome to the distance counter!",font=("Comic Sans MS", 10, "bold"),bg='lightgrey',activebackground='white')
b1 = Entry(width=20,bg='lightgrey')
b2 = Label(width=20,height=2,text = "The distance between ",font=("Comic Sans MS", 10, "bold"),bg='lightgrey',activebackground='white')
b3 = Entry(width=20,bg='lightgrey')
b4 = Button(width=20,height=2,text = "Welcome to the distance counter!",font=("Comic Sans MS", 10, "bold"),bg='lightgrey',activebackground='white')
b.pack(side=TOP,padx=2,pady=2)
b1.pack(side=LEFT,padx=2,pady=2)
b2.pack(side=LEFT,padx=90,pady=2)
b3.pack(side=RIGHT,padx=2,pady=2)
b4.pack(side=TOP,padx=2,pady=2)

root1.mainloop()


#==========================================================================================================#
destination = {"Kyiv": 482 , "Odesa": 454, "Lutsk": 880, "Rivne": 806, "Zhytomyr":619, "Cherniv":544, "Sumy":374, "Kharkiv":218, "Donetsk":262, "Zaporizhia":85,"Kherson":329, "Mykolaiv":321, "Odesa":454, "Kirovohrad":246, "Cherkasy":289, "Vinnytsia":572, "Khmelnitsky":700, "Ivano-Frankivsk":947, "Ternopil":815, "Uzhhorod":1290, "Poltava":206 }
print("Welcome to the distance counter.\nThis programm counts distance between Dnipro and other city.")
time.sleep(2)
#####################
#f = open('cities.txt')
#for line in f:
#    print(line)
#####################
while programmrun == (1):
    user_input = input("Enter your destination city: ")
    for _ in range(3):
        time.sleep(1)
        print(".")
    for key,value in destination.items():
        if user_input == key:
            time.sleep(2)
            print(f"The distance between Dnipro and {key} is {value} km")
        else:
            continue
        
        time.sleep(2)
        continuee = input("Do you want to continue? (Enter Yes to continue) ")
        if continuee == "Yes":
            time.sleep(2)
            print("ok")
            for _ in range(3):
                time.sleep(1)
                print(".")
            continue
        else:
            time.sleep(2)
            programmrun = 0
            break
#==========================================================================================================#    