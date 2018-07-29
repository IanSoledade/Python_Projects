#!/bin/python3
Feedback = open('Feedback2.txt', 'a')
from random import randint
import random
import time
from sys import exit

options = ['Ok. See you when you are!', 'Alright. **sniffles**', 'Come on, please???', 'Come back when you are!']
options2 = ['Great!', 'Awesome!', "I would ask for a high five, but I don't want your mitts on my screen.", 'Cool. Maybe someday I will learn how to play with "Lizard" and "Spock".', "OK then. Let's go!"]

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

def game():
  player = input('Enter Rock, Paper, or Scissors: ')

  computerchoice = randint(1,3)

  if computerchoice == 1:
    computer = 'Rock'
  elif computerchoice == 2:
    computer = 'Paper'
  else:
    computer = 'Scissors'
  print('3')
  time.sleep(1)
  print('2')
  time.sleep(1)  
  print('1')
  time.sleep(1)
  
  print('Computer played:', computer)
  if computer == 'Rock' and player == 'Rock':
    print("We're in between a Rock and a Hard Place. Tie!")
  elif computer == 'Rock' and player == 'Paper':
    print("I guess Paper came out on top of the Rock. You win!")
  elif computer == 'Rock' and player == 'Scissors':
    print("Those Scissors can't cut this Rock. I win!")
  elif computer == 'Paper' and player == 'Rock':
    print('My Paper is now covering your Rock. I do not know what to say other than I win!')
  elif computer == 'Paper' and player == 'Paper':
   print('There is nothing to do with two sheets of Paper. Tie!')
  elif computer == 'Paper' and player == 'Scissors':
    print('I guess I brought Paper to a Scissors fight. You win')
  elif computer == 'Scissors' and player == 'Rock':
    print('Rocks and Scissors. You win. You just win.')
  elif computer == 'Scissors' and player == 'Paper':
    print('Ahem. My Scissors are ''made'' for cutting Paper. I win!')
  elif computer == 'Scissors' and player == 'Scissors':
    print('I do not want to play swords with Scissors right now. Tie!')
  else:
    print("I am sorry. I do not understand '", player + "'.")
  
while True: 
  game()
  question = input('Play again? (y/n)')
  
  if question == 'n':
    feedback = input('Please write a short sentence or two to help make me even cooler!')
    Feedback.write(feedback)
    Feedback.close()
    break
  elif question == 'y':
    print(random.choice(options2))
  else:
    print("I'll take that as a no.")
    feedback = input('Please write a short sentence or two to help make me even cooler!')
    Feedback.write(feedback)
    Feedback.close()
    break

print('Thanks for playing!')
time.sleep(2)
