def bakery_rush(events, initial_energy=100, initial_coins=100):
    current_energy = initial_energy
    current_coins = initial_coins

    events_list = events.split("|")
    completed_day = True

    for event in events_list:
        event_info = event.split("-")
        event_name = event_info[0]
        event_value = int(event_info[1])

        if event_name == "rest":
            gained_energy = min(100 - current_energy, event_value)
            current_energy = min(100, current_energy + gained_energy)
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {current_energy}.")
        elif event_name == "order":
            if current_energy >= 30:
                current_energy -= 30
                current_coins += event_value
                print(f"You earned {event_value} coins.")
            else:
                current_energy += 50
                print("You had to rest!")
                if current_energy >= 100:
                    print(f"Current energy: {current_energy}.")
        else:
            if current_coins >= event_value:
                current_coins -= event_value
                print(f"You bought {event_name}.")
            else:
                print(f"Closed! Cannot afford {event_name}.")
                completed_day = False
                break

    if completed_day and current_energy >= 0:
        print("Day completed!")
        print(f"Coins: {current_coins}")
        print(f"Energy: {current_energy}")
    elif not completed_day:
        pass
    else:
        print("You are out of energy. Day has ended.")

# Четем вход от потребителя
events_input = input()

bakery_rush(events_input)
