def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  


def new_price():
    ...