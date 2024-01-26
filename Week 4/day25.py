"""
    Day 25: Metaclasses
        Understand metaclasses and create a simple metaclass to customize class creation.
"""

#Example 1 Override the current attribute
# Define a custom metaclass
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Modify class attributes before creation
        for key, value in attrs.items():
            if isinstance(value, str):
                attrs[key] = value.upper()

        # Create the class object
        return super().__new__(cls, name, bases, attrs)

# Use the custom metaclass in a class definition
class MyCustomClass(metaclass=MyMeta):
    message = "Hello, metaclasses!"

#----------------------------------------

#Example 2 Add a new attribute
class MyMeta1(type):
    def __new__(cls, name, bases, attrs):
        # Add a a new attribute attributes before class creation
        attrs['modified_attribute'] = 'This attribute is modified'
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta1):
    original_attribute = 'This is an original attribute'


# Run the examples
if __name__ == "__main__":

    # Instantiate the class
    my_instance = MyCustomClass()
    # Access the modified attribute
    print(my_instance.message)  # Output: HELLO, METACLASSES!
    
    # Testing the created class
    my_instance = MyClass()
    print(my_instance.original_attribute)   # Output: This is an original attribute
    print(my_instance.modified_attribute)   # Output: This attribute is modified
