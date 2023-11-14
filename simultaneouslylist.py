# Write a Python program to iterate over two lists simultaneously.

list1 = [1, 2, 3, 4,]
list2 = ['a', 'b', 'c', 'd',]

for item1, item2 in zip(list1, list2):

#In this program, zip(list1, list2) combines the elements of list1 and list2 into pairs, and the for loop iterates over these pairs. 
# This way, you can process elements from both lists at the same time within the loop.

    print(item1, item2)
