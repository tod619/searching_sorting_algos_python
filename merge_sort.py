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

def merge(left_half:list, right_half:list):
    if not left_half or not right_half:
        return left_half or right_half
    
    result = []

    i, j = 0, 0

    while True:

        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

        if i == len(left_half) or j == len(right_half):
            result.extend(left_half[i:] or right_half[j:])
            break

    return result

unsorted_list = [3, 1, 0, 9, 6, 11, 5]
print(unsorted_list)

sorted_list = merge_sort(unsorted_list)
print(sorted_list)
