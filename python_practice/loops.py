fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# print range values

for i in range(5):
    print(i)

# loops with in values

for i in range(1, 10, 2):
    print(i)


# break loop
while True:
    response = input("Type 'exit' to quit: ")
    if response == "exit":
        break

# nested loop

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
