#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def remove_elements_by_indices(input_list, indices_to_remove):
    filtered_list = [input_list[i] for i in range(len(input_list)) if i not in indices_to_remove]
    return filtered_list

# Sample list
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Indices to remove (0-based): 0, 4, and 5
indices_to_remove = [0, 4, 5]

# Call the function and print the result
result = remove_elements_by_indices(sample_list, indices_to_remove)
print("Modified list after removing specified indices:", result)
