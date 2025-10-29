from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location = "Unknown", capacity=0, plates = None, displays = None, sensors = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.sensors = sensors or []
        self.bays_availability = []
        self.bays_availability += [True] * self.capacity # if a bay is `True` it means it is available

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."
    
    def register(self, component):
        if not isinstance(component, (Sensor, Display)): # checks if the object component is an instance of either the Sensor or Display class
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)