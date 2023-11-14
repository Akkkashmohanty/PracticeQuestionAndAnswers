# Write a Python program access the index of a list. 
#Method---->1

#my_list = ['apple', 'banana', 'cherry', 'date']

#Access the index of each element using a for loop.
#for index in range(len(my_list)):
    #item = my_list[index]
    #print(f"Element at index {index} is: {item}")


#Method------>2

my_list = ['apple', 'banana', 'cherry', 'date']

#Access the index of each element using enumerate.
for index, item in enumerate(my_list):
    print(f"Element at index {index} is: {item}")