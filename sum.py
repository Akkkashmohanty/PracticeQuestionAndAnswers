#Write a Python program to sum all the items in a list. 

def sum_list_items(my_list):
    total = 0
    for item in my_list:
        total += item
    return total

#My list
my_list = [1, 2, 3, 4, 5]

# Call the function and print the result
result = sum_list_items(my_list)
print("Sum of items in the list:", result)
