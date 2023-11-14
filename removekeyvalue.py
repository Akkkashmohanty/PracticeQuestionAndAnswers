# Write a Python program to remove key values pairs from a list of dictionaries. 

def remove_key_value_pairs(data_list, key_to_remove):
    result = [{key: value for key, value in d.items() if key != key_to_remove} for d in data_list]
    return result

# Sample list of dictionaries
data_list = [
    {'name': 'Akash', 'age': 25, 'city': 'New York'},
    {'name': 'Happy', 'age': 30, 'city': 'Los Angeles'},
    {'name': 'Manish', 'age': 20, 'city': 'Chicago'},
]

# Key to remove from the dictionaries
key_to_remove = 'age'

# Call the function to remove key-value pairs
result_list = remove_key_value_pairs(data_list, key_to_remove)

# Print the result
for d in result_list:
    print(d)
