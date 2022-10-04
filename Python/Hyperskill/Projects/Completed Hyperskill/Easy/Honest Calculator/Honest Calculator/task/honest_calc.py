from operator import add, sub, mul, truediv, pow
M = 0


def is_one_digit(x):
    return -10.0 < x < 10.0 and x.is_integer()


def check(x, y, o):
    msg = ""
    msg += " ... lazy" if is_one_digit(x) and is_one_digit(y) else ""
    msg += " ... very lazy" if (x == 1.0 or y == 1.0) and o == "*" else ""
    msg += " ... very, very lazy" if (x == 0.0 or y == 0.0) and (o in "*+-") else ""
    print("You are" + msg if msg != "" else "")


while True:
    num1, op, num2 = input("Enter an equation").split()
    num1 = float(M) if num1 == 'M' else float(num1)
    num2 = float(M) if num2 == 'M' else float(num2)
    try:
        check(num1, num2, op)
        values = {'+': add, '-': sub, '*': mul, '**': pow}
        result = values[op](num1, num2) if op in '+-*' else truediv(num1, num2)
        print(result)
        initial = input("Do you want to store the result? (y / n):")
        if initial == 'y' and is_one_digit(result):
            a = input("Are you sure? It is only one digit! (y / n)")
            if a == 'y':
                b = input("Don't be silly! It's just one number! Add to the memory? (y / n)")
                if b == 'y':
                    c = input("Last chance! Do you really want to embarrass yourself? (y / n)")
                    if c == 'y':
                        M = result
                    elif c == 'n':
                        M = M
                elif b == 'n':
                    M = M
            elif a == 'n':
                M = M
        elif initial == 'y' and not is_one_digit(result):
            M = result
        elif initial == 'n':
            M = M
        if input("Do you want to continue calculations? (y / n):") == 'n':
            break
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except KeyError:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
