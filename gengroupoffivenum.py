# Write a Python program to generate groups of five consecutive numbers in a list. 

def generate_group_of_five_numbers(start, end):
    result = []
    for i in range(start, end + 1, 5):
        group = list(range(i, i + 5))
        result.append(group)
    return result

# In this program, the generate_groups_of_five_numbers function takes a starting and ending number as arguments. 
# It uses a loop to generate groups of five consecutive numbers, and the resulting groups are stored in a list. 
# You can adjust the start_number and end_number to define the desired range for generating groups of five consecutive numbers.

# Specify the range of numbers
start_number = 1
end_number = 20 # Adjust the range as needed

# Class the function to generate group of five consecutive number
groups = generate_group_of_five_numbers(start_number, end_number)

# Print the generate group
for group in groups:
    print(group)