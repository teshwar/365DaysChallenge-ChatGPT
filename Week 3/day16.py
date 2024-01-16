"""
    Day 16: Inheritance and Polymorphism
        Implement inheritance between classes.
        Demonstrate polymorphic behavior.

"""

#Definition of Inheritance:
#Inheritance is  a mechanism where a class (subclass) inherits properpties and behaviors
#from another class (superclass)
#It allows for code reuse and the creation of a heirarchical structure.
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def make_sound(self):
        return "Animal makes a generic sound"

#Dog is a subclass (dereived class) inheriting from Animal (superclass)
#Dog inherits the make_sound method from Animal and can provide its own implementation
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} is a {self.type} and  woofs."

#Cat is another subclass inehriting from Animal
#Cat also inherits the make_sound method from ANimal but provides its own impementation
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} is a {self.type} and  meows."
    
#Definition of polymorphism:
#Polymorphism allows objects of differnet class to be trated as objects of a common superclass.
#It provdes a common internface (method name) for interacting with objects of different types
    
def animal_sounds(animals):
    #The animal_sound function demonstrates polymorphism.
    #It takes a list of animals (objects of different types) and call their make_sound method

    for animal in animals:
        print(animal.make_sound())

# Creating instances of different animals
dog = Dog(name="Rocky", type = "Dog")
cat = Cat(name="Garfield",type = "Cat")

#Demonstrate polymorphic behavior by passing objects of different types to animal_sounds function
animal_sounds([dog, cat])