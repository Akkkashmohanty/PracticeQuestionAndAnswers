# Write a Python program to split a list based on first character of word. 

def split_list_by_first_char(word_list):
    word_dict = {}
    for word in word_list:
        first_char = word[0]
        if first_char in word_dict:
            word_dict[first_char].append(word)
        else:
            word_dict[first_char] = [word]

    result = list(word_dict.values()) 
    return result 

# In this program, the split_list_by_first_character function takes a list of words as an argument. 
# It uses a dictionary, word_dict, where the keys represent the first characters of the words. 
# It iterates through the list, checking the first character of each word. 
# If the first character is already a key in the dictionary, the word is appended to the corresponding list. 
# If the first character is not in the dictionary, a new list is created with the word, and the first character is used as the key. 
# Finally, the values of the dictionary are collected into a list of sublists, and that's the result.

# Sample list of word
word_list = ["apple", "banana", "cherry", "date", "apricot", "blueberry"]

# Call the function
split_result = split_list_by_first_char(word_list)

# Print The Result
for sublist in split_result:
    print(sublist)
