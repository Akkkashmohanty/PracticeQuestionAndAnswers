#Write a Python program to find the second largest number in a list. 

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Handle the case with fewer than 2 elements

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

# Example list of numbers
numbers_list = [12, 45, 3, 4, 1, 9, 7, 45]

# Call the function to find the second largest number
second_largest = find_second_largest(numbers_list)

if second_largest is not None:
    print("The second largest number in the list is:", second_largest)
else:
    print("There is no second largest number in the list.")
