# Write a Python program to count number of lists in a given list of lists. 

def count_lists_in_list_of_lists(lst):
    count = 0

    for item in lst:
        if isinstance(item, list):
            count += 1

    return count

# Original list
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

# Count the number of lists in the given lists
count1 = count_lists_in_list_of_lists(list1)
count2 = count_lists_in_list_of_lists(list2)

# Print the results
print("Original list 1:")
for sublist in list1:
    print(sublist)
print("Number of lists in the first list of lists:", count1)

print("Original list 2:")
for sublist in list2:
    print(sublist)
print("Number of lists in the second list of lists:", count2)
