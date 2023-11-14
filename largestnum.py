#Write a Python program to get the largest number from a list. 

def find_largest_number(my_list):
    if len(my_list) == 0:
        return None  # Handle the case of an empty list

    largest = my_list[0]  # Initialize largest to the first element

    for item in my_list:
        if item > largest:
            largest = item

    return largest

# Example list
my_list = [12, 45, 78, 34, 100, 9, 54]

# Call the function and print the result
largest_number = find_largest_number(my_list)
if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty.")
