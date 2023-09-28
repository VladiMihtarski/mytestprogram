n = int(input("Enter the number of strings: "))

for _ in range(n):
    string = input("Enter a string: ")

    if all(char not in string for char in ",._"):
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
