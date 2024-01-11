"""
    Day 10: Sorting Algorithms
        Implement basic sorting algorithms (e.g., bubble sort).
        Compare their time complexity.
"""
import time

def bubble_sort(arr):
    bubble_list = arr.copy()
    n = len(bubble_list)

    #Last i element will be already sorted
    for i in range(n):
        for j in range(0, n - i - 1):
            if bubble_list[j] > bubble_list[j+1]:
                bubble_list[j],bubble_list[j+1] = bubble_list[j+1], bubble_list[j]
    
    return bubble_list

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


def compare_sorting_algorithms():
    pi_list = [3,1,4,1,5,9,2,6]

    #Measure time taken for bubble sort
    bubble_start_time = time.time()
    bubble_plist = bubble_sort(pi_list.copy())
    bubble_stop_time = time.time()
    bubble_time = bubble_stop_time - bubble_start_time

    #Meausre time taken for selection sort
    selection_start_time = time.time()
    selection_list = selection_sort(pi_list.copy())
    selection_stop_time = time.time()
    selection_time = selection_stop_time - selection_start_time

    print(f"Original pi list: {pi_list}")
    print(f"After Bubble Sort: {bubble_plist}")
    print(f"Bubble Sort Time: {bubble_time} seconds")

    print(f"Original pi list: {pi_list}")
    print(f"After Bubble Sort: {selection_list}")
    print(f"Bubble Sort Time: {bubble_time} seconds")


if __name__ == "__main__":
    compare_sorting_algorithms()