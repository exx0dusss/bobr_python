import random
from random import randint
import time
import turtle
#=====================================================================================================================================
list_name = []
list_drakon = []
list_deystvie = ["Покормить","Погладить","Убить","Привести своих друзей"]
#=====================================================================================================================================
def deystvie():
    for i in range(len(list_deystvie)):
        print(list_deystvie[i])
#=====================================================================================================================================
print("="*40)
print("Здраствуй,путешественник!Вижу далеко ты собрался")
user_input = input("Введите своё имя")
print("Приятно познакомиться",user_input, "!")
print("="*40)
time.sleep(2)
#=====================================================================================================================================
print("Ты видишь перед собой две пещеры....")
time.sleep(2)
user_input = input("Готов ли ты начать свой путь?(Y/N)")
print("="*40)
if user_input == "no" or user_input == "N":
    print("Быстро же ты сдался,приходи в следующий раз когда наберешься духу")
    print('='*10,"Слишком быстрый конец",'='*9)
elif user_input == "yes" or user_input == "Y":
    time.sleep(2)
    print("Перед тобой 2 пещеры,в одной - добрый дракон,в другой - злой")
    time.sleep(2)
#=====================================================================================================================================
choose = True
while choose:
    n = input("Ну что ж,какую пещеру выберешь? (1/2)")
    for i in range(int(n)):
        if n == "1":
            print("Пойдём...")
            time.sleep(2)
            print("Ты встретил злого дракона....")
            time.sleep(2)
            print("Ты был съеден,твой путь окончен")
            user_input = input("Попробывать еще?")
            if user_input == "no" or user_input == "N":
                print('='*17,"Конец",'='*18)
                choose = False
            elif user_input =="yes" or user_input == "Y":
                print("Хорошо")
#=====================================================================================================================================
        elif n == "2":
            print("Пойдем...")
            time.sleep(2)
            print("Ты встретил доброго дракона....")
            time.sleep(2)
            print("Он тебя не тронул")
            print("="*40)
            deystvie()
            print("="*40)
            user_input = input("Что ты сделаешь?")
        if user_input == "Покормить" or user_input == "Погладить":
            print("Дракон тебя принял и будет рад тебя видеть в будущем")
            choose = False
            break
        elif user_input == "Убить":
             print("Вы ничего не смогли сделать дракону")
             print("Вы стали вкусным ужином дракона")
             choose = False
             break
        elif user_input == "Привести своих друзей":
             print("Дракон испугался толпы и съел вас всех")
             print("Вы стали вкусным ужином дракона")
             choose = False
             break

#=====================================================================================================================================
print("Спасибо за игру!")
print('='*17,"Конец",'='*18)
            
            
   