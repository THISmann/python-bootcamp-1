board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = {"name": "X", "index": []}
player2 = {"name": "0", "index": []}

res = {
    "res1": [0, 1, 2],
    "res2": [3, 4, 5],
    "res3": [6, 7, 8],
    "res4": [0, 3, 6],
    "res5": [1, 4, 7],
    "res6": [2, 5, 8],
    "res7": [0, 4, 8],
    "res8": [2, 4, 6]
}


def display_board():
    arterist_v = "*"
    print("Welcome to TIC TAC TOE ! \n \n TIC TAC TOE ")
    print(arterist_v*17)
    print(f"* {board[0]} | {board[1]} | {board[2]} *")
    print("*___|___|___*")
    print(f"* {board[3]} | {board[4]} | {board[5]} *")
    print("*___|___|___*")
    print(f"* {board[6]} | {board[7]} | {board[8]} *")
    print("*___|___|___*")
    print(arterist_v*17)


print(display_board())


def player_input(player):
    row = int(input(f"enter a row for {player['name']}:"))
    col = int(input(f"enter a colunm for {player['name']}:"))

    if col == 0 and row == 0:
        board[0] = player['name']
        player['index'].append(0)
    elif col == 1 and row == 0:
        board[1] = player['name']
        player['index'].append(1)
    elif col == 2 and row == 0:
        board[2] = player['name']
        player['index'].append(2)
    elif col == 0 and row == 1:
        board[3] = player['name']
        player['index'].append(3)
    elif col == 1 and row == 1:
        board[4] = player['name']
        player['index'].append(4)
    elif col == 2 and row == 1:
        board[5] = player['name']
        player['index'].append(5)
    elif col == 0 and row == 2:
        board[6] = player['name']
        player['index'].append(6)
    elif col == 1 and row == 2:
        board[7] = player['name']
        player['index'].append(7)
    elif col == 2 and row == 2:
        board[8] = player['name']
        player['index'].append(8)

    print("player1 index", *player1['index'])
    print("player2 index", *player2['index'])


# while flag:
#     if flag:
# player_input(player1)
#         flag = False
#     else:
#         player_input(player2)
#         flag = True


print(display_board())


def check_win():
    flag = True
    if len(player1['index']) or len(player2['index']) > 2:
        for x in res.values():
            if player1['index'] or player2['index'] == x:
                flag = False
                print("win")
            else:
                print("echec")
    while flag:
        player_input(player1)
        player_input(player2)


check_win()
