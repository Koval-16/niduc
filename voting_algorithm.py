class VotingAlgorithm:
    @staticmethod
    def average_algorithm(sensor_values, threshold=5.0):
        # Sprawdzamy, czy lista wartości nie jest pusta
        if not sensor_values:
            return 0

        # Obliczamy medianę wartości, sortujemy liste wartosci, dlugosc listy
        sorted_values = sorted(sensor_values)
        length = len(sorted_values)

        # Sprawdzamy, czy liczba wartości jest nieparzysta czy parzysta + mediana
        if length % 2 == 1:
            median_value = sorted_values[length // 2]
        else:
            median_value = (sorted_values[length // 2 - 1] + sorted_values[length // 2]) / 2

        # Odrzucamy wartości, które odbiegają mocno od mediany
        filtered_values = []
        for value in sensor_values:
            if abs(value - median_value) <= threshold:
                filtered_values.append(value)

        # Obliczamy średnią z poprawnych wartości
        if not filtered_values:
            return median_value

        average_value = sum(filtered_values) / len(filtered_values)
        return average_value
