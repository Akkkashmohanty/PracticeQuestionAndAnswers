#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

#Generate a list of square of numbers between 1 and 30
squares_list = [x**2 for x in range (1, 31)]

#Extract the first and last 5 elements
first_5_elements = squares_list[:5]
last_5_elements = squares_list[-5:]

#Print the first and last 5 elements
print("First 5 elements:", first_5_elements)
print("Last 5 elements:", last_5_elements)
