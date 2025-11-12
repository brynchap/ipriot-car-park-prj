import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark()
        self.entry_sensor = EntrySensor(1, False, self.car_park)
        self.exit_sensor = ExitSensor(2, False, self.car_park)
    def test_init(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 2)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 0)