# Write a Python program to split a list every Nth element. 
	
def split_list_by_nth_element(input_list, n):
    result = [input_list[i:i+n] for i in range(0, len(input_list), n)]
    return result

# In this program, the split_list_by_nth_element function takes a list and a value of N as arguments. 
# It uses list comprehension to split the list into sublists of size N, starting from the first element and incrementing by N. 
# The resulting list of sublists is then printed.

# Sample list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# Specify the value of N
N = 3

# Call the function to split the list every Nth element
split_result = split_list_by_nth_element(my_list, N)

# Print the result
for sublist in split_result:
    print(sublist)