"""
    Day 22: Decorators (Advanced)
        Explore more advanced decorator concepts, such as decorators with arguments and class decorators.
"""
# Decorator with Arguments
def repeat(times):
    """
    Decorator with arguments that repeats the decorated function a specified number of times.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    """
    A function decorated with `repeat` to repeat the greeting three times.
    """
    print(f"Hello, {name}!")

# Class Decorator
class Logger:
    """
    Class decorator that logs information about function calls.
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Function {self.func.__name__} completed")
        return result

@Logger
def add(x, y):
    """
    A function decorated with `Logger` to log information about its calls.
    """
    return x + y

# Example Usage
if __name__ == "__main__":
    # Using the repeat decorator
    greet("Alice")

    # Using the class decorator
    result = add(3, 5)
    print(f"Result of addition: {result}")
