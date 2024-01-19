"""
    Day 18: Design Patterns (Singleton, Factory)
        Implement Singleton and Factory design patterns.
        Discuss their use cases.
"""

"""
1. Singleton Pattern:
   - Ensures that a class has only one instance and provides a global point to this instance.
   - Common use cases: managing resources, configuration settings, logging, etc.

2. Factory Pattern:
   - Provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.
   - Common use cases: creating objects without specifying the exact class, managing object creation logic.
"""

# Singleton Pattern Implementation:

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Additional setup logic can go here
        return cls._instance

# Usage of Singleton:
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(f"Are both instances the same? {singleton_instance1 is singleton_instance2}")
# Output: Are both instances the same? True


# Factory Pattern Implementation:

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Usage of Factory:
animal_factory = AnimalFactory()
dog = animal_factory.create_animal("Dog")
cat = animal_factory.create_animal("Cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
