# the Snake game
# By patrick block Pblock1@cnm.edu
# 7/01/2024


import time
import random
import turtle

delay = 0.1 
score = 0
high_score = 0

#screen of the game
game_window = turtle.Screen()
game_window.title("Snake by patrick block")
game_window.bgcolor("black")
game_window.setup(width=900, height=900)
game_window.tracer(0) 

#head  of our snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#body of the snake
segments = []

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#points at the top
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 400)
pen.write("score: 0 high score: 0", align="center", font=("Arial", 20, "normal"))
# Functions

# movement cords
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

# movement direction
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

#binding
game_window.listen()
game_window.onkeypress(go_up, "w")
#gameWindow.onkeypress(go_up, "K_UP")
game_window.onkeypress(go_down, "s")
#gameWindow.onkeypress(go_down, "K_DOWN")
game_window.onkeypress(go_left, "a")
#gameWindow.onkeypress(go_left, "K_LEFT")
game_window.onkeypress(go_right, "d")
#gameWindow.onkeypress(go_right, "K_RIGHT")


#main
while True:
    game_window.update()

    #wall death
    if head.xcor()>440 or head.xcor()<-440 or head.ycor()>440 or head.ycor()<-440:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

    #scoring
    if head.distance(food) < 20 :
        x = random.randint(-440,440)
        y = random.randint(-440,440)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -=0.001
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #body death
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))
            


    time.sleep(delay)

gameWindow.mainloop()