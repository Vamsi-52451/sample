
# OBJECTS (CLASSES)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

p1 = Person("Alice", 30)
print(f"Name: {p1.name}, Age: {p1.age}")
p1.greet()

print()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 10)
print(f"Rectangle width: {r.width}, height: {r.height}")
print("Area:", r.area())
