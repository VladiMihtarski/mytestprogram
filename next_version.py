def increment_version(version):
    # Split the version string into individual numbers
    n1, n2, n3 = map(int, version.split('.'))

    # Increment the third number
    n3 += 1

    # Check if n3 exceeds 9
    if n3 > 9:
        n3 = 0
        n2 += 1

    # Check if n2 exceeds 9
    if n2 > 9:
        n2 = 0
        n1 += 1

    # Format the result and return
    result = f"{n1}.{n2}.{n3}"
    return result


# Example usage:
if __name__ == "__main__":
    current_version = input("Enter the current version (in the format {n1}.{n2}.{n3}): ")

    try:
        next_version = increment_version(current_version)
        print("Next version:", next_version)
    except ValueError:
        print("Invalid version format. Please enter the version in the format {n1}.{n2}.{n3}.")
