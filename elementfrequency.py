#Write a Python program to get the frequency of the elements in a list. 

def get_element_frequency(input_list):
    frequency_dict = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# In this program, the get_element_frequency function takes a list as an argument and initializes an empty dictionary frequency_dict. 
# It then iterates through the list, checking if each element is already a key in the dictionary. 
# If it is, it increments the frequency count; otherwise, it adds the element as a key with a count of 1. 
# The resulting dictionary contains the frequency of each element, which is then printed in the final loop.

# Example List
my_list = [1, 2, 2, 3, 4, 4, 5, 1, 2, 3, 4]

# Call the function and get the frequency of elements
element_frequency = get_element_frequency(my_list)

for item, frequency in element_frequency.items():
    print(f"{item}: {frequency} times")
