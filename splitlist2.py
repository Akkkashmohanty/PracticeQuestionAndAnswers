# Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

def split_list(input_list, length_of_the_first_part):

    if length_of_the_first_part < 0:
        length_of_the_first_part = 0
    elif length_of_the_first_part > len(input_list):
        length_of_the_first_part = len(input_list)

    first_part = input_list[:length_of_the_first_part]
    second_part = input_list[length_of_the_first_part:]

    return (first_part, second_part)

# In this program, the split_list function takes a list and the length of the first part as input. 
# It then uses list slicing to split the list into two parts, one from the beginning of the list to the specified length, and the other from the specified length to the end of the list. 
# The result is a tuple containing the two parts of the list.

# Original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Length of the first part of the list
length_of_the_first_part = 3

# Call the function to split the list
split_result = split_list(original_list, length_of_the_first_part)

# Print The result
print("Original list:", original_list)
print("Length of the first part of the list:", length_of_the_first_part)
print("Split the list into two parts:", split_result)