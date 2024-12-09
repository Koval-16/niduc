import voting_algorithm
import error
import math

def main():
    alg = voting_algorithm.VotingAlgorithm()
    err = error.Error()

    # Normalny przejazd dla 1 koła
    x = 0
    end = math.pi
    step = math.pi/90
    amp = 60
    noise = 2
    results_majority_5 = []
    results_majority_25 = []
    results_plurality = []
    results_median = []
    results_wages = []
    results_mn_1 = []
    results_mn_2 = []
    results_smoothing_2 = []
    results_linear_2 = []
    results_firstorder_2 = []
    while x <= end:
        y = amp*math.sin(x)
        x += step
        sensors = []
        for i in range(5):
            sensors.append(err.random_error(y, noise))
        print(f"{y:.2f} | Czujniki wskazuja: {[f'{value:.2f}' for value in sensors]}")
        results_majority_5.append(alg.majority_algorithm_tolerance(sensors,0.5))
        results_majority_25.append(alg.majority_algorithm_tolerance(sensors,0.25))

        results_plurality.append(alg.plurality_with_tolerance(sensors,0.5))
        results_median.append(alg.median_algorithm(sensors))
        results_wages.append(alg.wages_algorithm(sensors,[1,1,1,1,1]))

        if len(results_mn_1)==0: results_mn_1.append(alg.M_out_of_N_algorithm(sensors, [1, 1, 1, 1, 1], 0.2, 2, 3,0))
        else: results_mn_1.append(alg.M_out_of_N_algorithm(sensors,[1,1,1,1,1],0.2,2,3,results_mn_1[-1]))
        if len(results_mn_2)==0: results_mn_2.append(alg.M_out_of_N_algorithm(sensors, [1, 1, 1, 1, 1], 0.4, 4, 3,0))
        else: results_mn_2.append(alg.M_out_of_N_algorithm(sensors,[1,1,1,1,1],0.4,4,3,results_mn_2[-1]))

        if len(results_smoothing_2)==0: results_smoothing_2.append(alg.smoothing_algorithm(sensors,0,3))
        else: results_smoothing_2.append(alg.smoothing_algorithm(sensors,results_smoothing_2[-1],3))

        results_linear_2.append(alg.linear_predictor_algorithm(sensors,results_linear_2,5))

        results_firstorder_2.append(alg.firstorder_predictor_algorithm(sensors,results_firstorder_2,7))

    print(f"Wyniki majority 0.5: {[f'{value:.2f}' if value is not None else 'None' for value in results_majority_5]}")
    print(f"Wyniki majority 0.25: {[f'{value:.2f}' if value is not None else 'None' for value in results_majority_25]}")
    print(f"Wyniki plurality: {[f'{value:.2f}' if value is not None else 'None' for value in results_plurality]}")
    print(f"Wyniki median: {[f'{value:.2f}' if value is not None else 'None' for value in results_median]}")
    print(f"Wyniki wages: {[f'{value:.2f}' if value is not None else 'None' for value in results_wages]}")
    print(f"Wyniki M-out-of-N 1: {[f'{value:.2f}' if value is not None else 'None' for value in results_mn_1]}")
    print(f"Wyniki M-out-of-N 2: {[f'{value:.2f}' if value is not None else 'None' for value in results_mn_2]}")
    print(f"Wyniki smoothing: {[f'{value:.2f}' for value in results_smoothing_2]}")
    print(f"Wyniki linear: {[f'{value:.2f}' for value in results_linear_2]}")
    print(f"Wyniki firstorder: {[f'{value:.2f}' for value in results_firstorder_2]}")





if __name__ == "__main__":
    main()
