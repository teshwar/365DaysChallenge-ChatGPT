"""
    Day 4: Exception Handling
        Use try-except blocks to handle errors.
        Create a program that handles both built-in and custom exceptions.
"""

try :
    y = input("Give y for y/x: ")
    x = input("Give x for y/x: ")
    ans = y/int(x)
except ZeroDivisionError:
    print("There was a zero divisor error, change value of x and try again")
except:
    print("There was some kind of error, please debug")
    raise TypeError("Maybe change the str to an int type")
else:
    print(f"The answer for y/x = {ans}")
finally:
    print("The try-except block has been executed")