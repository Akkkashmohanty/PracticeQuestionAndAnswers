# Write a Python program to check whether all dictionaries in a list are empty or not. 

def are_all_dicts_empty(input_list):
    for d in input_list:
        if bool(d):  # Check if the dictionary is not empty
            return False
    return True

# Sample list of dictionaries
list1 = [{}, {}, {}]
list2 = [{1: 2}, {}, {}]

# Check if all dictionaries in list1 are empty
result1 = are_all_dicts_empty(list1)

# Check if all dictionaries in list2 are empty
result2 = are_all_dicts_empty(list2)

# Print the results
print("Sample list 1:", result1)
print("Sample list 2:", result2)
