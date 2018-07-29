#!/bin/python3

import time

def wage_calculator(wage_rate, hours, weeks, days):
  weekly_wage = wage_rate * hours * days
  total_wage = weeks * weekly_wage
  return total_wage

while True:
  wagerate = float(input('How much do you make an hour?'))
  hour = float(input('How many hours do you work a day?'))
  day = float(input('How many days do you work a week?'))
  week = float(input('How many weeks of pay would you like to calculate?'))

  total_wage = wage_calculator(wagerate, hour, week, day)

  print('Your total wage is', str(total_wage))
  
  answer = input('Would you like to calculate another job? (y/n)')
  
  if answer == 'n':
    print("Have a nice day!")
    time.sleep()
    break