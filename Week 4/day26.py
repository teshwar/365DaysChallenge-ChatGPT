"""
    Day 26: Python Memory Management
        Explore Python memory management, including garbage collection and memory optimization techniques.
"""

import sys
import gc


class Person:
    def __init__(self, name):
        self.name = name

def memory_management_example():
    # Create instances with circular references
    person1 = Person("Alice")
    person2 = Person("Bob")

    person1.friend = person2
    person2.friend = person1

    # Print initial reference counts (subtracting 2 for actual references)
    print("Initial Reference Counts:")
    print("Person1:", sys.getrefcount(person1) - 2)
    print("Person2:", sys.getrefcount(person2) - 2)

    """
    Explanation:

    Initially, both person1 and person2 have a reference count of 1, which is the expected behavior when ignoring the temporary references added by sys.getrefcount.

    After breaking the circular reference and running garbage collection, the reference counts should ideally drop to 0, indicating that the objects are eligible for collection.

    However, due to internal references and the asynchronous nature of garbage collection, the counts may not always drop to 0 immediately.
    """
    # Remove references to break the circular reference
    del person1
    del person2

    # Run garbage collection
    gc.collect()

    # Print reference counts after garbage collection
    print("\nReference Counts After Garbage Collection:")
    # Note: The reference counts may not always decrease to 0 due to internal references
    print("Person1:", sys.getrefcount(person1) - 2 if 'person1' in locals() else "Object Collected")
    print("Person2:", sys.getrefcount(person2) - 2 if 'person2' in locals() else "Object Collected")

if __name__ == "__main__":
    memory_management_example()
