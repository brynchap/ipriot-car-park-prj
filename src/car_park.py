class CarPark:
    def __init__(self, location = "Unknown", capacity=0, plates = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.bays_availability = []
        self.bays_availability += [True] * self.capacity # if a bay is `True` it means it is available

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."