"""
    Day 2: Control Flow
        Implement a simple program using if-else statements.
        Use loops (while or for) for repetitive tasks.
"""

i = 0
while(i<5):
    if (i == 0):
        print(f"i value is currently 0") 
    elif(i==1):
        print("i vaule is currently 1")
    elif(i==2):
        print("i vaule is currently 2")
    else:
        print("i greater than 2")
    
    i += 1

for y in range(0,5) :
    if (y == 0):
        print("y is currently 0")
    elif(y == 1):
        print("y is currently is 1")
    elif(y== 2):
        print("y is currently is 2")
    else:
        print("y is greater 2")