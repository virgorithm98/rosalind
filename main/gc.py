def convert_fasta_to_dict(file_path: str) -> dict:
    id_dna_string_pair = {}

    with open("../data/gc_case_1.txt", 'r') as text:
        fasta_id = ""
        for line in text:
            if line.startswith(">"):
                fasta_id = line[1:].strip()
                id_dna_string_pair.update({fasta_id:""})
            else:
                id_dna_string_pair.update({fasta_id:id_dna_string_pair[fasta_id] + line.strip()})

    return id_dna_string_pair


def calculate_gc_content(id_dna_string_pair: dict) -> str:
    fasta_id = ""
    gc_content = 0.0

    for key, value in id_dna_string_pair.items():
        temp_gc_content = (value.count("G") + value.count("C")) / len(value) * 100

        if gc_content < temp_gc_content:
            gc_content, fasta_id = temp_gc_content, key

    return f"{fasta_id} {round(gc_content, 6)}"

print(calculate_gc_content(convert_fasta_to_dict("../data/gc_case_1.txt")))