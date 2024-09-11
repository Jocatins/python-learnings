# Polymorphism allows you to use a unified interface to interact with different types of objects, 
# enabling methods to behave differently based on object

class Bird:
    def sound(self):
        return "Chirp"
    
class Dog:
    def sound(self):
        return "Woof"
    
def make_sound(animal):
    print(animal.sound())

bird = Bird()
dog = Dog()

make_sound(bird)  
make_sound(dog)