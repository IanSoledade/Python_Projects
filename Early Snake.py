import random
import turtle
import time

screen = turtle.Screen()
screen.bgcolor('orange')

s = turtle.Turtle()
s.shape('circle')
s.color('brown')
s.speed(0)
s.penup()
s.hideturtle()

l = turtle.Turtle()
l.shape('circle')
l.color('green')
l.penup()
l.hideturtle()

m = turtle.Turtle()
m.shape('circle')
m.color('red')
m.penup()
m.hideturtle()

u = turtle.Turtle()
u.shape('circle')
u.color('black')
u.penup()
u.hideturtle()

leafdistance = 75
gameStarted = False
score = 0
highscore = open('High Scores - DO NOT OPEN/highScore.txt', 'r')
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
  leftWall = float(-turtle.window_width())/2
  rightWall = float(turtle.window_width())/2
  bottomWall = float(-turtle.window_height())/2
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
  s.hideturtle()
  l.hideturtle()
  u.hideturtle()
  m.hideturtle()
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
  x = (turtle.window_width()/2) - 100
  y = (turtle.window_height()/2) - 25
  sT.setpos(x,y)
  sT.write('HS: ' + str(hscore) + ' Score: ' + str(score), align='center',font=('Comic Sans MS', 10))

def placeLeaf():
  global leafdistance
  l.hideturtle()
  l.setx(random.randint(-int(turtle.window_width()/2) + leafdistance, int(turtle.window_width()/2) - leafdistance))
  l.sety(random.randint(-int(turtle.window_height()/2) + leafdistance, int(turtle.window_height()/2) - leafdistance))
  l.showturtle()

def placeMega():
  global leafdistance
  m.hideturtle()
  m.setx(random.randint(-int(turtle.window_width()/2) + leafdistance, int(turtle.window_width()/2) - leafdistance))
  m.sety(random.randint(-int(turtle.window_height()/2) + leafdistance, int(turtle.window_height()/2) - leafdistance))
  m.showturtle()

def placeUltra():
  global leafdistance
  u.hideturtle()
  u.setx(random.randint(-int(turtle.window_width()/2) + leafdistance, int(turtle.window_width()/2) - leafdistance))
  u.sety(random.randint(-int(turtle.window_height()/2) + leafdistance, int(turtle.window_height()/2) - leafdistance))
  u.showturtle()

def startGame():
  global gameStarted
  global score
  global hscore
  global leafdistance
  if gameStarted:
    return
  gameStarted = True
  tT.clear()
  s.speed = 3
  sLength = 3
  s.resizemode('user')
  s.turtlesize(1, sLength, 1)
  s.showturtle()
  displayScore()
  placeLeaf()
  placeMega()
  placeUltra()
  while True:
    if outsideWindow():
      gameOver()
      break
    if s.distance(l) < 20:
      placeLeaf()
      sLength += 1
      s.shapesize(1, sLength, 1)
      s.speed += 1
      score += 10
      if score >= int(hscore):
        highScore = open('High Scores - DO NOT OPEN/highScore.txt', 'w')
        hscore = score
        highScore.write(str(hscore))
        highScore.close()
      displayScore()
    elif s.distance(m) < 15:
      placeMega()
      sLength += 2
      s.shapesize(1, sLength, 1)
      s.speed += 1.5
      score += 50
      if score >= int(hscore):
        highScore = open('highScore.txt', 'w')
        hscore = score
        highScore.write(str(hscore))
        highScore.close()
      displayScore()
    elif s.distance(u) < 10:
      placeUltra()
      sLength += 3
      s.shapesize(1, sLength, 1)
      s.speed += 2
      score += 100
      if score >= int(hscore):
        highScore = open('highScore.txt', 'w')
        hscore = score
        highScore.write(str(hscore))
        highScore.close()
      displayScore()
    s.forward(s.speed)

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
  
screen.onkey(startGame, 'space')
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")
screen.onkey(moveLeft, "Left")
screen.onkey(moveRight, "Right")

screen.listen()
turtle.mainloop()
