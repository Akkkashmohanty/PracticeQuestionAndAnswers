# Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 


def run_length_encoding(input_list):
    if not input_list:
        return []

    result = []
    current_item = input_list[0]
    count = 1

    for item in input_list[1:]:
        if item == current_item:
            count += 1
        else:
            result.append([count, current_item])
            current_item = item
            count = 1

    result.append([count, current_item])

    return result

# In this program, the run_length_encoding function takes a list as input and iterates through it, counting consecutive occurrences of the same item. 
# When a different item is encountered, the count and item are added as a sublist to the result list. 
# The result is a list reflecting the run-length encoding of the input list, whether it's a list of integers or characters.


# Sample list of integers
integer_list = [1, 1, 2, 3, 4, 4.3, 5, 1]

# Sample string
string_list = "automatically"

# Call the function to perform run-length encoding on the integer list
encoded_integer_list = run_length_encoding(integer_list)

# Call the function to perform run-length encoding on the string
encoded_string_list = run_length_encoding(list(string_list))

# Print the results
print("Original list:", integer_list)
print("List reflecting the run-length encoding from the integer list:", encoded_integer_list)
print("Original String:", string_list)
print("List reflecting the run-length encoding from the string:", encoded_string_list)
