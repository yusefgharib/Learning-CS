import copy
import random


class TicTacToe:
    def __init__(self):
        self.other_player = None
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.x, self.y, self.status, self.player = None, None, "Game not finished", "X"

    def get_player_move(self):
        while True:
            try:
                self.x, self.y = map(int, input("Enter the coordinates:").split())
                assert 0 < self.x < 4 and 0 < self.y < 4
                self.x, self.y = self.x - 1, self.y - 1
                if self.board[self.x][self.y] == " ":
                    break
                print("This cell is occupied! Choose another one!")
            except AssertionError:
                print("Coordinates should be from 1 to 3!")
            except (IndexError, ValueError, TypeError):
                print("You should enter numbers!")
        self.set_move()

    def get_available_moves(self, board):
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        return available_moves

    def minimax(self, board, maximizing):
        status = self.temp_check_win(board)
        if status is not None:
            if self.player in status:
                return -1, None
            if self.other_player in status:
                return 1, None
            if status == "Draw":
                return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_squares = self.get_available_moves(board)
            for (row, col) in empty_squares:
                # temp_board = copy.deepcopy(self.board)
                board = self.temp_set_move(board, self.other_player, row, col)
                eval_ = self.minimax(board, False)[0]
                if eval_ > max_eval:
                    max_eval = eval_
                    best_move = (row, col)
            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_squares = self.get_available_moves(board)
            for (row, col) in empty_squares:

                board = self.temp_set_move(board, self.player, row, col)
                eval_ = self.minimax(board, True)[0]
                if eval_ < min_eval:
                    min_eval = eval_
                    best_move = (row, col)
            return min_eval, best_move

    def get_comp_move(self, level):
        self.other_player = "X" if self.player == "O" else "O"
        d1_items = [self.board[0][0], self.board[1][1], self.board[2][2]]
        d1_points = [(0, 0), (1, 1), (2, 2)]
        d2_items = [self.board[0][2], self.board[1][1], self.board[2][0]]
        d2_points = [(0, 2), (1, 1), (2, 0)]
        winning_moves = [(i, j) for i, row in enumerate(self.board)
                         for j, point in enumerate(row)
                         if row.count(self.player) == 2 and point == " "]
        blocking_moves = [(i, j) for i, row in enumerate(self.board)
                          for j, point in enumerate(row)
                          if row.count(self.other_player) == 2 and point == " "]
        for i in range(3):
            if [self.board[0][i], self.board[1][i], self.board[2][i]].count(self.player) == 2:
                for j in range(3):
                    if self.board[j][i] == " ":
                        winning_moves.append((j, i))
            elif [self.board[0][i], self.board[1][i], self.board[2][i]].count(self.other_player) == 2:
                for j in range(3):
                    if self.board[j][i] == " ":
                        blocking_moves.append((j, i))
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        if level == "hard":
            temp_board = copy.deepcopy(self.board)
            eva, move = self.minimax(temp_board, False)
            self.x, self.y = move
            print(eva)

        if level in ["medium", "hard"]:
            if len(winning_moves) > 0:
                self.x, self.y = winning_moves[0]
            elif d1_items.count(" ") == 1 and d1_items.count(self.player) == 2:
                self.x, self.y = d1_points[d1_items.index(" ")]
            elif d2_items.count(" ") == 1 and d2_items.count(self.player) == 2:
                self.x, self.y = d2_points[d2_items.index(" ")]
            elif len(blocking_moves) > 0:
                self.x, self.y = blocking_moves[0]
            elif d1_items.count(" ") == 1 and d1_items.count(self.other_player) == 2:
                self.x, self.y = d1_points[d1_items.index(" ")]
            elif d2_items.count(" ") == 1 and d2_items.count(self.other_player) == 2:
                self.x, self.y = d2_points[d2_items.index(" ")]
            else:
                if level != "hard":
                    self.x, self.y = available_moves[random.randint(0, len(available_moves) - 1)]
                else:
                    self.x, self.y = random.choice(available_moves)
        else:
            self.x, self.y = random.choice(available_moves)
        print(f'Making move level "{level}"')
        self.set_move()

    def temp_set_move(self, board, player, x, y):
        board[x][y] = "X" if player == "X" else "O"
        return board

    def set_move(self):
        self.board[self.x][self.y] = "X" if self.player == "X" else "O"
        self.player = "O" if self.player == "X" else "X"
        self.print_board()

    def print_board(self):
        print(f"---------\n"
              f"| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} |\n"
              f"| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} |\n"
              f"| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} |\n"
              f"---------")
        self.check_win()

    def temp_check_win(self, board):
        status = None
        space_count = sum(row.count(" ") for row in board)
        if board[0][2] == board[1][1] == board[2][0] and board[1][1] != " ":
            status = f"{board[1][1]} wins"
        elif board[0][0] == board[1][1] == board[2][2] and board[1][1] != " ":
            status = f"{board[1][1]} wins"
        for i in range(3):
            if board[i].count("X") == 3 or board[i].count("O") == 3:
                status = f"{board[i][0]} wins"
            elif (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != " "):
                status = f"{board[0][i]} wins"
        return status

    def check_win(self):
        space_count = sum(row.count(" ") for row in self.board)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != " ":
            self.status = f"{self.board[1][1]} wins"
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != " ":
            self.status = f"{self.board[1][1]} wins"
        for i in range(3):
            if self.board[i].count("X") == 3 or self.board[i].count("O") == 3:
                self.status = f"{self.board[i][0]} wins"
            elif (self.board[0][i] == self.board[1][i] == self.board[2][i]) and (self.board[0][i] != " "):
                self.status = f"{self.board[0][i]} wins"
        if not space_count and self.status == "Game not finished":
            self.status = "Draw"
        if self.status != "Game not finished":
            print(self.status)
            exit()
        return False


while True:
    choice = input("Input command:").split()
    if "exit" in choice:
        exit()
    elif len(choice) == 3:
        if choice[0] == "start":
            if choice[1] in ["easy", "medium", "hard", "user"] and choice[2] in ["easy", "medium", "hard", "user"]:
                break
    print("Bad parameters!")
t = TicTacToe()
t.print_board()
while not t.check_win():
    t.get_player_move() if choice[1] == "user" else t.get_comp_move(choice[1])
    t.get_player_move() if choice[2] == "user" else t.get_comp_move(choice[2])
