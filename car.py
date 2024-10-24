from wheel import Wheel
from error_model import ErrorModel

class Car:
    def __init__(self, initial_speed):
        # Tworzymy model błędów z 20% szansą na awarię czujnika
        error_model = ErrorModel(fault_probability=0.2)

        # Tworzymy cztery koła z podaną początkową prędkością i modelem błędów
        self.wheels = {
            'LF': Wheel(initial_speed, error_model),  # Lewy Przedni
            'RF': Wheel(initial_speed, error_model),  # Prawy Przedni
            'LR': Wheel(initial_speed, error_model),  # Lewy Tylny
            'RR': Wheel(initial_speed, error_model)   # Prawy Tylny
        }

        # Przypisujemy początkową prędkość samochodu
        self.speed = initial_speed

    def update_speed(self, new_speed):
        """
        Aktualizuje prędkość samochodu i jego kół.
        """
        # Ustawiamy nową prędkość samochodu
        self.speed = new_speed

        # Aktualizujemy rzeczywistą prędkość we wszystkich kołach
        for wheel in self.wheels.values():
            wheel.update_real_value(new_speed)

    def update_measured_values(self):
        """Aktualizuje zmierzone prędkości wszystkich kół, uwzględniając ewentualne zablokowanie kół."""
        for wheel in self.wheels.values():
            wheel.simulate_lock()  # Sprawdzamy, czy koło jest zablokowane
            wheel.update_measured_value()  # Aktualizujemy zmierzone wartości

    def get_wheel_values(self):
        """
        Zwraca odczyty czujników ze wszystkich kół oraz prędkości zmierzone.
        """
        wheel_values = {}

        # Dla każdego koła pobieramy odczyty czujników i prędkości zmierzone
        for wheel_label, wheel in self.wheels.items():
            wheel_values[wheel_label] = {
                'sensor_values': wheel.get_sensor_values(),
                'measured_value': wheel.get_measured_value()
            }

        return wheel_values
