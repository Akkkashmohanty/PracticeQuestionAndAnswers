# Write a Python program to check whether the n-th element exists in a given list. 

def check_nth_element_existence(input_list, n):
    if n >= 0 and n < len(input_list):
        return True
    else:
        return False
    
# Sample List
my_list = [1, 2, 3, 5,]

#Specify the value of n to check
n = 3

# Call the function to check if the n-th element exsists
result = check_nth_element_existence(my_list, n)

# Print the result
if result:
    print(f"The {n}-th element exsists in the list")
else:
    print(f"The {n}-th element does not exist in the list")