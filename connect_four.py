import numpy as np


def present():
    global board
    print(str(board).replace(' [', '').replace('[', '').replace(']', '').replace("'", ""))


while True:
    board = np.array(
        [["-", "-", "-", "-", "-", "-",],
         ["-", "-", "-", "-", "-", "-",],
         ["-", "-", "-", "-", "-", "-",],
         ["-", "-", "-", "-", "-", "-",],
         ["-", "-", "-", "-", "-", "-",],
         ["-", "-", "-", "-", "-", "-",]]
    )

    bottom_row = [0, 0, 0, 0, 0, 0]

    players = ("X", "O")
    winner = None
    game_over = False

    present()
    while True:
        for player in players:
            four_in_a_row = []
            for i in range(4):
                four_in_a_row.append(player)
            four_in_a_row = "".join(four_in_a_row)
            if bottom_row == [6, 6, 6, 6, 6, 6]:
                game_over = True
                break
            while True:
                move = int(input(f"\n{player}'s turn: "))
                if bottom_row[move - 1] >= 6:
                    print("That column is full. Please try again.")
                else:
                    break
            board[5 - bottom_row[move - 1]][move - 1] = player        
            present()
            for row in board:
                if four_in_a_row in "".join(row):
                    winner = player
                    game_over = True
                    break
            columns = []
            for i in range(len(board)):
                columns.append(board[:, i])
            for col in columns:
                if four_in_a_row in "".join(col):
                    winner = player
                    game_over = True
                    break
            asc_diags = []
            for idx, space in np.ndenumerate(board):
                asc_diag_chunk = []
                for i in range(4):
                    try:
                        asc_diag_chunk.append(board[idx[0] - i][idx[1] + i])
                    except IndexError:
                        asc_diag_chunk.append("-")
                asc_diags.append(asc_diag_chunk)
            for diag in asc_diags:
                if four_in_a_row in "".join(diag):
                    winner = player
                    game_over = True
                    break
            desc_diags = []
            for idx, space in np.ndenumerate(board):
                desc_diag_chunk = []
                for i in range(4):
                    try:
                        desc_diag_chunk.append(board[idx[0] + i][idx[1] + i])
                    except IndexError:
                        desc_diag_chunk.append("-")
                desc_diags.append(desc_diag_chunk)
            for diag in desc_diags:
                if four_in_a_row in "".join(diag):
                    winner = player
                    game_over = True
                    break
            bottom_row[move - 1] += 1
            if winner is None:
                continue
            else:
                break
        if game_over is True:
            break
    if winner is None:
        print("\nDraw!")
    else:
        print(f"\n{winner} wins!")
    new_game = input("Play again? y/n ")
    if new_game == "y":
        continue
    else:
        break

