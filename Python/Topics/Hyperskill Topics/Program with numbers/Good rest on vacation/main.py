duration = int(input())
food_cost = int(input()) * duration
flight_cost = int(input()) * 2
hotel_cost = int(input()) * (duration - 1)
print(food_cost + flight_cost + hotel_cost)
