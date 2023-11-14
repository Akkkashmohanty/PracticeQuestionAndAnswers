#Write a Python program to get the smallest number from a list.

def find_smallest_number(my_list):
    if len(my_list) == 0:
        return None  # Handle the case of an empty list

    smallest = my_list[0]  # Initialize smallest to the first element

    for item in my_list:
        if item < smallest:
            smallest = item

    return smallest

# Example list
my_list = [12, 45, 78, 34, 100, 9, 54]

# Call the function and print the result
smallest_number = find_smallest_number(my_list)
if smallest_number is not None:
    print("The smallest number in the list is:", smallest_number)
else:
    print("The list is empty.")
