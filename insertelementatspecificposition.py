# Write a Python program to insert an element at a specified position into a given list. 

def insert_element_at_position(input_list, k, element_to_insert):

    if k < 0:
        k = 0 # Ensure k is not negative
    elif k > len(input_list):
        k = len(input_list) # Ensure k is within the valid range

    input_list.insert(k, element_to_insert) # Insert the element at position k
    return input_list

# In this program, the insert_element_at_position function takes a list, a position k, and an element to insert as input. 
# It ensures that the position k is not negative and is within the valid range of the list. 
# Then, it uses the insert method to insert the element at the specified position. 
# The result is the modified list with the element inserted at the specified position.

# Original List
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Position to insert the element (0-based index)
k = 2

# Element to insert
element_to_insert = 12

# Call the function to insert the element at the specified position
new_list = insert_element_at_position(original_list, k, element_to_insert)

# Print the result
print("Original list:", original_list)
print("After inserting an element at kth position in the said list:", new_list)
