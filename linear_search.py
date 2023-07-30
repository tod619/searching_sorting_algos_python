# Linear search algorithm example
# 30/07/2023

# Problem:
# Find if an item is in a list or a tuple
# If the item is found return the index
# If it is not found return -1

def linear_search(main_list: list, search_item: int ) -> int:

    for item in main_list:
        if item == search_item:
            return main_list.index(item)
        
    return -1


nums = [1, 3, 6, 9, 10]

print(linear_search(nums, 9))
print(linear_search(nums, 11))
