while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue

    repeated_string = ""
    for character in string:
        repeated_string += character * 2

    print(repeated_string)
