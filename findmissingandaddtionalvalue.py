# Write a Python program to find missing and additional values in two lists.      
 
def find_missing_and_additional_values(list1, list2):
    missing_values = [item for item in list1 if item not in list2]
    additional_values = [item for item in list2 if item not in list1]
    return missing_values, additional_values

# Sample data
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['b', 'c', 'g', 'h', 'i']

# Call the function to find missing and additional values
missing_values, additional_values = find_missing_and_additional_values(list1, list2)

# Print the results
print("Missing values in the second list:", missing_values)
print("Additional values in the second list:", additional_values)
