# Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
	
def swap_elements_at_nth_positions(input_list):
    for i in range(0, len(input_list) - 1, 2):
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list

# Sample list
my_list = [0, 1, 2, 3, 4, 5]

# Call the function to swap elements at nth positions
result_list = swap_elements_at_nth_positions(my_list)

# Print the result
print(result_list)
