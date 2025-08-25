# Import the entire math module
import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# Import only specific functions
from random import randint, choice

print("Random number between 1 and 100:", randint(1, 100))

colors = ['red', 'green', 'blue']
print("Randomly chosen color:", choice(colors))

# Import a module with an alias
import datetime as dt

now = dt.datetime.now()
print("Current date and time:", now)
