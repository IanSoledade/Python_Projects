#!/bin/python3
import time
score = 0
from sys import exit
import random

options = ['Ok. See you when you are!', 'Alright. **sniffles**', 'Come on, please???', 'Come back when you are!']
options2 = ['Great!', 'Awesome!', "I would ask for a high five, but I don't want your mitts on my screen.", "OK then. Let's go!"]

def ready():
  readyness = input('Are you ready? (y/n) ')
  if readyness == 'n':
    print(random.choice(options))
    time.sleep(2)
    exit(0)
  elif readyness == 'y':
    print(random.choice(options2))
  else:
    print("I'm sorry. I don't understand '", readyness + "'.")

ready()

Feedback = open('Feedback.txt', 'a')

def checkAnswer(guess, correctAnswer, correctAnswer2):
  if guess.upper().find(str(correctAnswer2).upper()) > -1 or guess.upper().find(str(correctAnswer).upper()) > -1 and not guess.upper().find(str(correctAnswer).upper() + correctAnswer) > -1:
    print('Correct!')
    valueReturn = True
  else:
    print('Wrong!')
    valueReturn = False
  return valueReturn

def askQuestion(question, answer, answer2):
  while True:
    global score
    Guess = str(input(question))
    trueOrFalse = checkAnswer(Guess, answer, answer2)
    if trueOrFalse == False:
      Guess = input("Try again! ")
      trueOrFalse = checkAnswer(Guess, answer, answer2)
    else:
      score += 3
      break
    if trueOrFalse == False:
      Guess = input("One more try! ")
      trueOrFalse = checkAnswer(Guess, answer, answer2)
    else:
      score += 2
      break
    if trueOrFalse == False:
      print("The answer was", answer + '.')
      break
    else:
      score += 1
      break
  return

askQuestion("What is the slope of the line y=2x+5? ", '2', 'two')
print('Score: ', score)
askQuestion("Fill in the blank: For those about to rock, we _____ you! ", 'Salute', 'Salute')
print('Score: ', score)
askQuestion("What was Wade's fake identity's last name in the book Ready Player One? ", 'Lynch', 'Lynch')
print('Score: ', score)
askQuestion("What is the line you would use to define a function called turnLeft in Swift with no parameters? ", 'func turnLeft():', 'func turnLeft():')
print('Score: ', score)
askQuestion("In a 3-4-3 formation in soccer, how many forwards are there? ", '3', "Three")
print('Your final score is: ', score)
feedback = input('Please write a short sentence or two so we can improve this quiz. ')
Feedback.write('\n' + feedback + '\n')
Feedback.close()
print('Thanks for playing!')
time.sleep(2)
