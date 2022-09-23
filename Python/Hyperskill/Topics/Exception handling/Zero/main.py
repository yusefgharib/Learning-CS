n, denominator = int(input()), int(input())
try:
    print(n // denominator)
except ZeroDivisionError:
    print("Division by zero is not supported")
