# Write a Python program to insert a given string at the beginning of all items in a list.

def insert_string_at_beginning(input_list, prefix):
    result = [prefix + str(item) for item in input_list]
    return result

# Sample list
my_list = [1, 2, 4, 5]

# String to insert at the beginning
prefix = 'emp'

# call the function to insert the srting at the beginning of list items
result_list = insert_string_at_beginning(my_list, prefix)

# Print the result
print(result_list)
