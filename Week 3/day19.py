"""
    Day 19: Exception Handling in OOP
        Implement exception handling within classes.
        Discuss best practices for error handling in OOP.
        
"""

"""
In this example, we'll implement exception handling within classes and discuss best practices for error handling in OOP.

Best Practices:
1. Use specific exception classes.
2. Handle exceptions at an appropriate level.
3. Provide informative error messages.
4. Avoid using bare except clauses.
5. Use finally block cautiously.

"""

# Custom exception class for a specific scenario
class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative value not allowed: {value}")

class FirstValueStringError(Exception):
    def __init__(self, value):
        super().__init__(f"First value is a string: {value}")

# Example class with exception handling
class Calculator:
    def add(self, x, y):
        try:
            #Check if first value a string, and raise custom exception
            if type(x) is str:
                raise FirstValueStringError(x)
            
            # Check for negative values and raise custom exception
            if x < 0 or y < 0:
                raise NegativeValueError(x if x < 0 else y)    
            
            result = x + y
            return result
        except NegativeValueError as e:
            print(f"Error: {e}")
            return None
        
        except FirstValueStringError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

# Usage of the Calculator class
calculator = Calculator()

# Positive case
result1 = calculator.add(5, 3)
print(f"Result 1: {result1}")  # Output: Result 1: 8

# Case with negative value
result2 = calculator.add(-2, 4)
print(f"Result 2: {result2}")  # Output: Error: Negative value not allowed: -2, Result 2: None

# Case with unexpected error
result3 = calculator.add("abc", 3)
print(f"Result 3: {result3}")  # Output: Unexpected error: unsupported operand type(s) for +: 'str' and 'int', Result 3: None
