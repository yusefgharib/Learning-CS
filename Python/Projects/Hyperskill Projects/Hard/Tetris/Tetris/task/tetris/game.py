from collections import defaultdict
import numpy as np


class Board:
    def __init__(self, col, row):
        self.col, self.row = col, row
        self.grid = np.array([['-' for i in range(self.col)] for _ in range(self.row)])
        self.pieces_on_board = defaultdict(list)
        self.print_grid()

    def print_grid(self):
        print()
        for i in range(self.row):
            print(*self.grid[i])

    def clear_bottom(self, piece_):
        full = np.all(self.grid[self.row - 1] == '0')
        while full:
            prev_items = self.pieces_on_board
            self.pieces_on_board = defaultdict(list)
            for key in prev_items:
                for l in prev_items[key]:
                    self.pieces_on_board[key].append([[i[0] + 1, i[1]] for i in l if i[0] != self.row - 1])
            piece_.current_position = [[]]
            self.update(piece_)
            full = np.all(self.grid[self.row - 1] == '0')

    def game_over(self):
        for x in range(self.col):
            column = [self.grid[y, x] for y in range(self.row)]
            if '-' not in column:
                self.print_grid()
                print("\nGame Over!")
                exit()

    def update(self, piece_):
        self.grid = np.array([['-' for i in range(self.col)] for _ in range(self.row)])
        if self.pieces_on_board:
            for val in self.pieces_on_board.values():
                for l in val:
                    for point in l:
                        x, y = point[0], point[1]
                        self.grid[x, y] = '0'
        for point in piece_.current_position:
            if not point:
                return
            x, y = point[0], point[1]
            self.grid[x, y] = '0'
        x_mx, y_mx = max(piece_.current_position, key=lambda item: item[0])
        for point in piece_.current_position:
            x, y = point[0], point[1]
            if x == self.row - 1 or (x_mx < self.row - 1 and self.grid[x_mx + 1][y_mx] == '0'):
                self.pieces_on_board[piece_.letter].append(piece_.current_position)
                self.print_grid()
                return False
        return True


class Piece:
    def __init__(self, letter):
        pieces = {'O': [[[0, 4], [0, 5], [1, 4], [1, 5]]],
                  'I': [[[0, 4], [1, 4], [2, 4], [3, 4]], [[0, 3], [0, 4], [0, 5], [0, 6]]],
                  'S': [[[0, 4], [0, 5], [1, 4], [1, 3]], [[0, 4], [1, 4], [1, 5], [2, 5]]],
                  'Z': [[[0, 4], [0, 5], [1, 5], [1, 6]], [[0, 5], [1, 5], [1, 4], [2, 4]]],
                  'L': [[[0, 4], [1, 4], [2, 4], [2, 5]], [[0, 5], [1, 5], [1, 4], [1, 3]],
                        [[0, 4], [0, 5], [1, 5], [2, 5]], [[0, 4], [0, 5], [0, 6], [1, 4]]],
                  'J': [[[0, 5], [1, 5], [2, 5], [2, 4]], [[1, 5], [0, 5], [0, 4], [0, 3]],
                        [[0, 5], [0, 4], [1, 4], [2, 4]], [[0, 4], [1, 4], [1, 5], [1, 6]]],
                  'T': [[[0, 4], [1, 4], [2, 4], [1, 5]], [[0, 4], [1, 3], [1, 4], [1, 5]],
                        [[0, 5], [1, 5], [2, 5], [1, 4]], [[0, 4], [0, 5], [0, 6], [1, 5]]]}
        self.letter = letter
        self.current_piece, self.rotation = pieces[letter], 0
        self.current_position = self.current_piece[self.rotation]

    def change_position(self, action):
        for rotation in self.current_piece:
            for point in rotation:
                point[0] += 1
        if action == 'rotate':
            self.rotation += 1
            if self.rotation > len(self.current_piece) - 1:
                self.rotation = 0
            self.current_position = self.current_piece[self.rotation]
        if action == 'right':
            for point in self.current_position:
                if point[1] == board.col - 1:
                    return
            for rotation in self.current_piece:
                for point in rotation:
                    point[1] += 1
        if action == 'left':
            for point in self.current_position:
                if point[1] == 0:
                    return
            for rotation in self.current_piece:
                for point in rotation:
                    point[1] -= 1


col, row = map(int, input().split())
board = Board(col, row)
while choice := input() != 'piece':
    board.print_grid()
    choice = input()
piece = Piece(input())
while True:
    board.game_over()
    while board.update(piece):
        board.print_grid()
        choice = input()
        if choice == 'exit':
            exit()
        piece.change_position(choice)
    choice = input()
    if choice == 'exit':
        exit()
    if choice == 'break':
        board.clear_bottom(piece)
        board.print_grid()
    if choice == 'piece':
        piece = Piece(input())
    continue

