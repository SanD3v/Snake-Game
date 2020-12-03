from turtle import *
from time import sleep
from random import randint

# Init Window
win = Screen()
win.setup(height=600, width=600)
win.bgcolor('blue')
win.title('Snake Game')
win.tracer(0)

# Scores
score = 0
highScore = 0

delay = 0.1
tails = []

# Snake Head
char = Turtle()
char.speed(0)
char.shape('circle')
char.color('yellow')
char.penup()
char.goto(0, 0)
char.direction = 'stop'

# snake food
food = Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(randint(-270, 270), randint(-270, 270))

# Init Border
border = Turtle()
border.color('cyan')
border.penup()
border.goto(-280, 280)
border.pendown()
border.begin_fill()
border.forward(560)
border.left(-90)
border.forward(560)
border.left(-90)
border.forward(560)
border.left(-90)
border.forward(560)
border.end_fill()
border.penup()
border.goto(1000, 1000)
border.pendown()

# ScoreBoard
sc = Turtle()
sc.speed(0)
sc.shape('square')
sc.color('black')
sc.penup()
sc.goto(0, 250)
sc.hideturtle()
sc.write('Score : {} HighScore : {}'.format(score, highScore), align='center', font=('', '20', 'normal'))


def up():
    if char.direction != 'down':
        char.direction = 'up'


def down():
    if char.direction != 'up':
        char.direction = 'down'


def right():
    if char.direction != 'left':
        char.direction = 'right'


def left():
    if char.direction != 'right':
        char.direction = 'left'


def stop():
    char.direction = 'stop'


def move():
    if char.direction == 'up':
        char.sety(char.ycor() + 10)

    if char.direction == 'down':
        char.sety(char.ycor() - 10)

    if char.direction == 'right':
        char.setx(char.xcor() + 10)

    if char.direction == 'left':
        char.setx(char.xcor() - 10)


# KeyBoard Bindigs
win.listen()
win.onkeypress(up, 'w')
win.onkeypress(down, 's')
win.onkeypress(right, 'd')
win.onkeypress(left, 'a')
win.onkeypress(win.bye, 'q')  # quit
win.onkeypress(stop, 'e')  # Pause

while True:
    win.update()
    # check for collision with food
    if char.distance(food) < 20:
        score += 10
        delay -= 0.001
        food.goto(randint(-270, 270), randint(-270, 270))
        tail = Turtle()
        tail.speed(0)
        tail.shape('square')
        tail.color('yellow')
        tail.penup()
        tails.append(tail)
        if score > highScore:
            highScore = score
            sc.clear()
            sc.write('Score : {} HighScore : {}'.format(score, highScore), align='center', font=('', '20', 'normal'))

    # check for collision with wall
    if char.ycor() == 270 or char.ycor() == -270 or char.xcor() == 270 or char.xcor() == -270:
        score = 0
        delay = 0.1
        char.goto(0, 0)
        char.direction = 'stop'
        # Move the tail out of the window and clear tails
        for t in tails:
            t.goto(1000, 1000)
        tails = []
    # moving the tails wrt the head
    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)
    if len(tails) > 0:
        x = char.xcor()
        y = char.ycor()
        tails[0].goto(x, y)

    move()

    # check for collision with body
    for k in tails:
        if k.distance(char) < 10:
            sleep(1)
            char.goto(0, 0)
            char.direction = "stop"

            # hide segments
            for m in tails:
                m.goto(1000, 1000)
            tails.clear()
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score, highScore), align="center", font=("", 24, "normal"))
    sleep(delay)

mainloop()
