#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
a = int(str(number)[-1])
if a > 5:
    print("Last digit of " + number + " is " + a + " and is greater than 5")
elif a = 0:
    print("Last digit of " + number + " is " + a + " and is 0")
else:
    print("Last digit of " + number + " is " + a + " and is less than 6 and not 0)
