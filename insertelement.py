# Write a Python program to insert an element before each element of a list.

def insert_element_before_each(input_list, element_to_insert):
    modified_list = [element_to_insert, *input_list]
    return modified_list

# Sample List
my_list = [2, 4, 6, 8]

# Element to insert before each element
element_to_insert = 0

# Call the function to insert the element before each element
modified_list = insert_element_before_each(my_list, element_to_insert)

# Print the modified list
print("Modified list:", modified_list)