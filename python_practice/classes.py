# Define a class
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says Woof!")
    
    # Method to display dog's info
    def info(self):
        print(f"{self.name} is {self.age} years old.")

# Create objects (instances) of the class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Use the methods
dog1.bark()   
dog2.info()   
