# Insertion Sort Implementation
# 14/08/2023

def insertion_sort(lst: list):
    """ An Implementation of the insertion sort algorithm """
    for i in range(1, len(lst)):
        elem_selected = lst[i]

        while i > 0 and elem_selected < lst[i - 1]:
            lst[i] = lst[i - 1]
            i -= 1

        lst[i] = elem_selected

    return lst


my_list = [1, 8, 2, 6]
print(my_list)
sorted_list = insertion_sort(my_list)
print(sorted_list)