# Write a Python program to create a list of empty dictionaries. 

# Specify the number of empty dictionaries you want in the list
num_empty_dicts = 5

# Create a list of empty dictionaries using a list comprehension
list_of_empty_dicts = [{} for _ in range(num_empty_dicts)]

# Print the list of empty dictionaries
print(list_of_empty_dicts)
