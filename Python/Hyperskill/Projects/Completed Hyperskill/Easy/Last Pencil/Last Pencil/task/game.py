name1, name2, bot = "Jack", "John", "Jack"
take_one, take_two, take_three, winning_num = [1, ], [], [], []

num_pencils = input("How many pencils would you like to use?\n")

if num_pencils.isdigit():
    for i in range(5, int(num_pencils) + 1, 4):
        winning_num.append(i)
    for i in range(3, int(num_pencils) + 1, 4):
        take_two.append(i)
    for i in range(2, int(num_pencils) + 1, 4):
        take_one.append(i)
    for i in range(4, int(num_pencils) + 1, 4):
        take_three.append(i)


def numeric():
    global num_pencils
    while not num_pencils.isnumeric():
        num_pencils = input("The number of pencils should be numeric")
        return numeric()
    while int(num_pencils) <= 0:
        num_pencils = input("The number of pencils should be positive")
        return positive()
    return True


def positive():
    global num_pencils
    while not num_pencils.isnumeric():
        num_pencils = input("The number of pencils should be numeric")
        return numeric()
    while int(num_pencils) <= 0:
        num_pencils = input("The number of pencils should be positive")
        return positive()
    return True


def bot_func():
    global take, num_pencils, player
    if int(num_pencils) in take_one and player == bot:
        take = '1'
        print(take)
    if int(num_pencils) in take_two and player == bot:
        take = '2'
        print(take)
    if int(num_pencils) in take_three and player == bot:
        take = '3'
        print(take)
    if int(num_pencils) in winning_num and player == bot:
        take = '2'
        print(take)
    return take


def name():
    global player
    while player == name1 or player == name2:
        return True
    return False


def take_check():
    global take
    while not take.isnumeric():
        take = input("Possible values: '1', '2', or '3'\n")
        return take_check()
    while int(take) > 3 or int(take) < 1:
        take = input("Possible values: '1', '2', or '3'\n")
        return take_check()
    return True


while not numeric():
    num_pencils = input("The number of pencils should be numeric")
while not positive():
    num_pencils = input("The number of pencils should be positive")

player = input("Who will be the first (John, Jack)\n")

while not name():
    player = input(f"Choose between {name1} and {name2}")

while int(num_pencils) > 0:
    print(f"{player}'s turn:")
    print("|" * int(num_pencils))

    if player == "Jack":
        bot_func()
    else:
        take = input()

    while not take_check():
        take = input("Possible values: '1', '2', or '3'\n")
    # noinspection PyUnboundLocalVariable
    while int(take) > int(num_pencils):
        take = input("Too many pencils were taken\n")
    num_pencils = int(num_pencils) - int(take)
    if num_pencils == 0:
        if player == "Jack":
            winner = "John"
            print(f"{winner} won!")
        elif player == "John":
            winner = "Jack"
            print(f"{winner} won!")
    else:
        if player == name1:
            player = name2
        else:
            player = name1
