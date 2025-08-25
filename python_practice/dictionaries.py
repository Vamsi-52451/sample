person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("Original Dictionary:", person)

# 1. get() – Safely access a key
print("\n1. get():")
print(person.get("name"))        
print(person.get("email", "N/A"))

# 2. keys() – Get all keys
print("\n2. keys():")
print(person.keys())             

# 3. values() – Get all values
print("\n3. values():")
print(person.values())          

# 4. items() – Get all key-value pairs
print("\n4. items():")
for key, value in person.items():
    print(f"{key} = {value}")

# 5. update() – Update or add new key-value pairs
print("\n5. update():")
person.update({"age": 31, "email": "alice@example.com"})
print(person)

# 6. pop() – Remove a key and return its value
print("\n6. pop():")
age = person.pop("age")
print("Removed age:", age)
print(person)

# 7. popitem() – Remove the last inserted key-value pair
print("\n7. popitem():")
last_item = person.popitem()
print("Removed:", last_item)
print(person)

# 8. clear() – Remove all items
print("\n8. clear():")
person.clear()
print("After clear:", person)
