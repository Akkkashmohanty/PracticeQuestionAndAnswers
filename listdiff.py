#Write a Python program to get the difference between the two lists. 

def list_difference(list1, list2):
    difference = [item for item in list1 if item not in list2]
    return difference

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Call the function to get the difference
result = list_difference(list1, list2)

# Print the difference
print("Difference between list1 and list2:", result)

