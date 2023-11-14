#Write a python program to check whether two lists are circularly identical.

def are_lists_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False

    extended_list1 = list1 + list1
    return set(list2).issubset(extended_list1)

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 1, 2, 3]

# Check if the lists are circularly identical
result = are_lists_circularly_identical(list1, list2)

if result:
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
