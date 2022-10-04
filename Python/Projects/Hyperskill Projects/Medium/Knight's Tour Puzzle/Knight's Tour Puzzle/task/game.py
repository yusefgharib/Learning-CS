class Knight:
    def __init__(self):
        self.board, self.visited, self.count_possible_moves, self.sol = {}, [], [], None
        self.cols, self.rows, self.placeholder, self.possible_moves, self.border = None, None, None, None, None
        self.legal_moves = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]
        self.setup_board()

    def setup_board(self):
        while True:
            dimensions = input('Enter your board dimensions:')
            if self.validate_positions(dimensions, 'setup'):
                break
        self.cols, self.rows = map(int, dimensions.split())
        self.placeholder = ('_' * len(str(self.cols * self.rows)))
        self.border = '-' * (len(f'| {self.placeholder * self.cols} |') + self.cols - 1)
        for i in range(self.rows, 0, -1):
            for j in range(1, self.cols + 1):
                self.board[i] = {x: self.placeholder for x in range(1, self.cols + 1)}
        self.get_start_pos()

    def get_start_pos(self):
        while True:
            start_pos = input('Enter the knight\'s starting position:')
            if self.validate_positions(start_pos, "start"):
                break
        start_col, start_row = map(int, start_pos.split())
        self.set_pos(start_row, start_col)

    def validate_positions(self, pos, msg):
        if len(pos.split()) == 2:
            try:
                start_col, start_row = map(int, pos.split())
                if msg == 'setup':
                    if start_col > 0 and start_row > 0:
                        return True
                else:
                    if 0 < start_col <= self.cols and 0 < start_row <= self.rows:
                        if msg == 'start':
                            return True
                        else:
                            if [start_col, start_row] in self.possible_moves:
                                return True
            except ValueError:
                pass
        if msg == 'next':
            print('Invalid move!', end=' ')
        elif msg == 'start':
            print('Invalid position!')
        else:
            print('Invalid dimensions!')

    def set_pos(self, row, col):
        self.visited.append([col, row])
        self.board[row][col] = ' X'
        self.get_possible_moves(col, row)
        for c, pair in enumerate(self.possible_moves):
            self.board[pair[1]][pair[0]] = ' ' + str(self.count_possible_moves[c])

    def print_board(self):
        column_nums, c = '', self.rows
        print('', self.border)
        for row in self.board:
            print(f'{c}| ', end='')
            for col in self.board[row]:
                print(self.board[row][col], '', end='')
            print('|')
            c -= 1
        print('', self.border)
        for i in range(1, self.cols + 1):
            column_nums = column_nums + (' ' * len(str(self.cols * self.rows))) + str(i)
        print('  ' * (len(str(self.rows)) * 1), column_nums, sep='')

    def get_next_move(self):
        while True:
            next_pos = input('Enter your next move:')
            if self.validate_positions(next_pos, 'next'):
                break
        start_col, start_row = map(int, next_pos.split())
        for key in self.board:  # clear the board of previous numbers and turn X into *
            for index in self.board[key]:
                for char in self.board[key][index]:
                    if char.isnumeric():
                        self.board[key][index] = self.placeholder
                    elif char == 'X':
                        self.board[key][index] = ' *'
        self.set_pos(start_row, start_col)
        self.print_board()

    def get_possible_moves(self, col, row):
        self.possible_moves, self.count_possible_moves = [], []
        for pair in self.legal_moves:
            if 0 < (col + pair[0]) <= self.cols and 0 < (row + pair[1]) <= self.rows:
                self.possible_moves.append([col + pair[0], row + pair[1]])
        for pair in self.visited:
            if pair in self.possible_moves:
                self.possible_moves.remove(pair)
        for possible in self.possible_moves:
            c = 0
            for pair in self.legal_moves:
                if 0 < (possible[0] + pair[0]) <= self.cols:
                    if 0 < (possible[1] + pair[1]) <= self.rows:
                        if [possible[0] + pair[0], possible[1] + pair[1]] not in self.visited:
                            c += 1
            self.count_possible_moves.append(c)

    def show_solution(self):
        x, column_nums, c = 0, '', self.rows
        print('', self.border)
        for row in self.board:
            y = 0
            print(f'{c}| ', end='')
            for col in self.board[row]:
                if len(str(self.sol[x][y])) == 1:
                    self.board[row][col] = f' {str(self.sol[x][y])}'
                    print(str(self.board[row][col]), '', end='')
                else:
                    self.board[row][col] = str(self.sol[x][y])
                    print(str(self.board[row][col]), '', end='')
                y += 1
            x, c = x + 1, c - 1
            print('|')
        print('', self.border)
        for i in range(1, self.cols + 1):
            column_nums = column_nums + (' ' * len(str(self.cols * self.rows))) + str(i)
        print('  ' * (len(str(self.rows)) * 1), column_nums, sep='')

    def create_solution_board(self):
        self.sol = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        return self.check_solution(self.sol, 0, 0, 0)

    def check_solution(self, board, col, row, counter):
        if counter == self.rows * self.cols:
            return True
        if (col < 0) or (col >= self.cols) or (row < 0) or (row >= self.rows) or board[row][col] != -1:
            return False
        board[row][col] = counter + 1
        for pair in self.legal_moves:
            if self.check_solution(board, col + pair[0], row + pair[1], counter + 1):
                return True
        board[row][col] = -1


k = Knight()
while True:
    choice = input('Do you want to try the puzzle? (y/n):')
    if choice == 'y':
        if k.create_solution_board():
            break
        else:
            print('No solution exists!')
            exit()
    elif choice == 'n':
        if k.create_solution_board():
            print("\nHere's the solution!")
            k.show_solution()
            exit()
        else:
            print('No solution exists!')
            exit()
    else:
        print('Invalid input!')
while k.possible_moves:
    k.get_next_move()
print('What a great tour! Congratulations!' if len(k.visited) == k.cols * k.rows
      else f'No more possible moves!\nYour knight visited {len(k.visited)} squares!')
