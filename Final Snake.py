import random
import turtle
import time

screen = turtle.Screen()
screen.bgcolor('orange')

s = turtle.Turtle()
s.shape('square')
s.color('blue')
s.speed(0)
s.penup()
s.pencolor('brown')
s.hideturtle()

first = True

l = turtle.Turtle()
l.shape('circle')
l.color('green')
l.penup()
l.hideturtle()

leafdistance = 75
gameStarted = False
score = 0
highscore = open('High Scores - DO NOT OPEN/highScore2.txt', 'r')
high_score = highscore.read()
hscore = high_score
highscore.close()

tT = turtle.Turtle()
tT.hideturtle()
tT.color('blue')
tT.write('Press SPACE to start.', align='center', font=('Comic Sans MS', 20))
tT.penup()

sT = turtle.Turtle()
sT.color('blue')
sT.hideturtle()

def outsideWindow():
  leftWall = -float(turtle.window_width())/2
  rightWall = float(turtle.window_width())/2
  bottomWall = -float(turtle.window_height())/2
  topWall = float(turtle.window_height())/2
  (x,y) = s.position()
  outside = \
  x < leftWall or \
  x > rightWall or \
  y < bottomWall or \
  y > topWall
  return outside

def gameOver():
  global score
  global gameStarted
  global first
  first = True
  s.clearstamps()
  s.hideturtle()
  l.hideturtle()
  tT.setpos(0,0)
  s.setpos(0,0)
  score = 0
  tT.write('Game OVER!', align='center',font=('Comic Sans MS', 20))
  gameStarted = False
  time.sleep(3)
  tT.clear()
  sT.clear()
  s.setheading(0)
  tT.write('Press SPACE to start.', align='center', font=('Comic Sans MS', 20))

def displayScore():
  global score
  global hscore
  sT.clear()
  sT.penup()
  x = int((turtle.window_width()/2)) - 100
  y = int((turtle.window_height()/2)) - 25
  sT.setpos(x,y)
  sT.write('HS: ' + str(hscore) + ' Score: ' + str(score), align='center', font=('Comic Sans MS', 10))

def placeLeaf():
  global leafdistance
  l.hideturtle()
  l.setx(random.randint(-int(turtle.window_width()/2) + leafdistance, int(turtle.window_width()/2) - leafdistance))
  l.sety(random.randint(-int(turtle.window_height()/2) + leafdistance, int(turtle.window_height()/2) - leafdistance))
  l.showturtle()

def runGame():
    global gameStarted
    global score
    global hscore
    global first
    if gameStarted:
        return
    gameStarted = True
    tT.clear()
    speed = 10
    s.showturtle()
    displayScore()
    placeLeaf()
    while True:
        if outsideWindow():
            gameOver()
            break
        if s.distance(l) < 15:
            placeLeaf()
            s.fd(10)
            s.color('brown')
            stamp = s.stamp()
            s.fd(10)
            stamp = s.stamp()
            s.color('blue')
            score += 10
            if score > int(hscore):
                highScore = open('High Scores - DO NOT OPEN/highScore2.txt', 'w')
                hscore = score
                highScore.write(str(hscore))
                highScore.close()
            displayScore()
        if first == True:
            for i in range(1,5):
                stamp = s.stamp()
                s.fd(10)
                first = False
        else:
            s.fd(10)
            s.color('brown')
            stamp = s.stamp()
            s.color('blue')
            s.clearstamps(1)
                
def moveUp():
  if s.heading() != 270:
    s.setheading(90)
  
def moveDown():
  if s.heading() != 90:
    s.setheading(270)
  
def moveLeft():
  if s.heading() != 0:
    s.setheading(180)
  
def moveRight():
  if s.heading() != 180:
    s.setheading(0)
  
screen.onkey(runGame, 'space')
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")
screen.onkey(moveLeft, "Left")
screen.onkey(moveRight, "Right")

screen.listen()
turtle.mainloop()
