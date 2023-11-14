# Write a Python program to find a tuple, the smallest second index value from a list of tuples.

def find_tuple_with_smallest_second_index(tuples_list):
    if not tuples_list:
        return None
    
    min_tuples = min(tuples_list, key=lambda x: x[1])
    return min_tuples

# Sample list of tuples
tuples_list = [(1, 5), (2, 3), (3, 7), (4, 2), (5, 9)]

# Call the function to find the tuple with the smallest second index values
result_tuples = find_tuple_with_smallest_second_index(tuples_list)

# Print The Result
print("Tuples with the smallest second index value:", result_tuples)
