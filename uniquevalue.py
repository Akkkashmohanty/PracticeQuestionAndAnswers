#Write a Python program to get unique values from a list. 

def get_unique_values(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

# In this program, the get_unique_values function takes a list as an argument and first converts the list to a set using set(input_list). 
# A set automatically removes duplicate values. Then, it converts the set back to a list using list(unique_set), and the resulting list contains only the unique values. 
# These unique values are returned as the output.

#Example list with duplicate values
my_list = [11, 12, 12, 13, 14, 14, 15]

#Call the function and get unique values
unique_values = get_unique_values(my_list)

# Print the unique values
print("Unique values in the list:", unique_values)