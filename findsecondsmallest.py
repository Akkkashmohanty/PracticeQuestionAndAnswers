#Write a Python program to find the second smallest number in a list. 

def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None  # Handle the case with fewer than 2 elements

    smallest = second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

# Example list of numbers
numbers_list = [12, 45, 2, 4, 1, 9, 7, 1]

# Call the function to find the second smallest number
second_smallest = find_second_smallest(numbers_list)

if second_smallest is not None:
    print("The second smallest number in the list is:", second_smallest)
else:
    print("There is no second smallest number in the list.")


