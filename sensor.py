import random

class Sensor:
    def __init__(self, real_value, error_model=None):
        self.real_value = real_value
        self.measured_value = real_value
        self.error_model = error_model

    # Symuluje odczyt z czujnika, uwzględniając ewentualne błędy i małe odchylenie.
    def update_measured_value(self):
        # Sprawdzamy, czy jest podany model błędu i czy czujnik jest uszkodzony
        if self.error_model is not None and self.error_model.is_faulty():
            self.measured_value = self.error_model.get_faulty_value()
        else:
            # Dodajemy losowe odchylenie do wartości rzeczywistej w zakresie ±1 km/h
            odchylenie = random.uniform(-1, 1)
            self.measured_value = self.real_value + odchylenie

    def get_measured_value(self):
        return self.measured_value
