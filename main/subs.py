def separate_two_dna_strings(file_path: str) -> tuple[str, str]:
    with open(file_path, "r") as text:
        dna_string, dna_substring = text.read().split("\n")

    return dna_string.strip(), dna_substring.strip()


def locate_motif_starting_position(dna_string: str, pattern: str):
    starting_position = []
    for i in range(len(dna_string)):
        if dna_string[i:].startswith(pattern):
            starting_position.append(i + 1)

    return starting_position


print(locate_motif_starting_position(*separate_two_dna_strings("../data/subs_case_1.txt")))
