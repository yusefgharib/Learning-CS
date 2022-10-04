room_one = int(input())
room_two = int(input())
room_three = int(input())
if room_one % 2 == 0 and room_one > 0:
    desks_one = room_one / 2
elif room_one % 2 != 0 and room_one > 0:
    desks_one = room_one // 2 + 1
else:
    desks_one = 0
if room_two % 2 == 0 and room_two > 0:
    desks_two = room_two / 2
elif room_two % 2 != 0 and room_two > 0:
    desks_two = room_two // 2 + 1
else:
    desks_two = 0
if room_three % 2 == 0 and room_three > 0:
    desks_three = room_three / 2
elif room_three % 2 != 0 and room_three > 0:
    desks_three = room_three // 2 + 1
else:
    desks_three = 0

print(int(desks_one) + int(desks_two) + int(desks_three))
