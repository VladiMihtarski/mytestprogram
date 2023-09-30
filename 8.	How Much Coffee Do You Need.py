coffee_count = 0

while True:
    event = input()

    if event == "END":
        break

    if event == "coding" or event == "dog" or event == "cat" or event == "coding" or event == "movie":
        coffee_count += 1
    elif event.isupper():
        coffee_count += 2

if coffee_count <= 5:
    print(coffee_count)
else:
    print("You need extra sleep")
