from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None, sensors=None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] # uses the first value if not None, otherwise uses the second value
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        #self.config_file.touch(exist_ok=True)

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
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

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

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open(self.config_file, "w") as f:  # TODO: use self.config_file; use Path; add optional parm to __init__
            # Because JSON is dictionary-like. The `json.dump()` method is used to write the dictionary to the file
            json.dump({"location": self.location, "capacity": self.capacity, "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
