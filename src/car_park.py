from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None, sensors=None): #log_file="log.txt"
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.sensors = sensors or []
        #self.log_file = log_file
        #self.bays_availability = []
        #self.bays_availability += [True] * self.capacity # if a bay is `True` it means it is available

    def __str__(self): # `__str__` is used when somebody tries to use the initialised class in string format.
        return f"Car park at {self.location}, with {self.capacity} bays." # EG: `print (carpark1)` Outputs: `Car park at Perth, with 100 bays.`
    
    def register(self, component):
        if not isinstance(component, (Sensor, Display)): # checks if the object component is an instance of either the Sensor or Display class
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property # A `@property` decorator will make a method behave like an attribute (i.e. we access it rather than call it).
    def available_bays(self):
        if len(self.plates) >= self.capacity:
            return 0 # returns `0` if number of cars in parking lot exceeds available bays
        else:
            return self.capacity - len(self.plates)
    
    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25, "weather": "Sunny"}
        for display in self.displays:
            display.update(data)