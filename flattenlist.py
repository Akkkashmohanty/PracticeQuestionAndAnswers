#Write a Python program to flatten a shallow list. 

def flatten_list(shallow_list):
    flattened = []
    for item in shallow_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

#Example shallow list
shallow_list = [1, [2, 3], [4, 5], 6, [7, 8, 9]]

#Call the function to flatten the list
flattened_list = flatten_list(shallow_list)

#Print the flattened list
print("Flattened list:", flattened_list)
