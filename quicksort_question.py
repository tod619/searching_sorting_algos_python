# A school wants to reward its high performing instructors
# It has asked its students to rate each instructor between 0 - 5
# Any instructor that scores a 4.5 or higher the school wants to reward
# the school would like to know how many instructors acheive the higher scores

# Write your code below this line
def sort_instructors(lst, low, high):
    
    counter = 0
    
    # Sort the list
    quicksort(lst, low, high)
    
    for elm in lst:
        if elm[1] >= "4.5":
            counter += 1 
            
    return counter
    
def quicksort(lst, low, high):
    if low < high:
        
        pivot_index = partition(lst, low, high)
        
        quicksort(lst, low, pivot_index -1)
        quicksort(lst, pivot_index + 1, high )
        
def partition(lst, low, high):
    
    pivot = lst[high]
    
    i = low-1
    
    for j in range(low, high):
        if lst[j] >= pivot:
            i+=1 
            lst[i], lst[j] = lst[j], lst[i]
            
    lst[i+1], lst[high] = lst[high], lst[i+1]
    
    return i+1 


a = [("Nora", "4.5"), ("Gino", "3.2"), ("Danny", "5.0"), ("William", "2.3"), ("Sarah", "4.6"), ("Eric", "4.1")]

print(sort_instructors(a, 0, len(a)-1))