def faro_shuffle(cards, num_shuffles):
    length = len(cards)
    for _ in range(num_shuffles):
        half = length // 2
        shuffled_deck = []

        for i in range(half):
            shuffled_deck.append(cards[i])
            shuffled_deck.append(cards[i + half])

        cards = shuffled_deck  # Обновяваме тестето след разбъркването

    return cards

if __name__ == "__main__":
    cards_input = input("Въведете карти, разделени с интервал: ")
    cards = cards_input.split()
    num_shuffles = int(input("Въведете броя на фаро разбъркванията: "))

    result = faro_shuffle(cards, num_shuffles)
    print(result)
