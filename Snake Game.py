# Basic Snake Game - Python 3.7
# By - Berkan Karalar 
"""
A LITTLE NOTE: This basic-game programing is beginner friendly. And still, you can add/discard things as you want. For EXAMPLE;
With the "Pickle" formula you can make a Score Table. Like in the old arcade games. So you can see your score with the name you input.
Basically a score saving system. I tried my best to explain chapter by chapter what command works on which purpose. 
"""
#Every imports are already exists in Python 3 already. You don't need any else addons or neither modules
#If you are a beginner don't wory. You can start this in Lunix & W10. All you need is only PYTHON 3.6 or newer versions

import turtle
import time
import random

delay = 0.1

# Score Table 
score = 0 
high_score = 0 # You can use some variations to save your scores. 

# Screen
wn = turtle.Screen() 
wn.title("Python Snake by @Vintern")
wn.bgcolor("black") # Background color
wn.setup(width=600, height=600) # Screen Border lenght - Changeble but WARNING! You need to re-code some in "Main Game Loop" and Snake Border Setup
wn.tracer(0)  # Turns off the screen updates - You need to update screen manually

# Head of The Snake 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white") # Change able
head.penup()
head.goto(0, 0)
head.direction = "stop" # Game Start Position

# Food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100) # Food will spawn randomly between ZERO & HUNDRED. 0 -ZERO- is the center of the screen.  

segments = []

# Pen "Score System" -seen from this creator -Christian Thompson- 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white") # Score Color
pen.penup()
pen.hideturtle()
pen.goto(0, 260) # Do not change it if you don't know what it is 
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Fonctions for Snake - movements -
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Key Bindings - IF YOU WANT TO BIND TYPICAL ↑↓→ KEYS; you need to basically write "Up" - "Down"
wn.listen()
wn.onkeypress(go_up, "w") # Up can changable with ↑↓→ - START WITH A CAPITAL LETTER like in the example
wn.onkeypress(go_down, "s") # Down
wn.onkeypress(go_left, "a") # Left
wn.onkeypress(go_right, "d") # Right

"""
NOTE: In readme file i stated a known bug. Here it is in this part. 
The codes in the below for border-death. Which i said that the game will still run on a 600x600 angle even if you fullscreen the window.
So basically when coding i set up the screen as 600x600 and even if you fullsize the window without any re-setup it will still run in 600x600
If you want to fix this bug by change the resulotion you also need to change setup border-death - food spawn codes to work the game correctly. 
"""

# Main Game Loop -Score - Keybinds - Game Over etc.-
while True:
    wn.update()

    # BORDER DEATH
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # DONT DELETE THIS CODE
        # When the snake dies, body of the snake still can seeable in the screen. This code below spawns body-parts to off-screen places.
        for segment in segments:
            segment.goto(1000, 1000)

        # Same usage as the above code. - it doesn't resets the writen high score 
        segments.clear()

        # Score-Reset after death 
        score = 0

        # Even after the death & game reset snake still goes with the same-speed before death.
        # We can call this as a "Little Bug". But we can change this with this delay code too. 
        delay = 0.1

        pen.clear()
        pen.write("Puan: {}  En Yüksek Puan: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Snake gets bigger & gets score after food
    if head.distance(food) < 20:
        # Random-Spawn for the food.
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # A new body-segment after every food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Reduce Delay
        delay -= 0.001

        # Score per Food 
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # BODY SEGMENTS OF THE SNAKE - Minus numbers is for them to follow the Head 
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Head of the Snake 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Second Game-Over Reason - Game-Overs if snake hits its own body. 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000, 1000)


            segments.clear()


            score = 0

            
            delay = 0.1

            
            pen.clear()
            pen.write("Score: {}  Hight Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()