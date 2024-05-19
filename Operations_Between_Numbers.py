def mathematical_function(N1, N2, operator):
    if operator == "+":
        result = N1 + N2
        if result % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        print(f"{N1} {operator} {N2} = {result} - {parity}")

    elif operator == "-":
        result = N1 - N2
        if result % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        print(f"{N1} {operator} {N2} = {result} - {parity}")

    elif operator == "*":
        result = N1 * N2
        if result % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        print(f"{N1} {operator} {N2} = {result} - {parity}")

    elif operator == "/":
        if N2 == 0:
            print(f"Cannot divide {N1} by zero")
        else:
            result = N1 / N2
            print(f"{N1} / {N2} = {result:.2f}")

    elif operator == "%":
        if N2 == 0:
            print(f"Cannot divide {N1} by zero")
        else:
            result = N1 % N2
            print(f"{N1} % {N2} = {result}")

    else:
        print("Invalid operator")


input_N1 = int(input())
input_N2 = int(input())
input_operator = input()
mathematical_function(input_N1, input_N2, input_operator)
