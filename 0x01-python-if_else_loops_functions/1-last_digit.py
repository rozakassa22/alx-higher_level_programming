#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number

if n < 0:
    n *= -1
    ld = n % 10
    ld *= -1
else:
    ld = n % 10

if ld > 5:
    print(f'Last digit of {number} is {ld} and is greater than 5')
elif ld == 0:
    print(f'Last digit of {number} is {ld} and is 0')
else:
    print(f'Last digit of {number} is {ld} and is less than 6 and not 0')
