def calculate_snowball_value(weight, time, quality):
    """
    Calculate the value of a snowball using the given weight, time, and quality.

    Args:
        weight (int): The weight of the snowball.
        time (int): The time needed for the snowball to get to its target.
        quality (int): The quality of the snowball.

    Returns:
        float: The calculated snowball value.
    """
    return (weight / time) ** quality


def main():
    # Read the number of snowballs
    n = int(input())

    highest_value = -1  # Initialize with a value lower than any possible snowball value

    # Iterate through each snowball
    for _ in range(n):
        weight = int(input())
        time = int(input())
        quality = int(input())

        # Calculate the value of the current snowball
        snowball_value = calculate_snowball_value(weight, time, quality)

        # Update the highest value if necessary
        if snowball_value > highest_value:
            highest_value = snowball_value
            best_weight = weight
            best_time = time
            best_quality = quality

    # Print the details of the snowball with the highest value
    print(f"{best_weight} : {best_time} = {highest_value:.0f} ({best_quality})")


if __name__ == "__main__":
    main()
