"""
    Day 9: Tuples and Sets
        Explore tuple operations and immutability.
        Perform set operations and eliminate duplicates from a list using sets.
"""

#Example 1, tuple and their immutation
numbers = [3,1,4,1,5,9,2,6]
pi_tuple = tuple(numbers)
print(f"My Tuple: {pi_tuple}")
print(f"First Element of pi_tupole: {pi_tuple[0]}")
#Uncommenting the follwing result in error(as tuple non-mutables)
#pi_tuple[0] =  4

#Example 2: Set Operations
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

#Union of sets
union_set = set_a.union(set_b)
print(f"Union of sets: {union_set}")

#Intersection of sets
intersection_set = set_a.intersection(set_b)
print(f"Intersection of Sets: {intersection_set}")

# Difference of sets
difference_set = set_a.difference(set_b)
print(f"Difference of Sets A - B: {difference_set}")

# Eliminate duplicates from a list using sets
my_list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5]
unique_set = set(my_list_with_duplicates)
list_without_duplicates = list(unique_set)
print(f"List with Duplicates: {my_list_with_duplicates}")
print(f"List without Duplicates: {list_without_duplicates}")
