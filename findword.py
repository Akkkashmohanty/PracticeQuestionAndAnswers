#Write a Python program to find the list of words that are longer than n from a given list of words. 

def find_words_longer_than_n(word_list, n):
    longer_words = [word for word in word_list if len(word) > n]
    return longer_words

# Example list of words
word_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# Specify the minimum length 'n'
n = 5

# Call the function and print the result
result = find_words_longer_than_n(word_list, n)
print("Words longer than", n, "characters:", result)


