def help_():
    print("""Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list
        Special commands: !help !done""")


def done():
    global text
    with open('output.md', 'w') as output_file:
        output_file.write(text)
    exit()


def plain():
    p = input('Text: >')
    return p


def link():
    label = input('Label: >')
    url = input('URL: >')
    return f'[{label}]({url})'


def bold():
    text_ = input('Text: >')
    return f'**{text_}**'


def italic():
    text_ = input('Text: >')
    return f'*{text_}*'


def inline():
    text_ = input('Text: >')
    return f'`{text_}`'


def header():
    while True:
        level = int(input('Level: >'))
        if 0 < level < 6:
            break
        print('The level should be within the range of 1 to 6')
    text_ = input('Text: >')
    return (level * '#') + f' {text_}\n'


def newline():
    return '\n'


def list_(msg):
    output = ''
    while True:
        rows = int(input('Number of rows : >'))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    elements = [input(f'Row #{i}: >') for i in range(1, rows + 1)]
    if msg == 'ordered':
        for i in range(len(elements)):
            output += f'{i + 1}. {elements[i]}\n'
    elif msg == 'unordered':
        for i in range(len(elements)):
            output += f'* {elements[i]}\n'
    return output


def process(choice_):
    if choice_ == 'header':
        return header()
    if choice_ == 'new-line':
        return newline()
    if choice_ == 'inline-code':
        return inline()
    if choice_ == 'plain':
        return plain()
    if choice_ == 'italic':
        return italic()
    if choice_ == 'link':
        return link()
    if choice_ == 'bold':
        return bold()
    if choice_ == '!help':
        return help_()
    if choice_ == '!done':
        return done()
    if choice_ == 'ordered-list':
        return list_('ordered')
    if choice_ == 'unordered-list':
        return list_('unordered')


text = ''
valid_choices = ['!help', '!done', 'plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list',
                 'ordered-list', 'new-line']
while True:
    choice = input('Choose a formatter: >')
    if choice in valid_choices:
        text += process(choice)
        print(text)
    else:
        print('Unknown formatting type or command')
