# Write a Python program to scramble the letters of string in a given list. 

import random

def scramble_string(input_str):
    # Convert the string to a list of characters
    char_list = list(input_str)
    # Shuffle the characters randomly
    random.shuffle(char_list)
    # Join the characters back into a string
    scrambled_str = ''.join(char_list)
    return scrambled_str

# Original list of strings
original_list = ['Python', 'list', 'exercises', 'practice', 'solution']

# Scramble the letters of the strings in the list
scrambled_list = [scramble_string(word) for word in original_list]

# Print the original and scrambled lists
print("Original list:")
print(original_list)
print("After scrambling the letters of the strings of the said list:")
print(scrambled_list)
