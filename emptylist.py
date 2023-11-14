#Write a Python program to check a list is empty or not. 

def is_list_empty(my_list):
    return len(my_list) == 0

#Example List
empty_list = []
non_empty_list = [1, 2, 3, 4]

#Check if the list is empty
is_empty1 = is_list_empty(empty_list)
is_empty2 = is_list_empty(non_empty_list)

if is_empty1:
    print("The first list is empty")
else:
    print("The first list is not empty")
if is_empty2:
    print("The second list is empty")
else:
    print("The second list is not empty")
