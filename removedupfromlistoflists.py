# Write a Python program to remove duplicates from a list of lists.     

def remove_duplicates_from_list_of_lists(input_list):
    seen = set()
    result = []
    
    for sublist in input_list:
        # Convert the sublist to a tuple to make it hashable
        sublist_tuple = tuple(sublist)
        
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            result.append(list(sublist_tuple))
    
    return result

# In this program, the remove_duplicates_from_list_of_lists function removes duplicates from the list of lists by converting each sublist into a tuple, 
# (which is hashable) and keeping track of the unique tuples using a set (seen). 
# If a tuple is not in the set, it means it's not a duplicate, and it's added to the result list. 
# The result is a list of lists with duplicates removed.

# Sample list of lists
original_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Call the function to remove duplicates
new_list = remove_duplicates_from_list_of_lists(original_list)

# Print the result
print("Original List:", original_list)
print("New List:", new_list)
