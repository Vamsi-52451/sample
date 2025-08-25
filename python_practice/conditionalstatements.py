age = 20

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")

# Multiple conditions with logical operators
temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("It's warm and dry outside.")
elif temperature > 20 and is_raining:
    print("It's warm but raining.")
else:
    print("It's cold outside.")

# Using ternary operator (inline if-else)
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
   
