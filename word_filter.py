# Input text separated by space
input_text = input("Enter some text separated by space: ")

# Use list comprehension to filter words with even length
even_length_words = [word for word in input_text.split() if len(word) % 2 == 0]

# Print each even-length word on a new line
for word in even_length_words:
    print(word)
