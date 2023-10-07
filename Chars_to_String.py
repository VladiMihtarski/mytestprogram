def concatenate_characters(char1, char2, char3):
    """
  Concatenate three characters into a single string and print it.

  Args:
      char1 (str): The first character.
      char2 (str): The second character.
      char3 (str): The third character.
  """
    concatenated_string = char1 + char2 + char3
    print(concatenated_string)


# Input three characters from the user
char1 = input()
char2 = input()
char3 = input()

# Call the function to concatenate and print the characters
concatenate_characters(char1, char2, char3)
