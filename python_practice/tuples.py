# Creating tuples
fruits = ("apple", "banana", "cherry")
one_item = ("apple",)           
numbers = 1, 2, 3              

print("Fruits tuple:", fruits)
print("One item tuple:", one_item)
print("Numbers tuple:", numbers)

# Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice fruits[1:]:", fruits[1:])

# Loop through tuple
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# Tuple immutability demo
print("\nAttempting to change tuple item (will cause error if uncommented):")
# fruits[0] = "orange"  

# Workaround: convert to list, modify, convert back
temp_list = list(fruits)
temp_list[0] = "orange"
fruits = tuple(temp_list)
print("Modified tuple after converting to list:", fruits)

# Tuple unpacking
print("\nTuple unpacking:")
person = ("Alice", 30, "New York")
name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)

# Tuple methods
print("\nTuple methods:")

t = (5, 10, 15, 10, 20, 10)
print("Tuple:", t)

# count()
print("Count of 10:", t.count(10))

# index()
print("Index of 15:", t.index(15))
