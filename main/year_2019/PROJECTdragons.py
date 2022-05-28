import random
from random import randint
import time
import turtle
#======================================================FIRST=Location========================================================================
turtle.bgcolor("lightblue")
zoo=turtle.Turtle()
chucha=turtle.Turtle()
textovik=turtle.Turtle()
textovik.hideturtle()
chucha.hideturtle()
zoo.hideturtle()
turtle.hideturtle()
chucha.speed(200)
zoo.speed(200)
chucha.up()
chucha.goto(0,-50)
chucha.down()
turtle.speed(200)
chucha.pensize(5)
chucha.fillcolor("grey")
chucha.begin_fill()
chucha.up()
chucha.backward(50)
chucha.left(90)
chucha.forward(50)
chucha.right(90)

chucha.down()
chucha.left(55)
chucha.pencolor("dim grey")
for i in range(4):
    chucha.left(45)
    chucha.forward(100)
    chucha.right(45)
    chucha.forward(100)
    chucha.right(45)
    chucha.forward(100)
chucha.right(67.5)
chucha.forward(630)
chucha.end_fill()
turtle.bgcolor("lightblue")
turtle.pencolor("green")
turtle.fillcolor("lightgreen")
turtle.begin_fill()
turtle.forward(2000)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(4000)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(2000)
turtle.end_fill()
zoo.hideturtle()
zoo.lt(90)
#recursion
def draw(l):
    if(l<10):
        return
    else:
        zoo.forward(l)
        zoo.left(30)
        draw(l/2)
        zoo.right(60)
        draw(l/2)
        zoo.left(30)
        zoo.backward(l)
def turtles():
    turtle.reset()
    chucha.reset()
    textovik.reset()
    zoo.reset()

zoo.pensize(5)
zoo.color("green","red")
zoo.up()
zoo.goto(-200,-350)
zoo.down()
draw(120)
zoo.goto(-50,-200)
draw(100)
zoo.goto(50,-100)
draw(80)
zoo.goto(100,-50)
zoo.up()
zoo.goto(50,-350)
zoo.down()
zoo.goto(250,-50)
textovik.up()
textovik.goto(100,300)
textovik.backward(700)
textovik.down()
textovik.pensize(3)
textovik.up()
textovik.write("Вы находитесь в землях, заселенных драконами.\nПеред собой вы видите две пещеры.\nВ одной из них — дружелюбный дракон,\nкоторый готов поделиться с вами своими сокровищами.\nВо второй — жадный и голодный дракон,\n который мигом вас съест.", font=("Arial", 16, "normal"))
chucha.up()
chucha.goto(60,250)
chucha.right(245)
chucha.forward(150)
chucha.down()
chucha.pencolor("darkgrey")
chucha.fillcolor("dim grey")
chucha.begin_fill()
chucha.circle(80)
chucha.circle(70)
chucha.end_fill()
chucha.up()
chucha.goto(300,80)
chucha.down()
chucha.pencolor("darkgrey")
chucha.fillcolor("dim grey")
chucha.begin_fill()
chucha.circle(80)
chucha.circle(70)
chucha.up()
chucha.end_fill()

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
    for i in range(1):
        if n == "1":
            print("Пойдём...")
            turtles()
            cave=turtle.Turtle()
            cave.hideturtle()
            turtle.bgcolor("black")
            cave.speed(200)
            turtle.speed(200)
            turtle.fillcolor("maroon")
            turtle.begin_fill()
            turtle.speed(200)
            turtle.up()
            turtle.goto(-300,-10)
            turtle.down()
            for i in range(6):
                turtle.forward(25)
                turtle.left(80)
                turtle.forward(25)
                turtle.right(80)
            turtle.forward(25)
            turtle.circle(-50,60)
            turtle.circle(-25,80)
            turtle.right(100)
            turtle.forward(15)
            turtle.backward(15)
            turtle.left(100)
            turtle.circle(-25,80)
            turtle.right(180)
            turtle.circle(-80,160)
            turtle.circle(125,50)
            turtle.circle(-45,50)
            turtle.left(20)
            turtle.right(40)
            turtle.forward(25)
            turtle.left(90)
            turtle.backward(55)
            turtle.end_fill()
            turtle.up()
            turtle.goto(-150,115)
            turtle.left(125)
            turtle.forward(70)
            turtle.down()
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.circle(5)
            turtle.end_fill()
            turtle.begin_fill()
            turtle.fillcolor("darkred")
            turtle.circle(3)
            turtle.end_fill()
            turtle.up()
            turtle.goto(-175,115)
            turtle.goto(-300,-10)
            turtle.down()
            turtle.left(5)
            for i in range(4):
                turtle.forward(25)
                turtle.left(80)
                turtle.forward(25)
                turtle.right(80)
            turtle.right(45)
            turtle.right(180)
            turtle.fillcolor("maroon")
            turtle.begin_fill()
            turtle.forward(125)
            turtle.left(75)
            turtle.forward(62.5)
            turtle.left(165)
            for k in range(4):
                turtle.circle(-15,80)
                turtle.circle(15,80)
            turtle.left(100)
            turtle.forward(125)
            turtle.left(75)
            turtle.forward(62.5)
            turtle.left(165)
            for k in range(4):
                turtle.circle(-15,80)
                turtle.circle(15,80)
            turtle.forward(8)
            turtle.up()
            turtle.goto(-180,-52)
            turtle.down()
            turtle.right(180)
            turtle.circle(45,50)
            turtle.end_fill()

            turtle.left(45)
            turtle.left(90)
            turtle.fillcolor("maroon")
            turtle.begin_fill()
            turtle.circle(-50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(50,50)
            turtle.left(180)
            turtle.right(30)
            turtle.circle(-50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(50,50)
            turtle.circle(50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(-45,45)
            turtle.circle(50,50)
            turtle.end_fill()
            turtle.up()
            turtle.pencolor("maroon")
            turtle.goto(-150,-10)
            turtle.goto(-195,-50)
            turtle.left(110)
            turtle.forward(115)
            turtle.right(35)
            turtle.forward(15)
            turtle.left(90)
            turtle.down()
            turtle.fillcolor("maroon")
            turtle.begin_fill()
            turtle.circle(-150,50)
            turtle.left(180)
            turtle.circle(360,23)
            turtle.end_fill()
            turtle.up()
            cave.up()
            cave.goto(0,-100)
            cave.pencolor("lightgrey")
            cave.fillcolor("grey")
            cave.begin_fill()
            cave.down()
            cave.forward(2000)
            cave.right(90)
            cave.forward(700)
            cave.right(90)
            cave.forward(4000)
            cave.right(90)
            cave.forward(700)
            cave.right(90)
            cave.forward(2000)
            cave.end_fill()
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
            turtles()
            cave=turtle.Turtle()
            turtle.bgcolor("black")
            cave.speed(200)
            turtle.speed(200)
            turtle.fillcolor("forest green")
            turtle.begin_fill()
            turtle.speed(200)
            turtle.up()
            turtle.goto(-300,-10)
            turtle.down()
            for i in range(6):
                turtle.forward(25)
                turtle.left(80)
                turtle.forward(25)
                turtle.right(80)
            turtle.forward(25)
            turtle.circle(-50,60)
            turtle.circle(-25,80)
            turtle.right(100)
            turtle.forward(15)
            turtle.backward(15)
            turtle.left(100)
            turtle.circle(-25,80)
            turtle.right(180)
            turtle.circle(-80,160)
            turtle.circle(125,50)
            turtle.circle(-45,50)
            turtle.left(20)
            turtle.right(40)
            turtle.forward(25)
            turtle.left(90)
            turtle.backward(55)
            turtle.end_fill()
            turtle.up()
            turtle.goto(-150,115)
            turtle.left(125)
            turtle.forward(70)
            turtle.down()
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.circle(5)
            turtle.end_fill()
            turtle.begin_fill()
            turtle.fillcolor("darkred")
            turtle.circle(3)
            turtle.end_fill()
            turtle.up()
            turtle.goto(-175,115)
            turtle.goto(-300,-10)
            turtle.down()
            turtle.left(5)
            for i in range(4):
                turtle.forward(25)
                turtle.left(80)
                turtle.forward(25)
                turtle.right(80)
            turtle.right(45)
            turtle.right(180)
            turtle.fillcolor("forest green")
            turtle.begin_fill()
            turtle.forward(125)
            turtle.left(75)
            turtle.forward(62.5)
            turtle.left(165)
            for k in range(4):
                turtle.circle(-15,80)
                turtle.circle(15,80)
            turtle.left(100)
            turtle.forward(125)
            turtle.left(75)
            turtle.forward(62.5)
            turtle.left(165)
            for k in range(4):
                turtle.circle(-15,80)
                turtle.circle(15,80)
            turtle.forward(8)
            turtle.up()
            turtle.goto(-180,-52)
            turtle.down()
            turtle.right(180)
            turtle.circle(45,50)
            turtle.end_fill()

            turtle.left(45)
            turtle.left(90)
            turtle.fillcolor("forest green")
            turtle.begin_fill()
            turtle.circle(-50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(50,50)
            turtle.left(180)
            turtle.right(30)
            turtle.circle(-50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(50,50)
            turtle.circle(50,50)
            turtle.left(180)
            turtle.left(15)
            turtle.circle(-45,45)
            turtle.circle(50,50)
            turtle.end_fill()
            turtle.up()
            turtle.pencolor("darkgreen")
            turtle.goto(-150,-10)
            turtle.goto(-195,-50)
            turtle.left(110)
            turtle.forward(115)
            turtle.right(35)
            turtle.forward(15)
            turtle.left(90)
            turtle.down()
            turtle.fillcolor("forest green")
            turtle.begin_fill()
            turtle.circle(-150,50)
            turtle.left(180)
            turtle.circle(360,23)
            turtle.end_fill()
            turtle.up()
            cave.up()
            cave.goto(0,-100)
            cave.pencolor("lightgrey")
            cave.fillcolor("grey")
            cave.begin_fill()
            cave.down()
            cave.forward(2000)
            cave.right(90)
            cave.forward(700)
            cave.right(90)
            cave.forward(4000)
            cave.right(90)
            cave.forward(700)
            cave.right(90)
            cave.forward(2000)
            cave.end_fill()
            cave.pencolor("yellow")
            cave.fillcolor("saddle brown")
            cave.begin_fill()
            cave.forward(200)
            cave.left(90)
            cave.forward(100)
            cave.left(90)
            cave.forward(200)
            cave.left(90)
            cave.forward(100)
            cave.left(90)
            cave.forward(200)
            cave.left(45)
            cave.forward(50)
            cave.left(45)
            cave.forward(100)
            cave.left(135)
            cave.forward(50)
            cave.right(45)
            cave.forward(200)
            cave.right(135)
            cave.forward(50)
            cave.right(45)
            cave.forward(200)
            cave.left(45)
            cave.circle(50,100)
            cave.left(35)
            cave.forward(200)
            cave.right(35)
            cave.circle(50,-100)
            cave.end_fill()
            time.sleep(2)
            print("Ты встретил доброго дракона....")
            time.sleep(2)
            print("Он тебя не тронул")
            print("="*40)
            deystvie()
            print("="*40)
            user_input = input("Что ты сделаешь?")
        if user_input == "Покормить":
             print("Дракон тебя принял и будет рад тебя видеть в будущем")
             choose = False
        elif user_input == "Погладить":
             print("Дракон тебя принял и будет рад тебя видеть в будущем")
             choose = False
        elif user_input == "Убить":
             print("Вы ничего не смогли сделать дракону")
             print("Вы стали вкусным ужином дракона")
             choose = False
        elif user_input == "Привести своих друзей":
             print("Дракон испугался толпы и съел вас всех")
             print("Вы стали вкусным ужином дракона")
             choose = False
        else:
            print("Данной опции не существует")
            choose = False
             

#=====================================================================================================================================
print("Спасибо за игру!")
konets = turtle.Turtle()
konets.hideturtle()
konets.speed(200)
konets.pensize(3)
konets.pencolor("white")
konets.write("Конец", font=("Arial", 128, "normal"))
print('='*17,"Конец",'='*18)
time.sleep(5)