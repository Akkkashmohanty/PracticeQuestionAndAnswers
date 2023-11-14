# Write a Python program to create a multidimensional list (lists of lists) with zeros. 

def create_multidimensional_list(row, cols):
     multidimensional_list = [[0 for _ in range(cols)] for _ in range(rows)]
     return multidimensional_list

# Specify the number of rows and columns for the multidimensional list
rows = 3
cols = 2

# In this program, 
# the create_multidimensional_list function takes the number of rows and columns as input and uses list comprehensions to create a multidimensional list filled with zeros. 
# The result is a list of lists, as shown in the example.

# Call the function to create the multidimensional list
result = create_multidimensional_list(rows, cols)

# Print the result
print("Multidimensional list:", result)









