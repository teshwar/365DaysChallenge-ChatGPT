"""
Day 27: Design Patterns (Part 1)
    Introduce design patterns such as Singleton, Factory, and Observer. Implement them in Python.

--------------------------------------------------------------------------------------------------------------------
    
    Singleton Design Pattern:
        The Singleton class ensures that there is only one instance of the class. Subsequent calls to the constructor return the same instance.

    Factory Design Pattern:
        The ShapeFactory class acts as a factory that creates different shapes based on the provided shape type. In this example, it creates Circle and Square objects.

    Observer Design Pattern:
        The Subject class maintains a list of observers and notifies them of any changes. The Observer class registers with the subject and receives updates when the subject's state changes.
"""

# Singleton Design Pattern
class Singleton:
    _instance = None

    def __new__(cls):
        # Check if instance is not created, create one and return
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Factory Design Pattern
class ShapeFactory:
    def create_shape(self, shape_type):
        # Factory method to create different shapes based on shape type
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")

class Circle:
    def draw(self):
        return "Drawing Circle"

class Square:
    def draw(self):
        return "Drawing Square"

# Observer Design Pattern
class Subject:
    _observers = []

    def add_observer(self, observer):
        # Add observer to the list
        self._observers.append(observer)

    def remove_observer(self, observer):
        # Remove observer from the list
        self._observers.remove(observer)

    def notify_observers(self, message):
        # Notify all observers with the given message
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        # Update method to be called when notified
        print(f"Observer with: {id(self)} received message: {message}")

if __name__ == "__main__":
    # Singleton
    singleton_instance1 = Singleton()
    singleton_instance2 = Singleton()
    print(f"Are Singleton instances the same? {singleton_instance1 is singleton_instance2}")

    # Factory
    shape_factory = ShapeFactory()
    circle = shape_factory.create_shape("circle")
    square = shape_factory.create_shape("square")
    print(circle.draw())
    print(square.draw())

    # Observer
    subject = Subject()
    observer1 = Observer()
    print(f"Created observer 1 with {id(observer1)}")
    observer2 = Observer()
    print(f"Created observer 2 with {id(observer2)}")

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.notify_observers("Hello, Observers!")
