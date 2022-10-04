import random


class Dominos:
    dominos = [[i, j] for i in range(7) for j in range(i, 7)]

    def __init__(self):
        self.player_hand, self.computer_hand, self.stock_dominos = [], [], []
        self.snake, self.current_player = [[0, 0]], ''
        self.header = '=' * 70

    def set_hands(self):
        random.shuffle(self.dominos)
        self.computer_hand = self.dominos[:7]
        self.player_hand = self.dominos[7:14]
        self.stock_dominos = self.dominos[14:]

    def get_action(self):
        if self.current_player == 'player':
            try:
                action = int(input())
                if abs(action) < 0 or abs(action) > len(self.player_hand):
                    raise ValueError()
                if action == 0:
                    if len(self.stock_dominos) > 0:
                        self.player_hand.append(random.choice(self.stock_dominos))
                        self.stock_dominos.remove(self.player_hand[-1])
                else:
                    if 0 < action <= len(self.player_hand):
                        if self.player_hand[action - 1][0] == self.snake[-1][1]:
                            self.snake.extend([self.player_hand[action - 1]])
                        elif self.player_hand[action - 1][1] == self.snake[-1][1]:
                            self.snake.extend(reversed([self.player_hand[action - 1]]))
                        else:
                            raise AssertionError
                    elif action < 0 and abs(action) <= len(self.player_hand):
                        if self.player_hand[abs(action) - 1][1] == self.snake[0][0]:
                            self.snake = ([self.player_hand[abs(action) - 1]]) + self.snake
                        elif self.player_hand[abs(action) - 1][0] == self.snake[0][0]:
                            self.snake = (list([self.player_hand[abs(action) - 1][::-1]])) + self.snake
                        else:
                            raise AssertionError
                    self.player_hand.remove(self.player_hand[abs(action) - 1])
                self.current_player = 'computer'
                return self.return_round()
            except ValueError:
                print('Invalid input. Please try again.')
            except AssertionError:
                print('Illegal move. Please try again')
            return self.get_action()
        elif self.current_player == 'computer':
            available_moves = []
            action = None
            for pair in self.computer_hand:
                if self.snake[0][0] in pair or self.snake[-1][1] in pair:
                    available_moves.append(pair)
            if available_moves:
                scores = []
                for pair in self.snake:
                    for num in pair:

            if action is not None:
                if action[0] == self.snake[-1][1]:
                    self.snake.extend([action])
                elif action[1] == self.snake[-1][1]:
                    self.snake.extend([action[::-1]])
                elif action[1] == self.snake[0][0]:
                    self.snake = [action] + self.snake
                elif action[0] == self.snake[0][0]:
                    self.snake = [action[::-1]] + self.snake
                self.computer_hand.remove(action)
            else:
                if self.stock_dominos:
                    self.computer_hand.append(random.choice(self.stock_dominos))
                    self.stock_dominos.remove(self.computer_hand[-1])
            self.current_player = 'player'
            return self.return_round()

    def determine_first_player(self):
        for pair1, pair2 in zip(self.player_hand, self.computer_hand):
            self.snake[0] = pair1 if sum(pair1) > sum(self.snake[0]) else self.snake[0]
            self.snake[0] = pair2 if sum(pair2) > sum(self.snake[0]) else self.snake[0]
        if self.snake[0] in self.player_hand:
            self.player_hand.remove(self.snake[0])
            self.current_player = 'computer'
        else:
            self.computer_hand.remove(self.snake[0])
            self.current_player = 'player'

    def check_draw(self):
        count = 0
        if self.snake[0][0] == self.snake[-1][1]:
            for pair in self.snake:
                count += pair.count(self.snake[0][0])
        return True if count > 7 else False

    def return_round(self):
        print(f'{self.header}')
        print(f'Stock size: {len(self.stock_dominos)}')
        print(f'Computer pieces: {len(self.computer_hand)}')
        if len(self.snake) <= 6:
            print('\n', *self.snake, '\n', sep='')
        else:
            print('\n', *self.snake[0:3], '...', *self.snake[-3:], '\n', sep='')
        print('Your pieces:')
        if self.player_hand:
            for i, piece in enumerate(self.player_hand):
                print(f'{i + 1}:{piece}')
        if len(self.player_hand) == 0:
            print('\nStatus: The game is over. You won!')
            exit()
        if len(self.computer_hand) == 0:
            print('\nStatus: The game is over. The computer won!')
            exit()
        if len(self.stock_dominos) == 0:
            if self.check_draw():
                print('\nStatus: The game is over. It\'s a draw!')
                exit()
        if self.current_player == 'computer':
            input('\nStatus: Computer is about to make a move. Press Enter to continue...')
        elif self.current_player == 'player':
            print('\nStatus: It\'s your turn to make a move. Enter your command.')
        return self.get_action()


game = Dominos()
game.set_hands()
game.determine_first_player()
game.return_round()
