#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -(digit)
pit = "Last digit of {} is {}".format(number, digit)
if digit > 5:
    print(f"{pit} and is greater than 5")
elif digit == 0:
    print(f"{pit} and is 0")
else:
    print(f"{pit} and is less than 6 and not 0")
