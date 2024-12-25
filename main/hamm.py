from helper import util

def calculate_hamming_distance(string_a, string_b):
    return [a != b for a, b in zip(string_a, string_b)].count(True)


print(calculate_hamming_distance(*util.separate_two_dna_strings("../data/hamm_case_1.txt")))