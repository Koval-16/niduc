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

    # algorytm jednogłośny; jeżeli wszystkie wartości są równe to wtedy zwraca wynik
    def unanimity_agorithm(self, values):
        if not values: return None
        if all(value == values[0] for value in values):
            return values[0]
        else: return None

    # każdy wynik ma przypisaną wagę, liczona jest średnia ważona
    def wages_algorithm(self,values_and_wages):
        if not values_and_wages: return None
        length = len(values_and_wages)
        total_values = 0
        total_wages = 0
        for value, wage in values_and_wages:
            total_values += value*wage
            total_wages += wage
        total = total_values/total_wages
        return total

    # zaawansowany algorytm M z N, czyli M czujników musi byc zgodnych ze soba
    # jezeli nie znajdzie M zgodnych czujnikow (w tolerancji tolerance)
    # to wówczas szuka najbliższego wyniku do last_result w tolerancji gamma
    def M_out_of_N_algorithm(self, inputs, weights, tolerance, gamma, m, last_result):
        n = len(inputs)
        objects = []
        tallies = []
        objects.append(inputs[0])
        tallies.append(weights[0])
        for i in range(1, n):
            found = False
            for j in range(len(objects)):
                if abs(inputs[i] - objects[j]) <= tolerance:
                    tallies[j] += weights[i]
                    found = True
                    break
            if not found:
                if len(objects) < m:
                    objects.append(inputs[i])
                    tallies.append(weights[i])
                else:
                    min_tally_index = tallies.index(min(tallies))
                    if weights[i] > tallies[min_tally_index]:
                        reduction_value = tallies[min_tally_index]
                        tallies = [max(0, t - reduction_value) for t in tallies]
                        objects[min_tally_index] = inputs[i]
                        tallies[min_tally_index] = weights[i]
                    else:
                        tallies = [max(0, t - weights[i]) for t in tallies]  # Redukcja bez zastąpienia
        for j in range(len(objects)):
            if tallies[j] >= m:
                return objects[j]
        distances = [abs(last_result - x) for x in inputs]
        min_distance = min(distances)
        if min_distance <= gamma:
            return inputs[distances.index(min_distance)]
        return None


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
            if distance < smallest_distance:
                closest_value = value
                smallest_distance = distance
        if smallest_distance <= threshold:
            return closest_value
        return None

    # algorytm predykcyjny liniowy (2 ostatnie wyniki)
    def linear_predictor_algorithm(self, values, previous_results, threshold):
        if len(previous_results) <2: return None
        predicted_value = 2*previous_results[-1] - previous_results[-2]
        best_candidate = None
        best_distance = float('inf')
        for value in values:
            distance = abs(value - predicted_value)
            if distance < threshold and distance < best_distance:
                best_candidate = value
                best_distance = distance
        return best_candidate

    # algorytm predykcyjny first_order (3 ostatnie wyniki)
    def firstorder_predictor_algorithm(self, values, previous_results, threshold):
        if len(previous_results) <3: return None
        predicted_value = (1*previous_results[-1])+(0.2*previous_results[-2]+(0.1*previous_results[-3]))
        best_candidate = None
        best_distance = float('inf')
        for value in values:
            distance = abs(value - predicted_value)
            if distance < threshold and distance < best_distance:
                best_candidate = value
                best_distance = distance
        return best_candidate