#Write a Python program to print the numbers of a specified list after removing even numbers from it. 

def remove_even_numbers(input_list):
    filtered_list = [num for num in input_list if num % 2 != 0]
    return filtered_list

# Sample list with numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function to remove even numbers
filtered_numbers = remove_even_numbers(numbers_list)

# Print the numbers after removing even numbers
print("Numbers after removing even numbers:", filtered_numbers)
