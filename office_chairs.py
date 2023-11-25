def check_chairs_in_rooms(n, rooms):
    total_free_chairs = sum(max(0, len(chairs) - visitors) for chairs, visitors in
                            [(room.split()[0], int(room.split()[1])) for room in rooms])

    needed_chairs = [f"{abs(len(chairs) - visitors)} more chairs needed in room {i + 1}" for i, (chairs, visitors) in
                     enumerate([(room.split()[0], int(room.split()[1])) for room in rooms]) if len(chairs) < visitors]

    if not needed_chairs:
        print(f"Game On, {total_free_chairs} free chairs left")
    else:
        for message in needed_chairs:
            print(message)


# Get input from the user
n = int(input())
rooms_info = []

for _ in range(n):
    room_input = input()
    rooms_info.append(room_input)

# Call the function with user input
check_chairs_in_rooms(n, rooms_info)
