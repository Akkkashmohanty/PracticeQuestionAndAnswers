# Write a Python program to generate a 3*4*6 3D array whose each element is *. 

# Define the dimensions of the 3D array
depth = 3
rows = 4
columns = 6

# Generate the 3D array filled with asterisks
array_3d = [[['*' for _ in range(columns)] for _ in range(rows)] for _ in range(depth)]

# Print the 3D array
for z in range(depth):
    for y in range(rows):
        for x in range(columns):
            print(array_3d[z][y][x], end=' ')
        print()  # Move to the next row
    print()  # Add an empty line to separate the 2D arrays in the third dimension
