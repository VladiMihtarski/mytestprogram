def fill_shells(electrons):
    filled_shells = []
    shell_number = 1

    while electrons > 0:
        max_electrons_in_shell = 2 * shell_number**2

        if electrons >= max_electrons_in_shell:
            filled_shells.append(max_electrons_in_shell)
            electrons -= max_electrons_in_shell
        else:
            filled_shells.append(electrons)
            electrons = 0

        shell_number += 1

    return filled_shells

# Get input from the user
electrons = int(input("Enter the number of electrons: "))

# Call the function with user input
result = fill_shells(electrons)

# Print the filled shells
print("Filled shells:", result)
