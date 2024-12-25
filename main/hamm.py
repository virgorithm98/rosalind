def separate_two_dna_strings(file_path: str) -> tuple[str, str]:
    with open(file_path, "r") as text:
        string_a, string_b = text.read().split("\n")

    return string_a, string_b


def calculate_hamming_distance(string_a, string_b):
    return [a != b for a, b in zip(string_a, string_b)].count(True)


print(calculate_hamming_distance(*separate_two_dna_strings("../data/hamm_case_1.txt")))