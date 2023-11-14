# Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 

def modified_run_length_encoding(input_list):
    if not input_list:
        return []

    result = []
    current_item = input_list[0]
    count = 1

    for item in input_list[1:]:
        if item == current_item:
            count += 1
        else:
            if count == 1:
                result.append(current_item)
            else:
                result.append([count, current_item])
            current_item = item
            count = 1

    if count == 1:
        result.append(current_item)
    else:
        result.append([count, current_item])

    return result

# In this program, the modified_run_length_encoding function takes a list as input and iterates through it, counting consecutive occurrences of the same item. 
# If the count is 1, it appends the item itself; otherwise, it appends a sublist with the count and the item. 
# The result is a list reflecting the modified run-length encoding of the input list, whether it's a list of integers or characters.

# Sample list of integers
integer_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Sample string
string_list = "aabcddddadnss"

# Call the function to perform modified run-length encoding on the integer list
encoded_integer_list = modified_run_length_encoding(integer_list)

# Call the function to perform modified run-length encoding on the string
encoded_string_list = modified_run_length_encoding(list(string_list))

# Print the results
print("Original list:", integer_list)
print("List reflecting the modified run-length encoding from the integer list:", encoded_integer_list)
print("Original String:", string_list)
print("List reflecting the modified run-length encoding from the string:", encoded_string_list)
