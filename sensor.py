import random

class Sensor:
    def __init__(self, real_value, error_model=None):
        # Przypisujemy wartości początkowe
        self.real_value = real_value
        self.measured_value = real_value  # Początkowa wartość zmierzona to wartość rzeczywista
        self.error_model = error_model

    def update_measured_value(self):
        """
        Symuluje odczyt z czujnika, uwzględniając ewentualne błędy i małe odchylenie.
        """
        # Sprawdzamy, czy jest podany model błędu i czy czujnik jest uszkodzony
        if self.error_model is not None and self.error_model.is_faulty():
            # Pobieramy wartość błędną z modelu błędu
            self.measured_value = self.error_model.get_faulty_value()
        else:
            # Dodajemy losowe odchylenie do wartości rzeczywistej w zakresie ±1 km/h
            odchylenie = random.uniform(-1, 1)
            self.measured_value = self.real_value + odchylenie

    def get_measured_value(self):
        """
        Zwraca zmierzoną prędkość z czujnika.
        """
        return self.measured_value
