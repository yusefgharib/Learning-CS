class CoffeeMachine:
    def __init__(self):
        self.money, self.water, self.milk, self.coffee_beans, self.cups = 550, 400, 540, 120, 9
        self.ingredients = {'espresso': {'water': 250, 'milk': 0, 'coffee beans': 16, 'cost': 4},
                            'latte': {'water': 350, 'milk': 75, 'coffee beans': 20, 'cost': 7},
                            'cappuccino': {'water': 200, 'milk': 100, 'coffee beans': 12, 'cost': 6}}
        self.action, self.num, self.coffee_types = '', '', {1: 'espresso', 2: 'latte', 3: 'cappuccino'}

    def remaining(self):
        print(f'The coffee machine has: \n{self.water} ml of water \n{self.milk} ml of milk\n'
              f'{self.coffee_beans} g of coffee beans \n{self.cups} disposable cups \n${self.money} of money\n')

    def start_machine(self):
        self.action = input('Write action (buy, fill, take, remaining, exit)')
        self.process_action()

    def take(self):
        print(f'I gave you {self.money}\n')
        self.money = 0

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:'))
        self.milk += int(input('Write how many ml of milk you want to add:'))
        self.coffee_beans += int(input('Write how many grams of coffee beans you want to add:'))
        self.cups += int(input('Write how many disposable cups you want to add:'))

    def check_ingredients(self):
        if self.water < self.ingredients[self.coffee_types[int(self.num)]]['water']:
            print('Sorry, not enough water')
        elif self.water < self.ingredients[self.coffee_types[int(self.num)]]['milk']:
            print('Sorry, not enough milk')
        elif self.water < self.ingredients[self.coffee_types[int(self.num)]]['coffee beans']:
            print('Sorry, not enough coffee beans')
        else:
            return True

    def buy(self):
        self.num = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if self.num == 'back':
            self.start_machine()
        else:
            if self.check_ingredients():
                print('I have enough resources, making you a coffee')
                self.water -= self.ingredients[self.coffee_types[int(self.num)]]['water']
                self.milk -= self.ingredients[self.coffee_types[int(self.num)]]['milk']
                self.coffee_beans -= self.ingredients[self.coffee_types[int(self.num)]]['coffee beans']
                self.cups -= 1
                self.money += self.ingredients[self.coffee_types[int(self.num)]]['cost']
            else:
                self.start_machine()

    def process_action(self):
        self.buy() if self.action == 'buy' else self.take() if self.action == 'take' else self.fill() if \
            self.action == 'fill' else self.remaining() if self.action == 'remaining' else 0


c = CoffeeMachine()
while True:
    c.start_machine()
    if c.action == 'exit':
        break
