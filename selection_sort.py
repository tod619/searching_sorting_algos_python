# Selection Sort Algorithm
# 02/08/2023

def selection_sort(lst:list):
    """A Selection Sort Implementation"""
    for i in range(len(lst)):
        min_index = i

        for curr_index in  range(i+1, len(lst)):
            if lst[min_index] > lst[curr_index]:
                min_index = curr_index

        lst[i], lst[min_index] = lst[min_index], lst[i]

my_list = [5, 9, 2, 7, 21, 10, 3, 11, 8, 1, 17, 16]

print(f"The unsorted list: {my_list}")

selection_sort(my_list)

print(f"The Sorted List: {my_list}")
