#  Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 

import itertools

def generate_combinations(input_list, n):
    if n <= 0 or n > len(input_list):
        return []
    
    combinations = list(itertools.combinations(input_list, n))
    return combinations

# In this program, the generate_combinations function takes a list and the number n of distinct objects to select in each combination as input. 
# It uses itertools.combinations to generate all possible combinations of n distinct elements from the input list. 
# The result is a list of combinations.

# Original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Number of distinct objects in each combination
n = 2

# Call the function to generate combinations
combinations = generate_combinations(original_list, n)

# Print the result
print("Original list:", original_list)
print(f"Combinations of {n} distinct objects:")
for combination in combinations:
    print(combination)