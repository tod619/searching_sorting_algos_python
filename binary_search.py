# Binary search algorithm implementation
# 31/07/2023

# Problem Description
# Binary search is very efficant but the list or tuple has to be sorted
# Eliminates half the input operations per loop iteration

def binary_search_iterative(list_to_search: list, item_to_find: int) -> int:
    """
        Search through a sorted list of numbers
        return the index of the item to find if it is in the sorted list
        return -1 if the item is not in the list
    """
    low = 0
    high = len(list_to_search) - 1

    while low <= high:
        middle = (low + high) // 2

        if list_to_search[middle]  == item_to_find:
            return middle
        elif list_to_search[middle] > item_to_find:
            high = middle - 1
        else:
            low = middle + 1
        
    return -1


list_1 = [1, 5, 7, 8, 10, 11, 12, 14, 22, 27]
print(binary_search_iterative(list_1, 11))

list_2 = [3, 5, 7, 8, 15, 55, 71, 80, 87, 90, 97]
print(binary_search_iterative(list_2, 80))
print(binary_search_iterative(list_2, 2))