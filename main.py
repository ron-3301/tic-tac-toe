import itertools

def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if game_map[row][col] != 0:
            print("This space is occupied. Try another!")
            return False
        print("  0  1  2")
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play outside the board (0, 1, 2)?")
        return False

def win(current_game):
    def all_same(l):
        return l.count(l[0]) == len(l) and l[0] != 0

    # Horizontal win
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} wins horizontally!")
            return True

    # Vertical win
    for col in range(len(current_game)):
        check = [current_game[row][col] for row in range(len(current_game))]
        if all_same(check):
            print(f"Player {check[0]} wins vertically!")
            return True

    # Diagonal (\$$
    diags = [current_game[i][i] for i in range(len(current_game))]
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally (\$$!")
        return True

    # Diagonal (/)
    diags = [current_game[i][len(current_game)-1-i] for i in range(len(current_game))]
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally (/)!")
        return True

    return False

# Main game loop
play = True
players = [1, 2]
while play:
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game_won = False
    player_cycle = itertools.cycle(players)
    game_board(game, just_display=True)

    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player {current_player}'s turn")
            col_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player=current_player, row=row_choice, col=col_choice)

        if win(game):
            game_won = True
            again = input("The game is over. Play again? (y/n): ").lower()
            if again == "y":
                print("Restarting...")
            elif again == "n":
                print("Bye!")
                play = False
            else:
                print("Not a valid answer, but cya!")
                play = False   