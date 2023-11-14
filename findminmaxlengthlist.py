#Write a Python program to find the list with maximum and minimum length. 

def find_max_min_length_lists(lst):
    if not lst:
        return None, None

    max_length = len(lst[0])
    min_length = len(lst[0])
    max_list = lst[0]
    min_list = lst[0]

    for sublist in lst:
        length = len(sublist)
        if length > max_length:
            max_length = length
            max_list = sublist
        elif length < min_length:
            min_length = length
            min_list = sublist

    return max_length, max_list, min_length, min_list

# This program defines a function find_max_min_length_lists that finds the list with the maximum and minimum length within a given list of lists. 
# It then applies this function to the original lists and prints the results.

# Original lists
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
list3 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]

# Find the list with maximum and minimum length in each list
max_length1, max_list1, min_length1, min_list1 = find_max_min_length_lists(list1)
max_length2, max_list2, min_length2, min_list2 = find_max_min_length_lists(list2)
max_length3, max_list3, min_length3, min_list3 = find_max_min_length_lists(list3)

# Print the results
print("Original list 1:")
for sublist in list1:
    print(sublist)
print("List with maximum length of lists:", (max_length1, max_list1))
print("List with minimum length of lists:", (min_length1, min_list1))

print("Original list 2:")
for sublist in list2:
    print(sublist)
print("List with maximum length of lists:", (max_length2, max_list2))
print("List with minimum length of lists:", (min_length2, min_list2))

print("Original list 3:")
for sublist in list3:
    print(sublist)
print("List with maximum length of lists:", (max_length3, max_list3))
print("List with minimum length of lists:", (min_length3, min_list3))
