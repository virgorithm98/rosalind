def dominant_allele_offspring_probability(population_allele_data: dict, organism_1: str, organism_2: str) -> float:
    dominant_allele_occurrence = 0
    number_of_pair = 0
    for allele_1 in population_allele_data.get(organism_1):
        for allele_2 in population_allele_data.get(organism_2):
            if allele_1.isupper() or allele_2.isupper():
                dominant_allele_occurrence += 1
            number_of_pair += 1

    return dominant_allele_occurrence/number_of_pair if dominant_allele_occurrence > 0 else 0.0


def pairing_probability(number_of_population_data: dict, organism_1: str, organism_2: str) -> float:
    organism_1_probability = number_of_population_data.get(organism_1) / sum(number_of_population_data.values())
    number_of_population_data.update({organism_1:number_of_population_data.get(organism_1) - 1})
    organism_2_probability = number_of_population_data.get(organism_2) / sum(number_of_population_data.values())

    return organism_1_probability * organism_2_probability


def dominant_allele_probability_in_population(population_data: dict) -> float:
    population_allele_data = {}
    number_of_population_data = {}
    possible_random_pairing = []

    for key, value in population_data.items():
        population_allele_data.update({key:value[0]})
        number_of_population_data.update({key:value[1]})

    probability = 0.0
    for key_1 in population_data.keys():
        for key_2 in population_data.keys():
            if (key_1 + key_2 not in possible_random_pairing) and (key_2 + key_1 not in possible_random_pairing):
                temp_number_of_population_data = number_of_population_data.copy()
                probability += (pairing_probability(temp_number_of_population_data, key_1, key_2)
                                * dominant_allele_offspring_probability(population_allele_data, key_1, key_2))

    return probability


print(dominant_allele_probability_in_population({"k":["AA", 25], "m":["Aa",22], "n":["aa", 16]}))