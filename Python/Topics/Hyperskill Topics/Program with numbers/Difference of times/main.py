hours_one, minutes_one, seconds_one, hours_two, minutes_two, seconds_two  = input(), input(), input(), input(), input(), input()
difference = ((int(hours_two) * 60 * 60) + (int(minutes_two) * 60) + int(seconds_two)) - ((int(hours_one) * 60 * 60) + (int(minutes_one) * 60) + int(seconds_one))
print(difference)
