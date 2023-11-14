# Write a Python program to find the list in a list of lists whose sum of elements is the highest. 

def list_with_highest_sum(list_of_lists):
    max_list = max(list_of_lists, key=lambda lst: sum(lst))
    return max_list

# Sample list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# Call the function to find the list with the highest sum of elements
result_list = list_with_highest_sum(list_of_lists)

# Print the result
print("List with the highest sum of elements:", result_list)


