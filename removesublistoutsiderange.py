# Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. 

def remove_sublists_outside_range(lst, min_range, max_range):
    filtered_list = [sublist for sublist in lst if all(min_range <= element <= max_range for element in sublist)]
    return filtered_list

# Original list of lists
original_list = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]

# Define the range
min_range = 10
max_range = 20

# Remove sublists containing elements outside the given range
filtered_list = remove_sublists_outside_range(original_list, min_range, max_range)

# Print the filtered list
print("Original list:")
for sublist in original_list:
    print(sublist)

print("After removing sublists from a given list of lists, which contains an element outside the given range:")
for sublist in filtered_list:
    print(sublist)
