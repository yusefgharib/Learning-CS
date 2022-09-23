from operator import add, sub, mul, truediv, floordiv, pow, mod
x, y, op = float(input()), float(input()), input()
zero = ['/', 'div', 'mod']
values = {"+": add, "-": sub, "*": mul, "/": truediv, "mod": mod, "div": floordiv, "pow": pow}
try:
    print(values[op](x, y))
except ZeroDivisionError:
    print("Division by 0!")
