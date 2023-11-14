# Write a Python program to sort a list of nested dictionaries. 

def sort_nested_dictionaries(data_list, key_to_sort):
    sorted_list = sorted(data_list, key=lambda x: x[key_to_sort])
    return sorted_list

#In this program, the sort_nested_dictionaries function takes a list of nested dictionaries and a key to sort by. 
# It uses the sorted function with a custom sorting key that extracts the specified key (key_to_sort) from each dictionary. 
# The resulting list is sorted based on the values of the specified key, and the sorted list of nested dictionaries is then printed.

# Sample list of nested dictionaries
data_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20},
]

# Specify the key to sort by
key_to_sort = 'age'

# Call the function tp sort the list of nested dictionaries
sorted_data = sort_nested_dictionaries(data_list, key_to_sort)

# Print the sorted list
for item in sorted_data:
    print(item)