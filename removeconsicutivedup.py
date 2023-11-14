# Write a Python program to remove consecutive duplicates of a given list. 

def remove_consecutive_duplicates(input_list):
    if not input_list:
        return input_list
    
    result = [input_list[0]]

    for item in input_list[1:]:
        if item != result[-1]:
            result.append(item)

    return result

# Sample list with consecutive duplicates
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# Call the function to remove consecutive duplicates 
new_list = remove_consecutive_duplicates(original_list)

# Print the result
print("Original List:", original_list)
print("New List:", new_list)