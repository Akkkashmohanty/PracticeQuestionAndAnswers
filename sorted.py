#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 

def sort_tuples_by_last_element(tuples):
    sorted_list = sorted(tuples, key=lambda x: x[-1])
    return sorted_list

# Sample list of tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Call the function and print the result
result = sort_tuples_by_last_element(sample_list)
print("Sorted list in increasing order by the last element:", result)
