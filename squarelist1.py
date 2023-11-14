# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 

# Generate a list of squares of numbers between 1 and 30
squares_list = [x**2 for x in range(1, 31)]

# Exclude the first 5 elements
result_list = squares_list[5:]

# Print the list excluding the first 5 elements
print("List of squares excluding the first 5 elements:", result_list)
