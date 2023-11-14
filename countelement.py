#Write a Python program to count the number of elements in a list within a specified range. 

def count_elements_in_range(input_list, start, end):
    count = 0
    for item in input_list:
        if start <= item <= end:
            count += 1
    return count

# Example list of numbers
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Specify the range
start_range = 30
end_range = 70

# Call the function and count elements in the specified range
count = count_elements_in_range(my_list, start_range, end_range)

print(f"Number of elements in the range [{start_range}, {end_range}]: {count}")
