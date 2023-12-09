def convert_ascii_to_letter(word):
    # Extract the first character (which is a number) and convert it to a letter
    first_char = ""
    for char in word:
        if char.isdigit():
            first_char += char
        else:
            break
    first_letter = chr(int(first_char))

    return first_letter

def swap_first_and_last(word):
    # Swap the first and last letters in the word
    if len(word) > 1:
        swapped_word = word[-1] + word[1:-1] + word[0]
    else:
        swapped_word = word  # If the word has only one character, no need to swap
    return swapped_word

def decipher_secret_message(secret_message):
    words = secret_message.split()  # Split the input into words
    decoded_message = []

    for word in words:
        # Convert the first character in the word from ASCII to a letter
        first_letter = convert_ascii_to_letter(word)

        # Swap the first and last letters in the word (without numbers)
        cleaned_word = ''.join(char for char in word if not char.isdigit())
        swapped_word = swap_first_and_last(cleaned_word)

        # Combine the ASCII letter and swapped word with a space
        combined_output = first_letter + '' + swapped_word
        decoded_message.append(combined_output)

    # Join the combined output into a sentence
    final_decoded_message = ' '.join(decoded_message)

    return final_decoded_message

# Example usage:
secret_message = input()
decoded_message = decipher_secret_message(secret_message)

# Print the result
print(decoded_message)
