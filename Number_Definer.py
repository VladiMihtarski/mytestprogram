number = float(input())

if number == 0:
    print("zero")
else:
    # Initialize the label for positivity/negativity
    sign_label = "positive" if number > 0 else "negative"

    # Initialize the label for size
    size_label = "small" if abs(number) < 1 else "large" if abs(number) > 1000000 else ""

    # Format and print the output
    output = f"{size_label} {sign_label}" if size_label else f"{sign_label}"
    print(output)
