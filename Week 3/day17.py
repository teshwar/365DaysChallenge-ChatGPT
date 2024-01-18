"""
SOLID Principles Example:

SOLID is an acronym representing a set of design principles that aim to make software more maintanble, scalable, and flexbile. 

1. Single Responsilibility Principle (SRP) :
 -A class should have only one reason to change.
 -Each class should have a single responsibility.

2. Open/Closed Principle (OCP) :
 - Software Entities (Classes, modules, function, etc.) should be open for extension but closed for modification.

"""

# import the Abstrac Base Classes module, use to define common interface for group of related classes.
from abc import ABC, abstractmethod

#Apply SOLID principles:

#Single Responsibility Principle (SRP) :
#Seperate the responsibilities of managing shapes and calculating their area into different classes

#Introduce a common interface (abstract class) for different shapes, making the system open for extension
#Cannot be initiated on its own
class Shape(ABC): #ABC: Abstract Base class
    @abstractmethod
    def calculate_area(self):
        pass

#Implement Shape interface in Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    
#Implement Shape interface in Circle class
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

if __name__ == "__main__":
    shapes = [Rectangle(5,10), Circle(7)]

    total_area = 0

    for shape in shapes:
        total_area += shape.calculate_area()
    
    print(f"Total area of Rectangle(5,10) and Circle(7) is {total_area}")