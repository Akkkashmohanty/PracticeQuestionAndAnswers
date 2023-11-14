# Write a Python program to convert a list of multiple integers into a single integer. 

def list_to_single_integer(int_list):
    # Convert the integers to strings
    str_list = [str(num) for num in int_list]

    # Join the strings and convert back to an integer
    result = int(''.join(str_list))

    return result

# In this program, the list_to_single_integer function takes a list of integers as an argument. 
# It first converts each integer in the list to a string using a list comprehension. 
# Then, it joins these strings together using the join method to form a single string. 
# Finally, it converts the resulting string back to an integer using int(), which gives you the desired single integer.

#Sample lost of integer
int_list = [11, 33, 44]

# Call the function to convert the list to a single integer
single_integer = list_to_single_integer(int_list)

# Print the result
print("Converted single integer:", single_integer)