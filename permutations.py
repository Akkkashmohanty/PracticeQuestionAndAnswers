#Write a Python program to generate all permutations of a list in Python.

import itertools

#Sample List
my_list = [1, 2, 3,]

#Generate all permutations
permutation = list(itertools.permutations(my_list))

#Print the permutations
for perm in permutation:
    print(perm)