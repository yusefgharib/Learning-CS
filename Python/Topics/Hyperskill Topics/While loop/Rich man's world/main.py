initial = int(input())
counter, interest_rate, max_amount = 0, 1.071, 700000
while initial < max_amount:
    initial *= interest_rate
    counter += 1
print(counter)
