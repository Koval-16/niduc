import random

class ErrorModel:
    """Symuluje model błędu dla czujnika."""
    def __init__(self, fault_probability=0.1):
        self.fault_probability = fault_probability

    def is_faulty(self):
        """Określa, czy czujnik jest w stanie awarii."""
        return random.random() < self.fault_probability

    def get_faulty_value(self):
        """Zwraca wartość w przypadku całkowitej awarii (np. 0)."""
        return 0.0
