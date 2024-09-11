#  The is a mechanism where classes inherit properties and methods from another class, making the code reusable

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting!"
    
# Child class
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def describe(self):
        return f"{self.brand} {self.model} runs on {self.fuel_type}"
    
my_car = Car("Honda", "civic", "big-engine")

print(my_car.start()) 
print(my_car.describe())