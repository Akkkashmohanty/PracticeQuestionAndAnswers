#  Write a Python program to count the number of sublists contain a particular element. 

def count_sublists_with_element(nested_list, element):
    count = 0
    for sublist in nested_list:
        if element in sublist:
            count += 1
    return count

# Original lists
list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
list2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

# Count the number of sublists containing '1' in list1
count_1_list1 = count_sublists_with_element(list1, 1)

# Count the number of sublists containing '7' in list1
count_7_list1 = count_sublists_with_element(list1, 7)

# Count the number of sublists containing 'A' in list2
count_A_list2 = count_sublists_with_element(list2, 'A')

# Count the number of sublists containing 'E' in list2
count_E_list2 = count_sublists_with_element(list2, 'E')

# Print the results
print("Original list 1:")
for sublist in list1:
    print(sublist)
print("Count '1' in the said list:", count_1_list1)
print("Count '7' in the said list:", count_7_list1)

print("Original list 2:")
for sublist in list2:
    print(sublist)
print("Count 'A' in the said list:", count_A_list2)
print("Count 'E' in the said list:", count_E_list2)
