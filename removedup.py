#Write a Python program to remove duplicates from a list. 

def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

#Example list with duplicates

my_list = [1, 2, 2, 3, 4, 4, 5]

#Call the function and print the result

result = remove_duplicates(my_list)
print("List with duplicates removed:", result)