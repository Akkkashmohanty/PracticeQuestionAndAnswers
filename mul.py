#Write a Python program to multiply all the items in a list. 

def multiply_list_items(my_list):
    result = 1  # Initialize the result to 1
    for item in my_list:
        result *= item
    return result

# Example list
my_list = [1, 2, 3, 4, 5]

# Call the function and print the result
result = multiply_list_items(my_list)
print("Product of items in the list:", result)
