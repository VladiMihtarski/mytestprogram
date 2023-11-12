# Define a function
def isPalindrome(string):
    return string == string[::-1]

# Enter input strings separated by commas
input_strings = input()
strings_list = input_strings.split(',')

# Check if each string in the list is a palindrome
for string in strings_list:
    print(isPalindrome(string.strip()))
