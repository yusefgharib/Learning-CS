import random as r
tasks, right = 5, 0

def operations(choice_):
    global tasks, right
    while tasks > 0:
        if choice_ == '1':
            a, b, operator = r.randint(2, 9), r.randint(2, 9), r.choice(['+', '*', '-'])
            print(str(a), operator, str(b))
        else:
            a, b, operator = r.randint(11, 29), 2, '**'
            print(a)
        while True:
            try:
                answer = int(input())
                if answer == eval(str(a) + operator + str(b)):
                    print('Right!')
                    right += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Incorrect format')
        tasks -= 1
    print(f'Your mark is {right}/5')

while True:
    difficulty = input('Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - '
                       'integral squares of 11-29')
    if difficulty in '12':
        operations(difficulty)
        break
    else:
        print('Incorrect format.')
choice = 'integral squares of 11-29' if difficulty == '2' else 'simple operations with numbers 2-9'
save = input('Would you like to save your result to the file?')
if save.lower() == 'yes' or save.lower() == 'y':
    name = input('What is your name?')
    with open('results.txt', 'a') as output:
        output.write(f'{name.title()}: {right}/5 in level {difficulty} ({choice})')
    print('The results are saved in "results.txt".')
