# Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 

def process_numbers(input_list):
    # Round the numbers
    rounded_list = [round(number) for number in input_list]

    # Find the minimum and maximum values
    min_value = min(rounded_list)
    max_value = max(rounded_list)

    # Multiply all numbers by 5
    multiplied_list = [number * 5 for number in rounded_list]

    # Find unique numbers and sort them in ascending order
    unique_sorted_numbers = sorted(set(multiplied_list))

    return min_value, max_value, unique_sorted_numbers

# In this program, the process_numbers function takes a list of numbers as input. 
# It first rounds the numbers, finds the minimum and maximum values, 
# multiplies all numbers by 5, and then extracts the unique numbers, 
# sorts them in ascending order, and returns the results. 
# The final output displays the original list, minimum and maximum values, and the unique, rounded numbers separated by spaces.

# Original list of numbers
original_list = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

# Call the function to process the numbers
min_value, max_value, result = process_numbers(original_list)

# Print the results
print("Original list:", original_list)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Result:")
print(" ".join(map(str, result)))
