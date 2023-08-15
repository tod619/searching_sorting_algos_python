# Implementation of the merge sort algorithm
# 15/08/2023

def merge_sort(lst:list):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        middle_index = len(lst) // 2

        left = merge_sort(lst[:middle_index])
        right = merge_sort(lst[middle_index:])

        return merge(left, right)

def merge():
    pass