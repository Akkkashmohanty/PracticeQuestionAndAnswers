# Write a Python program to print a nested lists (each list on a new line) using the print() function. 

def print_nested_lists(nested_lists):
    for inner_list in nested_lists:
        print(inner_list)

# In this program, the print_nested_lists function takes a list of nested lists as an argument. 
# It iterates through the outer list and uses the print() function to print each inner list. 
# This results in each inner list being printed on a new line.

# Sample nested lists
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Call the function to print the nested lists
print_nested_lists(nested_lists)
