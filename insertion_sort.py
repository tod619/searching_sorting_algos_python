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

# Interview Question
# Return the name of the client with the larger bank balance, return the number of swaps
# & return the number of iterations in the inner while loop
# the function should return a tuple with the required info

def sort_clients(lst:list) -> tuple:
    
    num_swaps = 0
    num_iterations = 0
    
    for i in range(1, len(lst)):
        elem_selected = lst[i]
        
        while i > 0 and elem_selected[1] < lst[i - 1][1]:
            num_iterations += 1 
            lst[i] = lst[i - 1]
            i -= 1 
            
        lst[i] = elem_selected
        num_swaps += 1 
        
    return(num_swaps, num_iterations, lst[-1][0])
    
    
a = [("Nora", 20000), ("Gino", 500), ("Danny", 152), ("William", 1000)]

print(sort_clients(a))