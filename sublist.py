# Write a Python program to check whether a list contains a sublist.

def list_contains_sublist(main_list, sublist):

    # Iterate through the Main list

    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False

# In this program, the list_contains_sublist function takes a main list and a sublist as arguments. 
# It iterates through the main list, checking if each sublist of the same length as the desired sublist matches the desired sublist. 
# If a match is found, the function returns True; otherwise, it returns False.

# Example List
main_list = [1, 2, 3, 4, 5, 6, 7]
sublist1 = [3, 4, 5]
sublist2 = [6, 7, 8]

# Check if the main list contains the sublists
contains_sublist1 = list_contains_sublist(main_list, sublist1)
contains_sublist2 = list_contains_sublist(main_list, sublist2)

if contains_sublist1:
    print("The main list contains sublist1.")
else:
    print("The main list does not contain sublist1.")

if contains_sublist2:
    print("The main list contains sublist2.")
else:
    print("The main list does not contain sublist2.")