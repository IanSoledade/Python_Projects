#!/bin/python3

import string
import random
import time
import datetime

#Password_Generator
print('Password generator started at', datetime.datetime.now())

items = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '-', '%', '/', '.', '?', '1', '2', '3,' '4', '5', '6', '7', '8', '9', '0']

while True:
  q = random.choice(items)
  w = random.choice(items)
  e = random.choice(items)
  r = random.choice(items)
  t = random.choice(items)
  y = random.choice(items)
  u = random.choice(items)
  i = random.choice(items)
  o = random.choice(items)
  p = random.choice(items)
  a = random.choice(items)
  s = random.choice(items)
  d = random.choice(items)
  f = random.choice(items)
  g = random.choice(items)
  h = random.choice(items)

  password = q + w + e + r + random.choice(string.punctuation) + t + y + u + i + random.choice(string.punctuation) + o + p + a + s + random.choice(string.punctuation) + d + f + g + h + random.choice(string.punctuation) + random.choice(string.punctuation)

  print('Your password is: ', password)

  saved = input('Would you like to get another password? (y/n)')

  if saved == "n":
    print("Have a nice day!")
    print('Logout at', datetime.datetime.now())
    time.sleep(1.5)
    break
