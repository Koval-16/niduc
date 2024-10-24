from car import Car

def main():
    # Tworzymy samochód z początkową prędkością 50 km/h
    initial_speed = 50.0
    car = Car(initial_speed)

    # Liczba iteracji symulacji
    num_iterations = 5

    # Symulacja przez zadane liczby iteracji
    for iteration in range(num_iterations):
        # Zmieniamy prędkość auta w każdej iteracji (prędkość stopniowo maleje o 1 km/h)
        new_speed = initial_speed - iteration
        car.update_speed(new_speed)

        # Aktualizujemy zmierzone wartości prędkości we wszystkich kołach
        car.update_measured_values()

        print(f"\n--- Iteracja {iteration + 1} ---")
        print(f"Nowa prędkość auta: {new_speed:.2f} km/h")

        # Pobieramy odczyty z każdego koła
        wheel_values = car.get_wheel_values()

        for wheel_label, data in wheel_values.items():
            # Wyświetlamy wartości zmierzone przez czujniki i obliczoną prędkość koła po głosowaniu
            sensor_values = data['sensor_values']
            measured_value = data['measured_value']
            print(f"{wheel_label} wheel sensor values: {sensor_values}")
            print(f"{wheel_label} wheel measured value (with outlier rejection): {measured_value:.2f} km/h")

if __name__ == "__main__":
    main()
