import random

class ErrorModel:
    # Symuluje model błędu dla czujnika.
    def __init__(self, fault_probability=0.1):
        self.fault_probability = fault_probability

    # Określa, czy czujnik jest w stanie awarii.
    def is_faulty(self):
        return random.random() < self.fault_probability

    # Zwraca wartość w przypadku całkowitej awarii
    def get_faulty_value(self):
        return 0.0
