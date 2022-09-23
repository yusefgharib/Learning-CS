import random


class BillSplitter:

    def __init__(self):
        self.bill = 0
        self.num_people = int(input('Enter the number of friends joining (including you):'))
        if self.num_people > 0:
            print('\nEnter the name of every friend (including you), each on a new line:')
            self.names = {input(): 0 for _ in range(self.num_people)}
            self.split_bill()
        else:
            print('\nNo one is joining for the party')

    def random_lucky(self):
        yes_no = input('\nDo you want to use the "Who is lucky" feature? Write Yes/No')
        lucky = random.choice(list(self.names.keys()))
        if yes_no == 'Yes':
            print(f'\n{lucky} is the lucky one!')
            self.names[lucky] = 0
            for name in self.names:
                if name != lucky:
                    self.names[name] = round(self.bill / (self.num_people - 1), 2)
            print(self.names)
        else:
            print('\nNo one is going to be lucky', self.names, sep='\n')


    def split_bill(self):
        self.bill = int(input('\nEnter the total bill value:'))
        self.names = {name: round(self.bill / self.num_people, 2) for name in self.names}
        self.random_lucky()


if __name__ == '__main__':
    b = BillSplitter()
