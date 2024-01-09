"""
    Day 8: Lists and List Comprehensions
        Perform various operations on lists.
        Use list comprehensions to generate new lists.
"""

def minus_one_func(x: int):
    return x - 1

#Example 1: Creating a list and accessting elements
numbers = [3,1,4,1]
print(f"Original List: {numbers}")
print(f"First Element: {numbers[0]}")
print(f"Last Element: {numbers[-1]}")

#Example 2: Modifying to the list
numbers.insert(1,2)
print(f"Modify the list, new list = {numbers}")

numbers[1] = 1
print(f"Modifying list again, new list = {numbers}")


#Example 3: Appending and extending list
numbers.append(5)
print(f"After appending: {numbers}")

more_numbers= [9,2,6]
numbers.extend(more_numbers)
print(f"After extending list, new list: {numbers}")


#Example 4: List Slicing
subset = numbers[0:3]
print(f"Subset of list from index = 0 to 3, Subset = {subset}")

#Example 5: List comprehension to generate new list
squares = [x**2 for x in numbers]
print(f"Squares list = {squares}")

#Example 6: Filtering elements using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers list= {even_numbers} ")

#Example 7: Applying a function to each element using list comprehension
minus_one = [minus_one_func(x) for x in numbers]
print(f"Minus One: {minus_one}")

