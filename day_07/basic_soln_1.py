from statistics import mean

first_array = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)

goal = int(round(mean(first_array)))

list_of_distances_to_travel_to_median = []

for i in first_array:
    distance_to_travel = abs(i - goal)
    actual_amount = sum(range(int(distance_to_travel) + 1))
    list_of_distances_to_travel_to_median.append(actual_amount)

print(list_of_distances_to_travel_to_median)
print(sum(list_of_distances_to_travel_to_median))
