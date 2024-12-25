from helper import util


def locate_motif_starting_position(dna_string: str, pattern: str):
    starting_position = []
    for i in range(len(dna_string)):
        if dna_string[i:].startswith(pattern):
            starting_position.append(i + 1)

    return starting_position


print(locate_motif_starting_position(*util.separate_two_dna_strings("../data/subs_case_1.txt")))
