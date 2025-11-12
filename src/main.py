from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO LIST:
# 1 (X) TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# 2 (X) TODO: Write the car park configuration to a file called "moondalup_config.json"
# 3 (X) TODO: Reinitialize the car park object from the "moondalup_config.json" file
# 4 (X) TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# 5 (X) TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# 6 (X) TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# 7 (X) TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# 8 (X) TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)


# 1
car_park = CarPark("moondalup", 100, log_file="moondalup.txt", config_file="moondalup_config.json")

# 2
car_park.write_config()

# 3
car_park = car_park.from_config(car_park.config_file)

# 4
entry_sensor = EntrySensor(1, True, car_park)
car_park.register(entry_sensor)

# 5
exit_sensor = ExitSensor(2, True, car_park)
car_park.register(exit_sensor)

# 6
display = Display(1, "Welcome to Moondalup", True)
car_park.register(display)

# 7
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()

# 8
exit_sensor.detect_vehicle()
exit_sensor.detect_vehicle()