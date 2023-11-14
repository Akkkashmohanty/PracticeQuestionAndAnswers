# Write a Python program to sort a given list of lists by length and value. 

def sort_by_length_and_value(lst):
    lst.sort(key=lambda x: (len(x), x))
    return lst

# Original list of lists
original_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

# Sort the list of lists by length and value
sorted_list = sort_by_length_and_value(original_list)

# Print the sorted list
print("Original list:")
for sublist in original_list:
    print(sublist)

print("Sort the list of lists by length and value:")
for sublist in sorted_list:
    print(sublist)
