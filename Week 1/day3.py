"""
Day 3: Functions and Modularity
        Define a function and call it with various arguments.
        Explore different ways to pass arguments (positional, keyword).
        Create a simple module and import it into another script.
"""

def greeting_function(name: str = 'Bob', greeting : str = 'Hello'):
    print(f"{greeting} {name}")

greeting_function()
greeting_function("Tom","Waaa")