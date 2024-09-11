class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}"
    
    # This is the object, an instance of a class
my_dog = Dog("Buddy", "Chihuahua")

print(my_dog.describe())

# Notes
# - The `__init__` method is a special method in Python classes. it is the constructor of the class. It is called when a new object is created
# The self parameter refers to the object being created (in this case, my_dog)