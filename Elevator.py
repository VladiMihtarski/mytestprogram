from math import ceil


def calculate_courses_needed(num_people, elevator_capacity):
    """
       Calculate the number of courses needed to elevate a given number of people
       using an elevator with a specified capacity.

       Args:
           num_people (int): The total number of people to be elevated.
           elevator_capacity (int): The capacity of the elevator.

       Returns:
           int: The number of courses needed (rounded up to the nearest integer).
       """
    courses_needed = ceil(num_people / elevator_capacity)
    return courses_needed


def main():
    num_people = int(input("Enter the number of people: "))
    elevator_capacity = int(input("Enter the elevator capacity: "))

    courses_needed = calculate_courses_needed(num_people, elevator_capacity)

    print(f"Number of courses needed: {courses_needed}")


if __name__ == "__main__":
    main()
