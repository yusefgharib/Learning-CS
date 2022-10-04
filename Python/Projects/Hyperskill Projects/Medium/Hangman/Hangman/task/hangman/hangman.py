import random
words, guesses, lives, wins, losses = ['python', 'java', 'swift', 'javascript'], [], 8, 0, 0
rand_word, menu = random.choice(words), 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
hint, tmp = '-' * len(rand_word), rand_word
print('H A N G M A N\n')
user = input(menu)
while True:
    if user == 'results':
        user = input(f'You won: {wins} times \nYou lost: {losses} times\n' + menu)
    if user == 'play':
        rand_word = random.choice(words)
        hint, tmp, guesses, lives = '-' * len(rand_word), rand_word, [], 8
        user = ''
    if user == 'exit':
        break
    letter = input(f'{hint}\nInput a letter: ')
    if len(letter) > 1 or len(letter) == 0:
        print("Please, input a single letter.")
    elif letter.isupper() or not letter.isalpha():
        print("Please, enter a lowercase letter from the English alphabet.")
    else:
        if letter in rand_word:
            for i in range(len(rand_word)):
                if rand_word[i] == letter:
                    hint = hint[:i] + letter + hint[i + 1:]
                    rand_word = rand_word.replace(letter, ' ', 1)
        elif letter in guesses:
            print("You've already guessed this letter.")
        if letter not in tmp:
            print("That letter doesn't appear in the word")
            lives -= 1
        guesses.append(letter)
        if lives == 0:
            losses += 1
            user = input('You lost!\n' + menu)
        elif hint in words:
            wins += 1
            user = input(f'You survived!\nYou guessed the word {hint}!\n' + menu)
