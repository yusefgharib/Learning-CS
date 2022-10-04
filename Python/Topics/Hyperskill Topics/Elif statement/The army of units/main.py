army = int(input())

print(
    "no army" if army < 1 else
    "few" if army < 10 else
    "pack" if army < 50 else
    "horde" if army < 500 else
    "swarm" if army < 1000 else
    "legion"
)
