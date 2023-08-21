# An implementation fo the quick sort algorithm
# 17/08/2023

def quicksort(lst, low, high):
    if low < high:
        pivot_index = partition(lst, low, high)

        quicksort(lst, low, pivot_index - 1)
        quicksort(lst, pivot_index + 1, high)

def partition(lst, low, high):
    pivot = lst[high]

    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]

    return i + 1


a = [4, 9, 5, 3, 1, 2]
print(f"Unsorted List: {a}")
quicksort(a, 0, len(a) - 1)
print(f"Sorted List: {a}")