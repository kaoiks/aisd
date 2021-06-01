from random import randint

# Generuje listę kontenerów
# ship_capacity - Pojemność statku
# target_weight_sum - Docelowa suma mas kontenerów
# capacity_maxweight_ratio - Stosunek ładowności do maksymalnej masy pojedynczego kontenera
def generate(ship_capacity, target_weight_sum, capacity_maxweight_ratio = 4):
    min_cont_weight = 1
    max_cont_weight = 1 + int(ship_capacity / capacity_maxweight_ratio)
    current_weight_sum = 0
    containers = []

    while current_weight_sum < target_weight_sum:
        cont_weight = randint(min_cont_weight, max_cont_weight)
        cont_value = randint(1, 100)
        containers.append([cont_weight, cont_value])
        current_weight_sum += cont_weight

    return containers

# print(generate(50, 200))