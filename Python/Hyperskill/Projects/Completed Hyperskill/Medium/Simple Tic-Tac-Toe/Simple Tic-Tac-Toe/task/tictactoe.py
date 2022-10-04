player1, player2, game = 'X', 'O', ' ' * 9
player = player1
def field(board):
    print('---------')
    for i in range(0, len(board), 3):
        print('|', board[i], board[i + 1], board[i + 2], '|')
    print('---------')

def win_check(board):
    for i in range(0, len(board), 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
            return True
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            return True
    for i in range(0, 1):
        if board[i] == board[i + 4] == board[i + 8] and board[i] != ' ':
            return True
    for i in range(2, 3):
        if board[i] == board[i + 2] == board[i + 4] and board[i] != ' ':
            return True

field(game)
while True:
    if not win_check(game) and game.count(' ') == 0:
        print('Draw')
        break
    cell1, cell2 = input().split()
    index = int(cell1) - 1 + int(cell2) - 1 + (2 * (int(cell1) - 1))
    if (cell1.isdigit() and cell2.isdigit()) and (0 < int(cell1) < 4 and 0 < int(cell2) < 4):
        if game[index] == 'X' or game[index] == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            if player == player1:
                game = game[: index] + player1 + game[index + 1:]
                field(game)
                if win_check(game):
                  print(f'{player} wins')
                  break
                player = player2
            elif player == player2:
                game = game[: index] + player2 + game[index + 1:]
                field(game)
                if win_check(game):
                  print(f'{player} wins')
                  break
                player = player1
    elif 1 < int(cell1) > 3 or 1 < int(cell2) > 3:
        print("Coordinates should be from 1 to 3!")
    elif not cell1.isdigit() and not cell2.isdigit():
        print("You should enter numbers!")
