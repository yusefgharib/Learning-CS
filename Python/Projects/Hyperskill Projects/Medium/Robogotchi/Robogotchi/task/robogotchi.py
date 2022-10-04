import random
class Robot:
    def __init__(self):
        self.name = input('How will you call your robot?')
        self.overheat, self.skills, self.boredom, self.rust, self.battery = 0, 0, 0, 0, 100
        self.p_wins, self.c_wins, self.draws, self.game, self.choice = 0, 0, 0, '', ''
        self.choice_options = ['exit', 'info', 'recharge', 'sleep', 'play', 'oil', 'learn', 'work']
        self.game_options = ['rock-paper-scissors', 'numbers']
        self.start_menu()

    def start_menu(self):
        self.check_stats()
        print(f'\nAvailable interactions with {self.name}:')
        print('exit - Exit\ninfo - Check the vitals\nwork - Work\nplay - Play\noil - Oil\nrecharge - Recharge\nsleep '
              '- Sleep mode\nlearn - Learn skills')
        self.choice = input('\nChoose:\n').lower()
        self.process_choice()

    def process_choice(self):
        if self.choice not in self.choice_options:
            print('Invalid input, try again!')
            self.start_menu()
        elif self.battery == 0:
            print(f'The level of the battery is 0, {self.name} needs recharging!')
            if self.choice == 'recharge':
                self.recharge()
            elif self.choice == 'info':
                self.info()
            else:
                self.start_menu()
        elif self.boredom == 100:
            print(f'{self.name} is too bored! {self.name} needs to have fun!')
            if self.choice == 'play':
                self.play_menu()
            elif self.choice == 'info':
                self.info()
            else:
                self.start_menu()
        else:
            if self.choice == 'play':
                self.play_menu()
            elif self.choice == 'info':
                self.info()
            elif self.choice == 'recharge':
                self.recharge()
            elif self.choice == 'sleep':
                self.sleep()
            elif self.choice == 'learn':
                self.learn()
            elif self.choice == 'oil':
                self.oil()
            elif self.choice == 'work':
                self.work()
            elif self.choice == 'exit':
                print("Game over")
                exit()

    def info(self):
        print(f'\n{self.name}\'s stats are:'
              f'\nthe battery is {self.battery},'
              f'\noverheat is {self.overheat},'
              f'\nskill level is {self.skills},'
              f'\nboredom is {self.boredom},'
              f'\nrust is {self.rust}.')
        self.start_menu()

    def check_stats(self):
        print(f'{self.name} is in a great mood!') if self.boredom == 0 else None
        self.boredom = (0 if self.boredom < 0 else 100 if self.boredom >= 100 else self.boredom)
        if self.overheat == 100:
            print(f'The level of overheat reached 100, {self.name} has blown up! Game over. Try again?!')
            exit()
        self.overheat = (0 if self.overheat < 0 else 100 if self.overheat >= 100 else self.overheat)
        if self.rust >= 100:
            print(f'\n{self.name} is too rusty! Game over. Try again?')
            exit()

    def play_menu(self):
        game = ''
        while game not in self.game_options:
            game = input('Which game would you like to play?').lower()
            if game not in self.game_options:
                print('Please choose a valid option: Numbers or Rock-paper-scissors?')
        if game == 'numbers':
            self.play_numbers()
        elif game == 'rock-paper-scissors':
            self.play_RPS()

    def play_RPS(self):
        old_bored, old_heat, p_wins, c_wins, draws = self.boredom, self.overheat, 0, 0, 0
        moves = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
        while True:
            computer_move = random.choice(list(moves.keys()))
            player_move = input('What is your move?').lower()
            print(f'The robot chose {computer_move}')
            if player_move in moves:
                if computer_move == player_move:
                    print('It\'s a draw!')
                    draws += 1
                elif computer_move == moves[player_move]:
                    print('The robot won!')
                    c_wins += 1
                else:
                    print('You won!')
                    p_wins += 1
            elif player_move == 'exit game':
                print(f'You won: {p_wins},\nRobot won: {c_wins}, \nDraws: {draws}.')
                if old_heat <= 20:
                    print(f"{self.name}'s level of boredom was {old_bored}. Now it is {0}.")
                    self.boredom = 0
                else:
                    print(f"{self.name}'s level of boredom was {old_bored}. Now it is {old_bored - 20}.")
                    self.boredom -= 20
                print(f"{self.name}'s level of overheat was {old_heat}. Now it is {old_heat + 10}.")
                self.overheat += 10
                self.start_menu()
            else:
                print('No such option! Try again!')

    def play_numbers(self):
        old_bored, old_heat, p_wins, c_wins, draws = self.boredom, self.overheat, 0, 0, 0
        while True:
            num, computer_num = random.randint(0, 1000000), random.randint(0, 1000000)
            player_num = input('What is your number?')
            try:
                if int(player_num) > 1000000:
                    print('Invalid input! The number can\'t be bigger than 1000000.')
                elif int(player_num) < 0:
                    print('The number can\'t be negative!')
                else:
                    player_diff = abs(int(player_num) - num)
                    computer_diff = abs(computer_num - num)
                    print(f'The robot entered the number {computer_num}.\nThe goal number is {num}.')
                    if computer_diff > player_diff:
                        print('You won!')
                        p_wins += 1
                    elif computer_diff == player_diff:
                        print('It\'s a draw!')
                        draws += 1
                    else:
                        print('The robot won!')
                        c_wins += 1
            except ValueError:
                if player_num == 'exit game':
                    print(f'\nYou won: {p_wins},\nRobot won: {c_wins}, \nDraws: {draws}.')
                    if old_heat <= 20:
                        print(f"\n{self.name}'s level of boredom was {old_bored}. Now it is {0}.")
                        self.boredom = 0
                    else:
                        print(f"{self.name}'s level of boredom was {old_bored}. Now it is {old_bored - 20}.")
                        self.boredom -= 20
                    print(f"{self.name}'s level of overheat was {old_heat}. Now it is {old_heat + 10}.")
                    self.overheat += 10
                    self.start_menu()
                else:
                    print('A string is not a valid input!')

    def recharge(self):
        if self.battery == 100:
            print(f'{self.name} is charged!')
        else:
            if self.overheat >= 5:
                print(f"{self.name}'s level of overheat was {self.overheat}. Now it is {self.overheat - 5}.")
                self.overheat -= 5
            else:
                print(f"{self.name}'s level of overheat was {self.overheat}. Now it is {0}.")
                self.overheat = 0
            if self.battery >= 90:
                print(f"{self.name}'s level of the battery was {self.battery}. Now it is {100}.")
                self.battery = 100
            else:
                print(f"{self.name}'s level of the battery was {self.battery}. Now it is {self.battery + 10}.")
                self.battery += 10
            print(f"{self.name}'s level of boredom was {self.boredom}. Now it is {self.boredom + 5}.")
            print(f"{self.name} is recharged!")
            self.overheat -= 5
            self.boredom += 5
        self.start_menu()

    def sleep(self):
        if self.overheat - 20 <= 0:
            print(f"{self.name}'s level of overheat was {self.overheat}. Now it is {0}.")
            print(f"{self.name} cooled off!")
            self.overheat = 0
        else:
            print(f"{self.name} cooled off!")
            print(f"{self.name}'s level of overheat was {self.overheat}. Now it is {self.overheat - 20}.")
            self.overheat -= 20
        if self.overheat == 0:
            print(f"{self.name} is cool!")
            self.start_menu()
        self.start_menu()

    def learn(self):
        og_skill, og_heat, og_bored, og_rust, og_battery = self.skills, self.overheat, self.boredom,\
                                                           self.rust, self.battery
        random_chances = {f'\nOh no, {self.name} stepped into a puddle!': 10,
                          f'\nGuess what! {self.name} fell into the pool!': 50, '': 0}
        keys = []
        for key in random_chances:
            keys.append(key)
        if self.skills == 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            if og_battery - 10 < 10:
                event = keys[1]
            elif 10 <= og_battery - 10 < 30 or og_battery == 30:
                event = keys[0]
            else:
                event = keys[2]
            if event != '':
                print(event)
            self.skills += 10
            self.overheat += 10
            self.battery -= 10
            self.boredom += 5
            self.rust += random_chances[event]
            self.check_stats()
            print(f"\n{self.name}'s level of skill was {og_skill}. Now it is {og_skill + 10}."
                  f"\n{self.name}'s level of overheat was {og_heat}. Now it is {og_heat + 10}."
                  f"\n{self.name}'s level of the battery was {og_battery}. Now it is {og_battery - 10}."
                  f"\n{self.name}'s level of boredom was {og_bored}. Now it is {og_bored + 5}.")
            if event != '':
                print(f"{self.name}'s level of rust was {og_rust}. Now it is {og_rust + random_chances[event]}.")
            print(f"\n{self.name} has become smarter!")
        self.start_menu()

    def oil(self):
        og_rust = self.rust
        if self.rust == 0:
            print(f"{self.name} is fine, no need to oil!")
        elif 0 >= self.rust <= 20:
            self.rust = 0
        else:
            self.rust -= 20
            print(f"{self.name}'s level of rust was {og_rust}. Now it is {self.rust}. {self.name} is less rusty!")
        self.start_menu()

    def work(self):
        og_heat, og_bored, og_rust, og_battery = self.overheat, self.boredom, self.rust, self.battery
        random_chances = {f'\nOh no, {self.name} stepped into a puddle!': 10, f'\nGuess what! {self.name} fell into '
                                                                              f'the pool!': 50, '': 0}
        keys = []
        for key in random_chances:
            keys.append(key)
        if self.skills < 50:
            print(f"{self.name} has got to learn before working!")
        else:
            if og_battery - 10 < 10:
                event = keys[1]
            elif 10 <= (og_battery - 10) < 30 or og_battery == 30:
                event = keys[0]
            else:
                event = keys[2]
            if event != '':
                print(event)
            self.boredom += 10
            self.overheat += 10
            self.battery -= 10
            self.rust += random_chances[event]
            self.check_stats()
            print(f"\n{self.name}'s level of boredom was {og_bored}. Now it is {og_bored + 10}."
                  f"\n{self.name}'s level of overheat was {og_heat}. Now it is {og_heat + 10}."
                  f"\n{self.name}'s level of the battery was {og_battery}. Now it is {og_battery - 10}."
                  f"\n{self.name}'s level of rust was {og_rust}. Now it is {og_rust + random_chances[event]}.")
            print(f"\n{self.name} did well!")
        self.start_menu()
        
robo = Robot()
