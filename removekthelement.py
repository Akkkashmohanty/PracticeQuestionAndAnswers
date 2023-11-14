# Write a Python program to remove the K'th element from a given list, print the new list. Original list:

def remove_kth_element(input_list, k):

    if k < 0 or k >= len(input_list):
        return input_list  # Return the original list if K is out of range

    del input_list[k]  # Remove the element at position K
    return input_list

# In this program, the remove_kth_element function takes a list and the position k to remove as input. 
# It checks if k is within the valid range of the list, and if so, it uses the del statement to remove the element at position k. 
# The result is the modified list with the K'th element removed.

# Original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# K'th element to remove (0-based index)
k = 2

# Call the function to remove the K'th element
new_list = remove_kth_element(original_list, k)

# Print the result
print("Original list:", original_list)
print("After removing an element at the kth position of the said list:", new_list)
