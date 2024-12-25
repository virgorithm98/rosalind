from constant.rna_codon_table import RNA_CODON_TABLE
from helper import util


def translate_rna_to_protein(mrna_string: str) -> str:
    protein_string = ""

    for i in range(0, len(mrna_string), 3):
        amino_acid = RNA_CODON_TABLE[mrna_string[i:i+3]]
        protein_string += amino_acid if amino_acid.lower() != "stop" else ""

    return protein_string


print(translate_rna_to_protein(util.extract_string_from_txt("../data/prot_case_1.txt")))