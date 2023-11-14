# Write a Python program to convert a pair of values into a sorted unique array. 

def convert_pair_to_sorted_unique_array(pairs):
    combined_array = []
    for pair in pairs:
        combined_array.extend(pair)
    
    unique_sorted_array = sorted(set(combined_array))
    return unique_sorted_array

# In this program, the convert_pair_to_sorted_unique_array function takes a list of pairs as input. 
# It combines the values from the pairs into a single list (combined_array), sorts that list, and then converts it to a set to remove duplicates. 
# Finally, it converts the set back to a list to obtain the sorted unique array as the result.

# Sample pairs of values
pairs = [(2, 1), (4, 3), (6, 5), (3, 1)]

# Call the function to convert pairs to a sorted unique array
result_array = convert_pair_to_sorted_unique_array(pairs)

# Print the result
print("Sorted unique array:", result_array)
