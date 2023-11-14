# Write a Python program to create a list with infinite elements. 

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# In this example, the infinite_sequence function is a generator that yields an increasing sequence of numbers. 
# When you use next(sequence_generator), it generates the next element in the sequence. 
# You can continue generating elements as needed, but keep in mind that this is a pseudo-infinite list that generates elements on-the-fly and doesn't consume infinite memory.

# Create a generator for an "infinite" sequence of numbers
sequence_generator = infinite_sequence()

# Generate and print the first few elements
for _ in range(10):
    print(next(sequence_generator))
