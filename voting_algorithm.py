from collections import Counter

class VotingAlgorithm:
    def __init__(self):
        pass

    # algorytm wiekszosciowy z tolerancją (czyli dopuszczane jest odchylenie; jak go nie chcemy to tol=0)
    def majority_algorithm_tolerance(self, values, tolerance):
        if not values: return None
        votes = {val: 0 for val in values}
        for val in values:
            for candidate in values:
                if abs(val - candidate) <= tolerance:
                    votes[candidate] += 1
        max_votes = max(votes.values())
        candidates = [val for val, count in votes.items() if count == max_votes]
        if max_votes > len(values) // 2:
            return candidates[0]
        return None

    # w zasadzie bardzo podobny do majority, ale nie musi być wiekszosciowy
    def plurality_with_tolerance(self, values, tolerance):
        if not values: return None
        votes = {val: 0 for val in values}
        for val in values:
            for candidate in values:
                if abs(val - candidate) <= tolerance:
                    votes[candidate] += 1
        max_votes = max(votes.values())
        candidates = [val for val, count in votes.items() if count == max_votes]
        return candidates[0]

    # algorytm mediany, wynikiem jest mediana zbioru
    def median_algorithm(self,values):
        if not values: return None
        sorted_values = sorted(values)
        length = len(values)
        if length%2 == 0:
            a = sorted_values[len(values)//2]
            b = sorted_values[(len(values)//2)-1]
            return (a+b)/2
        elif length%2 == 1:
            return sorted_values[len(values)//2]

    # każdy wynik ma przypisaną wagę, liczona jest średnia ważona
    def wages_algorithm(self,values, wages):
        if not values or not wages or len(values) != len(wages):
            return None
        total_values = sum(value * wage for value, wage in zip(values, wages))
        total_wages = sum(wages)
        if total_wages == 0:
            return None
        return total_values / total_wages

    # zaawansowany algorytm M z N, czyli M czujników musi byc zgodnych ze soba
    # jezeli nie znajdzie M zgodnych czujnikow (w tolerancji tolerance)
    # to wówczas szuka najbliższego wyniku do last_result w tolerancji gamma
    def M_out_of_N_algorithm(self, inputs, weights, tolerance, gamma, m, last_result):
        n = len(inputs)
        objects = [None] * m
        tallies = [0] * m
        for i in range(n):
            found = False
            for j in range(m):
                if objects[j] is not None and abs(inputs[i] - objects[j]) <= tolerance:
                    tallies[j] += weights[i]
                    found = True
                    break
            if not found:
                for j in range(m):
                    if objects[j] is None:
                        objects[j] = inputs[i]
                        tallies[j] = weights[i]
                        found = True
                        break
            if not found:
                min_tally_index = tallies.index(min(tallies))
                if weights[i] > tallies[min_tally_index]:
                    reduction_value = tallies[min_tally_index]
                    tallies = [max(0, t - reduction_value) for t in tallies]
                    objects[min_tally_index] = inputs[i]
                    tallies[min_tally_index] = weights[i]
                else:
                    tallies = [max(0, t - weights[i]) for t in tallies]
        # Faza 2: Weryfikacja wyników
        tallies = [0] * m  # Reset tally
        for i in range(n):
            for j in range(m):
                if objects[j] is not None and abs(inputs[i] - objects[j]) <= tolerance:
                    tallies[j] += weights[i]
                    if tallies[j] >= m:
                        return objects[j]
        # Faza 3: Szukanie wyniku alternatywnego
        distances = [abs(last_result - x) for x in inputs]
        min_distance = min(distances)
        if min_distance <= gamma:
            return inputs[distances.index(min_distance)]
        return last_result #NONE

    # algorytm smoothing
    def smoothing_algorithm(self, values, previous_result, threshold):
        if not values: return None
        from collections import Counter
        counter = Counter(values)
        max_votes = max(counter.values())
        majority_candidates = [val for val, count in counter.items() if count==max_votes]
        if max_votes > len(values) // 2:
            return majority_candidates[0]
        closest_value = None
        smallest_distance = float('inf')
        for value in values:
            distance = abs(value-previous_result)
            if distance < smallest_distance and value!=0:
                closest_value = value
                smallest_distance = distance
        if smallest_distance <= threshold:
            return closest_value
        return 0 #NONE

    # algorytm predykcyjny liniowy (2 ostatnie wyniki)
    def linear_predictor_algorithm(self, values, previous_results, threshold):
        if len(previous_results) <2: return 0
        predicted_value = 2*previous_results[-1] - previous_results[-2]
        best_candidate = None
        best_distance = float('inf')
        for value in values:
            distance = abs(value - predicted_value)
            if distance < threshold and distance < best_distance and value!=0:
                best_candidate = value
                best_distance = distance
        if best_candidate == None: best_candidate=previous_results[-1] #NONE
        return best_candidate

    # algorytm predykcyjny first_order (3 ostatnie wyniki)
    def firstorder_predictor_algorithm(self, values, previous_results, threshold):
        if len(previous_results) <3: return 0
        predicted_value = (0.8*previous_results[-1])+(0.15*previous_results[-2]+(0.05*previous_results[-3]))
        best_candidate = None
        best_distance = float('inf')
        for value in values:
            distance = abs(value - predicted_value)
            if distance < threshold and distance < best_distance and value!=0:
                best_candidate = value
                best_distance = distance
        if best_candidate == None: best_candidate=previous_results[-1] #NONE
        return best_candidate