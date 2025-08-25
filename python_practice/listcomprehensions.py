# Create a list of squares from 0 to 9 using list comprehension
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# List comprehension with a condition: even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# Using list comprehension to convert strings to uppercase
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)
