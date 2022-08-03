board = [["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"]]

bot_nums = [5, 5, 5, 5, 5, 5, 5]

while True:
    player1 = input("Enter initial of player 1:\n> ")
    if len(player1) > 1 or not player1.isalpha():
        print("Initial should be one letter.")
        continue
    break
while True:
    player2 = input("Enter initial of player 2:\n> ")
    if len(player2) > 1 or not player2.isalpha():
        print("Initial should be one letter.")
        continue
    break

players = [player1, player2]

while True:
    for player in players:
        for row in board:
            print("".join(row))
        print("Enter a column between 1 and 7")
        while True:
            inp_col = (int(input()) - 1)
            if inp_col > 7:
                print("Enter a column between 1 and 7")
                continue
            if bot_nums[inp_col] == -1:
                print("No room left in that column")
                continue
            break
        board[bot_nums[inp_col]][inp_col] = player
        bot_nums[inp_col] -= 1
