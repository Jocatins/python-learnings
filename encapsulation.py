# Encapsulation is a concept of wrapping data and methods into a single unit class
# A variable can be made private in Python by prefixing it with two underscores

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.__brand} {self.model}'s engine is starting"
    
my_car = Car("Benz", "Audi")

print(my_car.start_engine())

# the __brand attribute is private and cannot be accessed directly from outside the class, 
# ensuring that it can only be changed through class methods