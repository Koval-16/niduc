# błędy losowe (wartosc czujnika zaburzona)
# błędy systematyczne (wartosc czujnika z przesunieta wartoscia)
# całkowita awaria czujnika (może pokazywać 0 / ostatnią wartość / maximum)
# błędy spowodowane szumem
import random

class Error:
    def __init__(self):
        pass

    def random_error(self, value, diff):
        bottom = value-diff
        top = value+diff
        return abs(random.uniform(bottom,top))

    def systematic_error(self,value,diff):
        return value+diff

    def failure_error(self, value):
        return 0
