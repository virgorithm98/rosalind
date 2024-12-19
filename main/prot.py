from constant.rna_codon_table import RNA_CODON_TABLE


def extract_mrna_string_from_txt(file_path: str) -> str:
    mrna_string = ""
    with open(file_path, "r") as text:
        for line in text:
            mrna_string += line

    return mrna_string.strip()


def translate_rna_to_protein(mrna_string: str) -> str:
    protein_string = ""

    for i in range(0, len(mrna_string), 3):
        amino_acid = RNA_CODON_TABLE[mrna_string[i:i+3]]
        protein_string += amino_acid if amino_acid.lower() != "stop" else ""

    return protein_string


print(translate_rna_to_protein(extract_mrna_string_from_txt("../data/prot_case_1.txt")))