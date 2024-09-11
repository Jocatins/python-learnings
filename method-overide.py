#  This is a situation whereby a child class modifies the behaiviour of methods inherited from the parent class

class Animal:
    def  make_sound(self):
        return "Some Generic sound"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
# create instances of the classes
animal = Animal()
cat = Cat()

print(animal.make_sound())
print(cat.make_sound())  # This will print "Meow" instead of "Some Generic sound    