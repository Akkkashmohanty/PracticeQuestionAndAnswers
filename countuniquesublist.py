# Write a Python program to count number of unique sublists within a given list. 

def count_unique_sublists(nested_list):
    unique_sublists = {}
    for sublist in nested_list:
        unique_sublists[tuple(sublist)] = unique_sublists.get(tuple(sublist), 0) + 1
    return unique_sublists

# Original lists
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
list2 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]

# Count the number of unique sublists in list1
unique_sublists_list1 = count_unique_sublists(list1)

# Count the number of unique sublists in list2
unique_sublists_list2 = count_unique_sublists(list2)

# Print the results
print("Original list 1:")
for sublist in list1:
    print(sublist)
print("Number of unique lists of the said list:")
print(unique_sublists_list1)

print("Original list 2:")
for sublist in list2:
    print(sublist)
print("Number of unique lists of the said list:")
print(unique_sublists_list2)

