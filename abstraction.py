#  Abstraction is hiding the complex implementation details and showing only essential features

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"
    
class Cat(Animal):
    def sound(self):
        return "meow!"
    
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())

# The Animal class is abstract because it contains an absract method sound(). 
#  The Subclasses Dog and Cats are required to implement the sound method