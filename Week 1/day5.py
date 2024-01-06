"""
Day 5: String Manipulation
    Explore string methods for manipulation.
    Solve a problem that involves string operations.
"""

#Finding the length of a string
name = "Tomy"
length = len(name)

#Finding the first index of a string, returns -1 if not present
name = "Tommy"
index = name.find("m")
print(f"First m in Tommy is at index {index}")
index = name.find("x")
print(f"First x in Tommy is at index {index}")

#Finding the last index of a string, returns -1 if not present
name = "Tommy"
index = name.rfind("m")
print(f"Last m in Tommy is at index {index}")

#Capitalizing the string
name = "tomy"
print(f"Current string is {name}")
name = name.capitalize()
print(f"Current name after capilatizing function is {name}")


#make everyting in UPPER case
name = "tomy"
print(f"Current string is {name}")
name = name.upper()
print(f"Current name after upper function is {name}")

#make everyting in lower case
name = "TOMY"
print(f"Current string is {name}")
name = name.lower()
print(f"Current name after lower function is {name}")

#Check if a string is fully anumber
name = "tomy"
result = name.isdigit()
print(f"{name} is digit : {result}")

name = "123"
result = name.isdigit()
print(f"{name} is digit : {result}")

#Check if a string is fully alphabets
name = "tomy"
result = name.isalpha()
print(f"{name} is alpha : {result}")

name = "123"
result = name.isalpha()
print(f"{name} is alpha : {result}")

#Count the number of letter in a string
name = "tommy"
result = name.count("m")
print(f"{name} count for 'm' : {result}")

name = "ya ya ya"
result = name.count(" ")
print(f"{name} count for ' ' : {result}")

#replace a character by another one
name = "Tommy"
result = name.replace("m", "b")
print(f"before : {name} and after m->b : {result}")

name = "ya ya ya"
result = name.replace(" ", "")
print(f"before : {name} and after ' '->'' : {result}")

#for more string manipulation
print("For more function, do print(help(str))")