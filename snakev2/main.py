from turtle import Turtle , Screen
from snake import Snake
from time import sleep
from random import randint



screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")

#all snake turtle will be inside of this list
listforsnake = []

#making the leader turtle which will lead the rest of the turtles
lisan_al_gaib = Snake()
lisan_al_gaib.color("green")

#turtle who will write the words game over when snake dies
busted = Turtle()
busted.ht()
busted.penup()
busted.color("white")

"""turtle who will write the score on the screen"""
scoreturtle = Turtle(visible=False)
highscoreturtle = Turtle(visible=False)
highscoreturtle.color("white")
highscoreturtle.penup()
highscoreturtle.teleport(0,260)

"""initial score"""
score = 0


"""turtle for the apple"""
apple = Turtle()
apple.teleport(randint(-250,250),randint(-250,250))
apple.shape("circle")
apple.color("red")
apple.penup()

"""append leader and rest 3 of the snake body"""
listforsnake.append(lisan_al_gaib)
for i in range(3):
    body = Snake()
    listforsnake.append(body)


#variable to make the game loop running
running = True


"""functions which will be used for the listen command in python"""
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

"""we will change this variable to increase the difficulty of the game with time"""
speed = 0.1


screen.listen()
screen.tracer(0)

def reading():
    with open("highscore.txt", "r") as file1:
        content = file1.read()
        return int(content)

def writing(towrite):
    with open("highscore.txt", "w") as file2:
        file2.write(str(towrite))



"""function which resets the game when pressed r"""

def restart():
    global score
    global body
    score = 0

    for body in listforsnake[4:]:
        body.hideturtle()
        listforsnake.remove(body)

    listforsnake[0].setheading(0)
    listforsnake[0].setpos(0.0,0.0)
    listforsnake[1].setpos(-20,0.0)
    listforsnake[2].setpos(-40, 0.0)
    listforsnake[3].setpos(-60, 0.0)

    busted.reset()
    busted.ht()
    busted.penup()
    busted.color("white")
def quit():
    global running
    running = False

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(quit, "q")



while running:
    """changing the difficulty of the game"""
    if score == 10:
        speed = 0.08
    if score == 20:
        speed = 0.05
    if score == 30:
        speed = 0.03




    leader_position_xcor = lisan_al_gaib.xcor()
    leader_position_ycor = lisan_al_gaib.ycor()
    lisan_al_gaib.fd(20)

    if lisan_al_gaib.distance(apple) <= 20:
        apple.teleport(randint(-250,250),randint(-250,250))
        score += 1
        body = Snake()
        listforsnake.append(body)

    for i in listforsnake[1:]:
        positiontempx = i.xcor()
        positiontempy = i.ycor()

        i.setx(leader_position_xcor)
        i.sety(leader_position_ycor)

        leader_position_xcor = positiontempx
        leader_position_ycor = positiontempy

    if lisan_al_gaib.xcor() >= 290:
        busted.write("Game Over", False, "center", ("courier", 20, "normal"))

        restart()

        screen.update()
        sleep(1)



    if lisan_al_gaib.xcor() <= -290:
        busted.write("Game Over", False, "center", ("courier", 20, "normal"))

        restart()

        screen.update()
        sleep(1)


    if lisan_al_gaib.ycor() >= 290:

        busted.write("Game Over", False, "center", ("courier", 20, "normal"))

        restart()


        screen.update()
        sleep(1)


    if lisan_al_gaib.ycor() <= -290:
        busted.write("Game Over", False, "center", ("courier", 20, "normal"))

        restart()

        screen.update()
        sleep(1)

    scoreturtle.reset()
    scoreturtle.ht()
    scoreturtle.color("white")
    scoreturtle.teleport(20,260)
    scoreturtle.write(f"score = {str(score)}", False, "left", ("courier", 20, "normal"))
    highscore = reading()
    if score > highscore:
        writing(score)
    highscoreturtle.reset()
    highscoreturtle.ht()
    highscoreturtle.color("white")
    highscoreturtle.penup()
    highscoreturtle.teleport(0, 260)
    highscoreturtle.write(f"high score = {highscore}", False, "right", ("courier", 20, "normal"))
    screen.update()
    sleep(speed)

