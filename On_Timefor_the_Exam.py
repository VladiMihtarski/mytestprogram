def get_valid_hour(prompt):
    while True:
        try:
            hour = int(input(prompt))
            if 0 <= hour <= 23:  # Ограничаване на часовете от 0 до 23
                return hour
            else:
                print("Моля, въведете валидно число за час (от 0 до 23).")
        except ValueError:
            print("Моля, въведете валидно цяло число.")

def get_valid_minute(prompt):
    while True:
        try:
            minute = int(input(prompt))
            if 0 <= minute <= 59:  # Ограничаване на минутите от 0 до 59
                return minute
            else:
                print("Моля, въведете валидно число за минути (от 0 до 59).")
        except ValueError:
            print("Моля, въведете валидно цяло число.")

def exam(hour, min, hour_arrival, min_arrival):
    exam_time = hour * 60 + min
    arrival_time = hour_arrival * 60 + min_arrival
    difference = arrival_time - exam_time

    if difference > 0:
        if difference < 60:
            print("Late")
            print(f"{difference} minutes after the start")
        else:
            hours = difference // 60
            minutes = difference % 60
            print("Late")
            print(f"{hours}:{minutes:02d} hours after the start")
    elif difference == 0:
        print("On time")
    elif difference >= -30:
        print("On time")
        print(f"{abs(difference)} minutes before the start")
    elif difference > -60:
        print("Early")
        print(f"{abs(difference)} minutes before the start")
    else:
        hours = abs(difference) // 60
        minutes = abs(difference) % 60
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")

# Валидиране на входовете
input_hour = get_valid_hour("Въведете час на изпита: ")
input_min = get_valid_minute("Въведете минути на изпита: ")
input_hour_arrival = get_valid_hour("Въведете час на пристигане: ")
input_min_arrival = get_valid_minute("Въведете минути на пристигане: ")

# Изпълнение на функцията
exam(input_hour, input_min, input_hour_arrival, input_min_arrival)
