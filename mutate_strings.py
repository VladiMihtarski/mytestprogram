def transform_string(first_string, second_string):
  """Transforms the first string into the second one, letter by letter, starting from the first one.

  Args:
    first_string: The first string.
    second_string: The second string.

  Returns:
    A list of unique strings that are the result of transforming the first string into the second string, letter by letter.
  """

  unique_strings = []
  current_string = first_string

  for i in range(len(first_string)):
    new_string = current_string[:i] + second_string[i] + current_string[i + 1:]

    if new_string != first_string and new_string not in unique_strings:
      print(new_string)
      unique_strings.append(new_string)

    current_string = new_string

  return unique_strings


# Example usage:

first_string = input()
second_string = input()

unique_strings = transform_string(first_string, second_string)



