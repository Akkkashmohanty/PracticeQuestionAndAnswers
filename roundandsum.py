#  Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. 

def round_and_sum(input_list):
    rounded_list = [round(number) for number in input_list]
    total_sum = sum(rounded_list)
    result = total_sum * len(input_list)
    return result

# Original list of numbers
original_list = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

# Call the function to round, sum, and multiply
final_result = round_and_sum(original_list)

# Print the result
print("Original list:", original_list)
print("result:", final_result)