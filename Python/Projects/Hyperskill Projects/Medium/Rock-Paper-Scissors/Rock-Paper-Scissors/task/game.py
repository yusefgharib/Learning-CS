import random
class RockPaperScissors:
    def __init__(self):
        self.player_points = 0
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}!')
        with open('rating.txt', 'r') as f:
            for line in f:
                if line.startswith(f'{self.name} '):
                    self.player_points += int(line.strip(f'{self.name} '))
            f.close()
        options = input()
        self.options = ['rock', 'paper', 'scissors']
        self.options = options.split(',') if options != '' else self.options
        print('Okay, let\'s start')

    def game(self):
        while True:
            player_move = input()
            if player_move in self.options:
                computer_move = random.choice(self.options)
                index = self.options.index(player_move)
                new_sort = [options for options in self.options if options != player_move]
                new_sort = new_sort[index:] + new_sort[0: index]
                losses = [new_sort[i] for i in range(round(len(new_sort) / 2), len(new_sort))]
                wins = [new_sort[i] for i in range(round(len(new_sort) / 2))]
                if computer_move == player_move:
                    print(f'There is a draw ({computer_move})')
                    self.player_points += 50
                elif computer_move in wins:
                    print(f'Sorry, but the computer chose {computer_move}')
                elif computer_move in losses:
                    print(f'Well done. The computer chose {computer_move} and failed')
                    self.player_points += 100
            elif player_move == '!exit':
                print('Bye!')
                break
            elif player_move == '!rating':
                print(f'Your rating: {self.player_points}')
            else:
                print('Invalid input')

if __name__ == '__main__':
    g = RockPaperScissors()
    g.game()
