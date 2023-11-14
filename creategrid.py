# Write a Python program to create a 3X3 grid with numbers.

def create_grid(rows, clos):
     grid = [[j for j in range(1, cols + 1)] for i in range(rows)]
     return grid

# In this program, the create_grid function takes the number of rows and columns as 
# input and uses list comprehensions to generate a grid filled with numbers starting from 1 and going up to the specified number of columns. 
# The result is a 3x3 grid with numbers, as shown in the example.

# Specify the number of rows and columns for the grid
rows = 3
cols = 3

# Call the function to create the grid
result = create_grid(rows, cols)

# Print the result
print(f"{rows}x{cols} grid with numbers:")
for row in result:
    print(row)
    