from math import pow, sqrt
a = int(input())
area = round(2 * sqrt(3) * pow(a, 2), 2)
vol = round(1 / 3 * sqrt(2) * pow(a, 3), 2)
print(f"{area} {vol}")
