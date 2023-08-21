# An implementation fo the quick sort algorithm
# 17/08/2023

def quicksort(lst, low, high):
    if low < high:
        pivot_index = partition(lst, low, high)

        quicksort(lst, low, pivot_index - 1)
        quicksort(lst, pivot_index + 1, high)

def partition():
    pass