import getpass
import requests
import os
import shutil
from io import BytesIO
import PIL.Image
from geopy.geocoders import *
from geopy.distance import *
from tkinter import *
from pymongo import MongoClient
from datetime import datetime

api_key_pixabay = '20269355-cd39894102aeebbc857a8e6f4'                #API

folder_name = "Maps"
full_path = os.path.join('C:\\', folder_name)
os.makedirs(full_path, exist_ok=True)
os.chdir(full_path)
os.getcwd()
n = getpass.getuser()
###########################################################################
mongo = MongoClient('localhost', port=27017)
all_db = mongo.list_database_names()
my_test_db = mongo['my_test_db']
mongo_client = my_test_db['Search_History']
attempt = 0
############################Functions######################################

def save_img():
    url = f'https://pixabay.com/api/?key={api_key_pixabay}&q={query}&image_type=photo'
    res = requests.get(url).json()
    img_obj_list = res['hits']
    folder_name = secondloc
    full_path = os.path.join('C:\\', 'Maps', folder_name)
    os.makedirs(full_path, exist_ok=True)
    os.chdir(full_path)
    os.getcwd()
    def save_image(img_obj):
        jpg_name = f"{img_obj['tags'].replace(',','_')}.jpg"
        img_res = requests.get(img_obj['largeImageURL'])
        #folder_creator
        jpg = PIL.Image.open(BytesIO(img_res.content))
        jpg.save(jpg_name)

    for el in range(5):
        img_obj = img_obj_list[el]
        save_image(img_obj)
        

def change():
    global query, firstloc, secondloc, attempt
    try:
        attempt += 1
        firstloc = str(b1.get())
        secondloc = str(b3.get())
        query = secondloc   
        geolocator = Nominatim(user_agent='Timur')
        location = geolocator.geocode(firstloc)
        location2 = geolocator.geocode(secondloc)
        firstcitycor = ((location.latitude, location.longitude))
        secondcitycor = ((location2.latitude, location2.longitude))
        os.chdir('C:\\Maps')
        bb1['text'] = (f'The distance is {great_circle(firstcitycor, secondcitycor)}')
        bb1.pack()
        user_to_insert = {'query':attempt,
                          'user': n,
                          'time': datetime.now(),
                          'first_location':firstloc,
                          'second_location':secondloc,
                          'result':(f'The distance is {great_circle(firstcitycor, secondcitycor)}')}
        res = mongo_client.insert_one(user_to_insert)
    except AttributeError as e:
        bb1['text'] = ('The place doesn`t exist or it is nothing to search, enter the query')
    save_img()
def folder_del():
    cwd = 'C:\\Maps'
    shutil.rmtree(cwd,ignore_errors=True)
def dbdrop():
    mongo_client.drop()    
############################Front-end######################################
root1 = Tk()
root1.focus_force()
root1.geometry('600x300')
root1.title("Maps v2.0.exe")
root1.resizable(False, False)
root1.configure(background='#232B32')
f_bot = Frame(root1)
f_top = Frame(root1)
b= Label(width=150,height=2,text = "Welcome to the distance counter!",font=("Comic Sans MS", 10, "bold"),bg='#232B32',activebackground='#232B32')
bb= Label(width=150,height=2,text = "Enter your locations",font=("Comic Sans MS", 10, "bold"),bg='#232B32',activebackground='#232B32')
bt= Label(width=150,height=3,bg='#1C2228')
b1 = Entry(width=20,font=("Comic Sans MS", 10, "bold"),bg='#465664')
b2 = Button(width=10,height=2,text = "Count! ",font=("Comic Sans MS", 10, "bold"),bg='#232B32',activebackground='#232B32')
b3 = Entry(width=20,font=("Comic Sans MS", 10, "bold"),bg='#465664')
b.pack()
bb.pack()
b1.pack()
b3.pack()
b2.config(command=change)
b2.pack()
bb1 = Label(width=150,height=2,text = (f''),font=("Comic Sans MS", 10, "bold"),bg='#232B32',activebackground='#232B32')
bb1.pack()
bt.pack(side = BOTTOM)

#########################################################################
print("To clear the image data enter 'folder_del()'")
print("To clear the database enter 'dbdrop()'")

