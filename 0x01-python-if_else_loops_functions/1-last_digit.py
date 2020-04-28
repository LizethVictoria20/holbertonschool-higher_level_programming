#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = "Last digit of "

if number < 0:
    last_numer = number % -10

if number >= 0:
    last_numer = number % 10

if last_numer > 5:
    print("{}{} is {} and is greater than 5".format(last_digit, number, last_numer))

elif last_numer == 0:
    print("{}{} is {} and is 0".format(last_digit, number, last_numer))
else:
    print("{}{} is {} and is less than 6 and not 0".format(last_digit, number, last_numer))
