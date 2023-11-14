# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 

def concatenate_list_with_range(input_list, n):
    concatenated_list = [item + str(i) for i in range(1, n + 1) for item in input_list]
    return concatenated_list

# In this program, the concatenate_list_with_range function takes a list and n as arguments. 
# It uses a list comprehension with nested loops to concatenate each element of the input list with a range from 1 to n. 
# The resulting list contains the concatenated elements, and it is returned as the output.

# Sample list
sample_list = ['p', 'q']
n = 5

# Call the function to create the concatenated list
result_list = concatenate_list_with_range(sample_list, n)

# Print the concatenated list
print(result_list)
