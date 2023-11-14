# Write a Python program to check if all items of a given list of strings is equal to a given string. 

def check_all_items_equal(input_list, target_string):
    return all(item == target_string for item in input_list)

# Sample list of strings 
my_list = ["apple", "apple", "apple", "apple", "apple"]
target_string = "apple"

# Check if all items in the list are equal to the target string
result = check_all_items_equal(my_list, target_string)

# Print the result
if result:
    print("All items are equal to the target string:")
else:
    print("Not all the items are equal to the target string:")
    