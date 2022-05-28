from geopy.geocoders import *
from geopy.distance import *
from tkinter import *
import os

folder_name = "Maps"
full_path = os.path.join('C:\\', folder_name)
os.makedirs(full_path, exist_ok=True)
os.chdir(full_path)
os.getcwd()
f = open('maps.txt','w')

############################Functions######################################
def change():
    firstloc = str(b1.get())
    secondloc = str(b3.get())
    geolocator = Nominatim(user_agent='Timur')
    location = geolocator.geocode(firstloc)
    location2 = geolocator.geocode(secondloc)
    firstcitycor = ((location.latitude, location.longitude))
    secondcitycor = ((location2.latitude, location2.longitude))
    os.chdir('C:\\Maps')
    filename = 'maps.txt'
    with open(filename, 'a') as my_file:
        my_file.write(f'\nThe distance between {firstloc} and {secondloc} {great_circle(firstcitycor, secondcitycor)}')
    bb1['text'] = (f'The distance is {great_circle(firstcitycor, secondcitycor)}')
    bb1.pack()
    root1.mainloop()
   
############################Functions######################################
root1 = Tk()
root1.focus_force()
root1.geometry('300x300')
root1.title("Maps.exe")
root1.resizable(False, False)
root1.configure(background='#ffffff')
f_bot = Frame(root1)
f_top = Frame(root1)
b= Label(width=150,height=2,text = "Welcome to the distance counter!",font=("Comic Sans MS", 10, "bold"),bg='white',activebackground='white')
bb= Label(width=150,height=2,text = "Enter your locations",font=("Comic Sans MS", 10, "bold"),bg='white',activebackground='white')
bt= Label(width=150,height=3,bg='Black')
b1 = Entry(width=20,font=("Comic Sans MS", 10, "bold"),bg='white')
b2 = Button(width=10,height=2,text = "Count! ",font=("Comic Sans MS", 10, "bold"),bg='white',activebackground='white')
b3 = Entry(width=20,font=("Comic Sans MS", 10, "bold"),bg='white')
b.pack()
bb.pack()
b1.pack()
b3.pack()
b2.config(command=change)
b2.pack()
bb1 = Label(width=150,height=2,text = (f''),font=("Comic Sans MS", 10, "bold"),bg='white',activebackground='white')
bb1.pack()
bt.pack(side = BOTTOM)
root1.mainloop()
#########################################################################