# Първо приемаме и обработваме списъка с подаръци
gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    tokens = command.split()
    action = tokens[0]

    if action == "OutOfStock":
        gift_to_remove = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = "None"
    elif action == "Required":
        gift = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gifts[-1] = tokens[1]

# Филтрираме подаръците, за да премахнем "None" стойностите
filtered_gifts = [gift for gift in gifts if gift != "None"]

# Принтираме филтрираните подаръци
print(" ".join(filtered_gifts))
