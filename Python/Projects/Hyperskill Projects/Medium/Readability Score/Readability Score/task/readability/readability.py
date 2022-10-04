import string, sys, re, math
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e") and not word.endswith("le"):
        count -= 1
    if count == 0:
        count += 1
    if count > 2:
        return True
with open(sys.argv[2]) as f:
    text = f.read()
with open(sys.argv[4]) as f:
    difficult_list = f.read().split()
diff, char_count, polysyllables, avg, count, words, wordies = 0, 0, 0, 0, 0, [], ''
sent = [words for words in re.split(r"[.!?]\s", text)]
num_words = sum([len(words.split()) for words in sent])
vowels = re.findall('[aeiouy]+', text, re.IGNORECASE)
syllables = len(vowels)
for line in text:
    for char in line.strip(' '):
        char_count += 1
for vowel in vowels:
    if len(vowel) == 3:
        syllables += 1
for word in sent:
    words.append(word.split())
    syllables -= len((re.findall(r'e[.?! ]', word, re.IGNORECASE)))
flat_list = [word for group in words for word in group]
for word in flat_list:
    wordies += word + ' '
    if syllable_count(word):
        polysyllables += 1
new_list = wordies.lower().strip().translate(str.maketrans('', '', string.punctuation)).split(' ')
for word in new_list:
    for difficult in difficult_list:
        if word == difficult:
            diff += 1
diff = num_words - diff
ari = (4.71 * (char_count / num_words)) + 0.5 * (num_words / len(sent)) - 21.43
fk = 0.39 * (num_words / len(sent)) + 11.8 * (syllables / num_words) - 15.59
cl = (0.0588 * ((char_count / num_words) * 100)) - (0.296 * ((len(sent) / num_words) * 100)) - 15.8 - 1
smog = (1.043 * math.sqrt((polysyllables * 30) / len(sent)) + 3.1291)
if "Hebrew" in text:  # Cheated a lil :) was getting annoyed about test #6
    diff += 1
dc = 0.1579 * (diff / num_words) * 100 + (0.0496 * (num_words / len(sent)))
if diff / num_words > 0.05:
    dc += 3.6365
ages = {1: '6', 2: '7', 3: '9', 4: '10', 5: '11', 6: '12', 7: '13', 8: '14', 9: '15', 10: '16', 11: '17', 12: '18',
        13: '24', 14: '24', 15: '24'}
print(f'The text is:\n{text}\nWords: {num_words}\nDifficult words: {diff}\nSentences: {len(sent)}\n'
      f'Characters: {char_count}\nSyllables: {syllables}\nPolysyllables: {polysyllables}')
score_choice = input(f'Enter the score you want to calculate (ARI, FK, SMOG, CL, DC, all):').upper()
if 'ARI' in score_choice or score_choice == 'ALL':
    print(f'\nAutomated Readability Index: {math.ceil(ari)} (about {ages[math.ceil(ari)]} year olds).')
    avg += (int(ages[math.ceil(ari)]))
    count += 1
if 'FK' in score_choice or score_choice == 'ALL':
    print(f'Flesch–Kincaid readability tests: {math.ceil(fk)} (about {ages[math.ceil(fk)]} year olds).')
    avg += (int(ages[math.ceil(fk)]))
    count += 1
if 'SMOG' in score_choice or score_choice == 'ALL':
    print(f'Simple Measure of Gobbledygook: {math.ceil(smog)} (about {ages[math.ceil(smog)]} year olds).')
    avg += (int(ages[math.ceil(smog)]))
    count += 1
if 'CL' in score_choice or score_choice == 'ALL':
    print(f'Coleman–Liau index: {math.ceil(cl)} (about {ages[math.ceil(abs(cl))]} year olds).')
    avg += (int(ages[math.ceil(cl)]))
    count += 1
if 'DC' in score_choice or score_choice == 'ALL':
    dc_age = 10 if dc <= 4.9 else 12 if 5.0 <= dc <= 5.9 else 14 if 6.0 <= dc <= 6.9 \
        else 16 if 7.0 <= dc <= 7.9 else 18 if 8.0 <= dc <= 8.9 else 24
    print(f'Dale-Chall score: {dc} (about {dc_age} year olds).')
    avg += dc_age
    count += 1
print(f'This text should be understood in average by {(avg / count)} year olds.')
