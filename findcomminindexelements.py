# Write a Python program to extract common index elements from more than one given list. 

def find_common_index_elements(*lists):
    if not lists:
        return []

    common_elements = []
    list_len = len(lists[0])

    for i in range(list_len):
        element = lists[0][i]
        is_common = all(element == lst[i] for lst in lists)
        if is_common:
            common_elements.append(element)

    return common_elements

# Original lists
list1 = [1, 1, 3, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 5, 7]
list3 = [0, 1, 2, 3, 4, 5, 7]

# Find common index elements of the lists
common_elements = find_common_index_elements(list1, list2, list3)

# Print the result
print("Original lists:")
print(list1)
print(list2)
print(list3)
print("Common index elements of the said lists:")
print(common_elements)
