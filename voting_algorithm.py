class VotingAlgorithm:
    @staticmethod
    def average_with_outlier_rejection(sensor_values, threshold=5.0):
        # Sprawdzamy, czy lista wartości nie jest pusta
        if not sensor_values:
            return 0

        # Krok 1: Obliczamy medianę wartości
        sorted_values = sorted(sensor_values)  # Sortujemy listę wartości
        length = len(sorted_values)  # Pobieramy długość listy

        # Sprawdzamy, czy liczba wartości jest nieparzysta czy parzysta
        if length % 2 == 1:
            # Jeśli nieparzysta, wybieramy środkowy element jako medianę
            median_value = sorted_values[length // 2]
        else:
            # Jeśli parzysta, obliczamy medianę jako średnią dwóch środkowych elementów
            median_value = (sorted_values[length // 2 - 1] + sorted_values[length // 2]) / 2

        # Krok 2: Odrzucamy wartości, które odbiegają od mediany o więcej niż threshold
        filtered_values = []
        for value in sensor_values:
            if abs(value - median_value) <= threshold:
                filtered_values.append(value)

        # Krok 3: Obliczamy średnią z pozostałych wartości
        if not filtered_values:
            # Jeśli wszystkie wartości są odrzucone, zwracamy medianę
            return median_value

        # Obliczamy średnią z pozostałych wartości
        average_value = sum(filtered_values) / len(filtered_values)
        return average_value
