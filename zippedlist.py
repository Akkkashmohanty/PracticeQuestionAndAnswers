# Original lists
list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]

# Zipped list
zipped_list = [list(a + b) for a, b in zip(list1, list2)]

# Print the zipped list
print("Zipped list:")
for sublist in zipped_list:
    print(sublist)
