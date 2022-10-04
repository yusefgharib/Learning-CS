def check_email(string):
    if ' ' in string or '@' not in string or '@.' in string:
        return False
    elif string.find('@') > string.rfind('.'):
        return False
    return True
