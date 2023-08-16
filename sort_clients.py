# Sort clients for an airline by miles traveled using merge sort algorithm
# A cleint is made of a tuple which contains (<Name>, <Age>, <Miles Travelled>)
# All the client tuples are stored in a list
# Sort the list so that the clients with the fewest miles appear first
# 16/08/2023

# Write your code below this line
def sort_airline_clients(lst):
    
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        middle_index = len(lst)//2

        # Calling the function recursively
        left = sort_airline_clients(lst[:middle_index])
        right = sort_airline_clients(lst[middle_index:])

        return merge(left, right)


def merge(left_half, right_half):

    if not left_half or not right_half:
        return left_half or right_half
    
    result = []
    i, j = 0, 0

    while True:

        # Compare the elements based on the
        # number of miles
        if left_half[i][2] < right_half[j][2]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

        if i == len(left_half) or j == len(right_half):
            result.extend(left_half[i:] or right_half[j:])
            break

    return result
     
clients = [("Nora", 35, 200000), ("Gino", 15, 500), ("Danny", 43, 152), ("William", 24, 1000), ("Sarah", 23, 4234), 
("Eric", 46, 2441)]

print(f"Unsorted List: {clients}")

sorted_by_miles = sort_airline_clients(clients)
print(f"Sorted List: {sorted_by_miles}")




        
        