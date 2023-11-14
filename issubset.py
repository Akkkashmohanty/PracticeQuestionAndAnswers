# Write a Python program to check if a nested list is a subset of another nested list. 

def is_subset(nested_list1, nested_list2):
    if isinstance(nested_list2, list):
        for sublist2 in nested_list2:
            if sublist2 not in nested_list1:
                return False
        return True
    return False

# This program defines a function is_subset to check if one nested list is a subset of another. 
# It then applies this function to the original lists and prints the results.

# Original List
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]
list3 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
list4 = [[1, 2], [2, 3]], [[3, 4], [5, 7]]
list5 = [[3, 4], [5, 6]]
         
# Check if list2 is a subset of list1
result1 = is_subset(list1, list2)

# Check if list3 is a subset of list4
result2 = is_subset(list3, list4)

# Check if list5 is a subset of list4
result3 = is_subset(list4, list5)

# Print the result
print("original list 1:")
for sublist in list1:
    print(sublist)
print("Original list 2:")
for sublist in list2:
    print(sublist)
print("If one of the said list is a subset of another:", result1)

print("Original list 3:")
for sublist in list3:
    print(sublist)
print("Original list 4:")
for sublist in list4:
    print(sublist)
print("If one of the said list is a subset of another:", result2)

print("Original list 4:")
for sublist in list4:
    print(sublist)
print("Original list 5:")
for sublist in list5:
    print(sublist)
print("If one of the said list is a subset of another:", result3)