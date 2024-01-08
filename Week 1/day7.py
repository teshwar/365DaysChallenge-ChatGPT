"""
    Day 7: Regular Expressions
        Learn the basics of regular expressions.
        Use regular expressions for pattern matching in strings.
"""
#Checkout this Geeksforgeek to understand the special sequence
#https://www.geeksforgeeks.org/regular-expression-python-examples/
#Note r in the following example is for the raw strings

import re 

#Example 1 : Matching a specific pattern
pattern = r'\b\d{1}-\d{3}-\d{3}-\d{4}\b' #Matches a phone number
text = "Ben 's phone number is 1-234-567-8910"

match = re.search(pattern, text)

if match :
    print(f"Found number: {match.group()}")
else: 
    print("No number found")


#Example 2: Extracting information from a string
pattern = r'(\w+) (\w+)'
text = "Ben Ten"

match = re.match(pattern, text)
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    print(f"first name is {first_name}, last name is {last_name}")

else:
    print("Invalid name format")


#Example 3: Replacing matced patterns
pattern = r'\bben\b'
text = "My name is ben, ben is cool"

replaced_text = re.sub(pattern, 'Jeff',text)
print(f"original text: {text}")
print(f"modified text: {replaced_text}")