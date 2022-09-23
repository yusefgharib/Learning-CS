class Fish:
    place = "aquarium"
    n_fish = 0  # number of fish in the aquarium

    def __init__(self, name, kind):
        Fish.n_fish += 1
        self.name = name
        self.kind = kind


greg = Fish("Greg", "guppy")
