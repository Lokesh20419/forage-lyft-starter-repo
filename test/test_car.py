import unittest
from datetime import date
from engine import (
    CapuletEngine,
    SternmanEngine,
    WilloughbyEngine,
    SpindlerBattery,
    NubbinBattery
)


class EngineTests(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        # Create a CapuletEngine instance with last_service_mileage and current_mileage
        engine = CapuletEngine(last_service_mileage=10000, current_mileage=12000)
        
        # Call the needs_service method and assert the result is False
        self.assertFalse(engine.needs_service())
        
        # Update the current_mileage to exceed the service threshold
        engine.current_mileage = 15000
        
        # Call the needs_service method and assert the result is True
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        # Create a SternmanEngine instance with warning_light_on set to True
        engine = SternmanEngine(warning_light_on=True)
        
        # Call the needs_service method and assert the result is True
        self.assertTrue(engine.needs_service())
        
        # Set the warning_light_on to False
        engine.warning_light_on = False
        
        # Call the needs_service method and assert the result is False
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        # Create a WilloughbyEngine instance with last_service_mileage and current_mileage
        engine = WilloughbyEngine(last_service_mileage=20000, current_mileage=22000)
        
        # Call the needs_service method and assert the result is False
        self.assertFalse(engine.needs_service())
        
        # Update the current_mileage to exceed the service threshold
        engine.current_mileage = 26000
        
        # Call the needs_service method and assert the result is True
        self.assertTrue(engine.needs_service())


class BatteryTests(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        # Create a SpindlerBattery instance with last_service_date and current_date
        battery = SpindlerBattery(last_service_date=date(2022, 1, 1), current_date=date(2023, 1, 1))
        
        # Call the needs_service method and assert the result is False
        self.assertFalse(battery.needs_service())
        
        # Update the last_service_date to exceed the service threshold
        battery.last_service_date = date(2020, 1, 1)
        
        # Call the needs_service method and assert the result is True
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        # Create a NubbinBattery instance with last_service_date and current_date
        battery = NubbinBattery(last_service_date=date(2022, 1, 1), current_date=date(2023, 1, 1))
        
        # Call the needs_service method and assert the result is False
        self.assertFalse(battery.needs_service())
        
        # Update the last_service_date to exceed the service threshold
        battery.last_service_date = date(2020, 1, 1)
        
        # Call the needs_service method and assert the result is True
        self.assertTrue(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
