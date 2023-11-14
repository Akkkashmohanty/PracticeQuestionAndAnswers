# Write a Python program to pack consecutive duplicates of a given list elements into sublists.

def pack_consecutive_duplicates(input_list):
    if not input_list:
        return []
    
    result = []
    current_group = [input_list[0]]

    for item in input_list[1:]:
        if item == current_group[0]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]

    return result

# In this program, the pack_consecutive_duplicates function takes a list as input. 
# It iterates through the list, creating sublists (current_group) for consecutive duplicates. 
# When it encounters a different element, it appends the current group to the result and starts a new group. 
# The result is a list of sublists where consecutive duplicates are packed together.

# Sample list with consecutive duplicates
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# Call the function to pack consecutive duplicates into sublists.
packed_list = pack_consecutive_duplicates(original_list)

# Print the result
print("Original list:", original_list)
print("After packing consecutive duplicates into sublists:", packed_list)
