# This Program will produce 2 random numbers and then
# prompts the user to guess the sum of the numbers.
# It will read user inputs continuously until the user guess 
# the right sum.

import random

a = random.randint(1, 21)
b = random.randint(1, 21)

sum = int(input("What is %d + %d? "%(a,b)))

while sum != a + b:
    print("Oh! it was incorrect.")
    sum = int(input("try again:"))

print("Congratulations! you guessed the correct number")
