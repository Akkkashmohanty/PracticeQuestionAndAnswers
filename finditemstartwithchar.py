# Write a Python program to find the items starts with specific character from a given list. 

def find_items_starting_with_char(input_list, char):
    result = [item for item in input_list if item.startswith(char)]
    return 

# In this program, the find_items_starting_with_char function takes a list and a character as arguments. 

# Sample list of strings
original_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

# Print the original list
print("Original list:")
print(original_list)

# Specify the characters to search for
chars_to_find = ['a', 'd', 'w']

# Find items starting with specific characters
for char in chars_to_find:
    items_starting_with_char = find_items_starting_with_char(original_list, char)
    print(f"Items start with {char} from the said list:")
    print(items_starting_with_char)


# It uses list comprehension and the startswith method to create a new list containing items that start with the specified character. 
# The program iterates over the specified characters and prints the items that start with each character.