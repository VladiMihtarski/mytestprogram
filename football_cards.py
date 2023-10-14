# Функция за решаване на задачата
def count_players(cards):
    team_a_players = set(range(1, 12))
    team_b_players = set(range(1, 12))
    game_over = False

    for card in cards:
        team, player_number = card.split("-")
        player_number = int(player_number)

        if team == "A" and player_number in team_a_players:
            team_a_players.remove(player_number)
        elif team == "B" and player_number in team_b_players:
            team_b_players.remove(player_number)

        if len(team_a_players) < 7 or len(team_b_players) < 7:
            game_over = True
            break

    print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")

    if game_over:
        print("Game was terminated")

# Основна част на програмата
if __name__ == "__main__":
    cards_input = input("Въведете последователност от карти: ")
    cards = cards_input.split()

    count_players(cards)
