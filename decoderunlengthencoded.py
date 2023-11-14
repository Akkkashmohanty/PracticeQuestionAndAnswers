# Write a Python program to decode a run-length encoded given list.

def decode_run_length_encoded(encoded_list):
    decoded_list = []

    for item in encoded_list:
        if isinstance(item, list):
            count, value = item
            decoded_list.extend([value] * count)
        else:
            decoded_list.append(item)
    return decoded_list

# In this program, the decode_run_length_encoded function takes an encoded list as input. 
# It iterates through the elements of the encoded list and reconstructs the original list by repeating the values according to the run-length encoding. 
# The result is the decoded list.

# Original encoded list
encoded_list = [[2, 1], 2, 3, [2, 4], 5, 1]

# Call the function to decode the run-length encoded list
decoded_list = decode_run_length_encoded(encoded_list)

# Print the result
print("Original encoded list:", encoded_list)
print("Decoded run-length encoded list:", decoded_list)
