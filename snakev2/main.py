from turtle import Turtle , Screen 
from snake import Snake
from time import sleep
from random import randint

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")

list = []

lisan_al_gaib = Snake()
lisan_al_gaib.color("green")

apple = Turtle()
apple.teleport(randint(-250,250),randint(-250,250))
apple.shape("circle")
apple.color("red")
apple.penup()

list.append(lisan_al_gaib)
for i in range(3):
    body = Snake()
    list.append(body)



running = True
def up():
    if lisan_al_gaib.heading() != 270.00:
        lisan_al_gaib.setheading(90)
    else:
        pass
def down():
    if lisan_al_gaib.heading() != 90.00:
        lisan_al_gaib.setheading(270)
    else:
        pass
def left():
    if lisan_al_gaib.heading() != 0.00:
        lisan_al_gaib.setheading(180)
    else:
        pass
def right():
    if lisan_al_gaib.heading() != 180.00:
        lisan_al_gaib.setheading(0)
    else:
        pass



screen.listen()
screen.tracer(0)
while running:
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")

    leader_position_xcor = lisan_al_gaib.xcor()
    leader_position_ycor = lisan_al_gaib.ycor()
    lisan_al_gaib.fd(20)
    if lisan_al_gaib.distance(apple) <= 20:
        apple.teleport(randint(-250,250),randint(-250,250))
        body = Snake()
        list.append(body)
    for i in list[1:]:
        positiontempx = i.xcor()
        positiontempy = i.ycor()

        i.setx(leader_position_xcor)
        i.sety(leader_position_ycor)

        leader_position_xcor = positiontempx
        leader_position_ycor = positiontempy

    if lisan_al_gaib.xcor() >= 290:
        running  = False
    if lisan_al_gaib.xcor() <= -290:
        running  = False
    if lisan_al_gaib.ycor() >= 290:
        running  = False
    if lisan_al_gaib.ycor() <= -290:
        running  = False

    screen.update()
    sleep(0.1)




screen.exitonclick()