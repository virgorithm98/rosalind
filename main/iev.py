from helper import util, constant

def count_allele_offspring(offspring_count: int, dominant: bool = True) -> float:
    count = 0.0

    for key, value in util.extract_genotype_number_pair("../data/iev_case_1.txt").items():
        count += value * offspring_count * (constant.DOMINANT_ALLELE_PROBABILITY[key] if dominant
                                            else constant.RECESSIVE_ALLELE_PROBABILITY[key])

    return count

print(count_allele_offspring(2))