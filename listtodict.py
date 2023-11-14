# Write a Python program to convert list to list of dictionaries.

def convert_to_list_of_dictionaries(color_names, color_codes):
    color_list = [{'color_name': name, 'color_code': code} for name, code in zip(color_names, color_codes)]
    return color_list

# In this program, the convert_to_list_of_dictionaries function takes two lists, color_names and color_codes, and uses a list comprehension with zip to create a list of dictionaries.
# Each dictionary contains the keys 'color_name' and 'color_code', which are assigned values from the corresponding lists. 
# The resulting list of dictionaries represents color names and their corresponding color codes.

# Sample lists
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Call the function to convert the lists into a list of dictionaries
color_list = convert_to_list_of_dictionaries(color_names, color_codes)

# Print the resulting list of dictionaries
for color in color_list:
    print(color)