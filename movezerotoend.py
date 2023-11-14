# Write a Python program to move all zero digits to end of a given list of numbers. 

def move_zeros_to_end(numbers):
    non_zero_elements = [num for num in numbers if num != 0]
    zero_elements = [0] * (len(numbers) - len(non_zero_elements))
    result = non_zero_elements + zero_elements
    return result

# Sample list of numbers
numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# Call the function to move all zero digits to the end
result_list = move_zeros_to_end(numbers)

# Print the original list
print("Original list:")
print(numbers)

# Print the modified list
print("Move all zero digits to the end of the list:")
print(result_list)
