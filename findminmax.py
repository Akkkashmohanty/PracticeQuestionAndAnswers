# Write a Python program to find the maximum and minimum values in a given heterogeneous list. 

def find_max_min(lst):
    # Filter the numeric values from the list
    numeric_values = [x for x in lst if isinstance(x, (int, float))]
    
    # Check if there are numeric values in the list
    if numeric_values:
        maximum = max(numeric_values)
        minimum = min(numeric_values)
        return maximum, minimum
    else:
        return None, None

# Original list
original_list = ['Python', 3, 2, 4, 5, 'version']

# Find the maximum and minimum values in the list
max_value, min_value = find_max_min(original_list)

# Print the results
print("Original list:")
print(original_list)
print("Maximum and Minimum values in the said list:")
print((max_value, min_value))
