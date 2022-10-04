from math import ceil, log, pow, floor
import argparse

parser = argparse.ArgumentParser(description='Choose the calculation')
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
choice = args.type
interest = args.interest
principal = args.principal
payment = args.payment
periods = args.periods
if type != 'diff' or 'annuity':
    print("Incorrect parameters")

if choice == 'diff':
    if payment is not None:
        print("Incorrect parameters")
    else:
        total = 0
        n_i = interest / (12 * 100)
        for i in range(1, periods + 1):
            diff = ceil((principal / periods) + (n_i * (principal - ((principal * (i - 1)) / periods))))
            print(f'Month {i}: payment is {diff}')
            total += diff
        print(f'Overpayment = {total - principal}')

elif choice == 'annuity':
    if interest is None:
        print("Incorrect parameters")
    elif principal is not None and periods is not None:
        nominal_interest = interest / (12 * 100)
        x = pow((1 + nominal_interest), periods)
        monthly_payment = ceil(principal * ((nominal_interest * x) / (x - 1)))
        print(f'\nYour annuity payment = {monthly_payment}!')
        print(f'Overpayment = {monthly_payment * periods - principal}')
    elif principal is None:
        nominal_interest = interest / (12 * 100)
        x = pow((1 + nominal_interest), periods)
        principal = floor(payment / ((nominal_interest * x) / (x - 1)))
        print(f'\nYour loan principal = {principal}!')
        print(f'Overpayment = {ceil(payment * periods - principal)}')
    elif periods is None:
        nominal_interest = interest / (12 * 100)
        num_months = round(
            log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))

        if 12 > num_months > 1:
            print(f'It will take {num_months} months to repay this loan!')
        elif num_months == 1:
            print(f'It will take {num_months} month to repay this loan!')
        elif num_months > 11 and num_months % 12 == 0:
            print(f'It will take {num_months // 12} years to repay this loan!')
        elif num_months > 11 and num_months % 12 == 1:
            print(f'It will take {num_months // 12} years and {num_months % 12} month to repay this loan!')
        elif num_months > 11 and num_months % 12 > 1:
            print(f'It will take {num_months // 12} years and {num_months % 12} months to repay this loan!')
        print(f'Overpayment = {ceil(payment * num_months - principal)}')
