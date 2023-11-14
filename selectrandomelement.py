# Write a Python program to extract a given number of randomly selected elements from a given list. 

import random

def select_random_elements(input_list, num_elements):
    if num_elements > len(input_list):
        num_elements = len(input_list) # Ensure not selecting more elements than available

    random_element = random.sample(input_list, num_elements)
    return random_element

# In this program, the select_random_elements function takes a list and the number of elements to select as input. 
# It uses random.sample to randomly select the specified number of elements from the input list. 
# The result is a list of randomly selected elements.

# Original list
original_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Number of random elements to select
num_elements = 3

# Call the function to select random elements
selected_elements = select_random_elements(original_list, num_elements)

# Print the result
print("Original List:", original_list)
print(f"Selected {num_elements} random number of the above list:", selected_elements)