# Bubble Sort implementation
# 01/08/2023

# Basic bubble sort implementation
def basic_bubble_sort(lst:list):
    """ Basic Bubble Sort Implementation"""
    n = len(lst)
    for i in range(n):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# my_list = [12, 9, 17, 4, 1, 2, 8]
# print(f"My List Before Sorting: {my_list}")
# basic_bubble_sort(my_list)
# print(f"MY List After Sorting: {my_list}")

# Optimized Bubble Sort Using swapped flag
def optimized_bubble_sort(lst:list):
    n = len(lst)

    for i in range(n):
        # Set swapped Flag to false
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j + 1]:
                lst[j],lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

my_list = [12, 9, 17, 4, 1, 2, 8]
print(f"My List Before Sorting: {my_list}")
optimized_bubble_sort(my_list)
print(f"MY List After Sorting: {my_list}")
