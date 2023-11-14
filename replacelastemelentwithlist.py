# Write a Python program to replace the last element in a list with another list. 

def replace_last_element_with_list(main_list, new_list):
    main_list[-1:] = new_list
    return main_list

# Sample data
main_list = [1, 3, 5, 7, 9, 10]
new_list = [2, 4, 6, 8]

# Call the function to replace the last element with the new list
result_list = replace_last_element_with_list(main_list, new_list)

# Print the result
print(result_list)

