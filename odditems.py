# Write a Python program to select the odd items of a list. 

def select_odd_items(input_list):
    odd_items = [item for item in input_list if item % 2 != 0]
    return odd_items

# Sample List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the function to select the odd items
odd_items = select_odd_items(my_list)

# Print the selected odd items
print("Selected odd items:", odd_items)
