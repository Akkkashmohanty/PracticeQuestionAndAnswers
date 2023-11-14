#Write a Python program to find the index of an item in a specified list. 

def find_index(item, my_list):
    if item in my_list:
        index = my_list.index(item)
        return index
    else:
        return None

# Sample list
my_list = [10, 20, 30, 40, 50]

# Item to find
item_to_find = 30

# Call the function to find the index
index = find_index(item_to_find, my_list)

if index is not None:
    print(f"The index of {item_to_find} is: {index}")
else:
    print(f"{item_to_find} is not in the list.")

