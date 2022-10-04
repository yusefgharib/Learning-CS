def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return closest_higher_mod_5(x + 1)
