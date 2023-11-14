# Write a Python program to flatten a given nested list structure.

def flatten_nested_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_nested_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Sample nested list
original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

# Call the function to flatten the nested list
flattened_list = flatten_nested_list(original_list)

# Print the result
print("Original list:", original_list)
print("Flatten list:", flattened_list)