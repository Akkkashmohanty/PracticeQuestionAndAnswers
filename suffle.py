#Write a Python program to shuffle and print a specified list.

import random

def shuffle_and_print(input_list):
    random.shuffle(input_list)
    for item in input_list:
        print(item, end=' ')

# Sample list
my_list = [1, 2, 3, 4, 5]

# Shuffle and print the list
print("Original list:", my_list)
print("Shuffled list:")
shuffle_and_print(my_list)
