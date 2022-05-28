import random

import time
#=======================================================================================================================================
list_name = []
list_group = []
list_janr = []
list_fantasy = ["The Lord of the Rings" , "Harry Potter", "The Witcher" ,"The Chronicles of Amber"]
list_skazka = ["The Scarlet Flower","Mowgli brothers","Donkey skin","Frog traveler"]
list_pritcha = ["Pisces become goddesses", "About Milarepa", "Student enlightenment","Why i don't see buddha"]
#=======================================================================================================================================
def fantasy():
    for i in range(len(list_fantasy)):
        print(list_fantasy[i])


def pritcha():
    for i in range(len(list_pritcha)):
        print(list_pritcha[i])


def skazka():
    for i in range(len(list_skazka)):
        print(list_skazka[i])
#=======================================================================================================================================

print("Здраствуйте!")

n = input("Сколько вас пришло?")
for i in range(int(n)):
    list_name.append(input("Как вас зовут?"))
    list_janr = (input("Какой жанр вы хотите выбрать?"))
    if list_janr == "fantasy":
        print("Погодите секундочку....")
        time.sleep(1)
        print (40 * "=")
        print("Вот что мы нашли!")
        print (40 * "=")
        fantasy()
        print (40 * "=")
    elif list_janr == "pritcha":
        print("Погодите секундочку....")
        time.sleep(1)
        print (40 * "=")
        print("Вот что мы нашли!")
        print (40 * "=")
        pritcha()
        print (40 * "=")
    elif list_janr == "skazka":
        print("Погодите секундочку....")
        time.sleep(1)
        print (40 * "=")
        print("Вот что мы нашли!")
        print (40 * "=")
        skazka()
        print (40 * "=")
#=====================================================================================================================================
user_input = input("Посоветовать вашему классу жанры и книги для прочтения?")
if user_input == "no" or user_input == "N":
    print("Хорошо,всего доброго")
#=====================================================================================================================================    
p = input("Сколько вас в группе?")
for i in range(int(p)):
    list_name.append(input("Как его/её зовут?"))

print(list_group[i], list_fantasy[random.randint(0,len(list_fantasy)-1)] or list_pritcha[random.randint(0,len(list_pritcha)-1)] or list_skazka[random.randint(0,len(list_skazka)-1)] )

#=====================================================================================================================================
print("Спасибо что пришли,до свиданья!")