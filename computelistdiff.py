# Write a Python program to compute the difference between two lists.      

def compute_list_difference(list1, list2):
    difference1 = [item for item in list1 if item not in list2]
    difference2 = [item for item in list2 if item not in list1]
    return difference1, difference2

#In this program, the compute_list_difference function takes two lists as arguments and uses list comprehension to compute the differences between the lists. 
# It creates two separate lists, difference1 and difference2, which contain items that are in the first list but not in the second list, and items that are in the second list but not in the first list, respectively. 
# The results are then printed as specified.

# Sample data
list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

# Call the function to compute the difference between
difference1, difference2 = compute_list_difference(list1, list2)

# Print the result
print("Color1 - Color2 :", difference1)
print("Color2 - Color1 :", difference2)

