def is_valid_password(password):
    # Rule 1: Check the length
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")

    # Rule 2: Check if it consists only of letters and digits
    if not password.isalnum():
        print("Password must consist only of letters and digits")

    # Rule 3: Check if it has at least 2 digits
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")

    # If all conditions are met, the password is valid
    if 6 <= len(password) <= 10 and password.isalnum() and digit_count >= 2:
        print("Password is valid")

# Example usage:
password_to_check = input("Enter the password: ")
is_valid_password(password_to_check)
