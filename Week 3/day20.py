"""
    Day 20: Decorators and Generators
        Implement decorators to modify class behavior.
        Create and use generators.
"""

"""
In this example, we'll implement decorators to modify class behavior and create and use generators.

1. Decorators:
   - A decorator is a function that takes another function as an argument and extends the behavior of the latter function.
   - Class decorators can modify the behavior of methods in a class.

   - Use a wrapper function which is called decorator tag is used
    Wrapper functions follows the following:
        Do something before calling the function
        Original function
        Do something after calling the function

        def my_decorator(func):
            def wrapper(*args, **kwargs):
            # Code to be executed before the original function
            print("Do something before calling the function")

            # Call the original function
            result = func(*args, **kwargs)

            # Code to be executed after the original function
            print("Do something after calling the function")

            return result

         # Return the wrapper function
        return wrapper




2. Generators:
   - A generator is a special type of iterator that allows lazy evaluation of values.
   - Generators use the `yield` keyword to produce a sequence of values.

"""

# Decorator to log method calls
def log_method_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Method {func.__name__} completed")
        return result
    return wrapper

# Decorator to ensure positive result
def ensure_positive_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Result must be positive")
        return result
    return wrapper

# Ensure the first argument is positive
def ensure_positive_first_arg(func):
    def wrapper(*args, **kwargs):

        #Check if the first argument is positive
        if args and args[1] < 0:
            raise ValueError("First argument must be positive")
        
        #Call original function
        result = func(*args, **kwargs)

        #Return the result
        return result
    
    return wrapper

# Example class with decorated methods
class Calculator:

    @log_method_calls
    @ensure_positive_first_arg
    @ensure_positive_result
    def add(self, x, y):
        return x + y

    @log_method_calls
    @ensure_positive_result
    def subtract(self, x, y):
        return x - y

# Usage of the Calculator class with decorated methods
calculator = Calculator()

result_add = calculator.add(5, 3)
print(f"Result of addition: {result_add}")

result_subtract = calculator.subtract(8, 2)
print(f"Result of subtraction: {result_subtract}")

# Generator function to generate Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage of the Fibonacci generator
fibonacci_sequence = fibonacci_generator(5)
print("Fibonacci Sequence:", list(fibonacci_sequence))
