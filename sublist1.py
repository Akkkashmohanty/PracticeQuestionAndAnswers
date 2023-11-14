# Write a Python program to generate all sublists of a list. 

def generate_sublists(input_list):
    sublists = []
    for start in range(len(input_list)):
        for end in range(start + 1, len(input_list) + 1):
            sublist = input_list[start:end]
            sublists.append(sublist)
    return sublists

# In this program, the generate_sublists function takes a list as an argument. 
# It uses two nested loops to iterate through all possible start and end positions of sublists within the input list. 
# For each combination, it extracts the sublist using slicing and appends it to the sublists list. 
# Finally, the function returns the list of all generated sublists, which are then printed in the loop.

# Example list
my_list = [1, 2, 3]

# Call the function to generate all sublists
all_sublists = generate_sublists(my_list)

# Print the generated sublists
for sublist in all_sublists:
    print(sublist)

