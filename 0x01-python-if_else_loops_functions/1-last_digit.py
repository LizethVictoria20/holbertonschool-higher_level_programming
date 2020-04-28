#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = "Last digit of "
less = " and is less than 6 and not 0"
if number < 0:
    lastNum = number % -10

if number >= 0:
    lastNum = number % 10

if lastNum > 5:
    print("{}{} is {} and is greater than 5".format(last, number, lastNum))
elif lastNum == 0:
    print("{}{} is {} and is 0".format(last, number, lastNum))
else:
    print("{}{} is {}{}".format(last, number, lastNum, less))
