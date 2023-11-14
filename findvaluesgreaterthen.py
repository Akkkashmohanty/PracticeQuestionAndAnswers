# Write a Python program to find all the values in a list are greater than a specified number. 

def find_values_greater_than(input_list, threshold):
    result = [value for value in input_list if value > threshold]
    return result

# Sample list of values
my_list = [1, 3, 5, 7, 9, 10, 2, 4, 6, 8]

# Specify the threshold value
threshold = 5

# Call the function to find values greater than the threshold
result_list = find_values_greater_than(my_list, threshold)

# Print the result
print("Values greater than", threshold, "in the list:", result_list)
