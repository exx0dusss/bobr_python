import turtle
turtle.speed(200)
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor("blue")
for b in range(3):
    turtle.fillcolor("purple")
    for j in range(6):
        for i in range(1):
            turtle.fillcolor("lightblue")
            for x in range(6):
                turtle.forward(50)
                turtle.left(60)
            turtle.right(120)
        turtle.forward(50)
        turtle.left(60)
    turtle.right(120)
turtle.end_fill()
turtle.mainloop()