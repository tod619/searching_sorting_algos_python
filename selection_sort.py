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

# Create an algoritm that compares the rankings of participants
# The function will return the number of swaps + the first and last place participants
def sort_participants(list):
    num_swaps = 0
    for i in range(len(list)):
        min_index = i
        
        for curr_index in range(i+1, len(list)):
            if list[min_index][1] > list[curr_index][1]:
                min_index = curr_index
                
        list[i], list[min_index] = list[min_index], list[i]
        
        num_swaps += 1
        
    return(num_swaps, list[0][0], list[-1][0])
            


a = [("Anna", 4), ("Federico", 1), ("Mandy", 3), ("Igor", 2)]

b = sort_participants(a)

print(b)
