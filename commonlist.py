#  Write a Python program to find common items from two lists.

def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_items = list(set1.intersection(set2))
    return common_items

# In this program, the find_common_items function takes two lists as arguments. 
# It converts each list into a set to perform set intersection using the intersection method. 
# The resulting set of common items is then converted back to a list, and that list contains the common items between the two input lists.

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Call the function to find common items
common_items = find_common_items(list1, list2)

# Print the common items
print("Common items:", common_items)