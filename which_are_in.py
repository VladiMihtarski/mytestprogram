def find_substrings(seq1, seq2):
    result = [s1 for s1 in seq1 if any(s1 in s2 for s2 in seq2)]
    return result

# Example usage:
if __name__ == "__main__":
    # Input sequences as strings separated by ", "
    input_line1 = input("Enter the first sequence of strings: ").split(", ")
    input_line2 = input("Enter the second sequence of strings: ").split(", ")

    # Find and print the substrings
    substrings = find_substrings(input_line1, input_line2)
    print("Substrings found in the second sequence:")
    print(substrings)
