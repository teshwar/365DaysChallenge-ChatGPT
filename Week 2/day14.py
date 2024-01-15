"""
    Day 14: Advanced List Manipulation
        Use advanced list manipulation techniques (slicing, zip, enumerate).
        Solve a problem that involves nested lists.
"""

def advanced_list_manipulation():

    #Example 1: Slicing
    pi_list = [3,1,4,1,5,9,2,6,5,3]

    #Select elements from index 2 to 7 (exclusive)
    sliced_list = pi_list[2:7]
    print("Example 1: Slicing")
    print(f"Original List: {pi_list}")
    print(f"Sliced List: {sliced_list} \n")

    #-----------------------------------------------

    #Example 2: Zip
    names = ["Spongebob", "Carlo", "Patrick"]
    ages = [42,69,21]
 
    #Combined two lists using zip
    combined_data = list(zip(names,ages))

    print("Example 2: Zip")
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Combined Data: {combined_data}\n")

    #-------------------------------------------------

    #Example 3: Enumerate
    courses = ["Physics", "Mathematics", "Chemistry"]
    
    #Enumerate the list with indeices
    enumerated_courses = list(enumerate(courses, start = 1))

    print("Example 3: Enumerate")
    print(f"Courses: {courses}")
    print(f"Enumerated Fruits: {enumerated_courses}\n")

    #--------------------------------------------------

    #Example 4: Nested List
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    #Flatten the metrix using list comprehension
    flattend_matrix = [element for row in matrix for element in row]

    print("Example 4: Nested Lists")
    print(f"Original Matrix: ")
    for row in matrix:
        print(row)
    
    print(f"Flattened Matrix: {flattend_matrix}")


if __name__ == "__main__":
    advanced_list_manipulation()