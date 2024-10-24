from wheel import Wheel
from error_model import ErrorModel

class Car:
    def __init__(self, initial_speed):
        error_model = ErrorModel(fault_probability=0.05)
        self.wheels = {
            'LF': Wheel(initial_speed, error_model),
            'RF': Wheel(initial_speed, error_model),
            'LR': Wheel(initial_speed, error_model),
            'RR': Wheel(initial_speed, error_model)
        }
        self.speed = initial_speed

    # aktualizuje realne predkosci samochodu i kół
    def update_speed(self, new_speed):
        self.speed = new_speed

        for wheel in self.wheels.values():
            wheel.update_real_value(new_speed)

    # Aktualizuje zmierzone prędkości wszystkich kół
    def update_measured_values(self):
        for wheel in self.wheels.values():
            wheel.simulate_lock()
            wheel.update_measured_value()

    # Zwraca odczyty czujników ze wszystkich kół oraz prędkości zmierzone.
    def get_wheel_values(self):
        wheel_values = {}
        for wheel_label, wheel in self.wheels.items():
            wheel_values[wheel_label] = {
                'sensor_values': wheel.get_sensor_values(),
                'measured_value': wheel.get_measured_value()
            }
        return wheel_values
