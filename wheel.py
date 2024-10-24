from sensor import Sensor
from voting_algorithm import VotingAlgorithm
import random

class Wheel:
    def __init__(self, real_value, error_model=None):
        # Tworzymy listę pięciu czujników
        self.sensors = []
        for _ in range(5):
            sensor = Sensor(real_value, error_model)
            self.sensors.append(sensor)

        # Przypisujemy początkowe wartości prędkości
        self.real_value = real_value
        self.measured_value = real_value  # Początkowa zmierzona prędkość koła to prędkość rzeczywista
        self.is_locked = False

    # Aktualizuje rzeczywiste predkosci koła i w czujnikach
    def update_real_value(self, new_value):
        self.real_value = new_value

        for sensor in self.sensors:
            sensor.real_value = new_value

    def simulate_lock(self):
        # Możemy ustawić prawdopodobieństwo blokady koła
        if random.random() < 0:
            self.is_locked = True
            self.measured_value = max(0, self.measured_value - random.uniform(5, 15))  # Zmniejszamy prędkość
        else:
            self.is_locked = False

    # Aktualizuje zmierzoną prędkość koła na podstawie algorytmu głosowania
    def update_measured_value(self):
        # Aktualizujemy wartości zmierzone w każdym czujniku
        for sensor in self.sensors:
            sensor.update_measured_value()

        # Jeśli koło jest zablokowane, zmniejszamy prędkość
        if self.is_locked:
            # Logika ABS: Wyrównujemy prędkość
            self.measured_value = min(self.real_value, self.measured_value + 1)  # Stopniowo wracamy do prędkości rzeczywistej
        else:
            # Pobieramy zmierzone wartości z czujników
            sensor_values = [sensor.get_measured_value() for sensor in self.sensors]
            # Obliczamy prędkość koła za pomocą algorytmu głosowania
            self.measured_value = VotingAlgorithm.average_algorithm(sensor_values)


    # Zwraca zmierzoną prędkość koła.
    def get_measured_value(self):
        return self.measured_value

    # Zwraca listę zmierzonych wartości ze wszystkich czujników.
    def get_sensor_values(self):
        sensor_values = []
        for sensor in self.sensors:
            sensor_values.append(sensor.get_measured_value())
        return sensor_values
