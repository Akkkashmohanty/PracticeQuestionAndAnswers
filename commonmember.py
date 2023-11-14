#Write a Python function that takes two lists and returns True if they have at least one common member.

def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Check if the lists have at least one common member
result = have_common_member(list1, list2)

if result:
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
