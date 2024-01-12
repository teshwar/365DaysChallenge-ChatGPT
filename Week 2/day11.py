"""
   Day 11: Searching Algorithms
        Implement linear and binary search algorithms.
        Analyze their time complexity
"""

import time

#Using sorting algorithms as example
def selection_sort(arr):
    selection_list = arr.copy()
    n = len(selection_list)

    for i in range(n):

        #Find min element in unsorted array
        min_index = i
        for j in range(i + 1, n):
            if selection_list[j] < selection_list[min_index]:
                min_index = j
        
        #Swap min_element with current element
        selection_list[i], selection_list[min_index] = selection_list[min_index], selection_list[i]
    
    return selection_list

#Look through each element in a list one by one until it finds the target
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#Sort the list first, then divde search space in half
def binary_search(arr,target):
    low, high = 0, len(arr)-1
    
    arr = selection_sort(arr.copy())
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        #narrow search to right path
        elif mid_value < target:
            low = mid + 1
        #narrow search to left path
        else: 
            high = mid - 1
    return 1




def analyze_search_algorithms():
    pi_list = [3,1,4,1,5,9,2,6]

    #Measure the time of linear search
    # +ve: does not need to be sorted
    linear_start_time = time.time()
    linear_search_index = linear_search(pi_list.copy(), 5)
    linear_stop_time = time.time()
    linear_time = linear_stop_time - linear_start_time

    #Measure time for binary search
    binary_start_time = time.time()
    binary_search_index = binary_search(pi_list.copy(),5)
    binary_end_time = time.time()
    binary_time = binary_end_time - binary_start_time

    print(f"Linear Search Index: {linear_search_index}")
    print(f"Linear Search Time: {linear_time} seconds")
    
    print(f"For sorted list in binary search: {selection_sort(pi_list.copy())}")
    print(f"Binary Search Index: {binary_search_index}")
    print(f"Binary Search Time: {binary_time} seconds")


if __name__ == "__main__":
    analyze_search_algorithms()